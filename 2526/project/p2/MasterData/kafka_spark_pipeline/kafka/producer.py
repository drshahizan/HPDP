import pandas as pd
from kafka import KafkaProducer
import json
import time

# Load your comments dataset (assume the same as earlier used: TrainVersion.xlsx)
df = pd.read_excel("data/TrainVersion.xlsx")

# Only keep necessary columns
df = df[["text"]]

# Clean nulls or empty
df = df.dropna()
df = df[df["text"].str.strip() != ""]

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

topic = "sentiment_comments"

print("Sending comments to Kafka...")
for index, row in df.iterrows():
    comment = row["text"]
    message = {"text": comment}
    producer.send(topic, value=message)
    print(f"Sent: {message}")
    time.sleep(0.1)  # simulate real-time delay

print("All comments sent.")
producer.flush()
