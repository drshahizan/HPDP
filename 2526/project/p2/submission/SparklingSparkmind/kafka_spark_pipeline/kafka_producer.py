import json
import pandas as pd
import time
from kafka import KafkaProducer
from datetime import datetime

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    acks='all',
    retries=3
)

# Load cleaned data
try:
    df = pd.read_csv(r'C:\Users\safiy\Project-SentimentAnalysis\data\cleaned_data.csv')
    print(f"✓ Loaded {len(df)} reviews from cleaned_data.csv")
except FileNotFoundError:
    print("❌ ERROR: cleaned_data.csv not found!")
    print("Ask Member 1 for the cleaned data file.")
    exit(1)

# Verify data structure
required_cols = ['review_id', 'cleaned_text', 'sentiment', 'review_date']
missing = [col for col in required_cols if col not in df.columns]
if missing:
    print(f"❌ ERROR: Missing columns: {missing}")
    exit(1)

print(f"Sentiment distribution in data:")
print(df['sentiment'].value_counts())
print()

# Send each review to Kafka
print("Sending reviews to Kafka topic 'sentiment-input'...")
for idx, row in df.iterrows():
    message = {
        'review_id': str(row['review_id']),
        'review_text': str(row['review_text']),  # Original text for context
        'cleaned_text': str(row['cleaned_text']),  # Cleaned text for prediction
        'true_sentiment': str(row['sentiment']),  # Ground truth (for evaluation)
        'star_rating': int(row['star_rating']),
        'review_date': str(row['review_date']),
        'source': 'shopee_reviews'
    }
    
    producer.send('sentiment-input', value=message)
    
    if (idx + 1) % 200 == 0:
        print(f"  → Sent {idx + 1}/{len(df)} reviews")
    
    time.sleep(0.02)  # 20ms delay per review

producer.flush()
producer.close()

print(f"\n✓ Successfully sent {len(df)} reviews to Kafka")
print("\nKafka producer finished.")
print("The streaming job will now consume and classify these reviews.")
