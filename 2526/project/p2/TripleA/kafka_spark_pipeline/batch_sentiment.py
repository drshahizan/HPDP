import pandas as pd
from model_loader import predict
from elasticsearch import Elasticsearch
import time
import os
from deep_translator import GoogleTranslator

def translate_to_english(text):
    try:
        translated = GoogleTranslator(source="auto", target="en").translate(text)
        return translated
    except Exception as e:
        print(f"Translation failed: {e}")
        return text

print("Batch processing start")
start = time.time()

es = Elasticsearch("http://localhost:9200")

# Check if file exists
csv_file = "comments.csv"
if not os.path.isfile(csv_file):
    print(f"Error: '{csv_file}' not found. Please run the scraper first to generate the CSV.")
    exit(1)

df = pd.read_csv(csv_file)

if df.empty:
    print(f"Error: '{csv_file}' is empty. No data to process.")
    exit(1)

print(f"Loaded {len(df)} records from '{csv_file}'")

for _, row in df.iterrows():
    translated = translate_to_english(row["comment"])
    label, confidence = predict(translated)

    doc = {
        "comment": row["comment"],
        "comment_translated": translated,
        "author": row["author"],
        "timestamp": row["timestamp"],
        "sentiment_label": label,
        "sentiment_confidence": confidence,
        "mode": "batch"
    }

    es.index(index="youtube_sentiment", document=doc)

end = time.time()
duration = end - start
throughput = len(df) / duration

es.index(index="pipeline_metrics", document={
    "mode": "batch",
    "total_records": len(df),
    "duration_seconds": duration,
    "throughput_per_second": throughput,
    "timestamp": pd.Timestamp.now().isoformat()
})

print(f"Batch processing completed")
print(f"Total records : {len(df)}")
print(f"Duration      : {duration:.2f}s")
print(f"Throughput    : {throughput:.2f} records/sec")