<h1 align="center"> 
  Assignment 2 - MAS(eCommerce Behavior Data from Multi Category Store)
</h1>

| Name              | Matric No       |
|-------------------|-----------------|
| MAISARAH BINTI RIZAL   | A22EC0192      |
| NADHRAH NURSABRINA BINTI ZULAINI  | A22EC0224    |

---

## 📚 Table of Contents
1. [Introduction](#1-introduction)
2. [Dataset Overview and Inspection](#2-dataset-overview-and-inspection)
3. [Big Data Handling Strategies](#3-big-data-handling-strategies)
4. [Comparative Analysis](#4-comparative-analysis)
5. [Conclusion and Reflection](#5-conclusion-and-reflection)
6. [References](#6-references)

---

## 1. Introduction

<div align="justify">
  
### 1.1 Background of the Project
In a data-driven world, the ability to manipulate large datasets is essential to transforming raw data into useful insights. Traditional tools, such as Pandas, can run into memory problems when working with large files. This project uses contemporary modules written in Python, such as Dask, Pandas, and Polars to evaluate the various ways of optimizing data loading, processing, and analysis. The aim is to know the performance of all options based on the speed, memory usage, and ease of implementation of each approach based on a real e-commerce dataset.

### 1.2 Objectives
This project's key aims include:

 1. To inspect and analyze a huge e-commerce dataset.
 2. To put various large data handling techniques into practice and evaluate them:
- Load Less Data
- Use Chunking
- Optimize Data Types
- Apply Sampling
 - Dask and Polars are used for parallel processing.
 3. To measure performance using throughput, memory use, and execution time.

### 1.3 Dataset Source
- **Dataset:** eCommerce behavior data from multi category store
- **Source:** [Kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)
- **Size:** 5.67GB (2019-Oct.csv)
- **Domain:** The dataset falls under the E-Commerce / Retail domain, focusing on user behavior tracking in an online multi-category store. It provides insights into how users interact with products across different categories and brands. 
- **Number of Records:** Over 10 millions entries (42448764rows x 9 columns)
- **Features/Columns:**

| Column Name       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `event_time`      | Time when event happened (in UTC)                                           |
| `event_type`      | Only one kind of event: purchase                                            |
| `product_id`      | ID of a product                                                             |
| `category_id`     | Product's category ID                                                       |
| `category_code`   | Product's category taxonomy (code name). Usually present for meaningful categories and skipped for different kinds of accessories. |
| `brand`           | Downcased string of brand name. Can be missing.                             |
| `price`           | Float price of a product. Always present.                                   |
| `user_id`         | Permanent user ID                                                           |
| `user_session`    | Temporary session ID. Same for each session, changed after long pause.      |

---
</div>

## 2. Dataset Overview and Inspection

### 2.1 Initial Loading

  ```
 🔽 STEP 1: Install kaggle CLI
!pip install -q kaggle

# 🔽 STEP 2: Upload kaggle.json API token
from google.colab import files
print("Please upload your kaggle.json file:")
files.upload()

# 🔽 STEP 3: Set up Kaggle CLI config
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# 🔽 STEP 4: Download your desired dataset
# Replace with your actual competition or dataset name
!kaggle datasets download mkechinov/ecommerce-behavior-data-from-multi-category-store

!unzip ecommerce-behavior-data-from-multi-category-store.zip
!ls

```

### 2.2 Basic Inspection

  ```
import pandas as pd

# Only load first 10,000 rows to avoid crash
filename = '2019-Oct.csv'
df_sample = pd.read_csv(filename)

print("📊" + "="*40)
print("     🔍 DATASET INSPECTION REPORT")
print("📊" + "="*40 + "\n")

# Shape
print("🧾 Shape (Rows, Columns):")
print(f"    ➤ {df_sample.shape[0]} rows, {df_sample.shape[1]} columns\n")

# Column Names
print("📌 Column Names:")
print("    ➤ " + "\n    ➤ ".join(df_sample.columns.tolist()) + "\n")

# Data Types
print("⚙️ Data Types:")
for col, dtype in df_sample.dtypes.items():
    print(f"    ➤ {col.ljust(20)} : {dtype}")
print()

# Memory Usage
print("💾 Memory Usage (MB):")
mem_usage = df_sample.memory_usage(deep=True) / (1024 ** 2)
for col, usage in mem_usage.items():
    print(f"    ➤ {col.ljust(20)} : {usage:.4f} MB")
print(f"\n    🧮 Total Memory : {mem_usage.sum():.4f} MB")

```

Output:
![image](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/MAS/RawDataOutput.png)

---

## 3. Big Data Handling Strategies

### 3.1 Part 1: Strategies with Pandas & Dask
- **Load Less Data**<br>
```
# 📊 Strategy 1: Load Less Data
df_lite = pd.read_csv(FILENAME, usecols=USECOLS, nrows=100_000)
start = time.time()
mean_lite = compute_mean_purchase_price(df_lite)
time_lite = time.time() - start
mem_lite = df_lite.memory_usage(deep=True).sum() / (1024 ** 2)
throughput_lite = len(df_lite) / time_lite if time_lite > 0 else float('nan')
results.append(print_strategy_results("Strategy 1: Load Less Data", mean_lite, mem_lite, time_lite, throughput_lite))
```
Output: 

![image](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/MAS/Output/LoadLessData.png)

- **Optimize Data Types**<br>

```
# 📊 Strategy 2: Optimize Data Types
df_optimized = pd.read_csv(FILENAME, usecols=USECOLS, dtype=DTYPE_MAP, nrows=100_000)
start = time.time()
mean_opt = compute_mean_purchase_price(df_optimized)
time_opt = time.time() - start
mem_opt = df_optimized.memory_usage(deep=True).sum() / (1024 ** 2)
throughput_opt = len(df_optimized) / time_opt if time_opt > 0 else float('nan')
results.append(print_strategy_results("Strategy 2: Optimize Data Types", mean_opt, mem_opt, time_opt, throughput_opt))
```
Output: 

![image](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/MAS/Output/OptimizeDataTypes.png)

- **Sampling**<br>

```
# 📊 Strategy 3: Sampling
df_sampled = df_optimized.sample(frac=0.01, random_state=42)
start = time.time()
mean_samp = compute_mean_purchase_price(df_sampled)
time_samp = time.time() - start
mem_samp = df_sampled.memory_usage(deep=True).sum() / (1024 ** 2)
throughput_samp = len(df_sampled) / time_samp if time_samp > 0 else float('nan')
results.append(print_strategy_results("Strategy 3: Sampling", mean_samp, mem_samp, time_samp, throughput_samp))
```
Output: 

![image](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/MAS/Output/Sampling.png)

- **Chunking**<br>

```
# 📊 Strategy 4: Chunked Processing
total_sum = 0
total_count = 0
peak_mem = 0
start = time.time()

for chunk in pd.read_csv(FILENAME, usecols=USECOLS, dtype=DTYPE_MAP, chunksize=CHUNKSIZE):
    filtered = chunk[chunk['event_type'] == TARGET_EVENT_TYPE]
    total_sum += filtered['price'].sum()
    total_count += len(filtered)
    mem = chunk.memory_usage(deep=True).sum() / (1024 ** 2)
    peak_mem = max(peak_mem, mem)

mean_chunk = total_sum / total_count
time_chunk = time.time() - start
throughput_chunk = total_count / time_chunk if time_chunk > 0 else float('nan')
results.append(print_strategy_results("Strategy 4: Chunked Processing", mean_chunk, peak_mem, time_chunk, throughput_chunk))
```
Output: 

![image](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/MAS/Output/Chunking.png)


- **Parallel Processing with Dask**<br>

```
start_time = time.time()

# Read CSV with Dask
ddf = dd.read_csv(filename, usecols=['event_type', 'price'])

# Filter and compute mean
mean_price_after = ddf[ddf['event_type'] == TARGET_EVENT_TYPE][MEASUREMENT_COLUMN].mean().compute()

shape_after = (len(ddf), len(ddf.columns))
time_after = time.time() - start_time
mem_after = ddf.memory_usage(index=True, deep=True).sum().compute() / (1024 ** 2)
throughput_after = shape_after[0] / time_after if time_after > 0 else 0

print(f"Shape: {shape_after}")
print(f"Memory Usage: {mem_after:.2f} MB")
print(f"Processing Time: {time_after:.2f} seconds")
print(f"Throughput: {throughput_after:.0f} rows/sec")
print(f"Mean Purchase Price: {mean_price_after:.2f}")
print("-" * 50)

```

Output: 

![image](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/MAS/DaskOutput.png)

- **Parallel Processing with Polars**<br>

```
# Strategy 5b: Polars
def run_polars():
    start = time.time()
    df_pl = pl.read_csv(FILENAME, columns=USECOLS)
    mean = df_pl.filter(pl.col('event_type') == TARGET_EVENT_TYPE)[MEASUREMENT_COLUMN].cast(pl.Float64).mean()
    shape = df_pl.shape
    mem = df_pl.estimated_size() / (1024 ** 2)
    t = time.time() - start
    throughput = shape[0] / t if t > 0 else float('nan')
    return {"mean": mean, "shape": shape, "mem": mem, "time": t, "throughput": throughput}

polars_result = run_polars()
results.append(print_strategy_results("Strategy 5b: Polars Processing", polars_result["mean"], polars_result["mem"], polars_result["time"], polars_result["throughput"]))

```

Output: 

![image](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/MAS/Output/Polars.png)

### 3.2 Part 2: Comparing Libraries Reading Raw Data


| Library | Visualization |
|---------|---------------|
| Pandas  |![image](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/MAS/PandasRawData.png) |  
| Dask    |![image](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/MAS/DaskRawData1.png) |
| Polars  |![image](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/MAS/PolarsRawData.png) |

---

## 4. Comparative Analysis

### 4.1 Metrics Used
| Metric  | Description |
|----------|----------|
| Processing Time (s)   | Total time taken to compute the mean purchase price. |
| Memory Usage (MB)     | Memory consumed during processing (peak or total).   |
| Throughput (rows/sec)   | Number of rows processed per second.   |


### 4.2 Results Summary

#### Part 1: Strategy Comparison

| **Strategies / Metrics**      | **Memory Usage (MB)** | **Execution Time (s)** | **Execution Time (s)** |
|------------------------------|--------------------|--------------|------------------------|
| **Load Less Data** | 6.58679   |           0.00918031 |             1.08929e+07               |
| **Optimize Data Types**        | 0.477244  |           0.00191927 |             5.21032e+07                |
| **Sampling** | 0.0126791 |           0.00188279 |        531126   |
| **Chunked Processing** | 0.477244  |          74.4943     |          9971.89    |
| **Dask** | 812.491     |         226.977      |        187018            |
| **Polars** |488.621     |          18.8699     |             2.24955e+06            |


#### Part 2: Library Comparison

| Library  | Time (s) | Memory (MB) | Throughput (records/sec)       |
|----------|----------|-------------|--------------------------------|
| Pandas   | 0 | 0     | 0                    |
| Dask     | 0   | 0     | 0                 |
| Polars   | 0   | 0      |                      |

### 4.3 Discussion
🔍 Performance Overview
From the comparative analysis, it is evident that different strategies yield varying levels of performance in terms of memory usage , processing speed , and throughput . Traditional methods like loading the full dataset into memory with Pandas are simple but inefficient for large datasets due to high memory consumption and slower execution times.

🧠 Strategy Insights

| Library  | Pros | Cons | Best For       |
|----------|----------|-------------|--------------------------------|
| Load Less Data   | Fast, low memory usage | May not represent full dataset accurately     | Quick exploratory analysis or prototyping                    |
| Optimize Data Types     | Reduces memory usage significantly without sacrificing accuracy   | Slight increase in preprocessing effort     |  General-purpose optimization with Pandas                 |
| Sampling   | Extremely fast and lightweight  | Provides approximate results only      |  Preliminary analysis or hypothesis testing                    |
| Chunking   | Handles large files without loading everything at once  | Slower than optimized libraries due to sequential processing      |  Limited RAM environments                    |
| Parallel Processing (Dask)   | Excellent for out-of-core computation; scales well   | More complex setup and slightly higher memory overhead     |  Large datasets exceeding available RAM                    |


⚙️ Library Comparison

| Library  |Pandas | Dask | Polars       |
|----|----------------------------------------|----------------------------------------------------------------------|-------------------------------------------|
| 1  | Simple and widely used                 | Parallelizes operations and supports lazy evaluation.                |Blazing-fast in-memory processing.         |
|2   | Not efficient for large-scale data.    | Efficient for large datasets.                                        | Low memory footprint.                     |
| 3  | High memory usage and moderate speed.  |Slightly slower than Polars but better for distributed computing.     |  Ideal for large datasets fitting in RAM. |

📈 Throughput & Efficiency
- Polars consistently showed the highest throughput and lowest memory usage.
- Dask offered a good balance between scalability and performance.
- Traditional Pandas was the slowest and most memory-intensive.

---

## 5. Conclusion and Reflection

### 5.1 Summary of Findings


### 5.2 Benefits & Limitations

| Tool     | Benefits                                  | Limitations                                |
|----------|-------------------------------------------|--------------------------------------------

### 5.3 Personal Reflection

#### Maisarah Binti Rizal


#### Nadhrah NurSabrina Binti Zulaini


---
## 6. References




