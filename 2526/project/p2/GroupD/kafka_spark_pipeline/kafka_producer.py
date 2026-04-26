import json
import time
from datetime import datetime
from google_play_scraper import reviews, Sort
from kafka import KafkaProducer

KAFKA_BROKER_URL = 'localhost:9092'
KAFKA_TOPIC = 'grab_reviews_final' 

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER_URL,
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8'),
    acks='all',
    retries=3,
    linger_ms=10
)

GRAB_APP_ID = 'com.grabtaxi.passenger'

processed_review_ids = set()

HISTORICAL_BATCH_SIZE = 2000
HISTORICAL_COLLECTION_DELAY_SECONDS = 5 
MAX_HISTORICAL_REVIEWS_TO_COLLECT = 450000 

print(f"Starting to collect reviews for app ID: {GRAB_APP_ID} and stream to Kafka topic: {KAFKA_TOPIC}")


def get_historical_reviews_and_send_to_kafka(app_id, lang='malay', country='my', batch_size=2000, max_reviews=None):
    current_continuation_token = None
    collected_count = 0
    
    print(f"Starting historical collection for {app_id} (lang={lang}, country={country})...")

    while True:
        try:
            result, current_continuation_token = reviews(
                app_id,
                lang=lang,
                country=country,
                sort=Sort.NEWEST,
                count=batch_size,
                continuation_token=current_continuation_token
            )

            if not result:
                print("No more reviews found via continuation token. Historical collection complete.")
                break

            newly_sent_in_batch = 0
            for r in result:
                review_id = r.get('reviewId')
                
                if max_reviews and collected_count >= max_reviews:
                    print(f"Reached max_reviews limit of {max_reviews}. Stopping historical collection.")
                    return collected_count 

                if review_id and review_id in processed_review_ids:
                    continue

                review_data = {
                    'app_id': GRAB_APP_ID, 'review_id': review_id, 'username': r.get('userName'),
                    'score': r.get('score'), 'content': r.get('content'),
                    'timestamp': r.get('at').isoformat() if r.get('at') else None,
                    'replyContent': r.get('replyContent'), 'repliedAt': r.get('repliedAt').isoformat() if r.get('repliedAt') else None,
                    'thumbsUpCount': r.get('thumbsUpCount'),
                }
                
                try:
                    producer.send(KAFKA_TOPIC, value=review_data)
                    if review_id:
                        processed_review_ids.add(review_id)
                    newly_sent_in_batch += 1
                    collected_count += 1
                except Exception as kafka_e:
                    print(f"Error sending historical review {review_id} to Kafka: {kafka_e}")

            producer.flush()
            print(f"Collected and sent {newly_sent_in_batch} reviews in this historical batch. Total historical sent: {collected_count}.")
            
            if max_reviews and collected_count >= max_reviews:
                print(f"Reached max_reviews limit of {max_reviews}. Stopping historical collection.")
                break
 
            if current_continuation_token is None:
                print("No more continuation token. End of available historical reviews.")
                break 

            print(f"Sleeping for {HISTORICAL_COLLECTION_DELAY_SECONDS} seconds before next historical batch...")
            time.sleep(HISTORICAL_COLLECTION_DELAY_SECONDS) 

        except Exception as e:
            print(f"An error occurred during historical collection: {e}")
            time.sleep(30) 
            break 

    return collected_count


try:
    print("\n--- Starting HISTORICAL COLLECTION PHASE ---")
    total_historical_collected = get_historical_reviews_and_send_to_kafka(
        GRAB_APP_ID, 
        lang='en', 
        country='my', 
        batch_size=HISTORICAL_BATCH_SIZE, 
        max_reviews=MAX_HISTORICAL_REVIEWS_TO_COLLECT
    )
    print(f"--- HISTORICAL COLLECTION PHASE Finished. Total: {total_historical_collected} reviews. ---")
    print("Producer has completed its task and will now exit.")

except KeyboardInterrupt:
    print("\nProducer stopped by user (Ctrl+C).")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
finally:
    producer.close()
    print("Kafka Producer closed.")
