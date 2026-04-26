import os
import time
import json
import praw
from kafka import KafkaProducer
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Kafka Configuration ---
KAFKA_TOPIC = 'reddit-comments'
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'

# --- Reddit API Configuration ---
SUBREDDIT_NAME = 'movies'  # The subreddit you want to stream

def create_kafka_producer():
    """Creates a Kafka producer instance."""
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("✅ Kafka Producer connected successfully.")
        return producer
    except Exception as e:
        print(f"❌ Could not connect to Kafka: {e}")
        return None

def connect_to_reddit():
    """Connects to the Reddit API using credentials from environment variables."""
    try:
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT")
        )
        print("✅ Reddit API connected successfully.")
        return reddit
    except Exception as e:
        print(f"❌ Could not connect to Reddit: {e}")
        return None

def stream_comments(producer, reddit):
    """Streams comments from the specified subreddit and sends them to Kafka."""
    if not producer or not reddit:
        return

    subreddit = reddit.subreddit(SUBREDDIT_NAME)
    print(f"📡 Streaming comments from r/{SUBREDDIT_NAME}...")

    try:
        for comment in subreddit.stream.comments(skip_existing=True):
            try:
                # Construct the message payload
                message = {
                    "post_id": comment.submission.id,
                    "post_title": comment.submission.title,
                    "comment_id": comment.id,
                    "comment_body": comment.body,
                    "comment_score": comment.score,
                    "created_utc": comment.created_utc
                }
                
                # Send the message to our Kafka topic
                producer.send(KAFKA_TOPIC, message)
                print(f"📤 Sent comment ID {comment.id}: {comment.body[:50]}...")

                time.sleep(1)  # Throttle to avoid overwhelming Kafka

            except Exception as e:
                print(f"⚠️ Error processing comment {comment.id}: {e}")
                continue # Skip to the next comment

    except Exception as e:
        print(f"❌ An error occurred during streaming: {e}")

if __name__ == "__main__":
    kafka_producer = create_kafka_producer()
    reddit_client = connect_to_reddit()
    
    if kafka_producer and reddit_client:
        stream_comments(kafka_producer, reddit_client)