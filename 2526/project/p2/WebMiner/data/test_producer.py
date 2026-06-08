from pyspark.sql import SparkSession

print("Starting Apache Spark... (This may take a minute to download the Kafka connector)")

# 1. Create the Spark Session and load the Kafka Plugin
spark = SparkSession.builder \
    .appName("WebMinerSpark") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .getOrCreate()

# Hide the massive walls of annoying Java INFO logs
spark.sparkContext.setLogLevel("WARN")

# 2. Your exact snippet (modified to use 127.0.0.1 to prevent Windows network errors)
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "127.0.0.1:9092") \
  .option("subscribe", "tweets") \
  .option("startingOffsets", "earliest") \
  .load()

# 3. Kafka stores data as raw binary bytes. We must cast it to a readable String.
readable_df = df.selectExpr("CAST(value AS STRING) as json_payload")

# 4. Stream the output directly to your VS Code terminal
print("Spark successfully connected to Kafka! Waiting for data...\n")
query = readable_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()