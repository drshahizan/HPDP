import time
import pickle
import numpy as np
import pandas as pd
import psutil
from datetime import datetime
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import accuracy_score
from elasticsearch import Elasticsearch

print("Starting Batch Pipeline initialization...")

# 1. Start the Performance Clock
start_time = time.time()

# 2. Read Your Cleaned Data (pandas directly — no Spark needed)
print("Loading cleaned_data.csv...")
pdf = pd.read_csv("data/cleaned_data.csv")
record_count = len(pdf)
print(f"Loaded {record_count} rows.")

# 5. Load your Saved Colab Assets
print("Loading CNN Model and Tokenizer from Colab download...")
with open("models/cnn_tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)
model = load_model("models/best_cnn_sentiment.keras")

# 6. Apply Tokenization Sequences
print("Converting text sequences...")
sequences = tokenizer.texts_to_sequences(pdf['clean_review'])
X = pad_sequences(sequences, maxlen=100)

# 7. Run Model Evaluation
print("Running batch predictions...")
predictions = model.predict(X)
predicted_indices = np.argmax(predictions, axis=1)

# Map the model's softmax class indices (0,1,2) back to the actual
# sentiment scale used in the dataset (-1 = negative, 0 = neutral, 1 = positive).
index_to_label = {0: -1, 1: 0, 2: 1}
pdf['predicted_label'] = [index_to_label[i] for i in predicted_indices]

# 8. Complete Metrics Computations
end_time = time.time()
processing_time = end_time - start_time
throughput = record_count / processing_time

# Accuracy check: compare 'label' column against 'predicted_label' (both on -1/0/1 scale now)
accuracy = accuracy_score(pdf['label'], pdf['predicted_label'])
cpu_usage = psutil.cpu_percent(interval=0.5)
memory_usage = psutil.virtual_memory().percent

# Add Metadata
pdf['mode'] = 'batch'
pdf['timestamp'] = datetime.now()
pdf = pdf.rename(columns={'label': 'actual_label'})

# 9. Send Everything to Elasticsearch via the Python Client
print("Storing documents in local Elasticsearch...")
es = Elasticsearch(["http://localhost:9200"])

# Clear out previous run's data so document counts and metrics
# don't accumulate / duplicate across repeated runs.
print("Clearing previous run's indices (if they exist)...")
es.indices.delete(index="sentiment_batch", ignore_unavailable=True)
es.indices.delete(index="performance_metrics", ignore_unavailable=True)

# Push Batch metrics
metrics_doc = {
    "mode": "batch",
    "processing_time": float(processing_time),
    "throughput": float(throughput),
    "accuracy": float(accuracy),
    "cpu_usage": float(cpu_usage),
    "memory_usage": float(memory_usage),
    "timestamp": datetime.now().isoformat()
}
es.index(index="performance_metrics", document=metrics_doc)

# Bulk send the data rows
print("Indexing row-level predictions...")
for index, row in pdf.iterrows():
    doc = {
        "text": str(row['clean_review']),
        "actual_label": int(row['actual_label']),
        "predicted_label": int(row['predicted_label']),
        "mode": row['mode'],
        "timestamp": row['timestamp'].isoformat()
    }
    es.index(index="sentiment_batch", id=index, document=doc)

print("\nBatch Processing Successfully Finished!")
print(f"Throughput achieved: {throughput:.2f} rows/sec")
