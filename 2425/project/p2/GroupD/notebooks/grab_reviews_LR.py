import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, from_json, when
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
from pyspark.ml import Pipeline
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
import logging

logger = logging.getLogger('py4j')
logger.setLevel(logging.WARN)

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

KAFKA_PACKAGE = "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.6"

spark = SparkSession.builder \
    .appName("Grab Reviews - Logistic Regression (Score Labeling)") \
    .config("spark.jars.packages", KAFKA_PACKAGE) \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

review_schema = StructType([
    StructField("app_id", StringType()),
    StructField("review_id", StringType()),
    StructField("username", StringType()),
    StructField("score", IntegerType()),
    StructField("content", StringType()), 
    StructField("timestamp", StringType()), 
    StructField("replyContent", StringType()),
    StructField("repliedAt", StringType()), 
    StructField("thumbsUpCount", IntegerType()),
])

print("Reading data from Kafka topic 'grab_reviews_final' for Logistic Regression (Score Labeling) training...")
kafka_df = spark \
    .read \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "grab_reviews_final") \
    .option("startingOffsets", "earliest") \
    .load()

df = kafka_df.selectExpr("CAST(value AS STRING) as json_data") \
             .select(from_json(col("json_data"), review_schema).alias("data")) \
             .select("data.*")

df = df.withColumnRenamed("content", "text")
df = df.withColumn("text", lower(col("text"))) # Lowercase text early

# --- Labeling based on Score (PRIMARY LABELING FOR THIS SCRIPT) ---
df = df.withColumn("score_based_label", 
                    when(col("score") >= 4, "positive") \
                    .when(col("score") == 3, "neutral") \
                    .otherwise("negative")) 

df = df.dropna(subset=["text", "score_based_label"])

print(f"Successfully loaded {df.count()} records from Kafka for training.")
df.printSchema() 
df.show(5, truncate=False) 

# Index string labels to numeric for score_based_label
label_indexer = StringIndexer(inputCol="score_based_label", outputCol="labelIndex").fit(df)

tokenizer = Tokenizer(inputCol="text", outputCol="tokens")
custom_stopwords = StopWordsRemover.loadDefaultStopWords("english") + ['la', 'eh', 'je', 'tak', 'gak', 'tp', 'x', 'dah', 'saja', 'aja', 'pun', 'lah']
stopword_remover = StopWordsRemover(inputCol="tokens", outputCol="filtered_tokens")
stopword_remover.setStopWords(custom_stopwords)

hashingTF = HashingTF(inputCol="filtered_tokens", outputCol="rawFeatures", numFeatures=5000)
idf = IDF(inputCol="rawFeatures", outputCol="features") # IDF is part of LR pipeline

lr = LogisticRegression(featuresCol="features", labelCol="labelIndex", maxIter=100)

pipeline = Pipeline(stages=[
    label_indexer,
    tokenizer,
    stopword_remover,
    hashingTF,
    idf, # Added for LR
    lr
])

train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

print("Starting Logistic Regression (Score Labeling) model training...")
model = pipeline.fit(train_df)
print("Logistic Regression (Score Labeling) model training completed.")

model_path_lr_score = "lr_model_score_labeling" # Unique path for this model
model.write().overwrite().save(model_path_lr_score)
print(f"Logistic Regression model (Score Labeling) saved to {model_path_lr_score}")

predictions = model.transform(test_df)

print("\n--- Logistic Regression Model (Score Labeling) Evaluation ---")

f1_evaluator = MulticlassClassificationEvaluator(labelCol="labelIndex", predictionCol="prediction", metricName="f1")
f1_score = f1_evaluator.evaluate(predictions)
print("F1 Score:", f1_score)

accuracy_evaluator = MulticlassClassificationEvaluator(labelCol="labelIndex", predictionCol="prediction", metricName="accuracy")
accuracy = accuracy_evaluator.evaluate(predictions)
print("Accuracy:", accuracy)

precision_evaluator = MulticlassClassificationEvaluator(labelCol="labelIndex", predictionCol="prediction", metricName="weightedPrecision")
precision = precision_evaluator.evaluate(predictions)
print("Precision:", precision)

recall_evaluator = MulticlassClassificationEvaluator(labelCol="labelIndex", predictionCol="prediction", metricName="weightedRecall")
recall = recall_evaluator.evaluate(predictions)
print("Recall:", recall)

print("Confusion Matrix:")
predictions.groupBy("labelIndex", "prediction").count().show()

label_mapping = label_indexer.labels
print(f"Label Index Mapping: {', '.join([f'{i}: {label_mapping[i]}' for i in range(len(label_mapping))])}")

spark.stop()