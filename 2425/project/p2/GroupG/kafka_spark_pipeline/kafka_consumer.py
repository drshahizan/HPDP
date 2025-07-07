import json
import logging
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from textblob import TextBlob
import pandas as pd

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GameReviewConsumer:
    def __init__(self, topics, bootstrap_servers=['localhost:9092'], group_id='review-processor'):
        self.consumer = KafkaConsumer(
            *topics,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            key_deserializer=lambda k: k.decode('utf-8') if k else None,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            consumer_timeout_ms=10000
        )
        
    def process_sentiment(self, review_text):
        """Process sentiment using TextBlob"""
        try:
            polarity = TextBlob(review_text).sentiment.polarity
            if polarity > 0.1:
                return "positive"
            elif polarity < -0.1:
                return "negative"
            else:
                return "neutral"
        except Exception as e:
            logger.error(f"Error processing sentiment: {e}")
            return "unknown"
    
    def consume_and_process(self):
        """Consume messages and process them"""
        processed_reviews = []
        
        try:
            logger.info("Starting to consume messages...")
            
            for message in self.consumer:
                try:
                    review_data = message.value
                    
                    # Process sentiment if not already present
                    if review_data.get('sentiment') == 'unknown' or not review_data.get('sentiment'):
                        review_data['sentiment'] = self.process_sentiment(review_data['review'])
                    
                    # Add processing metadata
                    review_data['processed_timestamp'] = pd.Timestamp.now().isoformat()
                    review_data['partition'] = message.partition
                    review_data['offset'] = message.offset
                    
                    processed_reviews.append(review_data)
                    
                    logger.info(f"Processed review from {review_data['game']}: {review_data['sentiment']}")
                    
                    # Save batch every 100 reviews
                    if len(processed_reviews) >= 100:
                        self.save_processed_reviews(processed_reviews)
                        processed_reviews = []
                        
                except Exception as e:
                    logger.error(f"Error processing message: {e}")
                    continue
                    
        except KeyboardInterrupt:
            logger.info("Stopping consumer...")
        finally:
            # Save remaining reviews
            if processed_reviews:
                self.save_processed_reviews(processed_reviews)
            self.consumer.close()
    
    def save_processed_reviews(self, reviews):
        """Save processed reviews to CSV"""
        try:
            df = pd.DataFrame(reviews)
            df.to_csv('processed_reviews.csv', mode='a', header=False, index=False)
            logger.info(f"Saved {len(reviews)} processed reviews")
        except Exception as e:
            logger.error(f"Error saving reviews: {e}")

if __name__ == "__main__":
    # Create consumer for game-reviews topic
    consumer = GameReviewConsumer(['game-reviews'])
    
    # Start consuming and processing
    consumer.consume_and_process()
