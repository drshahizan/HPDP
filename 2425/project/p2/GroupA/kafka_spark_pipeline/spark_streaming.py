import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # Suppress TensorFlow INFO and WARNING messages

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, from_json
from pyspark.sql.types import StringType, StructType, StructField, IntegerType, FloatType
import re
import joblib
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences

# --- Configuration ---
KAFKA_TOPIC = "reddit-comments"
KAFKA_SERVER = "kafka:29092"
ELASTICSEARCH_NODE = "elasticsearch"
ELASTICSEARCH_PORT = "9200"
ELASTICSEARCH_INDEX = "reddit-comments-lstm"
CHECKPOINT_LOCATION = "/tmp/spark_checkpoint_reddit_lstm"

# Define a maximum sequence length for padding.
# This should match the length used during model training.
MAX_SEQUENCE_LENGTH = 150 

# --- Model Loading and Broadcasting ---
# Load the tokenizer and the Keras model on the driver
tokenizer = joblib.load("/opt/bitnami/spark/work/models/tokenizer.pkl")
model = tf.keras.models.load_model("/opt/bitnami/spark/work/models/lstm_sentiment_model.h5")

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("RedditSentimentLSTM") \
    .config("spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.2,"
            "org.elasticsearch:elasticsearch-spark-30_2.12:8.13.4") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Broadcast the tokenizer and the model's weights to all worker nodes
tokenizer_broadcast = spark.sparkContext.broadcast(tokenizer)
model_weights_broadcast = spark.sparkContext.broadcast(model.get_weights())

# --- Schema Definition for Kafka Messages ---
schema = StructType([
    StructField("post_id", StringType(), True),
    StructField("post_title", StringType(), True),
    StructField("comment_id", StringType(), True),
    StructField("comment_body", StringType(), True),
    StructField("comment_score", IntegerType(), True),
    StructField("created_utc", FloatType(), True)
])

# --- Text Cleaning Function ---
def clean_text(text):
    if text is None:
        return ""
    text = str(text).lower()
    text = re.sub(r"https[^\s]+|www[^\s]+", '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)       # Remove special characters/emojis
    text = re.sub(r'\s+', ' ', text).strip()         # Normalize whitespace
    return text

clean_text_udf = udf(clean_text, StringType())


# --- Sentiment Prediction UDF for LSTM Model ---
def predict_sentiment_lstm(text_series):
    # This function is designed to work with Pandas UDFs for efficiency
    # but a standard UDF is used here for simplicity.
    
    # 1. Get the broadcasted tokenizer and weights
    local_tokenizer = tokenizer_broadcast.value
    local_weights = model_weights_broadcast.value
    
    # 2. Re-create the model architecture and set the broadcasted weights
    #    This avoids serializing the entire model object.
    local_model = tf.keras.models.load_model("/opt/bitnami/spark/work/models/lstm_sentiment_model.h5")
    local_model.set_weights(local_weights)

    predictions = []
    for text in text_series:
        if not text or len(text.strip()) < 2:
            predictions.append("NEUTRAL")
            continue
        try:
            # 3. Tokenize and pad the text
            sequence = local_tokenizer.texts_to_sequences([text])
            padded_sequence = pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH)

            # 4. Make a prediction
            prediction_prob = local_model.predict(padded_sequence, verbose=0)[0][0]

            # 5. Interpret the prediction
            if prediction_prob > 0.5:
                predictions.append("POSITIVE")
            else:
                predictions.append("NEGATIVE")
        except Exception as e:
            print(f"Prediction error: {e}")
            predictions.append("ERROR")
            
    return predictions

# We need to wrap the function slightly for a standard UDF
def predict_sentiment(text):
    return predict_sentiment_lstm([text])[0]

predict_udf = udf(predict_sentiment, StringType())


# --- Spark Streaming Pipeline ---
print("🚀 Reading from Kafka...")
# 1. Read from Kafka
raw_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_SERVER) \
    .option("subscribe", KAFKA_TOPIC) \
    .option("startingOffsets", "latest") \
    .load()

# 2. Decode the Kafka message and parse the JSON
json_df = raw_df.selectExpr("CAST(value AS STRING)")
parsed_df = json_df.select(from_json(col("value"), schema).alias("data")).select("data.*")

# Add this to see the raw JSON from Kafka in your console
json_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

parsed_df = json_df.select(from_json(col("value"), schema).alias("data")).select("data.*")

# 3. Clean the comment text
print("🚀 Cleaning comments...")
clean_df = parsed_df.withColumn("clean_comment", clean_text_udf(col("comment_body")))
clean_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

print("🚀 Streaming to console started...")

# 4. Predict sentiment using the LSTM model
print("🚀 Predicting sentiment...")
result_df = clean_df.withColumn("sentiment", predict_udf(col("clean_comment")))

print("🚀 Starting Spark writeStream to Elasticsearch...")
# --- Write to Elasticsearch ---
es_query = result_df.writeStream \
    .outputMode("append") \
    .format("org.elasticsearch.spark.sql") \
    .option("es.nodes", ELASTICSEARCH_NODE) \
    .option("es.port", ELASTICSEARCH_PORT) \
    .option("checkpointLocation", CHECKPOINT_LOCATION) \
    .option("es.resource", ELASTICSEARCH_INDEX) \
    .start()
    
print("✅ writeStream started. Awaiting termination...")

es_query.awaitTermination()