from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import *
from datetime import datetime
import os
from supabase import create_client, Client

# ========== Environment Setup ==========
# Set correct Hadoop path (if you're on Windows)
os.environ['HADOOP_HOME'] = r"C:\hadoop"
os.environ['PATH'] = r"C:\hadoop\bin;" + os.environ['PATH']

# ========== Supabase Setup ==========
SUPABASE_URL = "https://qavwgrhcqquyjcgdjedp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhdndncmhjcXF1eWpjZ2RqZWRwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MTU0MzA0NywiZXhwIjoyMDY3MTE5MDQ3fQ.uadeKF1kvQt4lWIpqtgoQUvygnDCUOekvvTCwn_53Hg"  # Do not hardcode this in production
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ========== Spark Session ==========
spark = SparkSession.builder \
    .appName("RedditSentimentStream") \
    .master("local[*]") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# ========== Schema ==========
schema = StructType([
    StructField("id", StringType(), True),
    StructField("body", StringType(), True),
    StructField("author", StringType(), True),
    StructField("created_utc", LongType(), True),
    StructField("subreddit", StringType(), True),
    StructField("sentiment", StringType(), True),
    StructField("sentiment_score", FloatType(), True),
])

# ========== Supabase Writer ==========
def write_to_supabase(df, epoch_id):
    records = df.collect()
    for record in records:
        data = {
            "id": record["id"],
            "body": record["body"],
            "author": record["author"],
            "created_utc": record["created_utc"],
            "subreddit": record["subreddit"],
            "sentiment": record["sentiment"],
            "sentiment_score": float(record["sentiment_score"]),
            "processed_at": datetime.now().isoformat(),
        }
        try:
            supabase.table("reddit_comments").upsert(data).execute()
        except Exception as e:
            print("⚠️ Supabase Error:", e)

# ========== Kafka Stream ==========
raw_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "reddit-sentiment") \
    .option("startingOffsets", "latest") \
    .load()

parsed_df = raw_df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# ========== Write to Supabase ==========
query = parsed_df.writeStream \
    .foreachBatch(write_to_supabase) \
    .outputMode("append") \
    .trigger(processingTime="10 seconds") \
    .start()

query.awaitTermination()
