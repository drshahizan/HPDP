# 📘 Assignment 2: Mastering Big Data Handling

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>MUHAMMAD MUKHRITZ AL IMAN BIN MOHD RAFFI</td>
    <td>A23CS0250</td>
  </tr>
  <tr>
    <td>MUHAMMAD NAIM BIN ABDULLAH</td>
    <td>A23CS0134</td>
  </tr>
</table>

---

## 1. Dataset Description 📊

- **Name**: 2019 Airline Delays and Cancellations
- **Source**: [Kaggle - threnjen](https://www.kaggle.com/datasets/threnjen/2019-airline-delays-and-cancellations)
- **Domain**: Transportation / Aviation
- **File Size**: ~754 MB (Zipped) / 1.3+ GB (Uncompressed CSV)
- **Structure**: 6,489,062 rows × 26 columns
- **Dataset Description**:

| Columns/Features | Description |
|---|---|
| `MONTH` | Month of the flight (1-12) |
| `DAY_OF_WEEK` | Day of the week of the flight (1-7) |
| `DEP_DEL15` | Binary indicator for departure delay of 15 minutes or more (0 or 1) |
| `DEP_TIME_BLK` | Block of time for departure (e.g., 0800-0859) |
| `DISTANCE_GROUP` | Distance group of the flight |
| `SEGMENT_NUMBER` | The segment number of the flight |
| `CONCURRENT_FLIGHTS` | Number of concurrent flights at the airport |
| `NUMBER_OF_SEATS` | Total number of seats on the aircraft |
| `CARRIER_NAME` | Name of the airline carrier |
| `DEPARTING_AIRPORT` | The name of the departing airport |
| `LATITUDE` / `LONGITUDE` | Coordinates of the airport |
| `PRCP` / `SNOW` / `TMAX` | Weather variables such as precipitation, snow, and max temperature |

---

## 2. Library Choices 📚

Three main libraries were evaluated and utilized for big data processing performance and tracking:

1. **Pandas**
2. **Dask**
3. **Polars**

**Reasons for choosing Pandas:**
- It is the industry standard for data analysis. It is highly intuitive, has massive community support, and is excellent for basic inspection, sampling, and downcasting datatypes. However, it struggles with datasets that approach or exceed system RAM limits since it is single-threaded.

**Reasons for choosing Dask:**
- Dask provides an out-of-core computation model that prevents "Out of Memory" errors. It processes data in chunks and builds task graphs, making it highly effective for reading our massive 6.5 million row dataset in parallel while using a familiar Pandas-like API.

**Reasons for choosing Polars:**
- Polars is a blazing fast DataFrame library written in Rust. It utilizes all CPU cores and is highly memory efficient due to its Apache Arrow backend framework. It allows us to process multimillion-row datasets locally on standard hardware without needing a distributed cluster.

---

## 3. Data Loading and Inspection 📝

### Step 1 — Import Kaggle Credentials

To easily download the massive dataset, we uploaded `kaggle.json` to authenticate the Kaggle API directly in Google Colab.

```python
from google.colab import files
files.upload()  # Upload kaggle.json
```

### Step 2 — Configure Kaggle API Environment

We moved the uploaded file to the `.kaggle` directory and set proper permissions to ensure secure access so Kaggle allows us to download the data.

```python
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
```

### Step 3 — Download Dataset from Kaggle

We downloaded the 2019 Airline Delays dataset directly into the Colab environment.

```python
!kaggle datasets download -d threnjen/2019-airline-delays-and-cancellations
```

### Step 4 — Unzip the Dataset

We unzipped the downloaded file to access the `full_data_flightdelay.csv` file.

```python
!unzip 2019-airline-delays-and-cancellations.zip
```

### Step 5 — Read the CSV

The raw CSV was loaded into a Pandas DataFrame for initial exploration.

```python
import pandas as pd
df = pd.read_csv('full_data_flightdelay.csv')
```

### Step 6 — Display Rows, Shape, Columns and Data Types

We inspected the first few rows, overall shape, and the data type of each column to understand the dataset structure.

```python
print(df.head())
```

```python
df.info()
```

```python
print(f"\nDataset Shape:\nRows: {df.shape[0]}, Columns: {df.shape[1]}")
```

```python
display(df.dtypes.to_frame(name='Data Type').T)
```

**Output Observations:**
- The dataset successfully loaded **6,489,062 rows** and **26 columns**.
- The initial memory usage was over **1.3+ GB**, indicating that reading the entire file directly into Pandas puts significant strain on standard computing RAM.

> *<img width="511" height="406" alt="image" src="https://github.com/user-attachments/assets/0b3172d1-62b7-4f69-8a21-4f9c11b2d8a5" />
*

---

## 4. Big Data Handling Strategies 🛠️

To manage this 1.3+ GB dataset effectively, we applied five strategies organized into two parts:

- **Part 1** — Traditional Pandas optimizations: Load Less Data, Chunking, Optimized Data Types, Sampling, and Parallel Processing with Dask
- **Part 2** — Full library benchmark: Pandas vs Dask vs Polars

We built a custom `track_performance` function using `psutil` and `time` to measure execution time, memory usage, CPU load, and throughput for each strategy.

### The Tracker Function

```python
import pandas as pd
import dask.dataframe as dd
import polars as pl
import os
import time
import psutil
import random

file_path = 'full_data_flightdelay.csv'
all_results = []  # List to store results across different cells

def track_performance(description, load_function, file_path):
    print(f"Running: {description}...")
    process = psutil.Process(os.getpid())
    num_cores = psutil.cpu_count()

    process.cpu_percent(interval=None)
    mem_before = process.memory_info().rss / (1024 * 1024)
    start_time = time.time()

    success = False
    result = None

    try:
        result = load_function(file_path)
        success = True
    except Exception as e:
        print(f"  -> Error: {e}")

    end_time = time.time()
    exec_time = end_time - start_time
    mem_after = process.memory_info().rss / (1024 * 1024)
    mem_used = mem_after - mem_before
    avg_cpu = process.cpu_percent(interval=None) / num_cores

    throughput = 0
    if success and exec_time > 0:
        if isinstance(result, (pd.DataFrame, pl.DataFrame)):
            throughput = len(result) / exec_time
        elif isinstance(result, int):
            throughput = result / exec_time

    metrics = {
        "Description": description,
        "Memory Used (MB)": round(mem_used, 2),
        "Execution Time (s)": round(exec_time, 4),
        "Success": success,
        "Average CPU (%)": round(avg_cpu, 2),
        "Throughput (records/sec)": round(throughput, 2)
    }

    all_results.append(metrics)  # Automatically save to our global list
    print(f"Done! Recorded execution time: {metrics['Execution Time (s)']}s\n")
```

---

### Part 1 — Pandas Optimization Strategies

#### Strategy 1: Load Less Data

Load only the necessary columns using the `usecols` parameter. This drastically reduces the memory footprint right from the loading phase.

```python
def strategy_less_data(path):
    cols = ['MONTH', 'DAY_OF_WEEK', 'DEP_DEL15', 'CARRIER_NAME', 'DEPARTING_AIRPORT']
    return pd.read_csv(path, usecols=cols)

track_performance("1. Load Less Data (5 cols)", strategy_less_data, file_path)
```

#### Strategy 2: Chunking

Process the data in manageable batches using the `chunksize` parameter. This prevents overwhelming the system's RAM by processing data piece by piece.

```python
def strategy_chunking(path):
    total = 0
    for chunk in pd.read_csv(path, chunksize=100000):
        total += len(chunk)
    return total

track_performance("2. Load via Chunking (100k)", strategy_chunking, file_path)
```

#### Strategy 3: Optimized Data Types

Downcast default 64-bit data types to smaller sizes (`int8`, `float32`) and convert string columns (like `CARRIER_NAME`) to categorical types to significantly reduce memory usage.

```python
def strategy_optimized(path):
    dtypes = {
        'MONTH': 'int8', 'DAY_OF_WEEK': 'int8', 'DEP_DEL15': 'float32',
        'CARRIER_NAME': 'category', 'DEPARTING_AIRPORT': 'category'
    }
    return pd.read_csv(path, dtype=dtypes)

track_performance("3. Load with Optimized Dtypes", strategy_optimized, file_path)
```

#### Strategy 4: Sampling

Load a random 5% subset of the data using skip indices for fast prototyping, avoiding the need to process the full dataset.

```python
def strategy_sampling(path):
    total_lines = 6500000
    skip_indices = random.sample(range(1, total_lines), int(total_lines * 0.95))
    return pd.read_csv(path, skiprows=skip_indices)

track_performance("4. Load Random 5% Sample", strategy_sampling, file_path)
```

#### Strategy 5: Parallel Processing with Dask

Use **Dask** to process data out-of-core across multiple CPU cores. Dask splits the file into partitions and schedules computation lazily, which is highly effective for avoiding memory overflow on large files.

```python
def strategy_dask(path):
    return dd.read_csv(path, dtype={'DEP_DEL15': 'float64', 'AWND': 'float64', 'PRCP': 'float64'}).compute()

track_performance("5. Load via Dask", strategy_dask, file_path)
```

#### Final Dashboard — Strategy Comparison

After all five strategies were run, we compiled the results into a summary table and a 2×2 visualization dashboard using Seaborn.

```python
print("=== FINAL PERFORMANCE DASHBOARD ===")
display(pd.DataFrame(all_results))
```
<img width="616" height="241" alt="image" src="https://github.com/user-attachments/assets/4e48b0ae-8a8f-4e7b-a056-51fe3be1740a" />

```python
import matplotlib.pyplot as plt
import seaborn as sns

final_df = pd.DataFrame(all_results)
sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Performance Comparison of Data Loading Strategies', fontsize=18, fontweight='bold')

sns.barplot(data=final_df, x='Description', y='Execution Time (s)', ax=axes[0, 0], hue='Description', palette='viridis', legend=False)
axes[0, 0].set_title('Execution Time (Lower is Better)', fontsize=14)
axes[0, 0].set_xlabel('')
axes[0, 0].tick_params(axis='x', rotation=45)

sns.barplot(data=final_df, x='Description', y='Memory Used (MB)', ax=axes[0, 1], hue='Description', palette='magma', legend=False)
axes[0, 1].set_title('Memory Used (Lower is Better)', fontsize=14)
axes[0, 1].set_xlabel('')
axes[0, 1].tick_params(axis='x', rotation=45)

sns.barplot(data=final_df, x='Description', y='Average CPU (%)', ax=axes[1, 0], hue='Description', palette='crest', legend=False)
axes[1, 0].set_title('Average CPU Utilization (%)', fontsize=14)
axes[1, 0].set_xlabel('')
axes[1, 0].tick_params(axis='x', rotation=45)

sns.barplot(data=final_df, x='Description', y='Throughput (records/sec)', ax=axes[1, 1], hue='Description', palette='flare', legend=False)
axes[1, 1].set_title('Throughput (Higher is Better)', fontsize=14)
axes[1, 1].set_xlabel('')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.show()
```

> *(<img width="652" height="491" alt="image" src="https://github.com/user-attachments/assets/cd5dd59d-517f-4c6b-845f-2ab57573f4c4" />
*

---

### Part 2 — Library Performance Comparison (Pandas vs Dask vs Polars)

In this section, we perform a full load of the dataset using each of the three libraries and benchmark them head-to-head across execution time, memory usage, CPU utilization, and data throughput.

```python
import time
import psutil
import os
import matplotlib.pyplot as plt
import pandas as pd
import dask.dataframe as dd
import polars as pl

file_path = 'full_data_flightdelay.csv'
file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

def get_memory():
    return psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024)

process = psutil.Process(os.getpid())
num_cores = psutil.cpu_count()
results = {}

print(f"File size: {file_size_mb:.2f} MB. Starting benchmark...\n")

# --- Library 1: Full Load with Pandas ---
process.cpu_percent(interval=None)
start_time = time.time()
mem_before = get_memory()

df_pd = pd.read_csv(file_path)

mem_after = get_memory()
time_taken = time.time() - start_time
avg_cpu = process.cpu_percent(interval=None) / num_cores

results['Pandas'] = {
    'Time (s)': time_taken,
    'Memory (MB)': mem_after - mem_before,
    'Avg CPU (%)': avg_cpu,
    'Throughput (MB/s)': file_size_mb / time_taken
}
del df_pd  # Free memory

# --- Library 2: Full Load with Dask ---
process.cpu_percent(interval=None)
start_time = time.time()
mem_before = get_memory()

df_dd = dd.read_csv(file_path, dtype={'DEP_DEL15': 'float64', 'AWND': 'float64', 'PRCP': 'float64'}).compute()

mem_after = get_memory()
time_taken = time.time() - start_time
avg_cpu = process.cpu_percent(interval=None) / num_cores

results['Dask'] = {
    'Time (s)': time_taken,
    'Memory (MB)': mem_after - mem_before,
    'Avg CPU (%)': avg_cpu,
    'Throughput (MB/s)': file_size_mb / time_taken
}
del df_dd

# --- Library 3: Full Load with Polars ---
process.cpu_percent(interval=None)
start_time = time.time()
mem_before = get_memory()

df_pl = pl.read_csv(file_path, ignore_errors=True)

mem_after = get_memory()
time_taken = time.time() - start_time
avg_cpu = process.cpu_percent(interval=None) / num_cores

results['Polars'] = {
    'Time (s)': time_taken,
    'Memory (MB)': mem_after - mem_before,
    'Avg CPU (%)': avg_cpu,
    'Throughput (MB/s)': file_size_mb / time_taken
}
del df_pl

# --- Summary Table ---
comparison_df = pd.DataFrame(results).T
display(comparison_df.round(2))
```

```python
plt.style.use('seaborn-v0_8-whitegrid')
colors = ['#4C72B0', '#DD8452', '#55A868']

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
fig.suptitle('Performance Comparison: Pandas vs Dask vs Polars', fontsize=16, fontweight='bold')

comparison_df['Time (s)'].plot(kind='bar', color=colors, ax=axes[0, 0], edgecolor='black')
axes[0, 0].set_title('Execution Time (Lower is Better)', fontsize=12)
axes[0, 0].set_ylabel('Seconds')

comparison_df['Memory (MB)'].plot(kind='bar', color=colors, ax=axes[0, 1], edgecolor='black')
axes[0, 1].set_title('Memory Usage (Lower is Better)', fontsize=12)
axes[0, 1].set_ylabel('Megabytes (MB)')

comparison_df['Avg CPU (%)'].plot(kind='bar', color=colors, ax=axes[1, 0], edgecolor='black')
axes[1, 0].set_title('Average CPU Utilization', fontsize=12)
axes[1, 0].set_ylabel('CPU % (Out of 100%)')

comparison_df['Throughput (MB/s)'].plot(kind='bar', color=colors, ax=axes[1, 1], edgecolor='black')
axes[1, 1].set_title('Data Throughput (Higher is Better)', fontsize=12)
axes[1, 1].set_ylabel('MB/s')

for ax in axes.flat:
    ax.tick_params(axis='x', rotation=0)
    for p in ax.patches:
        ax.annotate(f"{p.get_height():.1f}",
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center',
                    xytext=(0, 6), textcoords='offset points',
                    fontsize=10, fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
```
>* <img width="394" height="102" alt="image" src="https://github.com/user-attachments/assets/698f4365-d927-4e38-94f8-25b6dcebceb2" />


> <img width="660" height="477" alt="image" src="https://github.com/user-attachments/assets/002bbebd-04bc-492e-b5b2-e05bc7486322" />


---

## 5. Comparison Analysis 🔍

### Benefits and Limitations Table

| Method | Benefits | Limitations |
|---|---|---|
| **Pandas** | Very intuitive, huge community support, integrates well with Scikit-Learn. | Single-threaded. Struggles with datasets approaching RAM limits. |
| **Dask** | Out-of-core computation prevents "Out of Memory" errors. Familiar Pandas-like API. | Overhead from scheduling can make it slower on single machines than pure memory tools. |
| **Polars** | Blazing fast, utilizes all CPU cores, memory efficient due to Apache Arrow framework. | Syntax (Expressions API) is very different from Pandas, steeper learning curve. |

### Key Observations

- **Pandas** loaded the ~6.5 million flight records successfully but consumed a massive amount of RAM and took the longest execution time.
- **Dask** prevented memory crashing by splitting the airline data into partitions. However, because we forced it to `.compute()` into a single DataFrame for a fair comparison, the overhead of task scheduling made its execution time relatively long.
- **Polars** handled the massive dataset with ease. By leveraging multithreading in Rust, it significantly outperformed Pandas and Dask in both execution speed and memory efficiency.

---

## 6. Conclusion and Reflection 🧠

### 6.1 Conclusion

Handling the 6.5 million row 2019 Airline Delays dataset successfully demonstrated that big data requires intentional memory management. Naive Pandas operations quickly exhaust available RAM. Our benchmarking proved that optimizing data types and loading fewer columns are crucial first steps. Furthermore, adopting modern libraries like Polars and Dask allowed us to process multimillion-row datasets locally on standard hardware efficiently without needing expensive cluster setups.

### 6.2 Reflection

**Student 1: MUKHRITZ**

Working on this assignment opened my eyes to how quickly a standard Python environment can crash when dealing with big data. I was particularly amazed by Polars and how utilizing the Apache Arrow framework can drastically speed up computation times compared to the single-threaded nature of Pandas. Building the `track_performance` function was a huge learning curve but allowed me to truly understand the trade-offs between CPU utilization and memory limits in real-time.

**Student 2: NAIM**

This assignment shifted my perspective on data preprocessing. I used to think loading data was just a single line of code (`pd.read_csv`), but observing the massive 1.3+ GB footprint of the unoptimized Airline dataset showed me otherwise. Implementing data downcasting (like changing strings to categories) and chunking taught me that how you structure your memory is just as important as the code you write. Moving forward, I feel confident handling massive datasets without worrying about "Out of Memory" errors.

---

## References 🔬

- **Dataset** - Kaggle: [2019 Airline Delays and Cancellations](https://www.kaggle.com/datasets/threnjen/2019-airline-delays-and-cancellations)
- **Pandas Documentation**: https://pandas.pydata.org/docs/
- **Polars Documentation**: https://www.nvidia.com/en-us/glossary/polars/
- **Dask Documentation**: https://www.nvidia.com/en-us/glossary/dask/
- **Psutil Documentation**: https://psutil.readthedocs.io/en/latest/
