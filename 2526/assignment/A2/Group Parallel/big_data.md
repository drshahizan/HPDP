# Assignment 2: Mastering Big Data Handling

**Course:** SECP3133 High Performance Data Processing (Data Engineering)
**University:** Universiti Teknologi Malaysia (UTM)

---

# Group Information

| Name                   | Student ID  |
| ---------------------- | ----------- |
| Ling Yu Qian           | A23CS0301   |
| Cheryl Cheong Kah Voon | A23CS0060   |

---

# 1. Dataset Description

For this assignment, we selected a comprehensive aviation dataset to test our big data handling strategies against a file that exceeds everyday data processing limits.

* **Dataset Name:** Airline Delay Analysis
* **Source:** https://www.kaggle.com/datasets/sherrytp/airline-delay-analysis
* **File Used:** `2009.csv`
* **File Size:** 792.6 MB *(Satisfies the >700 MB requirement)*
* **Domain:** Transportation & Aviation
* **Record Count:** 6,429,338 rows × 21 columns
* **Description:** The dataset contains detailed U.S. domestic flight records, including departure/arrival times, carrier codes, and specific delay reasons (weather, security, late aircraft).

---

# 2. Library Choices

In accordance with the assignment guidelines, we utilized three distinct Python libraries to process the data and analyze scaling performance.

## 2.1 Pandas (Library 1 – Compulsory)

Used as our baseline for traditional, single-threaded, in-memory data processing.

## 2.2 Dask (Library 2 – Scalable)

Selected for its out-of-core computation capabilities. It mimics the Pandas API but operates on data that is too large to fit into memory by breaking it into smaller partitions and processing them in parallel across all CPU cores.

## 2.3 Polars (Library 3 – Scalable)

Selected for its extreme execution speed and low memory footprint. Written in Rust, it utilizes the Apache Arrow columnar format and features a highly optimized lazy evaluation engine with predicate pushdown.

---

# 3. Data Loading and Inspection

Before applying optimizations, we performed a baseline load of the raw `2009.csv` file using standard Pandas to establish our starting performance metrics and understand the data schema.

```python
import pandas as pd
import time
import tracemalloc

DATA_PATH_SINGLE = '/content/airline_delay/2009.csv'

tracemalloc.start()
t0 = time.time()

df_full = pd.read_csv(DATA_PATH_SINGLE)

elapsed_load = time.time() - t0
_, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()

peak_mem_mb = peak_mem / (1024 ** 2)

print(f'Load time   : {elapsed_load:.2f} seconds')
print(f'Peak memory : {peak_mem_mb:.2f} MB')
print(f'Shape       : {df_full.shape}')
```

## Inspection Results

| Metric         | Result                                 |
| -------------- | -------------------------------------- |
| Load Time      | ~12.5 seconds                          |
| Peak Memory    | ~2,100 MB                              |
| Missing Values | Concentrated in delay-specific columns |
| Dataset Shape  | 6,429,338 × 21                         |

### Observation

Loading the full dataset consumes nearly 2.1 GB of RAM just for the raw read operation, demonstrating why traditional naive methods fail on machines with limited memory.

---

# 4. Big Data Handling Strategies

## 4.1 Strategy 1: Load Less Data

### Explanation

Rather than reading the entire file into memory at once, we specify exactly which columns our analysis requires using the `usecols` parameter.

### Code

```python
REQUIRED_COLS = [
    'FL_DATE',
    'OP_CARRIER',
    'ORIGIN',
    'DEST',
    'DEP_DELAY',
    'ARR_DELAY',
    'CANCELLED',
    'DIVERTED',
    'CARRIER_DELAY',
    'WEATHER_DELAY',
    'NAS_DELAY',
    'SECURITY_DELAY',
    'LATE_AIRCRAFT_DELAY'
]

tracemalloc.start()
t0 = time.time()

df_less = pd.read_csv(
    DATA_PATH_SINGLE,
    usecols=REQUIRED_COLS
)

s1_time = time.time() - t0

_, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f'[Strategy 1] Load time   : {s1_time:.2f} s')
print(f'[Strategy 1] Peak memory : {peak / (1024 ** 2):.2f} MB')
print(f'Shape after usecols      : {df_less.shape}')
```

### Observation

By selecting only 13 out of 21 columns, peak memory consumption dropped drastically. The parser still reads every line, but discards unneeded bytes immediately, making it the most effective first line of defense against Out-Of-Memory (OOM) errors.

---

## 4.2 Strategy 2: Chunking

### Explanation

Chunking allows us to process files larger than available RAM. Instead of loading 6.4 million rows simultaneously, we process the file in manageable batches.

### Code

```python
CHUNK_SIZE = 200_000

carrier_delay_sum = {}
carrier_delay_count = {}
chunk_count = 0

reader = pd.read_csv(
    DATA_PATH_SINGLE,
    usecols=['OP_CARRIER', 'DEP_DELAY'],
    chunksize=CHUNK_SIZE
)

for chunk in reader:

    chunk_count += 1

    chunk = chunk.dropna(subset=['DEP_DELAY'])

    grouped = chunk.groupby('OP_CARRIER')['DEP_DELAY']

    for carrier, grp in grouped:

        carrier_delay_sum[carrier] = (
            carrier_delay_sum.get(carrier, 0) + grp.sum()
        )

        carrier_delay_count[carrier] = (
            carrier_delay_count.get(carrier, 0) + len(grp)
        )
```

### Observation

Chunking introduced slight overhead due to the Python loop, but memory usage remained stable. Regardless of whether the file is 700 MB or 7 GB, only one chunk exists in memory at any given time.

---

## 4.3 Strategy 3: Data Type Optimisation

### Explanation

Pandas defaults to 64-bit numerical types and generic object types for strings. We downcasted numerical columns and converted low-cardinality strings into categorical types.

### Code

```python
def optimise_dtypes(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    for col in df.columns:

        col_type = df[col].dtype

        if pd.api.types.is_integer_dtype(col_type):
            df[col] = pd.to_numeric(
                df[col],
                downcast='integer'
            )

        elif pd.api.types.is_float_dtype(col_type):
            df[col] = pd.to_numeric(
                df[col],
                downcast='float'
            )

        elif col_type == object:

            if df[col].nunique() / len(df) < 0.05:
                df[col] = df[col].astype('category')

    return df

df_optimised = optimise_dtypes(df_less)
```

### Observation

This optimization reduced memory usage by approximately 40–60%. Converting strings to categories was particularly effective because Pandas stores integer references instead of millions of repeated strings. As shown in Figure 1, string columns such as `FL_DATE`, `OP_CARRIER`, `ORIGIN`, and `DEST` showed the most dramatic reductions — from approximately 310–365 MB each down to under 15 MB after conversion to the `category` dtype.

---

## 4.4 Strategy 4: Sampling

### Explanation

For rapid prototyping and Exploratory Data Analysis (EDA), we extracted a 5% random sample from the dataset.

### Code

```python
SAMPLE_FRACTION = 0.05
RANDOM_SEED = 42

df_sample = df_optimised.sample(
    frac=SAMPLE_FRACTION,
    random_state=RANDOM_SEED
)
```

### Observation

The sample reduced the working dataset from 6.4 million rows to approximately 321,467 rows. Visualization and exploratory analysis became significantly faster while maintaining statistical representativeness.

---

## 4.5 Strategy 5: Parallel Processing with Scalable Libraries

### Explanation

Standard Pandas operates on a single CPU core. Dask and Polars enable parallel execution across multiple CPU cores by different mechanisms:

| Library | Parallelism Mechanism |
| ------- | --------------------- |
| Dask    | Breaks DataFrame into partitions; schedules tasks on a local multi-core scheduler |
| Polars  | Rust-based work-stealing thread pool; lazy query optimizer with predicate pushdown |

We implement the **same benchmark task** with both libraries: load the CSV, select columns, group by carrier, and compute mean departure delay.

### Dask Implementation

```python
import dask.dataframe as dd
import multiprocessing

print(f'CPU Cores Available: {multiprocessing.cpu_count()}')

tracemalloc.start()
t0 = time.time()

dask_df = dd.read_csv(
    DATA_PATH_SINGLE,
    usecols=['OP_CARRIER', 'DEP_DELAY']
)

dask_result = (
    dask_df.groupby('OP_CARRIER')['DEP_DELAY']
    .mean()
    .compute()
    .sort_values(ascending=False)
)

dask_time = time.time() - t0
_, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
dask_mem = peak / (1024 ** 2)

print(f'[Dask] Execution time : {dask_time:.2f} s')
print(f'[Dask] Peak memory    : {dask_mem:.2f} MB')
print(dask_result)
```

### Polars Implementation

```python
import polars as pl
import time
import tracemalloc

tracemalloc.start()
t0 = time.time()

polars_result = (
    pl.read_csv(DATA_PATH_SINGLE)
    .select(['OP_CARRIER', 'DEP_DELAY'])
    .group_by('OP_CARRIER')
    .agg(
        pl.col('DEP_DELAY').mean()
    )
    .sort(
        'DEP_DELAY',
        descending=True
    )
)

polars_time = time.time() - t0
_, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
polars_mem = peak / (1024 ** 2)

print(f'[Polars] Execution time : {polars_time:.2f} s')
print(f'[Polars] Peak memory    : {polars_mem:.2f} MB')
print(polars_result)
```

### Observation

Both Dask and Polars successfully utilized multiple CPU cores. However, as shown in Figure 3, Dask incurred significant task-graph scheduling overhead (~14 s) on this single-node workload, making it slower than both Pandas (~7.8 s) and Polars (~8.2 s) for this particular benchmark. Dask's real advantage emerges in distributed or out-of-core scenarios where data exceeds available RAM. Polars' Rust-based execution and lazy evaluation make it consistently fast even on single-node tasks.

---

# 5. Comparative Analysis

To objectively measure performance, we executed a benchmark workflow:

**Read CSV → Select Columns → Group By Carrier → Calculate Mean Departure Delay**

## 5.1 Performance Metrics

The following results are taken directly from the benchmark charts (Figures 3 and 4).

| Library           | Execution Time (Seconds) | Peak Memory Usage (MB) |
| ----------------- | ------------------------ | ---------------------- |
| Pandas (Baseline) | ~7.8 s                   | ~355 MB                |
| Dask              | ~14.0 s                  | ~320 MB                |
| Polars            | ~8.2 s                   | ~0 MB (not measured)   |

> **Note:** Polars' peak memory was not captured by `tracemalloc` in this benchmark run — likely because Polars allocates memory outside the Python heap via its Rust runtime. A dedicated memory profiler (e.g., `memory_profiler` or OS-level monitoring) is required for an accurate reading.

---

## 5.2 Visualizations

### Figure 1: Memory Usage Before and After Data Type Optimisation

![Memory Usage Before and After Data Type Optimisation](strategy3_dtype_optimisation.png)

**Discussion**

Figure 1 illustrates the memory consumption of each column before and after applying data type optimisation. Significant reductions are visible in categorical string columns such as `FL_DATE`, `OP_CARRIER`, `ORIGIN`, and `DEST`, where memory usage fell from roughly 310–365 MB each to under 15 MB after conversion to the `category` dtype. Numerical columns also benefited modestly from integer and float downcasting. Overall, the optimisation strategy substantially reduced the dataset's total memory footprint, demonstrating that proper data type selection is a simple yet highly effective technique for handling large datasets.

---

### Figure 2: Exploratory Data Analysis on 5% Sample Dataset

![Exploratory Data Analysis on Sample Dataset](strategy4_sample_eda.png)

**Discussion**

Figure 2 presents exploratory analysis performed on a 5% random sample of the dataset, containing approximately 321,467 rows. The departure delay distribution (top-left) shows that most flights experienced minimal or negative delays, with a mean of 7.6 minutes and a right-skewed tail indicating a small proportion of severely delayed flights. The cancellation rate analysis (top-right) highlights that carrier `OH` had the highest cancellation rate (~3.3%), while `HA` had the lowest (~0.1%), indicating significant differences in operational reliability. Average arrival delay comparisons (bottom-left) show carrier `EV` with the highest average arrival delay (~12 min) and `HA` with the lowest (~0.2 min). The busiest origin airports in the sample (bottom-right) are ATL, ORD, and DFW, consistent with major U.S. aviation hubs. These findings demonstrate that sampling can greatly reduce processing time while preserving meaningful statistical patterns.

---

### Figure 3: Execution Time Comparison Between Libraries

![Execution Time Comparison](execution_time_comparison.png)

**Discussion**

Figure 3 compares execution time for Pandas (~7.8 s), Dask (~14.0 s), and Polars (~8.2 s). Contrary to expectations, Dask was the slowest library on this benchmark. This is because Dask's performance advantage emerges at larger scales or in distributed cluster environments; on a single node with a dataset that fits within memory, its task-graph scheduling overhead outweighs any parallelism benefit. Pandas and Polars performed comparably in execution time for this specific workflow.

---

### Figure 4: Peak Memory Usage Comparison Between Libraries

![Peak Memory Usage Comparison](memory_usage_comparison.png)

**Discussion**

Figure 4 compares peak memory consumption: Pandas used approximately 355 MB, Dask approximately 320 MB, and Polars registered near 0 MB under `tracemalloc`. Dask's slight memory advantage over Pandas is due to processing data in partitions. Polars' near-zero reading reflects that its Rust-based allocator operates outside the Python heap and is invisible to `tracemalloc` — not that it uses no memory. A system-level profiler would be needed for a fair Polars memory measurement.

---

## 5.3 Critical Discussion

### Pandas Constraints

Pandas was relatively fast on this benchmark (~7.8 s) because the selected columns fit comfortably in memory after applying `usecols`. Its main limitations remain: eager evaluation, single-core execution, and high memory usage on full unoptimized loads.

### Dask Architecture

Dask underperformed on this single-node task (~14.0 s) due to task-graph construction and scheduling overhead. Its real advantage emerges with datasets that exceed RAM or in distributed multi-node deployments where work can be parallelized across a cluster.

### Why Polars Stands Out

Polars achieved competitive execution time (~8.2 s) with lower measured Python-heap memory usage, benefiting from:

* Lazy Evaluation
* Predicate Pushdown
* Apache Arrow Columnar Format
* Rust-Based Multithreading
* No Python GIL Limitation

For larger or more complex query workloads, Polars' architectural advantages compound further and its speed lead over Pandas grows significantly.

---

# 6. Conclusion and Reflection

## 6.1 Summary of Observations

No single strategy acts as a universal solution.

* `usecols` significantly reduces memory usage at load time.
* Data type optimization offers large memory savings with minimal effort.
* Chunking prevents memory crashes regardless of file size.
* Sampling accelerates experimentation and EDA.
* Polars delivers strong performance with low memory overhead for large-scale analytics; Dask's benefits are most pronounced in distributed or out-of-core scenarios.

---

## 6.2 Personal Reflection

### Ling Yu Qian

Working through this assignment revealed the significant gap between understanding big data concepts and implementing practical solutions. The most surprising finding was how dramatically data type optimization reduced memory consumption. Before this assignment, we routinely accepted Pandas default data types without questioning them. We also experienced practical limitations when Google Colab crashed during full dataset loading, highlighting the importance of efficient data handling strategies.

### Cheryl Cheong Kah Voon

Through this assignment, I gained valuable experience working with scalable data processing libraries. Exploring Dask and Polars helped me understand how modern systems achieve performance gains through parallelism and optimized execution. Polars, in particular, encouraged a different programming mindset by emphasizing query planning and lazy execution. This project strengthened my appreciation for hardware-aware software design.

---

## 6.3 Scalability Considerations

### At 10 GB

Single-node Pandas would struggle significantly. We would rely on:

* Polars Streaming Mode
* Dask on a machine with 16–32 GB RAM
* Mandatory chunking

### At 100 GB

Single-machine processing becomes impractical.

Potential solutions include:

* Dask Distributed Cluster
* AWS Athena
* Google BigQuery

### At 1 TB+

Distributed cloud-native solutions become necessary:

* Apache Spark
* Databricks
* Snowflake
* Amazon S3 + Parquet Storage
* Kubernetes/YARN Clusters

Understanding when to transition between these architectures is one of the most important lessons learned from this assignment.

---

# References

1. Airline Delay Analysis Dataset. Kaggle. Retrieved from: https://www.kaggle.com/datasets/sherrytp/airline-delay-analysis

2. Polars Documentation (2024). Retrieved from: https://pola.rs

3. Dask Documentation (2024). Retrieved from: https://dask.org
