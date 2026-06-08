import time
import json
import os
import pandas as pd
from kafka import KafkaProducer
from google_play_scraper import reviews, Sort

# ==========================================
# 1. CONFIGURATION
# ==========================================
TNG_APP_ID = 'my.com.tngdigital.ewallet'
KAFKA_TOPIC = 'tng_reviews'
KAFKA_BROKER = '127.0.0.1:9092'
CSV_FILENAME = 'tng_raw_data.csv'
HISTORICAL_TARGET = 50000

# ==========================================
# 2. INITIALIZE KAFKA PRODUCER
# ==========================================
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    api_version=(0, 10, 2),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

processed_review_ids = set()

# Load existing IDs from CSV if it exists (to prevent duplicates across runs)
if os.path.exists(CSV_FILENAME):
    existing_df = pd.read_csv(CSV_FILENAME)
    processed_review_ids.update(existing_df['review_id'].tolist())
    print(f"Loaded {len(processed_review_ids)} existing IDs from {CSV_FILENAME}")

def save_and_send(review_list):
    """Saves reviews to CSV and sends them to Kafka"""
    new_data = []
    
    for r in review_list:
        rid = r['reviewId']
        if rid not in processed_review_ids:
            payload = {
                "app_id": TNG_APP_ID,
                "review_id": rid,
                "username": r['userName'],
                "score": r['score'],
                "content": r['content'],
                "timestamp": str(r['at']),
                "thumbsUpCount": r['thumbsUpCount']
            }
            
            # 1. Send to Kafka
            producer.send(KAFKA_TOPIC, value=payload)
            
            # 2. Add to list for CSV
            new_data.append(payload)
            processed_review_ids.add(rid)

    # 3. Append to CSV
    if new_data:
        df = pd.DataFrame(new_data)
        # header=False if file exists, so we don't repeat headers
        file_exists = os.path.isfile(CSV_FILENAME)
        df.to_csv(CSV_FILENAME, mode='a', index=False, header=not file_exists)
        return len(new_data)
    return 0

# ==========================================
# 3. EXECUTION LOGIC
# ==========================================
if __name__ == "__main__":
    try:
        # Phase 1: Bulk Load
        print(f"🚀 Fetching up to {HISTORICAL_TARGET} reviews for {CSV_FILENAME}...")
        token = None
        total_saved = 0
        
        while total_saved < HISTORICAL_TARGET:
            result, token = reviews(TNG_APP_ID, lang='en', country='my', 
                                    sort=Sort.NEWEST, count=1000, continuation_token=token)
            if not result: break
            
            batch_count = save_and_send(result)
            total_saved += batch_count
            print(f"📊 Progress: {len(processed_review_ids)} total reviews in CSV.")
            if not token: break
            time.sleep(1)

        # Phase 2: Real-Time Listening
        print(f"📡 Real-time mode active. Monitoring for new TNG reviews...")
        while True:
            result, _ = reviews(TNG_APP_ID, lang='en', country='my', sort=Sort.NEWEST, count=50)
            new_count = save_and_send(result)
            if new_count > 0:
                print(f"✨ {new_count} new reviews added to CSV and Kafka!")
            time.sleep(15)

    except KeyboardInterrupt:
        print("\n🛑 Stopped by user.")
    finally:
        producer.close()