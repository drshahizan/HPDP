# Assignment 2: Mastering Big Data Handling

## Group Information

**Group Name:** Potato  

**Members:**  
- Lau Yee Wen (A23CS0099)  
- Chau Ying Jia (A23CS0213)
---

## 1. Dataset Description

| Field | Details |
|---|---|
| **Dataset Name** | Netflix User Ratings |
| **Source** | [Kaggle — Netflix Movie Ratings](https://www.kaggle.com/datasets/evanschreiner/netflix-movie-ratings) |
| **Domain** | Entertainment / Recommendation Systems |
| **File Format** | CSV |
| **File Size** | 2585.43 MB |
| **Total Records** | 100,480,507 rows |
| **Number of Columns** | 4 (CustId, Rating, Date, MovieId) |

### Data Dictionary

| Column | Description | Data Type | Example | Purpose |
|---|---|---|---|---|
| **CustId** | A unique identifier for each Netflix customer who gave a rating. | Integer | 1488844 | Used to identify which customer provided the rating. |
| **Rating** | The rating score given by the customer for a movie. The value ranges from 1 to 5. | Integer | 3 | Used to measure user satisfaction and calculate average movie ratings. |
| **Date** | The date when the customer rating was recorded. | Date / Object before optimisation | 2005-09-06 | Used for time-based analysis, such as rating trends over time. |
| **MovieId** | A unique identifier for each movie in the Netflix dataset. | Integer | 1 | Used to group ratings by movie and calculate movie-level statistics. |

This dataset contains over 100 million Netflix user ratings. Each record captures a customer ID, the movie they rated, the rating they gave (1–5), and the date of the rating. Its scale and diversity of column types make it ideal for evaluating big data handling strategies.

---

## 2. Library Choices

| Library | Role |
|---|---|
| **Pandas** (Library 1) | Baseline — single-threaded, in-memory data processing |
| **Dask** (Library 2) | Scalable — partitioned, parallel processing for out-of-memory datasets |
| **Polars** (Library 3) | Scalable — Rust-based engine with lazy evaluation and multi-threading |

**Why Pandas?**  
Pandas is used as the baseline library because it is simple, widely used, and easy to understand for data analysis in Python. It provides a familiar DataFrame structure and many built-in functions for loading, filtering, grouping, and summarising data. In this assignment, Pandas is useful for showing the normal in-memory processing approach before comparing it with more scalable libraries such as Dask and Polars. However, because Pandas loads the full dataset into RAM, it may face memory limitations when handling very large datasets.

**Why Dask?**
Dask mirrors the Pandas API but splits data into partitions and processes them in parallel across CPU cores. It is well suited for datasets that exceed available RAM and supports distributed computing, making it a natural upgrade path from Pandas for very large-scale workloads.

**Why Polars?**
Polars is written in Rust and built around a lazy query engine. It applies query optimisation before execution, uses SIMD vectorisation, and is natively multi-threaded. These design choices make it exceptionally fast on single-machine analytical workloads.

---

## 3. Environment Setup

Before applying any big data strategies, we mount Google Drive to access the dataset and install all required libraries.

```python
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Install required libraries
!pip install dask polars memory_profiler

# Import all required libraries
import pandas as pd
import dask.dataframe as dd
import polars as pl
import time
import os
import tracemalloc
from memory_profiler import memory_usage

# Dataset file path (used throughout this notebook)
file_path = '/content/drive/MyDrive/HPDP/ASS 2 Dataset/Netflix_User_Ratings.csv'
```

**Output:**

```
Requirement already satisfied: dask in /usr/local/lib/python3.12/dist-packages (2026.3.0)
Requirement already satisfied: polars in /usr/local/lib/python3.12/dist-packages (1.35.2)
Requirement already satisfied: memory_profiler in /usr/local/lib/python3.12/dist-packages (0.61.0)
...
Drive already mounted at /content/drive
```

| Library | Version |
|---|---|
| Pandas | pre-installed |
| Dask | 2026.3.0 |
| Polars | 1.35.2 |
| memory_profiler | 0.61.0 |

---

## 4. Data Loading and Inspection

Before applying any big data strategies, we first inspect the dataset to understand its structure, size, and quality. This step is essential — it tells us how many rows and columns exist, what data types each column uses, whether any values are missing, and the actual file size on disk.

We use `nrows` to preview a small sample safely, then count total rows via chunking to avoid loading the full file into memory at once.

```python
# File size
file_size_bytes = os.path.getsize(file_path)
file_size_mb = file_size_bytes / (1024 ** 2)
print(f"File Size: {file_size_mb:.2f} MB")

# Preview structure (safe: only loads 5 rows)
df_preview = pd.read_csv(file_path, nrows=5)
print(f"\nColumn Names:\n{df_preview.columns.tolist()}")
print(f"\nData Types:\n{df_preview.dtypes}")

# Missing values (on a sample of 100,000 rows)
df_sample = pd.read_csv(file_path, nrows=100000)
print(f"\nMissing Values (first 100,000 rows):\n{df_sample.isnull().sum()}")

print("\nFirst 5 Rows:")
df_preview
```

**Output:**

```
File Size: 2585.43 MB

Column Names:
['CustId', 'Rating', 'Date', 'MovieId']

Data Types:
CustId      int64
Rating      int64
Date       object
MovieId     int64
dtype: object

Missing Values (first 100,000 rows):
CustId     0
Rating     0
Date       0
MovieId    0
dtype: int64

First 5 Rows:
     CustId  Rating        Date  MovieId
0   1488844       3  2005-09-06        1
1    822109       5  2005-05-13        1
2    885013       4  2005-10-19        1
3     30878       4  2005-12-26        1
4    823519       3  2004-05-03        1
```

```python
# Count total rows using chunking (avoids loading full file into RAM)
chunk_size = 100000
total_rows = 0

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    total_rows += len(chunk)

print(f"Total Number of Records: {total_rows:,}")
```

**Output:**

```
Total Number of Records: 100,480,507
```

### Inspection Summary

| Field | Value |
|---|---|
| **File Size** | 2585.43 MB |
| **Total Records** | 100,480,507 rows |
| **Number of Columns** | 4 (CustId, Rating, Date, MovieId) |
| **Missing Values** | None detected in sample |
| **Key Observation** | Default dtypes (int64, object) are memory-inefficient — optimisation will be applied in Strategy 3 |

---

## 5. Big Data Handling Strategies

### 5.1 Strategy 1: Load Less Data

**Explanation:** <br>
Although this dataset only has 4 columns, not all of them are needed for every analysis task. For example, calculating the average rating per movie only requires `MovieId` and `Rating` — loading `CustId` and `Date` wastes memory unnecessarily.

By using the `usecols` parameter, we load only the 2 columns relevant to our task. This demonstrates the principle of loading less data: only bring into memory what your analysis actually requires.

**When to use it:** At the very start of any data loading step, when you know in advance which columns are relevant. It is the simplest and most impactful first optimisation.

```python
import pandas as pd
import time
import tracemalloc

# Load ALL columns (baseline)
tracemalloc.start()
start = time.time()

df_all = pd.read_csv(file_path, nrows=500000)

end = time.time()
mem_all = tracemalloc.get_traced_memory()[1] / (1024 ** 2)
tracemalloc.stop()

time_all = end - start
size_all = df_all.memory_usage(deep=True).sum() / (1024 ** 2)

print("=== Load ALL Columns ===")
print(f"Columns loaded : {df_all.columns.tolist()}")
print(f"Time taken     : {time_all:.4f} seconds")
print(f"DataFrame size : {size_all:.2f} MB")
print(f"Peak RAM used  : {mem_all:.2f} MB")

# Load SELECTED columns only
tracemalloc.start()
start = time.time()

df_less = pd.read_csv(file_path, usecols=["CustId", "Rating"], nrows=500000)

end = time.time()
mem_less = tracemalloc.get_traced_memory()[1] / (1024 ** 2)
tracemalloc.stop()

time_less = end - start
size_less = df_less.memory_usage(deep=True).sum() / (1024 ** 2)

print("\n=== Load SELECTED Columns Only ===")
print(f"Columns loaded : {df_less.columns.tolist()}")
print(f"Time taken     : {time_less:.4f} seconds")
print(f"DataFrame size : {size_less:.2f} MB")
print(f"Peak RAM used  : {mem_less:.2f} MB")

print("\n=== Reduction Summary ===")
print(f"Memory saved   : {size_all - size_less:.2f} MB")
print(f"Reduction      : {((size_all - size_less) / size_all) * 100:.1f}%")
print(f"Time saved     : {time_all - time_less:.4f} seconds")
```

**Output:**

```
=== Load ALL Columns ===
Columns loaded : ['CustId', 'Rating', 'Date', 'MovieId']
Time taken     : 0.5888 seconds
DataFrame size : 39.58 MB
Peak RAM used  : 54.64 MB

=== Load SELECTED Columns Only ===
Columns loaded : ['CustId', 'Rating']
Time taken     : 0.4188 seconds
DataFrame size : 7.63 MB
Peak RAM used  : 16.08 MB

=== Reduction Summary ===
Memory saved   : 31.95 MB
Reduction      : 80.7%
Time saved     : 0.1700 seconds
```

#### Strategy 1 Results

| Metric | All Columns | Selected Columns Only |
|---|---|---|
| **Columns Loaded** | 4 | 2 |
| **DataFrame Size** | 39.58 MB | 7.63 MB |
| **Peak RAM Used** | 54.64 MB | 16.08 MB |
| **Load Time** | 0.5888 s | 0.4188 s |
| **Memory Reduction** | — | **80.7%** |

**Discussion:** <br>
By loading only `CustId` and `Rating`, memory usage dropped by 80.7% immediately. Even with only 4 columns in this dataset, selectively loading what is needed is the simplest and most impactful first step in any data pipeline.

---

### 5.2 Strategy 2: Chunking

**Explanation:** <br>
Chunking means reading a large file in small portions (called chunks) rather than loading it all at once. Each chunk is processed individually, then discarded before the next chunk is loaded.

This allows us to work with files that are larger than available RAM at any given moment, only one small chunk exists in memory.

**When to use it:** When you need to perform aggregation or filtering on a file too large to load in one go, especially in memory-limited environments like Google Colab's free tier.

```python
import pandas as pd
import time
import tracemalloc

chunk_size = 100000
total_sum = 0
total_count = 0
chunks_processed = 0

tracemalloc.start()
start = time.time()

for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    total_sum += chunk["Rating"].sum()
    total_count += len(chunk)
    chunks_processed += 1

end = time.time()
mem_chunk = tracemalloc.get_traced_memory()[1] / (1024 ** 2)
tracemalloc.stop()

average_rating = total_sum / total_count
chunk_time = end - start

print("=== Chunking Results ===")
print(f"Chunks processed : {chunks_processed}")
print(f"Total rows       : {total_count:,}")
print(f"Average Rating   : {average_rating:.4f}")
print(f"Total Time       : {chunk_time:.4f} seconds")
print(f"Peak RAM used    : {mem_chunk:.2f} MB")
print(f"\nKey insight: Only {chunk_size:,} rows existed in memory at any one time,")
print(f"regardless of the full dataset size.")
```

**Output:**

```
=== Chunking Results ===
Chunks processed : 1005
Total rows       : 100,480,507
Average Rating   : 3.6043
Total Time       : 68.0926 seconds
Peak RAM used    : 14.96 MB

Key insight: Only 100,000 rows existed in memory at any one time,
regardless of the full dataset size.
```

#### Strategy 2 Results

| Metric | Value |
|---|---|
| **Chunk Size** | 100,000 rows |
| **Total Chunks Processed** | 1,005 |
| **Total Rows Processed** | 100,480,507 |
| **Average Rating** | 3.6043 |
| **Total Time** | 68.09 seconds |
| **Peak RAM Used** | 14.96 MB |

**Discussion:** <br>
At no point did the full dataset exist in memory. Only 100,000 rows were held in RAM at any one time, making this approach viable even if the dataset were 10× larger. The trade-off is speed, chunking is slower than a direct load because of the repeated read operations. However, it is the only viable method when dataset size exceeds available RAM.

---

### 5.3 Strategy 3: Data Type Optimisation

**Explanation:** <br>
When Pandas loads a CSV file, it automatically assigns default data types to each column. These defaults are often larger than necessary and waste memory.

By downcasting each column to its smallest fitting type, we can reduce the dataset's memory footprint significantly without losing any data or accuracy.

**When to use it:** After initial inspection, once you know the value range of each column. Apply before any major processing so all subsequent operations benefit from the reduced memory.

| Column | Default Type | Actual Range | Optimised Type |
|---|---|---|---|
| `CustId` | int64 (8 bytes) | Large IDs | int32 (4 bytes) |
| `MovieId` | int64 (8 bytes) | Small IDs | int16 (2 bytes) |
| `Rating` | int64 (8 bytes) | 1 to 5 only | int8 (1 byte) |
| `Date` | object (string) | Date values | datetime64 |

```python
import pandas as pd
import tracemalloc
import time

# BEFORE Optimisation
tracemalloc.start()
start = time.time()

df_before = pd.read_csv(file_path, nrows=500000)

end = time.time()
mem_before_peak = tracemalloc.get_traced_memory()[1] / (1024 ** 2)
tracemalloc.stop()

time_before = end - start
size_before = df_before.memory_usage(deep=True).sum() / (1024 ** 2)

print("=== BEFORE Optimisation ===")
print(f"Data Types:\n{df_before.dtypes}")
print(f"\nDataFrame Size : {size_before:.2f} MB")
print(f"Peak RAM Used  : {mem_before_peak:.2f} MB")
print(f"Load Time      : {time_before:.4f} seconds")
```

**Output (Before):**

```
=== BEFORE Optimisation ===
Data Types:
CustId      int64
Rating      int64
Date       object
MovieId     int64
dtype: object

DataFrame Size : 39.58 MB
Peak RAM Used  : 54.63 MB
Load Time      : 0.5145 seconds
```

```python
# AFTER Optimisation
dtype_dict = {
    "CustId"  : "int32",
    "MovieId" : "int16",
    "Rating"  : "int8"
}

tracemalloc.start()
start = time.time()

df_after = pd.read_csv(file_path, dtype=dtype_dict, nrows=500000)
df_after["Date"] = pd.to_datetime(df_after["Date"])

end = time.time()
mem_after_peak = tracemalloc.get_traced_memory()[1] / (1024 ** 2)
tracemalloc.stop()

time_after = end - start
size_after = df_after.memory_usage(deep=True).sum() / (1024 ** 2)

print("=== AFTER Optimisation ===")
print(f"Data Types:\n{df_after.dtypes}")
print(f"\nDataFrame Size : {size_after:.2f} MB")
print(f"Peak RAM Used  : {mem_after_peak:.2f} MB")
print(f"Load Time      : {time_after:.4f} seconds")

mem_reduction = ((size_before - size_after) / size_before) * 100
time_diff = time_after - time_before

print("\n=== Reduction Summary ===")
print(f"Memory saved      : {size_before - size_after:.2f} MB")
print(f"Memory reduced    : {mem_reduction:.1f}%")
if time_diff > 0:
    print(f"Load time overhead: +{time_diff:.4f}s (due to type casting at load)")
else:
    print(f"Time saved        : {abs(time_diff):.4f} seconds")
```

**Output (After):**

```
=== AFTER Optimisation ===
Data Types:
CustId              int32
Rating               int8
Date       datetime64[ns]
MovieId             int16
dtype: object

DataFrame Size : 7.15 MB
Peak RAM Used  : 35.08 MB
Load Time      : 0.8676 seconds

=== Reduction Summary ===
Memory saved      : 32.42 MB
Memory reduced    : 81.9%
Load time overhead: +0.3531s (due to type casting at load)
```

#### Strategy 3 Results

| Metric | Before Optimisation | After Optimisation |
|---|---|---|
| `CustId` type | int64 | int32 |
| `MovieId` type | int64 | int16 |
| `Rating` type | int64 | int8 |
| `Date` type | object | datetime64 |
| **DataFrame Size** | 39.58 MB | 7.15 MB |
| **Peak RAM Used** | 54.63 MB | 35.08 MB |
| **Load Time** | 0.5145 s | 0.8676 s |

**Discussion:** <br>
**Memory Reduction: 81.9%**

Data type optimisation reduced the DataFrame size from 39.58 MB to 7.15 MB, achieving an 81.9% reduction by downcasting each column to its smallest fitting type. The `Rating` column alone decreased from 8 bytes per value (int64) to just 1 byte (int8), since ratings only range from 1 to 5.

**Note on load time:** The optimised load was slightly slower by 0.35 seconds because Pandas performs additional work during loading. These include casting each column to the specified type and parsing the `Date` column into datetime64 format. This small upfront cost is worthwhile because all subsequent operations on the optimised DataFrame will be faster and consume significantly less memory.

This trade-off is an important insight. Data type optimisation is not intended to improve loading speed. Instead, it focuses on reducing long term memory usage so that downstream processing becomes more efficient and scalable.

---

### 5.4 Strategy 4: Sampling

**Explanation:** <br>
Sampling involves selecting a smaller, representative subset of the full dataset for analysis. Instead of processing millions of rows during development, we work with a random sample that is large enough to be statistically meaningful but small enough to process instantly.

**When to use it:** During early exploration and code development. Once your pipeline is validated on the sample, apply it to the full dataset or process it via chunks.

**Important:** Sampling is not a replacement for full processing; it is a development tool. Final results should always be validated against the complete data.

```python
import pandas as pd
import tracemalloc
import time

# Load a base portion to sample from
df_base = pd.read_csv(file_path, nrows=500000)

# Take a random sample of 100,000 rows
df_sampled = df_base.sample(n=100000, random_state=42)

print("=== Dataset Sizes ===")
print(f"Full base shape   : {df_base.shape}")
print(f"Sampled shape     : {df_sampled.shape}")
print(f"Sample percentage : {(len(df_sampled) / len(df_base)) * 100:.1f}%")
```

**Output:**

```
=== Dataset Sizes ===
Full base shape   : (500000, 4)
Sampled shape     : (100000, 4)
Sample percentage : 20.0%
```

```python
# Compare processing time: full vs sample
operation = lambda df: df.groupby("MovieId")["Rating"].mean()

# Full data timing
tracemalloc.start()
start = time.time()
result_full = operation(df_base)
full_time = time.time() - start
mem_full = tracemalloc.get_traced_memory()[1] / (1024 ** 2)
tracemalloc.stop()

# Sample timing
tracemalloc.start()
start = time.time()
result_sample = operation(df_sampled)
sample_time = time.time() - start
mem_sample = tracemalloc.get_traced_memory()[1] / (1024 ** 2)
tracemalloc.stop()

print("=== Performance Comparison ===")
print(f"Full data    — Time: {full_time:.4f}s | Peak RAM: {mem_full:.2f} MB")
print(f"Sampled data — Time: {sample_time:.4f}s | Peak RAM: {mem_sample:.2f} MB")
print(f"\nSpeed improvement : {full_time / sample_time:.1f}x faster")
print(f"Memory saving     : {mem_full - mem_sample:.2f} MB")
```

**Output:**

```
=== Performance Comparison ===
Full data    — Time: 0.0241s | Peak RAM: 19.95 MB
Sampled data — Time: 0.0043s | Peak RAM: 2.79 MB

Speed improvement : 5.6x faster
Memory saving     : 17.16 MB
```

#### Strategy 4 Results

| Metric | Full Data (500k rows) | Sampled Data (100k rows) |
|---|---|---|
| **Rows Processed** | 500,000 | 100,000 |
| **Processing Time** | 0.0241 s | 0.0043 s |
| **Peak RAM Used** | 19.95 MB | 2.79 MB |
| **Speed Improvement** | baseline | **5.6× faster** |

**Discussion:** <br>
The sample processed 5.6 times faster with significantly lower memory usage. However, results from the sample may differ slightly from the full dataset — rare movies with very few ratings may not appear in the sample at all. For this dataset, sampling is most useful during the development phase when testing groupby logic, visualisations, or filtering conditions. Final conclusions should always be drawn from the full dataset.

---

### 5.5 Strategy 5: Parallel Processing with Scalable Libraries

**Explanation:** <br>
Standard Pandas operations are single-threaded — they use only one CPU core at a time, leaving the rest of the processor idle. Scalable libraries solve this by distributing work across multiple cores simultaneously.

In this strategy, we run the same aggregation operation (average movie rating grouped by MovieId) across all three libraries and measure each one.

| Library | Approach |
|---|---|
| **Pandas** | Single-threaded, loads full data into RAM |
| **Dask** | Breaks data into partitions, processes in parallel |
| **Polars** | Rust-based engine, vectorised + multi-threaded |

#### Pandas — Initial Attempt and Why It Failed

Our first attempt was to load the full dataset using Pandas without any optimisation. This caused the Google Colab session to crash due to memory exhaustion.

This is not a mistake. It is the core problem that this assignment exists to solve. Pandas loads the entire dataset into RAM at once. With a 2585 MB CSV file and Colab's limited free-tier RAM (~12 GB), the memory overhead of default int64 types caused an out-of-memory error.

**Solution:** We combined Strategy 1 (load selected columns only) and Strategy 3 (optimised data types) to make the Pandas baseline viable. This reflects a realistic scenario, as large datasets should not be loaded using default settings in practical applications.

```python
# Strategy 5: Parallel Processing — Pandas Baseline
import pandas as pd
import time
from memory_profiler import memory_usage

dtype_opt = {"CustId": "int32", "MovieId": "int16", "Rating": "int8"}
cols = ["CustId", "MovieId", "Rating"]

def test_pandas():
    global pandas_load, pandas_proc, pandas_total

    start_load = time.time()
    df = pd.read_csv(file_path, usecols=cols, dtype=dtype_opt)
    pandas_load = time.time() - start_load

    start_proc = time.time()
    result = df.groupby("MovieId")["Rating"].mean()
    pandas_proc = time.time() - start_proc

    pandas_total = pandas_load + pandas_proc

    print("=== PANDAS ===")
    print(f"Load Time       : {pandas_load:.4f}s")
    print(f"Processing Time : {pandas_proc:.4f}s")
    print(f"Total Time      : {pandas_total:.4f}s")

    return result

mem_pandas_val = max(memory_usage(test_pandas))
print(f"Peak Memory     : {mem_pandas_val:.2f} MiB")
```

**Output:**

```
=== PANDAS ===
Load Time       : 58.4377s
Processing Time : 2.6066s
Total Time      : 61.0443s
Peak Memory     : 10110.31 MiB
```

```python
# Strategy 5: Parallel Processing — Dask
import dask.dataframe as dd
from memory_profiler import memory_usage

def test_dask():
    global dask_load, dask_proc, dask_total

    start_load = time.time()
    ddf = dd.read_csv(file_path, usecols=cols, dtype=dtype_opt)
    dask_load = time.time() - start_load

    start_proc = time.time()
    result = ddf.groupby("MovieId")["Rating"].mean().compute()
    dask_proc = time.time() - start_proc

    dask_total = dask_load + dask_proc

    print("=== DASK ===")
    print(f"Load Time       : {dask_load:.4f}s")
    print(f"Processing Time : {dask_proc:.4f}s")
    print(f"Total Time      : {dask_total:.4f}s")

    return result

mem_dask_val = max(memory_usage(test_dask))
print(f"Peak Memory     : {mem_dask_val:.2f} MiB")
```

**Output:**

```
=== DASK ===
Load Time       : 0.3375s
Processing Time : 61.3795s
Total Time      : 61.7170s
Peak Memory     : 1715.29 MiB
```

```python
# Strategy 5: Parallel Processing — Polars
import polars as pl
from memory_profiler import memory_usage

def test_polars():
    global polars_load, polars_proc, polars_total

    dtype_pl = {"CustId": pl.Int32, "MovieId": pl.Int16, "Rating": pl.Int8}

    start_load = time.time()
    lf = pl.scan_csv(file_path, schema_overrides=dtype_pl).select(
        ["CustId", "MovieId", "Rating"]
    )
    polars_load = time.time() - start_load

    start_proc = time.time()
    result = lf.group_by("MovieId").agg(
        pl.col("Rating").mean()
    ).collect()
    polars_proc = time.time() - start_proc

    polars_total = polars_load + polars_proc

    print("=== POLARS ===")
    print(f"Load Time       : {polars_load:.4f}s")
    print(f"Processing Time : {polars_proc:.4f}s")
    print(f"Total Time      : {polars_total:.4f}s")

    return result

mem_polars_val = max(memory_usage(test_polars))
print(f"Peak Memory     : {mem_polars_val:.2f} MiB")
```

**Output:**

```
=== POLARS ===
Load Time       : 0.0765s
Processing Time : 13.4427s
Total Time      : 13.5192s
Peak Memory     : 4027.48 MiB
```

#### Strategy 5 Results <br>
**Discussion:** <br>
**Polars** achieved the fastest total execution time at 13.52 seconds — approximately **4.5× faster than both Pandas and Dask**. <br>
**Dask** consumed the least memory (1,715 MiB) by processing data in partitions rather than loading everything at once. <br>
**Pandas** required the most memory (10,110 MiB) as it holds the entire dataset in RAM simultaneously.

Polars delivers the fastest speed, Dask provides optimal memory efficiency through partitioned processing whereas Pandas remains the slowest and most resource-intensive option.

---

## 6. Comparative Analysis

To compare all three libraries fairly, we ran the same task on each one: calculating the average movie rating grouped by `MovieId` across the full 100 million row dataset. We measured memory usage, loading time, and processing time separately for each library.

---

### 6.1 Memory Usage

This table shows how much RAM each library used when processing the full dataset.

| Library | Peak Memory Used (MiB) | Notes |
|---|---|---|
| **Pandas** | 10,110.31 | Loads entire dataset into RAM at once |
| **Dask** | 1,715.29 | Processes data in partitions — lowest memory |
| **Polars** | 4,027.48 | Lazy evaluation reduces unnecessary memory use |

**Comparison Charts** <br>
The charts below visualise the execution time differences between the three libraries.
![Comparison Charts](images/memory_usage_comparison.png)

**Discussion:**  <br>
Dask used the least memory because it never loads the whole file at once — it works on one partition at a time. Pandas used the most memory by far because it has to hold all 100 million rows in RAM before doing anything. Polars sits in the middle — it is smarter than Pandas but still needs to bring the data into memory during execution.

---

### 6.2 Execution Time

This table breaks down how long each library took to load the data and process it.

| Library | Loading Time (s) | Processing Time (s) | Total Time (s) |
|---|---|---|---|
| **Pandas** | 58.44 | 2.61 | 61.04 |
| **Dask** | 0.34 | 61.38 | 61.72 |
| **Polars** | 0.08 | 13.44 | **13.52** ✅ |

**Comparison Charts** <br>
The charts below visualise the execution time differences between the three libraries.
![Comparison Charts](images/execution_time_comparison.png)

**Discussion:**  <br>
Polars was the clear winner with a total time of just 13.52 seconds about **4.5× faster** than both Pandas and Dask. Pandas had the slowest loading time (58.44s) because it reads the file sequentially with a single thread. Dask loaded almost instantly (0.34s) but its processing was slow (61.38s) because of the overhead involved in managing and scheduling many small partitions. Polars was fast at both stages.

---

### 6.4 Critical Discussion of Findings

Looking at the numbers alone is not enough, we need to understand why each library behaved the way it did.

<br>

**Pandas** loads the entire dataset into RAM before doing any work. For a 2,585 MB file with default int64 types, this means all 100 million rows have to exist in memory at the same time. Without the column selection and data type optimisations we applied in Strategies 1 and 3, Pandas crashed completely. Even with those fixes, it still used over 10,000 MiB which is about more than 5× what Dask needed. This shows that Pandas was simply not designed for datasets at this scale.

<br>

**Dask's** `read_csv` is lazy. It does not actually read the file when you call it. It only scans the headers and builds a plan. The real work happens when you call `.compute()`. That is why loading appears near-instant (0.34s) but processing takes a long time (61.38s). The 61 seconds comes from Dask having to schedule and coordinate 1,000+ partitions across the CPU. On a single machine with limited cores (like Google Colab), this coordination overhead actually slows things down. Dask's real advantage comes out in distributed environments across many machines or with much larger datasets that truly cannot fit into RAM at all.

<br>

**Polars** is written in Rust, which is a lower-level language than Python and runs much closer to the hardware. When we called `scan_csv`, Polars also worked lazily. However before executing, its built-in query optimiser decided the most efficient way to run the aggregation. On top of that, Polars used SIMD (Single Instruction Multiple Data) vectorisation, which processes multiple data values in a single CPU operation. All of this means Polars can do in 13 seconds what takes Pandas and Dask over a minute.

<br>

**Overall processing efficiency:**

| Library | Ease of Use | Handles Full Dataset | Best Use Case |
|---|---|---|---|
| **Pandas** | Easiest | Only with optimisation applied | Small to medium datasets (<1 GB), prototyping |
| **Dask** | Moderate | Yes | Very large or distributed datasets that exceed RAM |
| **Polars** | Moderate | Yes | Fast single-machine processing of large datasets |
<br>
The honest conclusion is that there is no single best library for every situation. Pandas is the easiest to use and perfectly fine for smaller data. Dask is choosed when data is too big to fit on one machine. Polars is the best option when you need speed on a single machine with a large dataset which is exactly the situation we had here.

---

## 7. Conclusion and Reflection

### 7.1 Summary of Key Observations

This assignment gave us a hands-on work to understand how different three popular libraries can perform on the exact same task. The key lesson is that handling big data is not just about picking a powerful library. A lot of the improvement came from how we loaded the data like fewer columns, smaller data types, processing in chunks before any scalable library was even involved. Without the optimisations we applied (column selection and data type downcasting), Pandas would crashed straight away. Even after we fixed that, it still used over 10 GB of RAM. That is a real limitation in any environment with restricted memory, like the free tier of Google Colab.

Next, Dask could actually solved the memory problem pretty well using only 1,715 MiB by splitting the data into partitions. However on a single machine, the overhead of managing all those partitions meant it was no faster than Pandas in total time. Dask's real strength would show in a distributed setting, not here.

On the other hand, Polars was the standout. It completed the same 100M-row aggregation in 13.52 seconds. It is about 4.5× faster than the other two libraries while keeping memory usage reasonable. Its lazy evaluation and rust-based engine made a visible difference in the actual numbers.

Among all the big data strategies, **data type optimisation** had the single biggest impact. Downcasting columns from int64 to int8/int16/int32 cut memory usage by over 80%. It is a simple change with a huge payoff and it is something we would apply in any future data project.

### Reflection on Learning

#### Lau Yee Wen
Through this assignment, I was able to learn and explore new data processing libraries, specifically Dask and Polars, in addition to Pandas which I was already familiar with. This experience helped me understand that different libraries have different strengths when handling large-scale datasets.

Using Dask introduced me to the concept of parallel and distributed processing, where large datasets can be split into smaller partitions and processed efficiently. Meanwhile, Polars showed me how modern data processing tools can achieve high performance through built-in optimisation and multi-threading.

By comparing these libraries, I gained a better understanding of how to choose the appropriate tool based on the dataset size and system limitations. Overall, this assignment expanded my knowledge beyond basic data processing and improved my awareness of scalable solutions for big data handling.

#### Chau Ying Jia

Before this assignment, I always used Pandas for everything without really thinking about whether it was the right tool or not. It was just the library I knew, so I used it. This assignment was the first time I know what and how it does things and it amaze me that actually there are more fantantic tools to explore.

The part that stuck with me the most was when Pandas crashed on the full dataset, I thought something was wrong with my code. However, actually I had not done anything wrong with the code, the problem was simply that Pandas was not built to handle data at this size. Seeing it fail made the whole idea of "big data handling" feel real instead of just theoretical.

What surprised me was how much we could improve things before even switching to a different library. Cutting down the columns and adjusting the data types already saved over 80% of memory. I did not expect such a simple change to make that big of a difference.

Between Dask and Polars, I found Polars more impressive since it finished the job nearly 4.5 times faster. Dask made sense by splitting work across partitions sounds powerful but in practice on a single machine it was actually slower. That taught me something I did not expect which is a tool being more advanced does not always mean it will be faster in every situation. There is no the best library to be used, it really depends on the environment and the scale of the data. 

### 7.3 Scalability Discussion

What if the dataset were not 2.5 GB but 100 GB — or even 1 TB?

At 10–100 GB, Polars would still likely perform well on a machine with enough RAM, but would start to hit limits. Dask becomes more valuable here because it can be pointed at a cluster of machines and distribute the work across all of them. At the terabyte scale, neither Pandas nor single-machine Polars would be viable. That is where tools like **Apache Spark** or cloud-native solutions like **Google BigQuery**, **AWS Athena**, or **Azure Synapse** come in. These platforms are designed from the ground up for data that lives across many servers.

The five strategies we used in this assignment including loading less data, chunking, type optimisation, sampling and parallel processing are not just academic exercises. They are the building blocks of real production data pipelines. The difference is that at true big data scale, those same ideas are implemented across distributed clusters instead of a single Colab session. Knowing how they work at a small scale makes it much easier to understand how they scale up.

---

## References

- Dataset: [Netflix Movie Ratings — Kaggle](https://www.kaggle.com/datasets/evanschreiner/netflix-movie-ratings)
- Pandas documentation: https://pandas.pydata.org/docs/
- Dask documentation: https://docs.dask.org/
- Polars documentation: https://docs.pola.rs/
- memory_profiler: https://github.com/pythonprofilers/memory_profiler
- tracemalloc: https://docs.python.org/3/library/tracemalloc.html
