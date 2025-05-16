# 🗂️ Import libraries
import polars as pl
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
print("🔄 Starting Polars cleaning process...")
print("==============================")

# 📥 Load the dataset
df = pl.read_csv('theedge_articles.csv', low_memory=False)
print(f"✅ Loaded {df.shape[0]} records.")

# 🔍 Check for missing values
null_counts = df.null_count()
print("Missing values per column:")
print(null_counts)

# 🧹 Fill missing values
fill_values = {
    'sub-category': 'General',
    'author': 'Unknown',
    'source': 'Unknown',
    'summary': '',
    'updated date': 'NaT'
}
for column, value in fill_values.items():
    if column in df.columns:
        df = df.with_columns(
            pl.col(column).fill_null(value)
        )
print("✅ Filled missing values.")

# 🗑️ Remove exact duplicates
initial_len = df.shape[0]
df = df.unique()
print(f"Removed {initial_len - df.shape[0]} exact duplicate records.")

# 🗑️ Remove duplicates based on 'title'
initial_len = df.shape[0]
if 'title' in df.columns:
    df = df.unique(subset=['title'])
    print(f"Removed {initial_len - df.shape[0]} duplicate records based on title.")
else:
    print("⚠️ 'title' column not found; skipping duplicate removal based on title.")

# 🕒 Convert date columns to datetime
if 'created date' in df.columns:
    df = df.with_columns(
        pl.col('created date').str.strip_chars().str.strptime(pl.Datetime, strict=False).alias('created date')
    )
if 'updated date' in df.columns:
    df = df.with_columns(
        pl.col('updated date').str.strip_chars().str.strptime(pl.Datetime, strict=False).alias('updated date')
    )
print("✅ Converted date columns to datetime.")

# ✂️ Strip whitespace from text columns
text_cols = ['title', 'summary', 'category', 'sub-category', 'author', 'source']
for col in text_cols:
    if col in df.columns:
        df = df.with_columns(
            pl.col(col).cast(pl.Utf8).str.strip_chars()
        )
print("✅ Stripped whitespace from text columns.")

# 💾 Save cleaned data
df.write_csv('theedge_cleaned_polars.csv')
print(f"✅ Saved cleaned dataset: {df.shape[0]} records to 'theedge_cleaned_polars.csv'.")

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

# Peak + average usage
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
print("==============================")
