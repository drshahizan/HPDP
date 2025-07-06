# spark_kafka_consumer.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, udf
from pyspark.sql.types import StructType, StringType
import tensorflow as tf
import pickle
import numpy as np

# ✅ Load tokenizer and encoder from local path
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# ✅ Load trained LSTM model
model = tf.keras.models.load_model('sentiment_lstm_model.h5')

# ✅ Create Spark session with Kafka support
spark = SparkSession.builder \
    .appName("KafkaReviewConsumer") \
    .getOrCreate()

# ✅ Define the schema of incoming Kafka JSON
schema = StructType() \
    .add("app", StringType()) \
    .add("username", StringType()) \
    .add("review", StringType()) \
    .add("rating", StringType()) \
    .add("date", StringType()) \
    .add("fetched_at", StringType())

# ✅ Read from Kafka topic
df_kafka = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "review_topic") \
    .load()

# ✅ Parse JSON value
df_parsed = df_kafka.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# ✅ Define UDF for LSTM prediction
def predict_sentiment(text):
    if not text:
        return "neutral"
    sequence = tokenizer.texts_to_sequences([text])
    padded = tf.keras.preprocessing.sequence.pad_sequences(sequence, maxlen=100)
    prediction = model.predict(padded)
    return label_encoder.inverse_transform([np.argmax(prediction)])[0]

sentiment_udf = udf(predict_sentiment, StringType())

# ✅ Add sentiment prediction
df_with_sentiment = df_parsed.withColumn("predicted_sentiment", sentiment_udf(col("review")))

# ✅ Write to console
query = df_with_sentiment.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()