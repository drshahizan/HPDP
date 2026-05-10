# Assignment 2: Mastering Big Data Handling

## Group Information
* **Group Name:** youtube_trending_video
* **Members:** CHOH JING YI & TAN ZHI MING

---

## 1. Dataset Description
* **Dataset Name:** YouTube Trending Video Dataset
* **Source URL:** [https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset]
* **File Size:** > 700 MB (Combined regional files including BR, CA, DE, FR)
* **Domain:** Social Media / Entertainment
* **Number of Records:** 1,075,056 rows
* **Description:** This dataset contains daily records of the top trending YouTube videos across multiple regions. It includes high-cardinality string data (titles, channel names, tags, descriptions) alongside heavy numerical engagement metrics (views, likes, dislikes, comment counts), making it an ideal candidate for memory optimization and parallel processing benchmarks.

---

## 2. Library Choices
To fulfill the core technical requirements, we selected the following libraries:
1. **Pandas (Library 1 - Compulsory Baseline):** Used as the standard, single-threaded reference point to measure memory consumption and execution time.
2. **Polars (Library 2 - Scalable):** Selected for its extremely fast, multi-threaded Rust backend and its "lazy evaluation" architecture, which optimizes query plans before executing them.
3. **Dask (Library 3 - Scalable):** Selected to demonstrate distributed computing. Dask mirrors the Pandas API but breaks massive datasets into out-of-core partitions, spreading tasks across multiple CPU cores.

---

## 3. Data Loading and Inspection
To establish a baseline, we loaded four regional CSV files and concatenated them into a single massive DataFrame using standard Pandas functions.

```python
import pandas as pd
import glob
import os

# 1. Define the folder path and find all CSV files
folder_path = '/content/drive/MyDrive/youtube_trending_video/'
all_files = glob.glob(os.path.join(folder_path, "*.csv"))

# 2. Load and concatenate
df_list = [pd.read_csv(file) for file in all_files]
df_baseline = pd.concat(df_list, ignore_index=True)

# 3. Inspect
print(f"Shape: {df_baseline.shape[0]:,} rows and {df_baseline.shape[1]} columns.")
memory_mb = df_baseline.memory_usage(deep=True).sum() / (1024 * 1024)
print(f"Baseline Memory Usage: {memory_mb:.2f} MB")

```

---

## 4. Big Data Handling Strategies

### 4.1 Load Less Data

**Explanation:**
When a dataset contains dozens of columns, loading all of them is highly inefficient if the analysis only requires a subset. By using the `usecols` parameter, we instruct Pandas to parse and load only the specified columns during the read operation, preventing unnecessary data from ever entering RAM.

```python
# Drop heavy text columns like 'description', 'tags', and 'thumbnail_link'
columns_to_load = [
    'video_id', 'title', 'channelTitle', 'categoryId', 
    'view_count', 'likes', 'dislikes', 'comment_count'
]

df_list_less = [pd.read_csv(file, usecols=columns_to_load) for file in all_files]
df_strategy1 = pd.concat(df_list_less, ignore_index=True)

memory_mb_less = df_strategy1.memory_usage(deep=True).sum() / (1024 * 1024)
print(f"Memory Usage after Strategy 1: {memory_mb_less:.2f} MB")

```

### 4.2 Chunking

**Explanation:**
Chunking prevents Out-Of-Memory (OOM) errors by reading data in smaller, sequential blocks. The system processes a chunk, stores the intermediate results, discards the chunk from memory, and moves to the next.

```python
import time

start_time = time.time()
chunk_size = 50000 
total_views_per_channel = pd.Series(dtype='int64')

for file in all_files:
    chunk_iterator = pd.read_csv(file, chunksize=chunk_size, usecols=['channelTitle', 'view_count'])
    for chunk in chunk_iterator:
        chunk_agg = chunk.groupby('channelTitle')['view_count'].sum()
        total_views_per_channel = total_views_per_channel.add(chunk_agg, fill_value=0)

top_5_channels = total_views_per_channel.sort_values(ascending=False).head(5)
print(f"Chunking execution completed in: {time.time() - start_time:.2f} seconds.")

```

### 4.3 Data Type Optimisation

**Explanation:**
Pandas assigns highly permissive data types (`int64` and `object`) by default. Optimising data types involves actively mapping columns to their most compact representation based on their actual value ranges, applying this directly at load time to prevent memory spikes.

```python
optimized_dtypes = {
    'channelTitle': 'category',  
    'categoryId': 'int16',       
    'view_count': 'uint32',      
    'likes': 'uint32',
    'dislikes': 'uint32',
    'comment_count': 'uint32'
}

df_list_opt = [pd.read_csv(file, usecols=columns_to_load, dtype=optimized_dtypes) for file in all_files]
df_strategy3 = pd.concat(df_list_opt, ignore_index=True)

memory_mb_opt = df_strategy3.memory_usage(deep=True).sum() / (1024 * 1024)
print(f"Memory Usage after Strategy 3: {memory_mb_opt:.2f} MB")

```

### 4.4 Sampling

**Explanation:**
Executing every test run on the full dataset severely bottlenecks the development process. Sampling extracts a statistically representative subset, allowing engineers to rapidly prototype logic and catch errors almost instantly.

```python
df_sample = df_strategy3.sample(frac=0.10, random_state=42)

start_time_sample = time.time()
sample_avg_views = df_sample.groupby('categoryId')['view_count'].mean().sort_values(ascending=False).head(5)
sample_execution_time = time.time() - start_time_sample

print(f"Exploratory aggregation on SAMPLE completed in: {sample_execution_time:.4f} seconds.")

```

### 4.5 Parallel Processing

**Explanation:**
Standard Pandas operations are single-threaded. To scale horizontally, we must distribute operations across multiple cores. We benchmarked a full "Load and Aggregate" pipeline across Pandas, Polars, and Dask.

```python
import polars as pl
import dask.dataframe as dd

# Polars (Lazy Evaluation)
polars_result = (
    pl.scan_csv(file_path_pattern)
    .select(columns_to_load) 
    .group_by('channelTitle')
    .agg(pl.col('view_count').sum())
    .sort('view_count', descending=True)
    .limit(5)
    .collect() 
)

# Dask (Distributed Partitions)
dask_df = dd.read_csv(file_path_pattern, usecols=columns_to_load)
dask_result = (
    dask_df.groupby('channelTitle')['view_count']
    .sum()
    .nlargest(5)
    .compute() 
)

```

---

## 5. Comparative Analysis

To evaluate the efficiency of our big data handling strategies, we benchmarked our baseline Pandas implementation against Polars and Dask.

### 5.1 Comparison Tables

**Table 1: Memory Usage Optimization (Pandas)**
This table illustrates the impact of vertical scaling strategies applied to the dataset before introducing scalable libraries.

| Processing Stage | Memory Usage (MB) | Reduction vs Baseline |
| --- | --- | --- |
| **Baseline (All Columns, Default Types)** | 3,430.50 MB | 0.0% |
| **Strategy 1 (Load Less Data)** | 300.19 MB | ~91.2% |
| **Strategy 3 (Optimized Data Types)** | 279.18 MB | ~91.8% |

**Table 2: Execution Time by Library**
This table compares the time taken to load the optimized dataset and perform the aggregation across all three libraries.

| Library | Architecture Type | Execution Time | Performance vs Pandas |
| --- | --- | --- | --- |
| **Pandas** | Single-Threaded (Baseline) | 26.37s | 1.0x (Baseline) |
| **Dask** | Distributed (Partitioned) | 26.12s | ~1.01x (Negligible) |
| **Polars** | Multi-Threaded (Lazy Evaluation) | 3.78s | ~7.0x Faster |

### 5.2 Charts and Graphs
<img width="1140" height="461" alt="image" src="https://github.com/user-attachments/assets/4184739c-8a76-4a46-9f11-984391c4c06d" />

### 5.3 Critical Discussion

The benchmark results clearly highlight the architectural differences and trade-offs between standard single-threaded processing and modern parallel processing frameworks.

**Memory Optimization Findings:**
Our baseline Pandas load consumed a massive 3,430.50 MB of RAM, threatening to crash the single-node environment. The most impactful strategy was "Load Less Data", which dropped memory usage down to 300.19 MB simply by excluding heavy, unneeded text columns. Data Type Optimisation further shaved off another 21 MB by downcasting integers. This proves that I/O filtration is the most critical first step in big data engineering before any computation even begins.

**Execution Time and Architecture Trade-offs:**
During the aggregation phase, Pandas created a clear bottleneck, taking 26.37s due to its reliance on eager evaluation and single-core processing.

While **Dask** is designed for parallel computing, its execution time (26.12s) was almost identical to Pandas. This highlights a crucial trade-off: Dask carries significant overhead for task scheduling and graph generation. On a single Colab instance with a limited number of CPU cores and a dataset of ~1 million rows, Dask's overhead essentially canceled out its parallel processing gains. Dask is architecturally built for massive clusters, not single machines.

**Polars**, however, drastically outperformed both, completing the task in just 3.78 seconds. This extreme performance jump is due to two key design features:

1. **Rust Backend:** It bypasses Python's Global Interpreter Lock (GIL), allowing it to utilize all CPU cores simultaneously.
2. **Lazy Evaluation:** Rather than executing code line-by-line, Polars compiled our `.scan_csv()` command into an optimized query engine. It performed "projection pushdown," intelligently reading *only* the needed columns directly from the disk, bypassing the memory ingestion phase entirely.

---

## 6. Conclusion and Reflection

### 6.1 Summary of Findings

This assignment highlighted the severe limitations of traditional data processing tools when applied to large datasets. The most impactful takeaway regarding memory optimization was that the simplest strategy—loading only necessary columns (`usecols`)—provided the greatest benefit, dropping our RAM usage from 3,430 MB down to just 300 MB. Regarding execution time, the architectural shift from single-threaded operations to parallel computing was transformative. While Dask provided steady distributed performance, Polars completely outclassed the competition (3.78 seconds) due to its Rust backend and lazy evaluation model, making it the clear choice for single-node data pipelines.

### 6.2 Personal Reflection

The most surprising aspect of this workflow was discovering how much memory standard Pandas wastes by defaulting to `int64` and `object` types. Downcasting data types and utilizing chunking forced a shift in mindset: instead of just writing code that works, we had to write code that respects the hardware limitations of the environment. Implementing Polars also shifted our perspective on query planning; explicitly separating the definition of a query from its execution (`.collect()`) feels much closer to how professional, scalable pipelines are built.

### 6.3 The Importance of Scalability (10 GB to 1 TB+)

While strategies like chunking and parallel processing using Polars are highly effective for a dataset of this size on a single machine, these approaches would eventually hit a ceiling. If this dataset scaled to 100 GB or 1 TB, a single Google Colab instance would fail regardless of optimization.

At the terabyte scale, we would need to abandon single-node processing entirely and migrate to distributed cloud infrastructure. The data would likely need to be structured within a Medallion architecture (Bronze, Silver, Gold layers) to systematically clean and aggregate the massive influx of logs. To process this, we would transition to enterprise platforms like Google Cloud Platform (GCP) or Azure Databricks, utilizing distributed engines like Apache Spark or Dask clusters to spread the compute load across multiple virtual machines.

---

## References

* Sharma, R. (2020). *YouTube Trending Video Dataset*. Kaggle. [https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset](https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset)
* Polars Documentation: [https://pola.rs/](https://pola.rs/)
* Dask Documentation: [https://dask.org/](https://www.google.com/search?q=https://dask.org/)

```

```
