import sys
import pickle
import json
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, from_json, struct, to_json, current_timestamp, 
    udf, explode, split, when, lit
)
from pyspark.sql.types import StructType, StructField, StringType, LongType, DoubleType
import time
import os
import requests

print("=" * 70)
print("SPARK STREAMING JOB - SENTIMENT ANALYSIS (3-CLASS)")
print("Shopee Reviews: Negative | Neutral | Positive [SINGLE-MODEL RUN]")
print("=" * 70)

# [1/5] Initialize Spark Session (Configured for Spark 4.x compatibility)
print("\n[1/5] Initializing Spark Session...")
spark = SparkSession.builder \
    .appName("SentimentAnalysisStreaming") \
    .config("spark.streaming.kafka.maxRatePerPartition", "500") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")
print("✓ Spark Session created")

# [2/5] Load trained models
print("\n[2/5] Loading trained models from Member 2...")
try:
    # Load Naive Bayes model + vectorizer
    with open('naive_bayes_model.pkl', 'rb') as f:
        nb_saved = pickle.load(f)
        nb_model = nb_saved['model']
        tfidf_vectorizer = nb_saved['vectorizer']
    print("✓ Naive Bayes model + TF-IDF vectorizer loaded")
    
    print("ℹ LSTM model skipped (TensorFlow disabled)")
    
    # Label mapping (from Member 2's training: 0=negative, 1=neutral, 2=positive)
    label_to_sentiment = {0: 'negative', 1: 'neutral', 2: 'positive'}
    print("✓ Label mappings ready")
    
except FileNotFoundError as e:
    print(f"❌ ERROR: Model files not found!\n{e}")
    print("\nMake sure you have:")
    print("  - naive_bayes_model.pkl")
    sys.exit(1)

# Define Kafka message schema
kafka_schema = StructType([
    StructField("review_id", StringType()),
    StructField("review_text", StringType()),
    StructField("cleaned_text", StringType()),
    StructField("true_sentiment", StringType()),  # Ground truth
    StructField("star_rating", LongType()),
    StructField("review_date", StringType()),
    StructField("source", StringType())
])

# [3/5] Read from Kafka
print("\n[3/5] Connecting to Kafka topic 'sentiment-input'...")
try:
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "sentiment-input") \
        .option("startingOffsets", "earliest") \
        .option("failOnDataLoss", "false") \
        .load()
    print("✓ Connected to Kafka")
except Exception as e:
    print(f"❌ ERROR: Cannot connect to Kafka\n{e}")
    sys.exit(1)

# Parse JSON payloads from Kafka
parsed_df = df.select(
    from_json(col("value").cast("string"), kafka_schema).alias("data")
).select("data.*")

# Broadcast models to workers
nb_model_broadcast = spark.sparkContext.broadcast((nb_model, tfidf_vectorizer))
label_map_broadcast = spark.sparkContext.broadcast(label_to_sentiment)

# === NAIVE BAYES PREDICTIONS USER DEFINED FUNCTIONS ===
@udf(returnType=StringType())
def predict_naive_bayes(text):
    """Predict sentiment using Naive Bayes with TF-IDF"""
    try:
        model, vectorizer = nb_model_broadcast.value
        vec = vectorizer.transform([text])
        pred_label = model.predict(vec)[0]
        label_map = label_map_broadcast.value
        return label_map.get(int(pred_label), 'unknown')
    except Exception as e:
        return 'error'

@udf(returnType=DoubleType())
def predict_naive_bayes_confidence(text):
    """Get confidence score for NB prediction"""
    try:
        model, vectorizer = nb_model_broadcast.value
        vec = vectorizer.transform([text])
        proba = model.predict_proba(vec)[0]
        return float(max(proba))
    except Exception as e:
        return 0.0

# [4/5] Apply predictions and transform data
print("\n[4/5] Building prediction pipeline...")
predictions_df = parsed_df \
    .withColumn("nb_sentiment", predict_naive_bayes(col("cleaned_text"))) \
    .withColumn("nb_confidence", predict_naive_bayes_confidence(col("cleaned_text"))) \
    .withColumn("lstm_sentiment", lit("Not Evaluated")) \
    .withColumn("lstm_confidence", lit(0.0)) \
    .withColumn("agreement", lit(True)) \
    .withColumn("processed_at", current_timestamp()) \
    .withColumn("is_correct_nb", col("nb_sentiment") == col("true_sentiment")) \
    .withColumn("is_correct_lstm", lit(False))

print("✓ Prediction pipeline ready")

# [5/5] Write to Elasticsearch using a custom foreachBatch handler via REST API
print("\n[5/5] Starting streaming to Elasticsearch via REST API...")

def send_batch_to_es(df, batch_id):
    """Worker function to send each micro-batch directly to ES over HTTP"""
    records = df.toJSON().collect()
    
    if not records:
        return

    # Construct the bulk index action-payload format required by Elasticsearch
    bulk_data = ""
    for record in records:
        data_dict = json.loads(record)
        review_id = data_dict.get("review_id")
        
        # Meta line specifying index and document routing ID
        bulk_data += json.dumps({"index": {"_index": "sentiment-predictions", "_id": review_id}}) + "\n"
        # Payload data line
        bulk_data += json.dumps(data_dict) + "\n"
        
    # Execute HTTP POST to Elasticsearch bulk endpoint
    try:
        url = "http://localhost:9200/_bulk"
        headers = {"Content-Type": "application/x-ndjson"}
        response = requests.post(url, data=bulk_data, headers=headers)
        if response.status_code == 200:
            print(f"✓ [Batch {batch_id}] Successfully indexed records into Elasticsearch!")
        else:
            print(f"⚠️ Batch {batch_id} ES warning: {response.text[:200]}")
    except Exception as e:
        print(f"❌ Failed to send batch {batch_id} to ES: {e}")

try:
    # Use a localized Windows directory path for checkpointing to prevent OS path errors
    query = predictions_df \
        .writeStream \
        .foreachBatch(send_batch_to_es) \
        .option("checkpointLocation", r"C:\Users\safiy\Project-SentimentAnalysis\kafka_spark_pipeline\checkpoint_es") \
        .start()
    
    print("✓ Elasticsearch REST pipeline started")
    print("\n" + "=" * 70)
    print("STREAMING ACTIVE - Processing reviews in real-time (Spark 4.x REST Mode)")
    print("=" * 70)
    print("\nDashboard: http://localhost:5601")
    print("Real-time predictions available in Elasticsearch index: sentiment-predictions")
    print("\nPress Ctrl+C to stop streaming")
    print("=" * 70 + "\n")
    
    query.awaitTermination()
    
except Exception as e:
    print(f"❌ ERROR: Cannot execute stream\n{e}")
    sys.exit(1)