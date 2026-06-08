import os
import sys
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 1. PATH FIXES
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
os.environ['SPARK_LOCAL_IP'] = '127.0.0.1'

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, get_json_object
import pyspark

print("Starting Apache Spark Engine...")
print(f"Detected PySpark Version: {pyspark.__version__}")

# 2. INITIALIZE NLP ONCE ON THE MAIN THREAD
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    if not text: return "Neutral"
    score = analyzer.polarity_scores(str(text))['compound']
    if score >= 0.05: return "Positive"
    elif score <= -0.05: return "Negative"
    else: return "Neutral"

# 3. THE SILVER BULLET: Process everything in Pandas to bypass Windows Sockets
def process_and_save_batch(df, epoch_id):
    # Convert the Spark micro-batch into a Pandas DataFrame instantly
    pdf = df.toPandas()
    
    if not pdf.empty:
        # Apply the sentiment analysis normally
        pdf['sentiment_label'] = pdf['review_text'].apply(get_sentiment)
        
        # Save directly to CSV using Pandas
        os.makedirs("./webminer_collected_data", exist_ok=True)
        csv_filename = f"./webminer_collected_data/batch_{epoch_id}.csv"
        
        # Keep only the required columns
        final_pdf = pdf[["review_text", "sentiment_label"]]
        final_pdf.to_csv(csv_filename, index=False)
        print(f"✅ SUCCESS: Saved {len(final_pdf)} records to {csv_filename}")

# 4. Create the Spark Session
spark = SparkSession.builder \
    .appName("WebMinerSpark") \
    .config("spark.jars.packages", f"org.apache.spark:spark-sql-kafka-0-10_2.13:{pyspark.__version__}") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# 5. Connect to Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "127.0.0.1:9092") \
    .option("subscribe", "tweets") \
    .option("startingOffsets", "earliest") \
    .load()

# Parse the JSON
raw_json_df = df.selectExpr("CAST(value AS STRING) as json_payload")
parsed_df = raw_json_df.withColumn("review_text", get_json_object(col("json_payload"), "$.text"))

print("Listening for data and saving to CSV...\n")

# 6. Stream directly to our bypass function
query = parsed_df.writeStream \
    .foreachBatch(process_and_save_batch) \
    .start()

query.awaitTermination()