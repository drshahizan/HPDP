import subprocess
import time
import logging
import threading
from kafka_producer import GameReviewProducer
from kafka_consumer import GameReviewConsumer
from spark_streaming import SparkGameReviewProcessor

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GameReviewPipeline:
    def __init__(self):
        self.producer = None
        self.consumer = None
        self.spark_processor = None
        
    def start_producer(self, csv_file="steam_game_reviews.csv"):
        """Start Kafka producer in a separate thread"""
        def producer_thread():
            try:
                self.producer = GameReviewProducer()
                logger.info("Starting producer...")
                self.producer.send_reviews_from_csv(csv_file, batch_size=50)
                self.producer.close()
            except Exception as e:
                logger.error(f"Producer error: {e}")
        
        thread = threading.Thread(target=producer_thread)
        thread.daemon = True
        thread.start()
        return thread
    
    def start_consumer(self):
        """Start Kafka consumer in a separate thread"""
        def consumer_thread():
            try:
                self.consumer = GameReviewConsumer(['game-reviews'])
                logger.info("Starting consumer...")
                self.consumer.consume_and_process()
            except Exception as e:
                logger.error(f"Consumer error: {e}")
        
        thread = threading.Thread(target=consumer_thread)
        thread.daemon = True
        thread.start()
        return thread
    
    def start_spark_streaming(self):
        """Start Spark streaming processor"""
        def spark_thread():
            try:
                self.spark_processor = SparkGameReviewProcessor()
                logger.info("Starting Spark streaming...")
                
                # Run batch analysis first
                self.spark_processor.run_batch_analysis()
                
                # Start streaming
                queries = self.spark_processor.process_reviews()
                
                # Wait for termination
                for query in queries:
                    if query.isActive:
                        query.awaitTermination()
                        
            except Exception as e:
                logger.error(f"Spark streaming error: {e}")
            finally:
                if self.spark_processor:
                    self.spark_processor.stop()
        
        thread = threading.Thread(target=spark_thread)
        thread.daemon = True
        thread.start()
        return thread
    
    def run_complete_pipeline(self, csv_file="steam_game_reviews.csv"):
        """Run the complete pipeline"""
        logger.info("Starting complete game review processing pipeline...")
        
        try:
            # Start Spark streaming first
            spark_thread = self.start_spark_streaming()
            time.sleep(10)  # Give Spark time to initialize
            
            # Start consumer
            consumer_thread = self.start_consumer()
            time.sleep(5)  # Give consumer time to initialize
            
            # Start producer (this will feed data to the pipeline)
            producer_thread = self.start_producer(csv_file)
            
            logger.info("All components started. Pipeline is running...")
            logger.info("Press Ctrl+C to stop the pipeline")
            
            # Keep main thread alive
            try:
                while True:
                    time.sleep(10)
                    logger.info("Pipeline running... Check Spark UI at http://localhost:8080")
            except KeyboardInterrupt:
                logger.info("Stopping pipeline...")
                
        except Exception as e:
            logger.error(f"Pipeline error: {e}")

if __name__ == "__main__":
    pipeline = GameReviewPipeline()
    pipeline.run_complete_pipeline()
