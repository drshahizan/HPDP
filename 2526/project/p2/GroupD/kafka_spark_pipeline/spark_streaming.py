import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, current_timestamp, to_timestamp
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
from pyspark.ml.functions import vector_to_array
from pyspark.ml import PipelineModel
from pyspark.ml.feature import IndexToString
from pyspark.sql.functions import lower 

# --- Configuration Constants ---
KAFKA_BROKER_URL = "localhost:9092"
KAFKA_TOPIC = "grab_reviews_final"
LR_MODEL_PATH = "lr_model_score_labeling"

ES_NODES = "localhost"
ES_PORT = "9200"
ES_INDEX = "grab_reviews_sentiment"

SPARK_VERSION = "3.4.4" 

# Environment
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Spark Session with required packages
spark = SparkSession.builder \
    .appName("GrabReviewSentimentAnalysisConsumer") \
    .config("spark.jars.packages", \
                        f"org.apache.spark:spark-sql-kafka-0-10_2.12:{SPARK_VERSION}," + \
                        f"org.elasticsearch:elasticsearch-spark-30_2.12:8.17.4") \
    .config("spark.es.nodes", ES_NODES) \
    .config("spark.es.port", ES_PORT) \
    .config("spark.es.nodes.wan.only", "false") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# JSON data schema
json_schema = StructType([
    StructField("app_id", StringType(), True),
    StructField("review_id", StringType(), True),
    StructField("username", StringType(), True),
    StructField("score", IntegerType(), True),
    StructField("content", StringType(), True),
    StructField("timestamp", StringType(), True),
    StructField("replyContent", StringType(), True),
    StructField("repliedAt", StringType(), True),
    StructField("thumbsUpCount", IntegerType(), True)
])

# --- Load only the chosen Logistic Regression model ---
print(f"Attempting to load Logistic Regression model from {LR_MODEL_PATH}...")
try:
    pipeline_model = PipelineModel.load(LR_MODEL_PATH)
    print("Logistic Regression model loaded successfully for real-time prediction.")
except Exception as e:
    print(f"ERROR: Could not load Logistic Regression model from {LR_MODEL_PATH}. "
          f"Make sure it's trained and saved correctly. Error: {e}")
    spark.stop()
    exit(1) 

# --- Extract sentiment_labels from the loaded model's StringIndexer ---
sentiment_labels = None
try:
    string_indexer_model = pipeline_model.stages[0] 
    if hasattr(string_indexer_model, 'labels'):
        sentiment_labels = string_indexer_model.labels
        print(f"Discovered sentiment labels from loaded model: {sentiment_labels}")
    else:
        print("WARNING: First stage of loaded model is not a StringIndexer or does not have 'labels' attribute.")
except IndexError:
    print("WARNING: Loaded pipeline model has no stages (or less than expected).")
except Exception as e:
    print(f"WARNING: Error extracting labels from loaded model: {e}")

if not sentiment_labels:
    print("WARNING: Using default sentiment labels. VERIFY THIS ORDER MATCHES YOUR TRAINING!")
    sentiment_labels = ["negative", "neutral", "positive"]

# Create IndexToString transformer for the chosen model
index_to_string = IndexToString(inputCol="prediction", outputCol="predicted_sentiment", labels=sentiment_labels)


# Read data from Kafka as a stream
kafka_df_stream = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BROKER_URL) \
    .option("subscribe", KAFKA_TOPIC) \
    .option("startingOffsets", "latest") \
    .load()

# Parse the Kafka message 'value' (which is binary/string JSON) and transform it
parsed_df_stream = kafka_df_stream.selectExpr("CAST(value AS STRING) as json_string") \
                                 .select(from_json(col("json_string"), json_schema).alias("data")) \
                                 .select("data.*")

# --- Data Preprocessing & Sentiment Prediction ---
# 1. Cast timestamp string to TimestampType
processed_df = parsed_df_stream.withColumn(
    "timestamp",
    to_timestamp(col("timestamp")) # Use to_timestamp for ISO 8601 string
).withColumn(
    "repliedAt", # Added casting for repliedAt as well
    to_timestamp(col("repliedAt"))
)

# 2. Rename 'content' to 'text' as this is the input column name expected by the ML pipeline
df_for_ml = processed_df.withColumnRenamed("content", "text")

# 3. Lowercase the text content for consistency with training
df_for_ml = df_for_ml.withColumn("text", lower(col("text")))

# Ensure no nulls in 'text' before applying the model
df_for_ml = df_for_ml.dropna(subset=["text"])

# 4. Apply the chosen Logistic Regression Model
predictions = pipeline_model.transform(df_for_ml)

# 5. Apply IndexToString to get readable sentiment labels
predictions_labeled = index_to_string.transform(predictions)

# --- Select final output columns for Elasticsearch ---
final_output_df = predictions_labeled.select(
    col("review_id").alias("review_id"),
    col("username").alias("username"),
    col("score").alias("original_score"), # Renamed from 'lr.score'
    col("text").alias("review_content"), # Renamed from 'lr.text'
    col("timestamp").alias("timestamp"),
    col("predicted_sentiment").alias("sentiment"), # Renamed to generic 'sentiment'
    col("probability").alias("probability_vector"), # Renamed to generic 'probability_vector'
    col("replyContent").alias("reply_content"), 
    col("repliedAt").alias("replied_at"), 
    col("thumbsUpCount").alias("thumbs_up_count"), 
    current_timestamp().alias("processing_timestamp") 
)

# Convert probability vector to array for Elasticsearch compatibility
final_output_df = final_output_df \
    .withColumn("probability_vector", vector_to_array(col("probability_vector")))

# --- Write Stream to Elasticsearch ---
print(f"Writing sentiment analysis results to Elasticsearch index: {ES_INDEX}...")

# Checkpoint location is critical for Structured Streaming for fault tolerance and exactly-once processing
CHECKPOINT_LOCATION = "C:/kafka/spark_checkpoint_grab_reviews_sentiment_consumer_lr" # Changed checkpoint name for clarity
# On Windows, you might want a path like: "file:///C:/tmp/spark_checkpoint_grab_reviews_sentiment_consumer_lr"

query = final_output_df \
    .writeStream \
    .outputMode("append") \
    .format("org.elasticsearch.spark.sql") \
    .option("checkpointLocation", CHECKPOINT_LOCATION) \
    .option("es.resource", ES_INDEX) \
    .start()

print("Spark Structured Streaming consumer started. Waiting for data...")
query.awaitTermination()
