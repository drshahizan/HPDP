# ============================================================
# Cell W3-3: Create Kafka topic
# ============================================================
import subprocess
import time
import os

KAFKA_DIR = "/content/kafka_2.13-3.7.1"

# Delete old topic
subprocess.run(
    f"{KAFKA_DIR}/bin/kafka-topics.sh --delete "
    f"--topic airasia-reviews "
    f"--bootstrap-server localhost:9092",
    shell=True, capture_output=True
)
time.sleep(3)

# Create topic
result = subprocess.run(
    f"{KAFKA_DIR}/bin/kafka-topics.sh --create "
    f"--topic airasia-reviews "
    f"--bootstrap-server localhost:9092 "
    f"--partitions 1 --replication-factor 1",
    shell=True, capture_output=True, text=True
)
print(result.stdout)
print(result.stderr)
time.sleep(2)

# Verify
verify = subprocess.run(
    f"{KAFKA_DIR}/bin/kafka-topics.sh --list "
    f"--bootstrap-server localhost:9092",
    shell=True, capture_output=True, text=True
)
topics = verify.stdout.strip()
print(f"Active topics: {topics}")

if "airasia-reviews" in topics:
    print("✅ Topic 'airasia-reviews' ready.")
else:
    print("❌ Topic creation failed — re-run W3-2 first.") 


# ============================================================
# Cell W3-4: Setup SQLite database for storing results
# ============================================================
import sqlite3
import os

DB_PATH = "/content/data/airasia_sentiment.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Drop and recreate for fresh start
cursor.execute("DROP TABLE IF EXISTS sentiment_results")
cursor.execute("""
    CREATE TABLE sentiment_results (
        id                  INTEGER PRIMARY KEY AUTOINCREMENT,
        reviewId            TEXT,
        review_text         TEXT,
        processed_text      TEXT,
        star_rating         INTEGER,
        actual_sentiment    TEXT,
        predicted_sentiment TEXT,
        confidence          REAL,
        review_date         TEXT,
        processed_at        REAL,
        model_used          TEXT
    )
""")
conn.commit()
conn.close()

print(f"✅ SQLite database ready at: {DB_PATH}")
print("✅ Table 'sentiment_results' created.") 


# ============================================================
# Cell W3-7: Kafka Producer — stream CSV rows into Kafka
# ============================================================
import pandas as pd
import json
import time
from kafka import KafkaProducer

df = pd.read_csv('/content/data/cleaned_data.csv')
df_stream = df[['reviewId', 'review_text', 'processed_text',
                 'star_rating', 'sentiment', 'review_date']].copy()
df_stream = df_stream.dropna(subset=['processed_text'])
df_stream = df_stream[df_stream['processed_text'].str.strip() != '']

print(f"Total reviews available: {len(df_stream):,}")

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

STREAM_LIMIT = 25000
DELAY        = 0.05
sent         = 0

print(f"📡 Streaming {STREAM_LIMIT} reviews into Kafka...")

for _, row in df_stream.head(STREAM_LIMIT).iterrows():
    message = {
        'reviewId'        : str(row['reviewId']),
        'review_text'     : str(row['review_text']),
        'processed_text'  : str(row['processed_text']),
        'star_rating'     : int(row['star_rating']),
        'actual_sentiment': str(row['sentiment']),
        'review_date'     : str(row['review_date']),
        'timestamp'       : time.time()
    }
    producer.send('airasia-reviews', value=message)
    sent += 1

    if sent % 100 == 0:
        print(f"  ✅ Sent {sent} / {STREAM_LIMIT} reviews...")

    time.sleep(DELAY)

producer.flush()
producer.close()
print(f"\n✅ Done! {sent} reviews sent to Kafka topic 'airasia-reviews'.")


# ============================================================
# Cell W3-8: Spark Structured Streaming Pipeline
# Reads from Kafka → predicts sentiment → stores to SQLite
# ============================================================
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import (StringType, StructType, StructField,
                                IntegerType, FloatType)
import joblib
import sqlite3
import time
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# ── Load models ──────────────────────────────────────────────
print("📦 Loading model artifacts...")
nb_model = joblib.load('/content/models/naive_bayes_model.pkl')
tfidf    = joblib.load('/content/models/tfidf_vectorizer.pkl')
print("✅ Models loaded.")

# ── Preprocessing ────────────────────────────────────────────
stop_words = set(stopwords.words('english'))
negations  = {'no', 'not', 'nor', "n't", 'never', 'none'}
stop_words = stop_words - negations
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(t) for t in tokens
              if t not in stop_words and len(t) > 1]
    return ' '.join(tokens)

DB_PATH = "/content/data/airasia_sentiment.db"

# ── Kafka Schema ─────────────────────────────────────────────
schema = StructType([
    StructField("reviewId",         StringType()),
    StructField("review_text",      StringType()),
    StructField("processed_text",   StringType()),
    StructField("star_rating",      IntegerType()),
    StructField("actual_sentiment", StringType()),
    StructField("review_date",      StringType()),
    StructField("timestamp",        FloatType()),
])

# ── Read stream from Kafka ───────────────────────────────────
print("📡 Connecting to Kafka...")
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "airasia-reviews") \
    .option("startingOffsets", "earliest") \
    .load()

parsed_df = kafka_df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# ── Predict and store each batch ─────────────────────────────
def predict_and_store(batch_df, batch_id):
    if batch_df.count() == 0:
        return

    rows = batch_df.collect()
    print(f"\n🔄 Batch {batch_id} — {len(rows)} reviews...")

    records = []
    for row in rows:
        try:
            text = row['processed_text'] if row['processed_text'] \
                   else preprocess(row['review_text'])

            text_tfidf = tfidf.transform([text])
            pred_label = nb_model.predict(text_tfidf)[0]
            pred_proba = nb_model.predict_proba(text_tfidf)[0]
            confidence = float(max(pred_proba))

            records.append((
                str(row['reviewId']),
                str(row['review_text']),
                str(text),
                int(row['star_rating']) if row['star_rating'] else 0,
                str(row['actual_sentiment']),
                str(pred_label),
                confidence,
                str(row['review_date']),
                time.time(),
                "naive_bayes"
            ))
        except Exception as e:
            print(f"  ⚠️  Skipped row: {e}")

    # Store to SQLite
    conn = sqlite3.connect(DB_PATH)
    conn.executemany("""
        INSERT INTO sentiment_results
        (reviewId, review_text, processed_text, star_rating,
         actual_sentiment, predicted_sentiment, confidence,
         review_date, processed_at, model_used)
        VALUES (?,?,?,?,?,?,?,?,?,?)
    """, records)
    conn.commit()
    conn.close()
    print(f"  ✅ Batch {batch_id} — {len(records)} reviews stored.")

# ── Start streaming ──────────────────────────────────────────
print("🚀 Starting Spark Streaming pipeline...")
query = parsed_df.writeStream \
    .foreachBatch(predict_and_store) \
    .outputMode("append") \
    .trigger(processingTime='10 seconds') \
    .start()

print("✅ Pipeline LIVE — processing for 90 seconds...\n")
query.awaitTermination(timeout=90)
print("\n✅ Streaming job completed.")


# ============================================================
# Cell W3-9: Verify results stored in SQLite
# ============================================================
import sqlite3
import pandas as pd

DB_PATH = "/content/data/airasia_sentiment.db"
conn = sqlite3.connect(DB_PATH)

# Total count
total = pd.read_sql("SELECT COUNT(*) as total FROM sentiment_results", conn)
print(f"Total reviews stored: {total['total'][0]:,}")

# Sentiment distribution
print("\n=== Predicted Sentiment Distribution ===")
dist = pd.read_sql("""
    SELECT predicted_sentiment,
           COUNT(*) as count,
           ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(), 1) as pct
    FROM sentiment_results
    GROUP BY predicted_sentiment
    ORDER BY count DESC
""", conn)
print(dist.to_string(index=False))

# Accuracy vs actual labels
print("\n=== Prediction Accuracy ===")
acc = pd.read_sql("""
    SELECT
        ROUND(100.0 * SUM(CASE WHEN predicted_sentiment = actual_sentiment
                          THEN 1 ELSE 0 END) / COUNT(*), 2) as accuracy_pct,
        COUNT(*) as total
    FROM sentiment_results
""", conn)
print(acc.to_string(index=False))

# Sample results
print("\n=== 5 Sample Results ===")
samples = pd.read_sql("""
    SELECT review_text, actual_sentiment,
           predicted_sentiment, confidence
    FROM sentiment_results
    LIMIT 5
""", conn)
for _, row in samples.iterrows():
    print(f"\n  Review    : {str(row['review_text'])[:80]}...")
    print(f"  Actual    : {row['actual_sentiment']}")
    print(f"  Predicted : {row['predicted_sentiment']}")
    print(f"  Confidence: {row['confidence']:.2%}")

conn.close()

# Export to CSV for dashboard use
df_results = pd.read_sql("SELECT * FROM sentiment_results",
                          sqlite3.connect(DB_PATH))
df_results.to_csv('/content/data/streaming_results.csv', index=False)
print("\n✅ Results exported to /content/data/streaming_results.csv")
