import dask.dataframe as dd
import time
import psutil
import threading

# Global flag to stop monitoring
monitoring = True

def monitor_performance(log_list, interval=1):
    process = psutil.Process()
    while monitoring:
        mem_usage = process.memory_info().rss / (1024 * 1024)  # MB
        cpu_usage = process.cpu_percent(interval=None)
        log_list.append((time.time(), mem_usage, cpu_usage))
        time.sleep(interval)

performance_logs = []
monitor_thread = threading.Thread(target=monitor_performance, args=(performance_logs, 0.5))
monitor_thread.start()

start_time = time.time()
print("==============================")
print("🔄 Starting Dask cleaning process...")
print("==============================")

# ✅ Tell Dask the exact type of each column
ddf = dd.read_csv('theedge_articles.csv', low_memory=False)
print(f"✅ Loaded {len(ddf)} records.")

# Cleaning steps (same as before)
print("✅ Filling missing values...")
ddf['sub-category'] = ddf['sub-category'].fillna('General')
ddf['author'] = ddf['author'].fillna('Unknown')
ddf['source'] = ddf['source'].fillna('Unknown')
ddf['summary'] = ddf['summary'].fillna('')
ddf['updated date'] = ddf['updated date'].fillna('NaT')

# Remove duplicates
ddf = ddf.drop_duplicates().drop_duplicates(subset=['title'])
print("✅ Removed duplicates.")

# Strip whitespace
text_cols = ['title', 'summary', 'category', 'sub-category', 'author', 'source']
for col in text_cols:
    if col in ddf.columns:
        ddf[col] = ddf[col].astype(str).str.strip()
print("✅ Stripped whitespace from text columns")

# Save result
ddf.compute().to_csv('theedge_cleaned_dask.csv', index=False, encoding='utf-8-sig', na_rep='N/A')
print("✅ Saved cleaned dataset to 'theedge_cleaned_dask.csv'.")

# Stop monitoring
monitoring = False
monitor_thread.join()

end_time = time.time()

total_time = end_time - start_time
num_records = ddf.shape[0].compute()  
throughput = num_records / total_time

print("==============================")
print("🚀 Performance Summary")
print("==============================")
print(f"Total time taken: {end_time - start_time:.2f} seconds")

# Peak + average usage
peak_mem = max([m for _, m, _ in performance_logs])
peak_cpu = max([c for _, _, c in performance_logs])
avg_mem = sum([m for _, m, _ in performance_logs]) / len(performance_logs)
avg_cpu = sum([c for _, _, c in performance_logs]) / len(performance_logs)
print(f"Average memory: {avg_mem:.2f} MB")
print(f"Peak memory: {peak_mem:.2f} MB")
print(f"Average CPU: {avg_cpu:.2f}%")
print(f"Peak CPU: {peak_cpu:.2f}%")
print(f"✅ Processed {num_records} records in {total_time:.2f} seconds.")
print(f"🚀 Throughput: {throughput:.2f} records per second.")
print("==============================")
