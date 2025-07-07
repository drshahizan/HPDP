import json
import time
import pandas as pd
from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GameReviewProducer:
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda k: k.encode('utf-8') if k else None,
            acks='all',
            retries=3,
            batch_size=16384,
            linger_ms=10,
            buffer_memory=33554432
        )
        
    def send_review(self, topic, review_data):
        """Send a single review to Kafka topic"""
        try:
            # Use game name as key for partitioning
            key = review_data.get('game', 'unknown')
            future = self.producer.send(topic, key=key, value=review_data)
            
            # Wait for message to be sent
            record_metadata = future.get(timeout=10)
            logger.info(f"Sent review to {record_metadata.topic} partition {record_metadata.partition}")
            return True
            
        except KafkaError as e:
            logger.error(f"Failed to send review: {e}")
            return False
    
    def send_reviews_from_csv(self, csv_file, topic='game-reviews', batch_size=100):
        """Send reviews from CSV file to Kafka"""
        try:
            df = pd.read_csv(csv_file)
            logger.info(f"Loaded {len(df)} reviews from {csv_file}")
            
            sent_count = 0
            for index, row in df.iterrows():
                review_data = {
                    'id': index,
                    'game': row['game'],
                    'review': row['review'],
                    'voted_up': bool(row['voted_up']),
                    'timestamp': str(row['timestamp']),
                    'platform': row['platform'],
                    'sentiment': row.get('sentiment', 'unknown')
                }
                
                if self.send_review(topic, review_data):
                    sent_count += 1
                
                # Add small delay to avoid overwhelming
                if sent_count % batch_size == 0:
                    logger.info(f"Sent {sent_count} reviews...")
                    time.sleep(1)
            
            logger.info(f"Successfully sent {sent_count} reviews to topic '{topic}'")
            
        except Exception as e:
            logger.error(f"Error sending reviews from CSV: {e}")
    
    def close(self):
        """Close the producer"""
        self.producer.close()

if __name__ == "__main__":
    # Example usage
    producer = GameReviewProducer()
    
    # Send reviews from your CSV file
    producer.send_reviews_from_csv('steam_game_reviews.csv', 'game-reviews')
    
    # Close producer
    producer.close()
