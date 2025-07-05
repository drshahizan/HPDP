from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, from_json
from pyspark.sql.types import StringType, StructType, StructField, IntegerType, LongType
import re
import joblib

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("YouTubeCommentsStreaming") \
    .config("spark.jars.packages", 
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.2,"
        "org.elasticsearch:elasticsearch-spark-30_2.12:8.13.4"
    ) \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Load vectorizer and model
vectorizer = joblib.load("/opt/bitnami/spark/work/model/tfidf_vectorizer.pkl")
svm_model = joblib.load("/opt/bitnami/spark/work/model/lr_sentiment_model.pkl")

# Broadcast both
vectorizer_broadcast = spark.sparkContext.broadcast(vectorizer)
svm_model_broadcast = spark.sparkContext.broadcast(svm_model)

# Kafka JSON schema
schema = StructType([
    StructField("video_id", StringType(), True),       
    StructField("title", StringType(), True),  
    StructField("published_at", StringType(), True), 
    StructField("comment_text", StringType(), True),
    StructField("likes", IntegerType(), True),
    StructField("view_count", LongType(), True)
])

# === STEP 2: Clean function ===
def clean_text(text):
    if text is None:
        return ""
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', text)  # Remove symbols/emojis
    text = re.sub(r'\s+', ' ', text).strip()  # Normalize whitespace
    return text

# Register UDF for cleaning
clean_text_udf = udf(clean_text, StringType())

# Define UDF to predict sentiment
def predict_sentiment(text):
    if text and len(text.strip()) > 2:
        try:
            X_vec = vectorizer_broadcast.value.transform([text])
            prediction = svm_model_broadcast.value.predict(X_vec)
            if prediction[0] == 1:
                return "POSITIVE"
            elif prediction[0] == 0:
                return "NEGATIVE"
            else:
                return "NEUTRAL"
        except Exception as e:
            print(f"Prediction error: {e}")
            return "error"
    return "NEUTRAL"


# Register UDF for prediction
predict_udf = udf(predict_sentiment, StringType())

# === STEP 3: Streaming from Kafka ===
raw_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:29092") \
    .option("subscribe", "youtube-comments") \
    .option("startingOffsets", "latest") \
    .load()

# Convert Kafka value to string and parse JSON
json_df = raw_df.selectExpr("CAST(value AS STRING)")
parsed_df = json_df.select(from_json(col("value"), schema).alias("data")).select("data.*")

# === STEP 4: Apply cleaning ===
clean_df = parsed_df.withColumn("clean_text", clean_text_udf(col("comment_text")))

# === STEP 5: Predict sentiment ===
result_df = clean_df.withColumn("sentiment", predict_udf(col("clean_text")))


# === STEP 7: Write to Elasticsearch ===
es_query = result_df.writeStream \
    .outputMode("append") \
    .format("org.elasticsearch.spark.sql") \
    .option("es.nodes", "elasticsearch") \
    .option("es.port", "9200") \
    .option("checkpointLocation", "/tmp/spark_checkpoint") \
    .option("es.resource", "youtube-comments6-index") \
    .start()

# Wait for both streams
es_query.awaitTermination()
