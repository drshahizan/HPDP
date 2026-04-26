from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SparkGameReviewProcessor:
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("GameReviewSentimentAnalysis") \
            .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
            .config("spark.sql.adaptive.enabled", "true") \
            .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
            .getOrCreate()
        
        self.spark.sparkContext.setLogLevel("WARN")
        
        # Define schema for incoming JSON data
        self.review_schema = StructType([
            StructField("id", IntegerType(), True),
            StructField("game", StringType(), True),
            StructField("review", StringType(), True),
            StructField("voted_up", BooleanType(), True),
            StructField("timestamp", StringType(), True),
            StructField("platform", StringType(), True),
            StructField("sentiment", StringType(), True)
        ])
    
    def create_kafka_stream(self, topic="game-reviews"):
        """Create Kafka streaming DataFrame"""
        return self.spark \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .option("subscribe", topic) \
            .option("startingOffsets", "latest") \
            .load()
    
    def process_reviews(self):
        """Process streaming reviews"""
        # Read from Kafka
        kafka_df = self.create_kafka_stream()
        
        # Parse JSON data
        parsed_df = kafka_df.select(
            col("key").cast("string").alias("game_key"),
            from_json(col("value").cast("string"), self.review_schema).alias("data"),
            col("timestamp").alias("kafka_timestamp"),
            col("partition"),
            col("offset")
        ).select("game_key", "data.*", "kafka_timestamp", "partition", "offset")
        
        # Add processing timestamp
        processed_df = parsed_df.withColumn("processing_time", current_timestamp())
        
        # Aggregate sentiment by game
        sentiment_agg = processed_df \
            .groupBy("game", "sentiment") \
            .count() \
            .withColumnRenamed("count", "sentiment_count")
        
        # Write processed data to console (for debugging)
        console_query = processed_df.writeStream \
            .outputMode("append") \
            .format("console") \
            .option("truncate", False) \
            .trigger(processingTime="10 seconds") \
            .start()
        
        # Write aggregated sentiment to Kafka
        sentiment_query = sentiment_agg.writeStream \
            .outputMode("update") \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .option("topic", "sentiment-results") \
            .option("checkpointLocation", "./checkpoints/sentiment") \
            .trigger(processingTime="30 seconds") \
            .start()
        
        # Write processed reviews to file
        file_query = processed_df.writeStream \
            .outputMode("append") \
            .format("json") \
            .option("path", "./spark-data/processed-reviews") \
            .option("checkpointLocation", "./checkpoints/files") \
            .trigger(processingTime="60 seconds") \
            .start()
        
        return console_query, sentiment_query, file_query
    
    def run_batch_analysis(self, csv_file="steam_game_reviews.csv"):
        """Run batch analysis on existing data"""
        try:
            # Read CSV file
            df = self.spark.read.csv(csv_file, header=True, inferSchema=True)
            
            logger.info(f"Loaded {df.count()} reviews for batch analysis")
            
            # Sentiment distribution by game
            sentiment_by_game = df.groupBy("game", "sentiment").count() \
                .orderBy("game", "sentiment")
            
            logger.info("Sentiment distribution by game:")
            sentiment_by_game.show(50, truncate=False)
            
            # Overall sentiment statistics
            overall_sentiment = df.groupBy("sentiment").count() \
                .orderBy(desc("count"))
            
            logger.info("Overall sentiment distribution:")
            overall_sentiment.show()
            
            # Save results
            sentiment_by_game.coalesce(1).write.mode("overwrite") \
                .csv("./spark-data/sentiment-by-game", header=True)
            
            overall_sentiment.coalesce(1).write.mode("overwrite") \
                .csv("./spark-data/overall-sentiment", header=True)
            
            logger.info("Batch analysis complete. Results saved to spark-data/")
            
        except Exception as e:
            logger.error(f"Error in batch analysis: {e}")
    
    def stop(self):
        """Stop Spark session"""
        self.spark.stop()

if __name__ == "__main__":
    processor = SparkGameReviewProcessor()
    
    try:
        # Run batch analysis first
        processor.run_batch_analysis()
        
        # Start streaming processing
        logger.info("Starting streaming processing...")
        console_query, sentiment_query, file_query = processor.process_reviews()
        
        # Wait for termination
        console_query.awaitTermination()
        
    except KeyboardInterrupt:
        logger.info("Stopping Spark streaming...")
    finally:
        processor.stop()
