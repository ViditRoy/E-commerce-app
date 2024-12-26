import random
import time
import json
import logging
from kafka import KafkaProducer
from kafka.errors import KafkaError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
def send_transactions(interval=1):
    while True:
        transaction = generate_transaction()
        try:
            producer.send('transactions', value=transaction).get(timeout=10)
            logger.info(f"Sent: {transaction}")
        except KafkaError as e:
            logger.error(f"Failed to send transaction: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    send_transactions()