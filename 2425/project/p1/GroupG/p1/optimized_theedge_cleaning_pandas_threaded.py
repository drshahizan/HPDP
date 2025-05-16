import pandas as pd
import time
import psutil
import threading
from concurrent.futures import ThreadPoolExecutor

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
print("🔄 Starting cleaning process (fully threaded column cleaning)...")
print("==============================")

# 📥 Load the dataset
df = pd.read_csv('theedge_articles.csv', low_memory=False)
print(f"✅ Loaded {len(df)} records.")

# 🔍 Check for missing values
print("Missing values per column:")
print(df.isnull().sum())


# 🧹 Fill missing values (threaded)
print("✅ Filling missing values (threaded)...")

def fill_missing(col_value):
    col, value = col_value    
    df[col] = df[col].fillna(value)

fill_values = {
    'sub-category': 'General',
    'author': 'Unknown',
    'source': 'Unknown',
    'summary': 'N/A',
    'updated date': 'NaT'
}

with ThreadPoolExecutor(max_workers=len(fill_values)) as executor:
    executor.map(fill_missing, fill_values.items())

# 🗑️ Remove exact duplicates
initial_len = len(df)
df = df.drop_duplicates().copy()
print(f"Removed {initial_len - len(df)} exact duplicate records.")

# 🗑️ Remove duplicates based on 'title'
initial_len = len(df)
df = df.drop_duplicates(subset=['title']).copy()
print(f"Removed {initial_len - len(df)} duplicate records based on title.")

# 🕒 Convert date columns to datetime (threaded)
print("✅ Converting date columns to datetime (threaded)")

def convert_date(col):    
    df[col] = pd.to_datetime(df[col], errors='coerce')

date_cols = ['created date', 'updated date']

with ThreadPoolExecutor(max_workers=len(date_cols)) as executor:
    executor.map(convert_date, date_cols)

# ✂️ Strip whitespace from text columns (threaded)
print("✅ Stripping whitespace from text columns (threaded)")

def strip_column(col):    
    df[col] = df[col].astype(str).str.strip()

text_cols = ['title', 'summary', 'category', 'sub-category', 'author', 'source']

with ThreadPoolExecutor(max_workers=len(text_cols)) as executor:
    executor.map(strip_column, text_cols)

# 💾 Save cleaned data
df.to_csv('theedge_cleaned_pandas_threaded.csv', index=False, encoding='utf-8-sig', na_rep='N/A')
print(f"✅ Saved cleaned dataset: {len(df)} records to 'theedge_cleaned_pandas_threaded.csv'.")

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
print(f"Total time taken: {total_time:.2f} seconds")

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