from kafka import KafkaProducer
from google_play_scraper import reviews, Sort
import json
import time
from datetime import datetime

# ✅ Kafka setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# ✅ Apps to track
apps = {
    'TouchNGo': 'my.com.tngdigital.ewallet',
    'Boost': 'my.com.myboost',
    'Grab': 'com.grabtaxi.passenger',
    'Setel': 'com.setel.mobile',
    'Shopee': 'com.shopeepay.my',
}

# ✅ Sent review cache to avoid duplicates
sent_reviews = set()

# ✅ Helper: Generate unique ID
def make_review_id(app, username, date):
    return f"{app}_{username}_{date}"

print("🚀 Starting real-time streaming to Kafka (every 60s)...\n")

while True:
    for app_name, package_name in apps.items():
        try:
            result, _ = reviews(
                package_name,
                lang='ms',  # Bahasa Melayu only
                country='my',
                sort=Sort.NEWEST,
                count=100  # max possible to catch up on latest reviews
            )

            for r in result:
                if not r.get('content'):
                    continue

                review_date = r['at'].strftime('%Y-%m-%d %H:%M:%S')
                review_id = make_review_id(app_name, r['userName'], review_date)

                if review_id in sent_reviews:
                    continue

                review_data = {
                    'app': app_name,
                    'username': r['userName'],
                    'review': r['content'].strip(),
                    'rating': r['score'],
                    'date': review_date,
                    'fetched_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }

                producer.send('review_topic', value=review_data)
                sent_reviews.add(review_id)

                print(f"✅ Sent: [{app_name}] {r['userName']} ({r['score']}) - {review_date}")

        except Exception as e:
            print(f"⚠️ Error scraping {app_name}: {e}")

    print("⏳ Sleeping 60 seconds before next fetch...\n")
    time.sleep(60)