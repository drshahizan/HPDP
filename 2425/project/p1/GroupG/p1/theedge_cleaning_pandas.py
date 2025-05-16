import pandas as pd
import time
import psutil
import threading

# Global flag to stop monitoring
monitoring = True

# Function to monitor performance DURING the process
def monitor_performance(log_list, interval=1):
    process = psutil.Process()
    while monitoring:
        mem_usage = process.memory_info().rss / (1024 * 1024)  # MB
        cpu_usage = process.cpu_percent(interval=None)         # %
        log_list.append((time.time(), mem_usage, cpu_usage))
        time.sleep(interval)

# List to store performance logs
performance_logs = []

# Start monitoring in a separate thread
monitor_thread = threading.Thread(target=monitor_performance, args=(performance_logs, 0.5))
monitor_thread.start()

# Track time
start_time = time.time()

print("==============================")
print("🔄 Starting cleaning process...")
print("==============================")

# 📥 Load the dataset
df = pd.read_csv('theedge_articles.csv', low_memory=False)
print(f"✅ Loaded {len(df)} records.")

# 🔍 Check for missing values
print("Missing values per column:")
print(df.isnull().sum())

# 🧹 Fill missing values
print("✅ Filling missing values...")
df['sub-category'] = df['sub-category'].fillna('General')
df['author'] = df['author'].fillna('Unknown')
df['source'] = df['source'].fillna('Unknown')
df['summary'] = df['summary'].fillna('')
df['updated date'] = df['updated date'].fillna('NaT')

# 🗑️ Remove exact duplicates
initial_len = len(df)
df = df.drop_duplicates().copy()
print(f"Removed {initial_len - len(df)} exact duplicate records.")

# 🗑️ Remove duplicates based on 'title'
initial_len = len(df)
df = df.drop_duplicates(subset=['title']).copy()
print(f"Removed {initial_len - len(df)} duplicate records based on title.")

# 🕒 Convert date columns to datetime
print("✅ Converted date columns to datetime")
df['created date'] = pd.to_datetime(df['created date'], errors='coerce')
df['updated date'] = pd.to_datetime(df['updated date'], errors='coerce')

# ✂️ Strip whitespace from text columns
print("✅ Stripped whitespace from text columns")
text_cols = ['title', 'summary', 'category', 'sub-category', 'author', 'source']
for col in text_cols:
    df[col] = df[col].astype(str).str.strip()


# 💾 Save cleaned data
df.to_csv('theedge_cleaned_pandas.csv', index=False, encoding='utf-8-sig', na_rep='N/A')
print(f"✅ Saved cleaned dataset: {len(df)} records to 'theedge_cleaned_pandas.csv'.")

# Stop monitoring
monitoring = False
monitor_thread.join()

end_time = time.time()

total_time = end_time - start_time
num_records = df.shape[0]
throughput = num_records / total_time

# ==========================
# 🚀 Performance Summary
# ==========================
print("==============================")
print("🚀 Performance Summary")
print("==============================")
print(f"Total time taken: {end_time - start_time:.2f} seconds")

# Print memory & CPU usage
peak_mem = max([m for _, m, _ in performance_logs])
peak_cpu = max([c for _, _, c in performance_logs])
avg_mem = sum([m for _, m, _ in performance_logs]) / len(performance_logs)
avg_cpu = sum([c for _, _, c in performance_logs]) / len(performance_logs)
print(f"Average memory usage during process: {avg_mem:.2f} MB")
print(f"Peak memory usage during process: {peak_mem:.2f} MB")
print(f"Average CPU usage during process: {avg_cpu:.2f}%")
print(f"Peak CPU usage during process: {peak_cpu:.2f}%")
print(f"✅ Processed {num_records} records in {total_time:.2f} seconds.")
print(f"🚀 Throughput: {throughput:.2f} records per second.")
