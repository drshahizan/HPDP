from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf, from_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, ArrayType
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your prediction function
from spark.predict import predict_sentiment

# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaSentimentConsumer") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.2,org.elasticsearch:elasticsearch-spark-30_2.12:8.12.0") \
    .config("es.nodes", "localhost") \
    .config("es.port", "9200") \
    .config("es.nodes.wan.only", "true") \
    .config("spark.sql.shuffle.partitions", "1") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

schema = StructType().add("text", StringType())


# Define schema for JSON Kafka messages
result_schema = StructType([
    StructField("text", StringType()),
    StructField("keywords", ArrayType(StringType())),  # ← ADD THIS LINE
    StructField("hugging_face_label", StringType()),
    StructField("hugging_face_score", FloatType()),
    StructField("hugging_face_value", IntegerType()),
    StructField("naive_bayes", IntegerType()),
    StructField("lstm", IntegerType())
])

@udf(result_schema)
def predict_udf(text):
    try:
        return predict_sentiment(text)
    except Exception as e:
        return {
            "text": text,
            "hugging_face_label": "error",
            "hugging_face_score": 0.0,
            "hugging_face_value": 0,
            "naive_bayes": 0,
            "lstm": 0
        }

# Read and parse Kafka stream
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sentiment_comments") \
    .option("startingOffsets", "latest") \
    .load()

# Parse JSON and extract 'text'
parsed_df = df.selectExpr("CAST(value AS STRING) as json_str") \
    .withColumn("data", from_json(col("json_str"), schema)) \
    .select("data.text")

# Apply prediction
predicted_df = parsed_df.withColumn("result", predict_udf(col("text")))
flattened_df = predicted_df.select("result.*")

# Write structured fields to Elasticsearch
query = flattened_df.writeStream \
    .format("org.elasticsearch.spark.sql") \
    .option("checkpointLocation", "./checkpoint") \
    .option("es.resource", "realtime_youtube_sentiment_results_v2") \
    .start()

query.awaitTermination()