'''
import json
import time
from kafka import KafkaProducer
from google_play_scraper import reviews, Sort

# 1. Connect to your local Kafka cluster
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 2. Set the target app
# 'com.grabtaxi.passenger' = Grab
# 'my.gov.malaysia.mysejahtera' = MySejahtera
# 'my.com.tngdigital.ewallet' = Touch 'n Go eWallet
app_package = 'com.grabtaxi.passenger'

print(f"Connecting to Google Play Store to fetch {app_package}...")

# 3. Scrape the live data (Bypassing BeautifulSoup entirely!)
result, continuation_token = reviews(
    app_package,
    lang='en',          # We want English reviews for Syahmi's NLP model
    country='my',       # Target the Malaysian app store
    sort=Sort.NEWEST,   # Get the most recent reviews
    count=100           # Grab 100 reviews for this batch
)

print(f"Successfully scraped {len(result)} reviews. Streaming to Kafka...\n")

# 4. Stream the data into Kafka one by one
for review in result:
    # Package only the data we care about
    clean_data = {
        "user": review['userName'],
        "score": review['score'], # The 1-5 star rating
        "text": review['content'].replace('\n', ' ') # Clean out weird line breaks
    }
    
    # Push into the 'tweets' topic
    producer.send('tweets', value=clean_data)
    
    # Print to your terminal so you can watch it work
    print(f"Sent: {clean_data['score']}⭐ | {clean_data['text'][:75]}...")
    
    # Pause for 1 second to simulate a realistic live data stream
    time.sleep(1)

producer.flush()
print("\nBatch complete! WebMiner Ingestion Pipeline is a success.")

'''

import json
import time
from kafka import KafkaProducer
from google_play_scraper import reviews, Sort

# 1. Bulletproof Connection to Local Kafka Server (KRaft Standalone Mode)
try:
    producer = KafkaProducer(
        bootstrap_servers=['127.0.0.1:9092'],   # Force raw local IP
        api_version=(3, 0, 0),                  # Bypass Kafka 4.x version-autodetection bug
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    print("🤖 Ingestion Pipeline: Successfully connected to Kafka Broker at 127.0.0.1:9092")
except Exception as e:
    print(f"❌ Error connecting to Kafka: {e}")
    print("Make sure your Kafka broker terminal is open and running!")
    exit(1)

# 2. Select Your Malaysian Battlefield (Uncomment the one you prefer)
# ---------------------------------------------------------------------
APP_ID = 'com.grabtaxi.passenger'             # Option A: Grab Malaysia
# APP_ID = 'my.com.tngdigital.ewallet'        # Option B: Touch 'n Go eWallet
# APP_ID = 'my.gov.malaysia.mysejahtera'      # Option C: MySejahtera
# APP_ID = 'com.maybank2u.mae'                 # Option D: MAE by Maybank
# ---------------------------------------------------------------------

print(f"📱 Data Source: Targeting Google Play App reviews for ID: '{APP_ID}'")
print("📥 Fetching live reviews from the Malaysian App Store store...")

# 3. Fetch Data Natively (Bypassing heavy browser DOM scraping rules)
TARGET_TOTAL = 20000
TARGET_PER_SCORE = TARGET_TOTAL // 5  # 4000 reviews per star rating
all_reviews = []

try:
    print(f"📥 Bypassing Google limits by iterating through 1 to 5 star ratings...\n")
    
    for score in [1, 2, 3, 4, 5]:
        print(f"⭐ Fetching {score}-Star reviews...")
        
        # Initial request for this specific star rating
        result, continuation_token = reviews(
            APP_ID,
            lang='en',
            country='my',
            sort=Sort.NEWEST,
            count=200,
            filter_score_with=score  # THE MAGIC PARAMETER
        )
        
        current_score_count = len(result)
        all_reviews.extend(result)
        
        # Loop through pages for THIS specific score until we hit 4000 or run out of pages
        while continuation_token and current_score_count < TARGET_PER_SCORE:
            print(f"   🔄 Downloaded {current_score_count}/{TARGET_PER_SCORE} {score}-star records. Fetching next page...")
            result, continuation_token = reviews(
                APP_ID,
                continuation_token=continuation_token
            )
            current_score_count += len(result)
            all_reviews.extend(result)
            time.sleep(0.5) # Anti-ban delay
            
        print(f"✅ Finished {score}-Star reviews! Total dataset size so far: {len(all_reviews)}\n")

    print(f"🚀 Successfully downloaded {len(all_reviews)} total records! Commencing high-speed stream...\n")
    
except Exception as e:
    print(f"❌ Error fetching reviews from Google Play: {e}")
    exit(1)

# 4. Continuous Live Streaming simulation into Kafka Topic 'tweets'
sent_count = 0
for review in all_reviews:
    payload = {
        "user": review.get('userName', 'Anonymous'),
        "score": review.get('score', 0),
        "text": str(review.get('content', '')).replace('\n', ' '),
        "timestamp": str(review.get('at', ''))
    }
    
    # Ship payload directly into Kafka broker bucket
    producer.send('tweets', value=payload)
    sent_count += 1
    
    # Real-time logging feedback to watch the data move
    print(f"[{sent_count}/{len(all_reviews)}] Sent ➡️ Score: {payload['score']}⭐ | User: {payload['user']} | Text: {payload['text'][:65]}...")
    
    # Fast delay: 0.05 seconds means we send 20 records per second!
    time.sleep(0.05)

# 5. Flush buffer and clean up connection handles
producer.flush()
print("\n🏁 Batch complete! WebMiner Ingestion Pipeline is 100% operational.")