import json
import time
import pandas as pd
from kafka import KafkaProducer

DATA_PATH = "data/grab_reviews_preprocessed.csv"
TOPIC_NAME = "grab-reviews"
LIMIT_MESSAGES = 50   # first test only send 50 reviews

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode("utf-8")
)

df = pd.read_csv(DATA_PATH)

print(f"Loaded {len(df)} Grab reviews.")
print(f"Streaming to Kafka topic: {TOPIC_NAME}")

for index, row in df.head(LIMIT_MESSAGES).iterrows():
    message = {
        "review_id": int(index),
        "content": str(row["content"]),
        "processed_text": str(row["processed_text"]),
        "true_sentiment": str(row["sentiment"]),
        "source": "Grab Malaysia Reviews",
        "event_time": pd.Timestamp.now().isoformat()
    }

    producer.send(TOPIC_NAME, value=message)

    print(f"Sent review {index}: {message['processed_text'][:80]}...")
    time.sleep(0.2)

producer.flush()
producer.close()

print("Kafka producer finished sending messages.")