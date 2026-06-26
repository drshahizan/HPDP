import json
import time
from google_play_scraper import reviews, Sort
from kafka import KafkaProducer

# ==========================================
# CONFIGURATION
# ==========================================

FOODPANDA_APP_ID = 'com.global.foodpanda.android'
KAFKA_TOPIC = 'foodpanda_reviews'
KAFKA_BROKER = 'localhost:9092'

HISTORICAL_BATCH_SIZE = 2000
HISTORICAL_COLLECTION_DELAY_SECONDS = 5
MAX_HISTORICAL_REVIEWS_TO_COLLECT = 50000

# ==========================================
# KAFKA PRODUCER
# ==========================================

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8'),
    acks='all',
    retries=3,
    linger_ms=10
)

processed_review_ids = set()

print(f"Starting Foodpanda review collection → Kafka topic: {KAFKA_TOPIC}")


# ==========================================
# SCRAPE + SEND TO KAFKA
# ==========================================

def get_historical_reviews_and_send_to_kafka(app_id, lang='en', country='my', batch_size=2000, max_reviews=None):
    current_continuation_token = None
    collected_count = 0

    print(f"\nStarting collection for {app_id} (lang={lang}, country={country})...")

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
                print("No more reviews found.")
                break

            newly_sent_in_batch = 0

            for r in result:
                review_id = r.get('reviewId')

                if max_reviews and collected_count >= max_reviews:
                    print(f"Reached limit of {max_reviews}. Stopping.")
                    return collected_count

                if review_id and review_id in processed_review_ids:
                    continue

                review_data = {
                    'review_id':   review_id,
                    'review_text': r.get('content'),
                    'username':    r.get('userName'),
                    'rating':      str(r.get('score')) if r.get('score') is not None else None,
                    'review_date': r.get('at').isoformat() if r.get('at') else None,
                    'thumbs_up':   r.get('thumbsUpCount'),
                    'reply':       r.get('replyContent'),
                    'replied_at':  r.get('repliedAt').isoformat() if r.get('repliedAt') else None,
                }

                try:
                    producer.send(KAFKA_TOPIC, value=review_data)
                    if review_id:
                        processed_review_ids.add(review_id)
                    newly_sent_in_batch += 1
                    collected_count += 1
                except Exception as kafka_e:
                    print(f"Error sending review {review_id} to Kafka: {kafka_e}")

            producer.flush()
            print(f"Sent {newly_sent_in_batch} reviews in batch. Total sent: {collected_count}.")

            if max_reviews and collected_count >= max_reviews:
                print(f"Reached limit of {max_reviews}. Stopping.")
                break

            if current_continuation_token is None:
                print("No more continuation token. End of available reviews.")
                break

            print(f"Sleeping {HISTORICAL_COLLECTION_DELAY_SECONDS}s before next batch...")
            time.sleep(HISTORICAL_COLLECTION_DELAY_SECONDS)

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(30)
            break

    return collected_count


# ==========================================
# RUN — English + Malay only
# ==========================================

try:
    print("\n--- Collecting ENGLISH (MY) reviews ---")
    total_en = get_historical_reviews_and_send_to_kafka(
        FOODPANDA_APP_ID,
        lang='en',
        country='my',
        batch_size=HISTORICAL_BATCH_SIZE,
        max_reviews=MAX_HISTORICAL_REVIEWS_TO_COLLECT // 2
    )
    print(f"English collection done. Total: {total_en} reviews.")

    print("\n--- Collecting MALAY (MY) reviews ---")
    total_ms = get_historical_reviews_and_send_to_kafka(
        FOODPANDA_APP_ID,
        lang='ms',
        country='my',
        batch_size=HISTORICAL_BATCH_SIZE,
        max_reviews=MAX_HISTORICAL_REVIEWS_TO_COLLECT // 2
    )
    print(f"Malay collection done. Total: {total_ms} reviews.")

    print(f"\n--- COLLECTION COMPLETE. Grand total: {total_en + total_ms} reviews. ---")

except KeyboardInterrupt:
    print("\nProducer stopped by user (Ctrl+C).")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
finally:
    producer.close()
    print("Kafka Producer closed.")