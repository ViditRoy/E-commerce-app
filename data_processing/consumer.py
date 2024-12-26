import json
from kafka import KafkaConsumer
import psycopg2
from psycopg2.extras import execute_values

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="ecommerce",
    user="postgres",
    password="password",
    host="localhost"
)
cursor = conn.cursor()

# Create table for transactions
cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        user_id INT,
        product_id INT,
        price INT,
        timestamp TIMESTAMP
    )
""")
conn.commit()

# Kafka Consumer setup
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Process data and store in DB
for message in consumer:
    transaction = message.value
    cursor.execute(
        "INSERT INTO transactions (user_id, product_id, price, timestamp) VALUES (%s, %s, %s, to_timestamp(%s))",
        (transaction['user_id'], transaction['product_id'], transaction['price'], transaction['timestamp'])
    )
    conn.commit()
    print(f"Stored: {transaction}")
