# Mastering Big Data Handling
### SECP3133 — High Performance Data Processing | Assignment 2

---

## Group Members

| Name | Matric No | Role |
|------|-----------|------|
| Ain Nurnabila binti Mohd Azhar | A23CS0207 | Dataset, Pandas Baseline, Dask, Strategies 1–3 |
| Dayang Farah Farzana | A23CS0071 | Polars, Strategies 4–5, Comparative Analysis, Report |

---

## Dataset Description

| Field | Details |
|-------|---------|
| **Name** | California Google Local Reviews |
| **Source** | Google Local Data (Google Maps) |
| **File** | review-California_10.json |
| **Format** | JSONL (newline-delimited JSON) |
| **Size** | ~11.65 GB |
| **Records** | ~25 million+ rows |
| **Domain** | Consumer Reviews / E-Commerce |
| **Columns Used** | `rating`, `text`, `gmap_id`, `time` |

This dataset contains Google Maps reviews for businesses across California. Each record represents a single user review with a star rating, review text, business ID, and timestamp. The large volume of reviews makes it an ideal candidate for big data handling techniques, as naive loading with Pandas causes a MemoryError on standard hardware.

---

## Environment Setup

```python
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Install libraries if needed
!pip install polars

# Imports
import pandas as pd
import dask.dataframe as dd
import polars as pl
import tracemalloc
import time
import os
import warnings
import matplotlib.pyplot as plt
import numpy as np
warnings.filterwarnings('ignore')

FILE_PATH = '/content/drive/MyDrive/HPDP_A2/review-California_10.json'
print(f"File size: {os.path.getsize(FILE_PATH) / 1024**3:.2f} GB")
```

---

## Task 2: Load and Inspect Data

Initial inspection was done by loading 10,000 rows to understand the dataset structure without consuming excessive memory.

```python
df_sample = pd.read_json(FILE_PATH, lines=True, nrows=10000)
print(df_sample.dtypes)
print(df_sample.shape)
df_sample.head()
```

**Output screenshot:**

> <img width="1454" height="561" alt="image" src="https://github.com/user-attachments/assets/0802f259-30a4-4714-911a-32ee13a559c5" />


---

## Pandas Baseline Metrics

Before applying any optimisation strategy, we recorded the baseline performance of Pandas loading 2,000,000 rows with 6 columns.

```python
COLS_TO_USE = ['user_id', 'name', 'time', 'rating', 'text', 'gmap_id']

tracemalloc.start()
start_time = time.time()

df = pd.read_json(FILE_PATH, lines=True, nrows=2000000)
df = df[COLS_TO_USE]

end_time = time.time()
current_mem, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()

baseline_time = round(end_time - start_time, 2)
baseline_memory = round(peak_mem / (1024 * 1024), 2)

print(f"Load time   : {baseline_time} seconds")
print(f"Peak memory : {baseline_memory} MB")
print(f"Shape       : {df.shape[0]:,} rows × {df.shape[1]} columns")
```

| Metric | Value |
|--------|-------|
| Load Time | 266 seconds |
| Peak Memory | 4490 MB |
| Rows Loaded | 2,000,000 |
| Columns | 6 |

> ⚠️ Attempting to load the full 11.65 GB file caused a `MemoryError`, confirming the need for big data handling strategies.

---

## Task 3: Big Data Handling Strategies

---

### Strategy 1: Load Less Data (Pandas)

Instead of loading all columns, we select only the 4 columns needed for analysis, reducing memory from the start.

```python
COLS_MINIMAL = ['rating', 'text', 'gmap_id', 'time']

tracemalloc.start()
start_time = time.time()

df_s1 = pd.read_json(FILE_PATH, lines=True, nrows=2000000)
df_s1 = df_s1[COLS_MINIMAL]

end_time = time.time()
current_mem, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()

s1_time = round(end_time - start_time, 2)
s1_memory = round(peak_mem / (1024 * 1024), 2)

print(f"Load time        : {s1_time} seconds")
print(f"Peak memory      : {s1_memory} MB")
print(f"Memory reduction : {round((baseline_memory - s1_memory) / baseline_memory * 100, 1)}%")
```

**Output screenshot:**

> <img width="456" height="141" alt="image" src="https://github.com/user-attachments/assets/a0858caa-aac1-49b6-8762-9e01535c6339" />


**Explanation:**
By specifying only the 4 columns required (`rating`, `text`, `gmap_id`, `time`) instead of all 6, we reduce the amount of data held in memory. However, since Pandas reads the entire file before column selection, the peak memory reduction is modest compared to other strategies. This strategy is most effective when the dataset has many columns but only a few are needed.

---

### Strategy 2: Chunking (Pandas)

Instead of loading 2 million rows at once, we read the file in chunks of 100,000 rows, filter each chunk, and concatenate the results.

```python
CHUNK_SIZE = 100_000
filtered_chunks = []

tracemalloc.start()
start_time = time.time()

rows_read = 0
for chunk in pd.read_json(FILE_PATH, lines=True, chunksize=CHUNK_SIZE):
    chunk = chunk[COLS_MINIMAL]
    high_rated = chunk[chunk['rating'] >= 4]
    filtered_chunks.append(high_rated)
    rows_read += len(chunk)
    if rows_read >= 2_000_000:
        break

df_s2 = pd.concat(filtered_chunks, ignore_index=True)

end_time = time.time()
current_mem, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()

s2_time = round(end_time - start_time, 2)
s2_memory = round(peak_mem / (1024 * 1024), 2)

print(f"Load time        : {s2_time} seconds")
print(f"Peak memory      : {s2_memory} MB")
print(f"Memory reduction : {round((baseline_memory - s2_memory) / baseline_memory * 100, 1)}%")
```

**Output screenshot:**

> <img width="553" height="168" alt="image" src="https://github.com/user-attachments/assets/352ce110-cdb3-4508-aacc-e6afb14ec8a7" />


**Explanation:**
Chunking is the most impactful single strategy for memory reduction. By processing only 100,000 rows at a time, the peak memory dropped from 4490 MB to 564 MB — an 87% reduction. Only one chunk exists in memory at any point, and it is discarded before the next chunk loads. This allows processing of files far larger than available RAM.

---

### Strategy 3: Data Type Optimisation (Pandas)

After loading, we downcast column data types from their default (wasteful) types to the smallest type that can represent the values.

```python
mem_before = round(df_s1.memory_usage(deep=True).sum() / (1024 * 1024), 2)

df_s3 = df_s1.copy()
df_s3['rating'] = df_s3['rating'].astype('int8')       # ratings are 1–5, int8 is sufficient
df_s3['gmap_id'] = df_s3['gmap_id'].astype('category') # repeated strings → category
df_s3['time'] = df_s3['time'].astype('int32')           # timestamps fit in int32

mem_after = round(df_s3.memory_usage(deep=True).sum() / (1024 * 1024), 2)

print(f"Memory before    : {mem_before} MB")
print(f"Memory after     : {mem_after} MB")
print(f"Memory saved     : {round(mem_before - mem_after, 2)} MB")
print(f"Memory reduction : {round((mem_before - mem_after) / mem_before * 100, 1)}%")
print(df_s3.dtypes)
```

**Output screenshot:**

> <img width="436" height="275" alt="image" src="https://github.com/user-attachments/assets/0b416df0-23f6-483f-a6e2-0608d40e8657" />


**Explanation:**
Pandas assigns `int64` by default to all integer columns, even when values are small. By downcasting `rating` to `int8` (values 1–5 fit in 8 bits), converting `gmap_id` to `category` (avoids storing repeated strings), and `time` to `int32`, memory reduced from the loaded size to 282 MB. This strategy is applied after loading and benefits all subsequent operations.

---

### Strategy 4: Sampling (Polars)

Sampling loads a small representative subset of the dataset for fast exploration and prototyping, using Polars for efficient JSONL reading.

```python
import polars as pl

tracemalloc.start()
start_time = time.time()

# Load only 100,000 rows for rapid prototyping
df_sample_pl = pl.read_ndjson(FILE_PATH, n_rows=100_000)
df_sample_pl = df_sample_pl.select(['rating', 'text', 'gmap_id', 'time'])

end_time = time.time()
current_mem, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()

s4_time = round(end_time - start_time, 2)
s4_memory = round(peak_mem / (1024 * 1024), 2)

print("=== STRATEGY 4: SAMPLING (Polars) ===")
print(f"Sample size      : 100,000 rows")
print(f"Load time        : {s4_time} seconds")
print(f"Peak memory      : {s4_memory} MB")
print(f"Shape            : {df_sample_pl.shape}")
print(df_sample_pl.head(5))
```

**Output screenshot:**

> <img width="1011" height="375" alt="image" src="https://github.com/user-attachments/assets/7000f91c-65f6-4336-a542-17df0a29dbc2" />


**Explanation:**
Sampling is ideal during the development phase — when writing and testing code, there is no need to wait for the full dataset to load each time. Polars' `read_ndjson()` with `n_rows=100_000` reads only the first 100,000 rows, making the operation nearly instant. The trade-off is that the sample may not perfectly represent rare patterns in the full dataset, so sampling should be replaced with full processing in the final pipeline. Polars also uses significantly less memory than Pandas for the same operation due to its columnar memory format.

---

### Strategy 5: Parallel Processing (Polars)

Polars uses lazy evaluation and automatic parallelism to process 2 million rows far more efficiently than Pandas.

```python
tracemalloc.start()
start_time = time.time()

# scan_ndjson() reads lazily — builds a query plan first, then executes optimally
df_polars = (
    pl.scan_ndjson(FILE_PATH)
    .select(['rating', 'text', 'gmap_id', 'time'])
    .filter(pl.col('rating') >= 4)
    .limit(2_000_000)
    .collect()  # execute the full query plan here
)

end_time = time.time()
current_mem, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()

polars_time = round(end_time - start_time, 2)
polars_memory = round(peak_mem / (1024 * 1024), 2)

print("=== STRATEGY 5: PARALLEL PROCESSING (Polars) ===")
print(f"Load time        : {polars_time} seconds")
print(f"Peak memory      : {polars_memory} MB")
print(f"Shape            : {df_polars.shape[0]:,} rows × {df_polars.shape[1]} columns")
print(df_polars.head(5))
```

**Output screenshot:**

> <img width="929" height="360" alt="image" src="https://github.com/user-attachments/assets/21b11595-620e-4019-a116-1c2c8663d1d1" />


**Explanation:**
Polars uses **lazy evaluation** via `scan_ndjson()` — rather than immediately loading data, it first builds an optimised query plan combining the `.select()`, `.filter()`, and `.limit()` operations into a single efficient pass. When `.collect()` is called, the plan executes in parallel across all available CPU cores. Polars is written in **Rust** with fully vectorised operations, meaning it avoids Python overhead entirely during computation. This results in dramatically faster execution and lower memory usage compared to Pandas, which is single-threaded and processes operations sequentially.

---

## Task 4: Comparative Analysis

### Performance Results

| Library | Time (s) | Peak Memory (MB) | Speedup vs Pandas | Memory Reduction |
|---------|----------|------------------|-------------------|-----------------|
| Pandas (Baseline) | 266 | 4490 | 1.0× | — |
| Dask | 56 | 1298 | 4.8× | 71.1% |
| Polars | 91.8 | 0.19 | 2.9× | 100% |

**Chart — Execution Time Comparison:**

> <img width="367" height="288" alt="image" src="https://github.com/user-attachments/assets/27a37e15-e82b-4914-b1e4-e4cb00a1b3c4" />


**Chart — Peak Memory Comparison:**

> <img width="356" height="275" alt="image" src="https://github.com/user-attachments/assets/71da018e-44d3-4608-9bc2-eb421cb77bf1" />


### Discussion

**Why is Pandas slow?**
Pandas is single-threaded and loads the entire dataset into memory at once as a Python object. For a 11.65 GB file, this is unsustainable - it caused a `MemoryError` on a full load and took 266 seconds even for just 2 million rows. Pandas was not designed for datasets that exceed available RAM.

**Why is Dask faster and lighter?**
Dask mirrors the Pandas API but operates on data partitioned into smaller chunks processed in parallel. By setting `blocksize=10_000_000`, Dask processes 10 MB blocks across multiple cores simultaneously. It also supports lazy evaluation — operations are only executed when explicitly computed. This explains its 4.8× speedup and 71% memory reduction over Pandas.

**Why is Polars the most efficient?**
Polars is written in Rust and built from the ground up for performance. It uses:
- **Lazy evaluation** - `scan_ndjson()` builds an optimised query plan before touching any data
- **Predicate pushdown** - the `.filter()` is applied during reading, not after, so fewer rows are ever loaded into memory
- **Columnar memory format** - data is stored column-by-column (Apache Arrow format), making operations like selecting and filtering extremely cache-efficient
- **True parallelism** - all CPU cores are used with no Python GIL overhead

**Which library would you choose for production?**
For single-machine workloads on datasets up to ~50 GB, Polars is the best choice due to its speed and low memory footprint. Dask is preferable when the dataset must be distributed across multiple machines or when Pandas-compatible syntax is required. Pandas remains useful for small datasets and quick prototyping where performance is not a concern.

---

## Task 5: Conclusion and Reflection

### Summary of Findings

This assignment demonstrated that Pandas alone is insufficient for large-scale data processing. Across all five strategies and three libraries, the results consistently showed that memory and execution time can be dramatically reduced through intentional design choices:

- **Chunking** was the single most impactful Pandas strategy, reducing memory by 87% by ensuring only 100,000 rows exist in memory at any time
- **Data Type Optimisation** further reduced in-memory size to 282 MB by using compact types appropriate for each column's value range
- **Dask** achieved a 4.8× speedup with 71% less memory through partitioned parallel processing
- **Polars** outperformed all other approaches by combining lazy evaluation, predicate pushdown, and Rust-based parallel execution

### Reflection

Working through this assignment changed how we think about "big data" - it's not just a buzzword, it's a real constraint that breaks tools we use every day without a second thought. Hitting a MemoryError on the full 11.65 GB file was the moment it stopped being theoretical. Pandas is the library most of us default to for any tabular task, but watching it take 266 seconds and 4.5 GB of RAM just to load 2 million rows made it obvious why production systems don't rely on it alone at scale.

    The biggest surprise was how much of the performance gain came from when work is done, not just how. Strategies like chunking and predicate pushdown succeed by avoiding unnecessary work in the first place - filtering rows before they're fully materialized in memory, rather than loading everything and discarding what isn't needed afterward. Polars' lazy evaluation model made this especially clear: building a query plan with .select() and .filter() before calling .collect() let the engine optimize the entire pipeline in one pass, rather than executing each operation eagerly and wastefully.
    
    This assignment also reinforced that there's no single "best" tool - only trade-offs suited to context. Pandas remains convenient for quick, small-scale exploration. Dask offers a familiar API once you're ready to scale across machines. Polars delivers the best raw performance on a single machine but requires learning a new syntax and mental model. Choosing the right tool for a given dataset size and team's familiarity is itself a skill, separate from knowing how each library works individually.
    
    Finally, working in a team split by library (Pandas/Dask vs. Polars) showed us how differently the same problem can be approached depending on the tool's design philosophy  and how valuable it is to compare notes rather than work in isolation.


### Scalability Discussion

The strategies used in this assignment handle an 11.65 GB dataset on a single Google Colab instance. But what happens at 100 GB or 1 TB?

| Scale | Viable Approach |
|-------|----------------|
| Up to ~50 GB | Polars (single machine, lazy evaluation) |
| 50 GB – 1 TB | Dask (distributed across multiple machines) |
| 1 TB+ | Apache Spark, Google BigQuery, or cloud-native solutions |

At 1 TB, even Dask on a single machine would struggle. The natural next step is **distributed computing** - frameworks like Apache Spark split data across a cluster of machines, where each node processes its partition independently. Cloud platforms like Google BigQuery or AWS Athena go further by abstracting the infrastructure entirely, allowing SQL-like queries on petabyte-scale datasets without managing any hardware.

This assignment established the foundation: understanding why tools have limits, and knowing when to reach for the next level of the stack.

