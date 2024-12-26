import json
import logging
from kafka import KafkaConsumer
import psycopg2
from psycopg2.extras import execute_values

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="ecommerce",
        user="postgres",
        password="password",
        host="localhost"
    )
    cursor = conn.cursor()
except psycopg2.Error as e:
    logger.error(f"Error connecting to PostgreSQL: {e}")
    raise

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
def process_messages(batch_size=100):
    buffer = []
    for message in consumer:
        transaction = message.value
        buffer.append((
            transaction['user_id'],
            transaction['product_id'],
            transaction['price'],
            transaction['timestamp']
        ))

        if len(buffer) >= batch_size:
            try:
                execute_values(cursor, """
                    INSERT INTO transactions (user_id, product_id, price, timestamp)
                    VALUES %s
                """, buffer, template=None, page_size=batch_size)
                conn.commit()
                logger.info(f"Stored batch of {len(buffer)} transactions")
                buffer.clear()
            except psycopg2.Error as e:
                logger.error(f"Error storing transactions: {e}")
                conn.rollback()

if __name__ == "__main__":
    try:
        process_messages()
    except KeyboardInterrupt:
        logger.info("Shutting down consumer...")
    finally:
        cursor.close()
        conn.close()