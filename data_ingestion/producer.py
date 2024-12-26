import random
import time
import json
from kafka import KafkaProducer

# Kafka Producer setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Simulate transaction data
def generate_transaction():
    return {
        "user_id": random.randint(1, 100),
        "product_id": random.randint(1, 50),
        "price": random.randint(100, 5000),
        "timestamp": time.time()
    }

# Send transactions to Kafka topic
while True:
    transaction = generate_transaction()
    producer.send('transactions', value=transaction)
    print(f"Sent: {transaction}")
    time.sleep(1)
