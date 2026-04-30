# Assignment 2: Mastering Big Data Handling

## Group Information
**Group Name:** Sayur    
**Members:**
1. Teh Ru Qian 
2. Tan Yi Ya 
---

## 📝 Task 1: Dataset Selection

### 📌 Dataset Overview

* **Name**: Pakistan Carbon Monoxide 2022–2025
* **Source**: [Kaggle: Pakistan Carbon Monoxide 2022 - 2025](https://www.kaggle.com/datasets/muhammadbilal77511/pakistan-carbon-monoxide-2022-2025)
* **Domain**: *Environmental Science / Air Quality*
* **Files Used**: `year_2024.csv`, `year_2025.csv`

### 📖 Description
This dataset contains daily tropospheric carbon monoxide (CO) observations over Pakistan derived from NASA’s TROPOMI instrument onboard the Sentinel 5P satellite. The dataset spans 2022 to 2025 and provides high spatial resolution atmospheric measurements suitable for air quality, emissions, and climate analysis.

### 📊 Data Column Description

| Column | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| `date` | datetime | ISO 8601 | Measurement date (YYYY-MM-DD) |
| `latitude` | float | degrees | Latitude of measurement point (WGS84) |
| `longitude` | float | degrees | Longitude of measurement point (WGS84) |
| `co_column` | float | mol/m² | Tropospheric CO column density; indicates CO amount in the vertical column of the atmosphere |
| `co_quality` | float | 0–1 | Quality assurance value; >**0.5** acceptable, >**0.75** high quality |
| `year` | int | - | Year of the observation (2022–2025) |
| `month` | int | 1–12 | Month of the observation |
| `day` | int | 1–31 | Day of month of the observation |
| `day_of_week` | int | 0–6 | Day of the week (0=Monday, 6=Sunday) |

---

## 📝 Task 2: Load and Inspect Data

### 🔹 Loading Strategy

To load the dataset into [Google Colab](https://colab.research.google.com/), the following steps were taken:

**1. Import Required Libraries**

```python
import pandas as pd
import os
import psutil
import time
import threading
from IPython.display import display
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import gc
import tracemalloc
```

**2. Imported `kaggle.json`**

Uploaded via the Colab file upload feature:

```python
from google.colab import files
files.upload()
```

**3. Configured Kaggle API Credentials**

Moved the uploaded file to the `.kaggle` directory and set proper permissions:

```bash
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
```

**4. Downloaded Dataset from Kaggle**

Using Kaggle CLI to fetch the dataset directly into the Colab environment:

```bash
!kaggle datasets download -d muhammadbilal77511/pakistan-carbon-monoxide-2022-2025
```

**5. Unzipped the Dataset File**

Extracted the dataset ZIP file:

```bash
!unzip pakistan-carbon-monoxide-2022-2025.zip
```

**6. Installed Additional Libraries**

```python
import dask.dataframe as dd
import polars as pl
```

---

### 🔹 Dataset Inspection

#### 📁 Dataset Size

```python
files = [
    "/content/co_data/processed/year_2024.csv",
    "/content/co_data/processed/year_2025.csv"
]

total_size_bytes = 0

for file_path in files:
    size_bytes = os.path.getsize(file_path)
    size_mb = size_bytes / (1024 * 1024)
    size_gb = size_bytes / (1024 * 1024 * 1024)

    total_size_bytes += size_bytes

    print(f"{file_path}")
    print(f"Size: {size_bytes} bytes")
    print(f"Size: {size_mb:.2f} MB")
    print(f"Size: {size_gb:.2f} GB\n")

# Total size
total_size_mb = total_size_bytes / (1024 * 1024)
total_size_gb = total_size_bytes / (1024 * 1024 * 1024)

print("===== TOTAL DATASET SIZE =====")
print(f"Total Size: {total_size_bytes} bytes")
print(f"Total Size: {total_size_mb:.2f} MB")
print(f"Total Size: {total_size_gb:.2f} GB")
```

This cell calculates and displays the individual and combined file sizes of the two CSV files in bytes, MB, and GB, giving an immediate sense of the dataset's scale before loading it into memory.

---

#### 📐 Number of Rows and Columns

```python
def count_rows(file_path):
    with open(file_path, "r") as f:
        return sum(1 for _ in f) - 1  # minus header

def get_columns(file_path):
    df = pd.read_csv(file_path, nrows=0)
    return len(df.columns)

total_rows = 0

for file_path in files:
    rows = count_rows(file_path)
    cols = get_columns(file_path)

    total_rows += rows

    print(file_path)
    print("Rows:", rows, "Columns:", cols, "\n")

print("===== TOTAL =====")
print("Total Rows:", total_rows)
```

Rather than loading the full dataset into memory just to inspect its dimensions, this cell counts rows by iterating over file lines (fast and memory-efficient) and reads zero rows to infer column count. This gives the dataset shape without any significant memory overhead.

---

#### 📋 Load Full Dataset using Pandas

```python
combined_df = pd.concat([pd.read_csv(f, low_memory=True) for f in files], ignore_index=True)
```

The two CSV files are loaded individually and concatenated into a single DataFrame. The `low_memory=True` flag instructs pandas to process data in chunks internally during type inference, reducing the risk of mixed-type warnings on large files.

---

#### 📌 First 5 Rows

```python
combined_df.head()
```

---

#### 📐 Shape of the Dataset

```python
combined_df.shape
print(f"Rows: {combined_df.shape[0]}, Columns: {combined_df.shape[1]}")
```

---

#### 🏷️ Column Names and Data Types

```python
print("===== Column Names and Datatypes =====")
combined_df.info()
```

---

#### ❓ Missing Values

```python
total_missing = combined_df.isnull().sum().sum()
total_cells = combined_df.shape[0] * combined_df.shape[1]

print("Total Missing Values:", total_missing)
print("Overall Missing %:", (total_missing / total_cells) * 100)
```

This cell computes the total number of null values across all cells and expresses it as a percentage of the total cell count. Understanding missingness is critical before applying any optimisation or analysis strategy.

---

#### 💾 Initial Memory Usage

```python
process = psutil.Process(os.getpid())

memory_bytes = process.memory_info().rss

print("Memory Usage (Bytes):", memory_bytes)
print("Memory Usage (MB):", memory_bytes / (1024 * 1024))
print("Memory Usage (GB):", memory_bytes / (1024 * 1024 * 1024))
```

`psutil` is used to query the Resident Set Size (RSS) of the current process — the actual physical RAM consumed. This baseline measurement is taken after loading the full dataset with default pandas settings, providing a reference point against which optimised loading strategies will be compared.

> **Initial Memory Usage for this dataset is approximately 1.49 GB.**

---

## 🛠️ Task 3: Apply Big Data Handling Strategies

### 📊 Performance Measurement Setup

Before applying any strategy, a reusable `measure_performance` function is implemented. This function wraps any data-loading function and captures key system metrics during execution, enabling objective, consistent comparison across all five strategies.

```python
def measure_performance(func, description="", *args, **kwargs):
    process     = psutil.Process(os.getpid())
    cpu_samples = []
    mem_samples = []
    done        = [False]

    def _track():
        while not done[0]:
            cpu_samples.append(process.cpu_percent(interval=0.1))
            mem_samples.append(process.memory_info().rss / 1024 / 1024)

    tracker = threading.Thread(target=_track, daemon=True)
    tracker.start()

    mem_before = process.memory_info().rss / 1024 / 1024
    start_time = time.perf_counter()

    try:
        result  = func(*args, **kwargs)
        success = True
        error   = None
    except Exception as e:
        result  = None
        success = False
        error   = str(e)

    exec_time = round(time.perf_counter() - start_time, 4)
    done[0]   = True
    tracker.join()

    mem_after  = process.memory_info().rss / 1024 / 1024
    mem_peak   = max(mem_samples) if mem_samples else mem_after   # highest RSS seen
    mem_final  = mem_after - mem_before                           # net change (can be negative)
    mem_used   = mem_peak  - mem_before

    num_records = None
    throughput  = None
    if success and result is not None:
        try:
            if isinstance(result, pd.DataFrame):
                num_records = len(result)
            elif hasattr(result, "compute"):
                num_records = int(result.shape[0].compute())
            elif hasattr(result, "__len__"):
                num_records = len(result)
            if num_records and exec_time > 0:
                throughput = round(num_records / exec_time, 2)
        except Exception:
            pass

    perf = {
        "Description"         : description,
        "Execution Time (s)"  : exec_time,
        "Memory Before (MB)"  : round(mem_before, 2),   # baseline
        "Peak Memory (MB)"    : round(mem_peak,   2),   # highest point during execution
        "Memory After (MB)"   : round(mem_after,  2),   # what remains when done
        "Peak Usage (MB)"     : round(mem_used,   2),   # peak - before  ← use this for comparison
        "Net Change (MB)"     : round(mem_final,  2),   # after - before (negative = freed memory)
        "CPU Avg (%)"         : round(sum(cpu_samples) / len(cpu_samples), 2) if cpu_samples else 0.0,
        "Records"             : num_records,
        "Throughput (rec/s)"  : throughput,
        "Success"             : success,
    }
    if not success:
        perf["Error"] = error

    return perf, result
```

**Explanation**: A background thread continuously samples CPU and RSS memory usage while the target function runs. Once execution completes, the function computes: execution time (via `time.perf_counter`), peak memory used (highest RSS minus baseline), net memory change, average CPU utilisation, total records processed, and throughput (records per second). All metrics are returned as a dictionary alongside the function's result, enabling a consistent side-by-side comparison across strategies.

---

### 🔹 Part 1: Memory- and Performance-Efficient Techniques

---

### Strategy 1: Load Less Data

**What is this strategy?**
Instead of loading the entire dataset with all available columns, only the columns that are necessary for the intended analysis are selected. This is done by passing a list of column names to the `usecols` parameter of `pd.read_csv()`. Additionally, rows with low-quality CO readings (`co_quality <= 0.5`) are filtered out immediately after loading.

**Why is it used?**
In large datasets, many columns are often irrelevant to a specific task. Loading unnecessary columns wastes memory and slows down I/O. By selecting only five key columns and filtering early, both memory consumption and processing time are reduced significantly without sacrificing analytical value.

#### 5.1 Performance Observation

```python
def strategy1_load_less():
    df_list = []
    SELECTED_COLS = ['date', 'latitude', 'longitude', 'co_column', 'co_quality'] # select only useful columns

    for file in files:
        df = pd.read_csv(
            file,
            usecols=SELECTED_COLS,          # ← load only what we need
            parse_dates=['date'],
        )
        df_list.append(df)

    combined = pd.concat(df_list, ignore_index=True)

    # filter: keep only acceptable quality readings
    filtered = combined[combined['co_quality'] > 0.5].reset_index(drop=True)  # filter the rows with good quality value
    return filtered

perf1, result1 = measure_performance(strategy1_load_less, "S1 – Load Less Data")
perf_df1 = pd.DataFrame([perf1])
print(perf_df1.to_string(index=False))
print('==== First 5 Rows ====')
display(result1.head())
```

In this function, only the five most analytically relevant columns are selected and passed to `pd.read_csv(usecols=SELECTED_COLS)`. After loading, rows where `co_quality <= 0.5` are dropped using boolean indexing. This ensures only high-quality readings are retained, reducing dataset size further.

#### 5.2 Compare with Full Dataset

A baseline unoptimised loader is also deployed to provide a fair reference point:

```python
# full dataset function
def load_full():
    df_list = []

    for file in files:
        df = pd.read_csv(file)
        df_list.append(df)

    return pd.concat(df_list, ignore_index=True)
```

```python
perf_full, result_full = measure_performance(
    load_full,
    "Full Dataset"
)
```

```python
comparison_df1 = pd.DataFrame([perf_full, perf1])
display(comparison_df1)
```

**What the results show**: Load Less Data reduces memory usage significantly compared to loading the full dataset. By restricting columns to only what is needed and filtering rows with poor quality, peak memory consumption is substantially lower. Execution time may also be faster due to reduced I/O. The trade-off is that columns excluded at load time cannot be recovered without re-reading the file.

---

### Strategy 2: Chunking

**What is this strategy?**
Chunking loads a large file incrementally in fixed-size batches (chunks) rather than all at once. The `chunksize` parameter in `pd.read_csv()` returns a `TextFileReader` iterator, which yields one chunk (a DataFrame) per iteration. All chunks are collected and concatenated into a single DataFrame.

**Why is it used?**
When a dataset is too large to fit into available RAM, loading it in its entirety will cause memory errors or severe performance degradation. Chunking provides a controlled, predictable memory footprint during loading, making it safer for environments with limited RAM. It also allows per-chunk preprocessing before the final concatenation.

#### 6.1 Performance Observation

```python
def strategy2_chunking():
    filtered = []

    for file in files:
        reader = pd.read_csv(
            file,
            parse_dates=['date'],
            chunksize=500000,         #use chunksize about 500000
        )
        for chunk in reader:
            filtered.append(chunk)

    return pd.concat(filtered, ignore_index=True)

perf2, result2 = measure_performance(strategy2_chunking, "S2 – Chunking")
perf_df2 = pd.DataFrame([perf2])
print(perf_df2.to_string(index=False))
print('==== First 5 Rows ====')
display(result2.head())
```

The dataset is loaded in chunks of 500,000 rows using `pd.read_csv(chunksize=500000)`. Each chunk is appended to a list, and all chunks are concatenated at the end with `pd.concat()`. The `parse_dates=['date']` argument ensures the date column is parsed correctly across all chunks.

#### 6.2 Compare with Full Dataset

```python
comparison_df2 = pd.DataFrame([perf_full, perf2])
display(comparison_df2)
```

**What the results show**: Chunking takes longer than a direct full load and may exhibit slightly lower throughput due to the overhead of repeated iterator calls and the final `pd.concat()` step. However, it is valuable precisely for its controlled memory behaviour — peak memory usage remains bounded by chunk size, making it the preferred approach when the dataset approaches or exceeds available RAM.

---

### Strategy 3: Optimize Data Types

**What is this strategy?**
Pandas defaults to using the most general data types when inferring column types: `float64` for decimals and `int64` for integers. Many datasets, however, do not require this level of precision. By explicitly casting columns to smaller types (e.g., `float32`, `int16`, `int8`) at read time via the `dtype` parameter, memory consumption per column is cut by half or more.

**Why is it used?**
For large datasets with millions of rows, the cumulative memory savings from downcasting even a few columns can amount to hundreds of megabytes. This strategy is especially effective for numeric-heavy datasets like this one, where most columns are continuous measurements or small integer indices. Reduced memory also means faster downstream operations due to better CPU cache utilisation.

#### 7.1 Performance Observation

```python
def strategy3_dtype_optimisation():
    ALL_COLS  = ['date', 'latitude', 'longitude', 'co_column',
                 'co_quality', 'year', 'month', 'day', 'day_of_week']

    dtype_map = {
        'latitude'   : 'float32',   # float64 → float32
        'longitude'  : 'float32',   # float64 → float32
        'co_column'  : 'float32',   # float64 → float32
        'co_quality' : 'float32',   # float64 → float32
        'year'       : 'int16',     # int64   → int16
        'month'      : 'int8',      # int64   → int8
        'day'        : 'int8',      # int64   → int8
        'day_of_week': 'int8',      # int64   → int8
    }

    chunks = []
    for file in files:
        df = pd.read_csv(
            file,
            usecols=ALL_COLS,
            dtype=dtype_map,
            parse_dates=['date'],   # object → datetime64[ns]
        )
        chunks.append(df)
        del df

    combined = pd.concat(chunks, ignore_index=True, copy=False)
    del chunks

    # ── memory breakdown before vs after ─────────────────────────────────────
    # reference: what memory would look like with all defaults (float64 / int64)
    default_bytes = {
        'date'       : 8,   # datetime64[ns]
        'latitude'   : 8,   # float64
        'longitude'  : 8,   # float64
        'co_column'  : 8,   # float64
        'co_quality' : 8,   # float64
        'year'       : 8,   # int64
        'month'      : 8,   # int64
        'day'        : 8,   # int64
        'day_of_week': 8,   # int64
    }
    optimised_bytes = {
        'date'       : 8,   # datetime64[ns] — unchanged
        'latitude'   : 4,   # float32
        'longitude'  : 4,   # float32
        'co_column'  : 4,   # float32
        'co_quality' : 4,   # float32
        'year'       : 2,   # int16
        'month'      : 1,   # int8
        'day'        : 1,   # int8
        'day_of_week': 1,   # int8
    }

    n_rows        = len(combined)
    mem_default   = sum(default_bytes.values())   * n_rows / 1e6
    mem_optimised = sum(optimised_bytes.values()) * n_rows / 1e6
    mem_saved     = mem_default - mem_optimised
    pct_saved     = (mem_saved / mem_default) * 100

    print(f"\n  Rows : {n_rows:,}")
    print(f"\n  {'Column':<14} {'Before':>10} {'After':>10} {'Saved':>10}")
    print(f"  {'-'*46}")
    for col in ALL_COLS:
        before = default_bytes[col]
        after  = optimised_bytes[col]
        saved  = (before - after) * n_rows / 1e6
        print(f"  {col:<14} {'float64/int64':>10} {str(combined[col].dtype):>10}   -{saved:.1f} MB")

    print(f"\n  Total memory (default)    : {mem_default:.2f} MB")
    print(f"  Total memory (optimised)  : {mem_optimised:.2f} MB")
    print(f"  Total saved               : {mem_saved:.2f} MB  ({pct_saved:.1f}% reduction)")

    return combined

perf3, result3 = measure_performance(strategy3_dtype_optimisation, "S3 – Type Optimisation")
perf_df3 = pd.DataFrame([perf3])
print(f"  {'-'*100}")
print(perf_df3.to_string(index=False))
print('\n== Columns ==  == Datatypes ==')
print(result3.dtypes)
print('\n==== First 5 Rows ====')
display(result3.head())
```

The function explicitly maps each column to a smaller type at read time (`dtype=dtype_map`). It also includes a detailed memory breakdown that compares theoretical default memory versus optimised memory per column, displaying the exact savings in MB. `del df` and `copy=False` in `pd.concat()` are used to avoid holding duplicate frames in memory during the merge.

#### 7.2 Compare with Full Dataset

```python
comparison_df3 = pd.DataFrame([perf_full, perf3])
display(comparison_df3)
```

**What the results show**: Type optimisation reduces peak memory usage considerably, particularly for integer columns where `int64 → int8` yields an 8× reduction. The trade-off is a slight increase in execution time due to the overhead of explicit type conversion during parsing. However, the long-term benefit of holding a smaller DataFrame in memory far outweighs the one-time conversion cost, especially for repeated downstream operations.

---

### Strategy 4: Sampling

**What is this strategy?**
Sampling randomly selects a small fraction of rows from the dataset to create a representative but much smaller subset. Here, 1% of the total rows are selected using `DataFrame.sample(frac=0.01)` with a fixed random seed for reproducibility.

**Why is it used?**
For exploratory data analysis, hypothesis testing, model prototyping, or debugging pipelines, working with the full dataset is often unnecessary and wasteful. Sampling allows fast iteration and lower memory consumption at the cost of completeness. The statistical properties of the sample should approximate those of the full dataset, provided the sampling is random and the fraction is not too small.

#### 8.1 Performance Observation

```python
def strategy4_sampling():
    SAMPLE_FRAC = 0.01   #1% of total rows
    RANDOM_SEED = 42
    chunks = []
    for file in files:
        df = pd.read_csv(file)
        chunks.append(df)
        del df

    combined = pd.concat(chunks, ignore_index=True, copy=False)
    del chunks

    total_rows = len(combined)
    sample     = combined.sample(frac=SAMPLE_FRAC, random_state=RANDOM_SEED).reset_index(drop=True)
    del combined

    print(f"  Full dataset rows : {total_rows:,}")
    print(f"  Sample rows       : {len(sample):,}  ({SAMPLE_FRAC*100:.0f}%)")
    return sample

perf4, result4 = measure_performance(strategy4_sampling, "S4 – Sampling")
perf_df4 = pd.DataFrame([perf4])
print(f"  {'-'*100}")
print(perf_df4.to_string(index=False))
print('==== First 5 Rows ====')
display(result4.head())
```

The function loads both CSV files, concatenates them, then calls `.sample(frac=0.01, random_state=42)` to extract 1% of rows. `del combined` is called immediately after sampling to release the full DataFrame from memory. `reset_index(drop=True)` ensures the sampled DataFrame has a clean sequential index.

#### 8.2 Compare with Full Dataset

```python
comparison_df4 = pd.DataFrame([perf_full, perf4])
display(comparison_df4)
```

**What the results show**: Sampling drastically reduces the number of records in the working DataFrame, resulting in lower memory usage and fast post-load operations. However, because the full dataset still has to be loaded before sampling, peak memory during execution is similar to the full-load baseline. Throughput is low relative to the number of records retained in the final output, as most loaded records are discarded. This strategy is best suited for prototyping and exploration rather than production pipelines.

---

### Strategy 5: Parallel Processing with Dask and Polars

---

### 5a. Dask

**What is this strategy?**
Dask reads CSV files lazily and distributes processing across multiple CPU cores using a task scheduler. Operations such as aggregations are performed in parallel on each partition, and only the final reduced result is materialised into memory via `.compute()`.

**Why is it used?**
For datasets that exceed available RAM, or for computationally expensive aggregations over millions of rows, Dask can significantly reduce wall-clock time by distributing the workload. Its API closely mirrors pandas, making it accessible. Crucially, because Dask only materialises the final aggregated result (not the full expanded DataFrame), peak memory usage is kept very low.

#### 9.1.1 Performance Overview

```python
def strategy5_dask():
  dask_dtype_map = {
    'latitude'   : 'float32',
    'longitude'  : 'float32',
    'co_column'  : 'float32',
    'co_quality' : 'float32',
    'year'       : 'int16',
    'month'      : 'int16',    # int8 can cause issues in Dask, use int16 to be safe
    'day'        : 'int16',
    'day_of_week': 'int16',
}

  ddf = dd.read_csv(
        files,
        dtype=dask_dtype_map,
        assume_missing=True,
  )

  print(f"  Partitions : {ddf.npartitions}")
  print(f"  Columns    : {list(ddf.columns)}")
  print(f"  Rows (est) : {len(ddf):,}")

  # parallel aggregation — each partition processed on a separate core,
  # only the small summary is brought into memory, not the full frame
  result = (
      ddf.groupby('year')[['co_column', 'co_quality']]
      .mean()
      .compute()                                  # triggers parallel execution
      .reset_index()
      .sort_values('year')
    )

  return result

perf5, result5 = measure_performance(strategy5_dask, "S5 – Dask Parallel")
perf_df5 = pd.DataFrame([perf5])
print(f"  {'-'*100}")
print(perf_df5.to_string(index=False))
```

`dd.read_csv()` reads the files lazily without loading data into memory. A `groupby` aggregation computing the mean CO column and quality per year is then defined as a deferred computation graph. `.compute()` triggers parallel execution across partitions. Because only the small summary DataFrame is returned, peak memory is very low. `assume_missing=True` ensures Dask safely handles columns that may contain nulls.

#### 9.1.2 Strategy Comparison Summary

```python
metrics = ['Description', 'Execution Time (s)', 'Peak Usage (MB)', 'CPU Avg (%)', 'Throughput (rec/s)']

summary = pd.DataFrame([perf1, perf2, perf3, perf4, perf5])[metrics].copy()
summary.columns = ['Strategy', 'Exec Time (s)', 'Peak Memory (MB)', 'CPU Avg (%)', 'Throughput (rec/s)']

print("\n" + "="*80)
print("STRATEGY COMPARISON SUMMARY")
print("="*80)
print(summary.to_string(index=False))
```

**Key Observations**:

- **Execution Time**: S4 (Sampling) is the fastest while S3 (Type Optimisation) is the slowest, showing that optimisation steps can sometimes introduce overhead rather than improve speed.
- **Peak Memory**: S5 (Dask Parallel) uses the least memory by far, while S3 (Type Optimisation) and S1/S2 consume significantly more, demonstrating that parallel/distributed processing is the most memory-efficient approach here.
- **CPU Usage**: S5 (Dask Parallel) shows the highest CPU utilisation, indicating strong parallel activity, while S2 has the lowest, suggesting lighter processing load.
- **Throughput**: S2 (Chunking) achieves the highest throughput, while S5 (Dask Parallel) is extremely low, indicating that distributed overhead can severely reduce performance in this setup when the final output is a small aggregation.

---

### 5b. Polars

**What is this strategy?**
Polars uses `scan_csv()` for lazy loading combined with `schema_overrides` for type optimisation, then executes a parallel grouped aggregation via `.collect()`. It is built on Rust and designed specifically for multi-threaded, vectorised data processing.

**Why is it used?**
Polars combines the benefits of both type optimisation and parallel processing in a single, tightly integrated library. Its lazy evaluation defers computation until `.collect()` is called, allowing the query planner to optimise the execution plan. As a result, it is often the fastest option for large-file CSV processing, typically outperforming both Pandas and Dask.

#### 9.2.1 Performance Overview

```python
def strategy5_polars():
    # Strategy 3: Data Type Optimisation (Schema Overrides)
    polars_schema = {
        'latitude': pl.Float32,
        'longitude': pl.Float32,
        'co_column': pl.Float32,
        'co_quality': pl.Float32,
        'year': pl.Int16,
        'month': pl.Int16,
        'day': pl.Int16,
        'day_of_week': pl.Int16,
    }

    # Use pl.scan_csv for lazy loading and parallel processing
    # 'files' is the list of CSV paths already defined in the notebook
    ldf = pl.scan_csv(files, schema_overrides=polars_schema, ignore_errors=True)

    # Strategy 5: Parallel Aggregation
    result = (
        ldf.group_by('year')
        .agg([
            pl.col('co_column').mean().alias('co_column'),
            pl.col('co_quality').mean().alias('co_quality')
        ])
        .sort('year')
        .collect() # This triggers the parallel execution
    )

    return result.to_pandas()

# Measure performance
perf_pl, result_pl = measure_performance(strategy5_polars, "S5 – Polars Parallel")
```

`pl.scan_csv()` creates a lazy DataFrame (LazyFrame) without reading any data. The `schema_overrides` dictionary applies type optimisation at scan time, equivalent to Strategy 3. A grouped aggregation is declared as a lazy operation, and `.collect()` triggers Polars' parallel query execution engine. The result is converted to a pandas DataFrame for consistency with the rest of the benchmark.

#### 9.2.2 Strategy Comparison Summary (Polars)

```python
polars_summary = pd.DataFrame([perf_pl])
display(polars_summary)

# Adding Polars to the main summary for a final look
if 'perf5' in locals() or 'perf5' in globals():
    all_strategies = [perf1, perf2, perf3, perf4, perf_pl]
else:
    all_strategies = [perf1, perf2, perf3, perf4, perf_pl]

final_comparison = pd.DataFrame(all_strategies)
display(final_comparison[['Description', 'Execution Time (s)', 'Peak Usage (MB)', 'CPU Avg (%)']])
```

---

## 📊 Task 4: Comparative Analysis

### 🔍 Part 1: Comparison of Optimised Loading Strategies

This section compares the five strategies in terms of **Execution Time**, **Peak Memory Usage**, **Average CPU Usage**, and **Throughput**.

#### 10.1 Visualising All 5 Strategies

```python
summary = pd.concat([summary, polars_summary], ignore_index=True)
strategies  = summary['Strategy'].tolist()
short_labels = ['S1\nLoad Less', 'S2\nChunking', 'S3\nDtype Opt', 'S4\nSampling', 'S5\nDask', 'S5\nPolar']

metrics_cfg = [
    {
        'col'   : 'Exec Time (s)',
        'title' : 'Execution Time',
        'unit'  : 'seconds',
        'color' : '#4C72B0',
        'note'  : 'Lower is better',
        'lower' : True,
    },
    {
        'col'   : 'Peak Memory (MB)',
        'title' : 'Peak Memory Usage',
        'unit'  : 'MB',
        'color' : '#DD8452',
        'note'  : 'Lower is better',
        'lower' : True,
    },
    {
        'col'   : 'CPU Avg (%)',
        'title' : 'Average CPU Usage',
        'unit'  : '%',
        'color' : '#55A868',
        'note'  : 'Higher = more parallelism',
        'lower' : False,
    },
    {
        'col'   : 'Throughput (rec/s)',
        'title' : 'Throughput',
        'unit'  : 'records/s',
        'color' : '#C44E52',
        'note'  : 'Higher is better',
        'lower' : False,
    },
]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Big Data Strategy — Performance Comparison', fontsize=15, fontweight='bold', y=1.01)
axes = axes.flatten()

for ax, cfg in zip(axes, metrics_cfg):
    values = summary[cfg['col']].fillna(0).tolist()
    bars   = ax.bar(short_labels, values, color=cfg['color'], alpha=0.85,
                    width=0.55, edgecolor='white', linewidth=0.8)

    # highlight best bar
    best_idx = int(np.argmin(values) if cfg['lower'] else np.argmax(values))
    bars[best_idx].set_edgecolor('#1a1a1a')
    bars[best_idx].set_linewidth(2)
    bars[best_idx].set_alpha(1.0)

    # value labels on each bar
    for bar, val in zip(bars, values):
        if val == 0:
            label = 'N/A'
        elif cfg['unit'] == 'records/s':
            label = f'{val/1e6:.2f}M' if val > 1e6 else f'{val:,.0f}'
        elif cfg['unit'] == 'seconds':
            label = f'{val:.1f}s'
        elif cfg['unit'] == 'MB':
            label = f'{val:.0f}'
        else:
            label = f'{val:.1f}%'

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(values) * 0.01,
            label,
            ha='center', va='bottom', fontsize=9, fontweight='500'
        )

    ax.set_title(cfg['title'], fontsize=12, fontweight='bold', pad=10)
    ax.set_ylabel(cfg['unit'], fontsize=10)
    ax.set_ylim(0, max(values) * 1.18)
    ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(axis='x', labelsize=9)
    ax.tick_params(axis='y', labelsize=9)
    ax.yaxis.grid(True, linestyle='--', alpha=0.4)
    ax.set_axisbelow(True)

    # note + best marker
    best_patch = mpatches.Patch(color=cfg['color'], alpha=1.0,
                                label=f'Best: {short_labels[best_idx].replace(chr(10)," ")}')
    ax.legend(handles=[best_patch], fontsize=8, loc='upper right',
              framealpha=0.6, edgecolor='none')
    ax.set_xlabel(cfg['note'], fontsize=8, color='grey', style='italic')

plt.tight_layout()
plt.show()
```
output:
<img width="1389" height="1014" alt="download" src="https://github.com/user-attachments/assets/e25b06ef-6a36-465b-bdfa-1013fe61a866" />

This chart plots all six strategy variants across four performance metrics, with the best-performing bar per metric highlighted with a darker border. The `metrics_cfg` list drives the subplot generation loop, keeping the chart code DRY and easily extendable.

---

### 📘 Part 2: Comparison Between Pandas, Dask, and Polars

#### 10.2 Benchmark Function

```python
def benchmark(func, label, n_runs=2):

    load_times    = []
    process_times = []
    total_times   = []
    peak_mems     = []
    last_result   = None

    for run in range(n_runs):
        gc.collect()                            # clear previous run's memory

        tracemalloc.start()

        t_total_start = time.time()

        # LOAD phase
        t_load_start = time.time()
        data = func['load']()
        t_load_end   = time.time()

        # PROCESS phase (full compute)
        t_proc_start = time.time()
        result = func['compute'](data)
        t_proc_end   = time.time()

        t_total_end  = time.time()

        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        load_times.append(t_load_end    - t_load_start)
        process_times.append(t_proc_end - t_proc_start)
        total_times.append(t_total_end  - t_total_start)
        peak_mems.append(peak / 1e6)            # bytes → MB

        last_result = result
        del data, result
        gc.collect()

        print(f"  [{label}] Run {run+1}/{n_runs} — "
              f"total: {total_times[-1]:.2f}s  peak: {peak_mems[-1]:.1f} MB")

    return {
        'Library'            : label,
        'Load Time (s)'      : round(np.mean(load_times),    4),
        'Process Time (s)'   : round(np.mean(process_times), 4),
        'Total Time (s)'     : round(np.mean(total_times),   4),
        'Peak Memory (MB)'   : round(np.mean(peak_mems),     2),
        'Runs averaged'      : n_runs,
    }, last_result
```

This benchmarking function separates timing into a **load phase** and a **compute/process phase**, allowing finer-grained comparison between libraries. `tracemalloc` tracks Python-level memory allocations for peak memory measurement. Each benchmark is averaged over `n_runs=2` runs to reduce noise, with `gc.collect()` called between runs to ensure a clean memory state.

#### 10.3 Full Load with Pandas

```python
pandas_funcs = {
    'load': lambda: [pd.read_csv(f) for f in files],
    'compute': lambda chunks: pd.concat(chunks, ignore_index=True),
}

print("Running Pandas baseline...")
perf_pandas, result_pandas = benchmark(pandas_funcs, "Pandas")
print(f"  Shape: {result_pandas.shape}\n")
del result_pandas
gc.collect()
```

The Pandas baseline reads each CSV file into memory eagerly and concatenates them. This represents the most straightforward approach and serves as the reference against which Dask and Polars are compared.

#### 10.4 Full Load with Dask

```python
dask_dtype_map = {
    'latitude'   : 'float32',
    'longitude'  : 'float32',
    'co_column'  : 'float32',
    'co_quality' : 'float32',
    'year'       : 'int16',
    'month'      : 'int16',    # int8 can cause issues in Dask, use int16 to be safe
    'day'        : 'int16',
    'day_of_week': 'int16',
}

dask_funcs = {
    'load'   : lambda: dd.read_csv(files, assume_missing=True, dtype=dask_dtype_map,),
    'compute': lambda ddf: ddf.compute().reset_index(drop=True),
}

print("Running Dask...")
perf_dask, result_dask = benchmark(dask_funcs, "Dask")
print(f"  Shape: {result_dask.shape}\n")
del result_dask
gc.collect()
```

Dask loads files lazily with type-optimised schema, then calls `.compute()` to materialise the full DataFrame. Because `.compute()` triggers parallel partition reads, the load and compute phases are more interleaved in practice. `int8` is avoided for Dask integer columns to prevent known type-handling issues in some Dask versions.

#### 10.5 Full Load with Polars

```python
import polars as pl
import pandas as pd
import gc

polars_dtype_map = {
    "latitude"   : pl.Float32,
    "longitude"  : pl.Float32,
    "co_column"  : pl.Float32,
    "co_quality" : pl.Float32,
    "year"       : pl.Int16,
    "month"      : pl.Int16,
    "day"        : pl.Int16,
    "day_of_week": pl.Int16,
}

polars_funcs = {
    "load"   : lambda: pl.scan_csv(files, schema_overrides=polars_dtype_map, ignore_errors=True),
    "compute": lambda ldf: ldf.collect().to_pandas(),
}

print("Running Polars...")
perf_polars, result_polars = benchmark(polars_funcs, "Polars")
print(f"  Shape: {result_polars.shape}\n")
del result_polars
gc.collect()
```

Polars uses lazy scanning (`scan_csv`) with schema overrides for type optimisation, then materialises the result with `.collect()`. The Rust-backed execution engine enables aggressive parallelism and memory efficiency. The result is converted to a pandas DataFrame for shape inspection and fair comparison.

#### 10.6 Summary Table

```python
import pandas as pd

# Construct the comparison dataframe using available metrics
comp_df = pd.DataFrame([perf_pandas, perf_dask, perf_polars])

print("\n" + "="*80)
print("SECTION 5 — COMPARATIVE ANALYSIS RESULTS")
print(f"Operation : Load + Full Dataset Compute   |   Runs averaged: {2}")
print("="*80)
print(comp_df.to_string(index=False))

# Highlight best per metric
print("\n── Best per metric ──")
for col in ["Load Time (s)", "Process Time (s)", "Total Time (s)", "Peak Memory (MB)"]:
    best_idx = comp_df[col].idxmin()
    print(f"  {col:<22}: {comp_df.loc[best_idx, 'Library']}  ({comp_df.loc[best_idx, col]})")
```

#### 10.7 Visualisation (Bar Chart)

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

libraries = [p["Library"] for p in [perf_pandas, perf_dask, perf_polars]]
colors    = ["#4C72B0", "#DD8452", "#55A868"]

metrics_cfg = [
    {"key": "Load Time (s)",    "title": "Load Time",       "unit": "s",  "lower": True },
    {"key": "Process Time (s)", "title": "Process Time",    "unit": "s",  "lower": True },
    {"key": "Total Time (s)",   "title": "Total Time",      "unit": "s",  "lower": True },
    {"key": "Peak Memory (MB)", "title": "Peak Memory",     "unit": "MB", "lower": True },
]

fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle(
    f"Section 5 — Pandas vs Dask vs Polars\n"
    f"Operation: Load + Full Compute  |  Avg of {2} runs",
    fontsize=13, fontweight="bold"
)
axes = axes.flatten()

for ax, cfg in zip(axes, metrics_cfg):
    values   = [comp_df.loc[comp_df["Library"]==lib, cfg["key"]].values[0] for lib in libraries]
    best_idx = int(np.argmin(values))

    bars = ax.bar(libraries, values, color=colors, alpha=0.82, width=0.5, edgecolor="white", linewidth=0.8)
    bars[best_idx].set_edgecolor("#1a1a1a")
    bars[best_idx].set_linewidth(2.5)
    bars[best_idx].set_alpha(1.0)

    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(values) * 0.015, f"{val:.2f}{cfg['unit']}", ha="center", va="bottom", fontsize=10, fontweight="500")

    ax.set_title(cfg["title"], fontsize=12, fontweight="bold", pad=8)
    ax.set_ylabel(cfg["unit"], fontsize=10)
    ax.set_ylim(0, max(values) * 1.2)
    ax.spines[["top", "right"]].set_visible(False)
    ax.yaxis.grid(True, linestyle="--", alpha=0.35)
    ax.set_xlabel("Lower is better", fontsize=8, color="grey", style="italic")

    best_patch = mpatches.Patch(color=colors[best_idx], label=f"Best: {libraries[best_idx]}")
    ax.legend(handles=[best_patch], fontsize=9, loc="upper right", framealpha=0.5, edgecolor="none")

plt.tight_layout()
plt.show()
```
Output:
<img width="1289" height="887" alt="download" src="https://github.com/user-attachments/assets/46855fa7-627c-45d7-9f3c-ec072ed653d6" />
This chart compares Pandas, Dask, and Polars across four metrics: load time, process time, total time, and peak memory. Each bar is labelled with its exact value, and the best-performing library per metric is highlighted with a darker border for easy identification.

---

### 🧠 Summary of Interpretation

#### Part 1 — Five Optimisation Strategies

| Strategy            | Peak Memory | Exec Time | CPU Avg | Throughput     |
| ------------------- | ----------- | --------- | ------- | -------------- |
| S1 – Load Less Data | Low         | Fast      | Moderate| Moderate       |
| S2 – Chunking       | Moderate    | Moderate  | Low     | High           |
| S3 – Type Optimisation | Moderate | Slow      | Moderate| Moderate      |
| S4 – Sampling       | Low (post)  | Fastest   | Moderate| Low            |
| S5 – Dask Parallel  | Lowest      | Slow      | Highest | Very Low       |
| S5 – Polars Parallel| Very Low    | Fast      | High    | High           |

#### Part 2 — Library Comparison (Full Load + Compute)

The comparative analysis between Pandas, Dask, and Polars reveals clear differences in execution behaviour and efficiency:

**Polars** consistently leads in total speed and memory efficiency. Its Rust-backed, multi-threaded engine enables aggressive parallelism during both CSV parsing and aggregation. With the lowest total execution time and competitive peak memory, it is the best choice when raw throughput matters.

**Pandas** provides a straightforward and reliable baseline. It performs reasonably for datasets that fit comfortably within available RAM and is the safest choice for familiar, well-tested workflows where setup simplicity is valued over peak performance.

**Dask** is designed for scale, not for speed on single-machine medium-sized datasets. Its lazy computation model shines when datasets exceed RAM capacity, as it avoids loading all data at once. However, when forced to materialise a full DataFrame via `.compute()`, its scheduling overhead can make it slower than both Pandas and Polars. Its strength is fault-tolerant, out-of-core processing on distributed or memory-constrained environments.

---

## 🧠 Task 5: Conclusion & Reflection

### 🔹 Conclusion
The key observation from this assignment is that parallel processing combined with optimized data types was the most successful technique for handling large datasets efficiently. While chunking reduced memory usage in Pandas, it still required iterative processing and higher execution time. In comparison, frameworks like Polars and Dask demonstrated superior performance by leveraging parallelism. Among them, Polars performed the best due to its lazy execution model (scan_csv) and efficient memory handling, achieving faster execution with lower memory usage than both Pandas and Dask.


### 🔹 Reflection

Throughout this assignment, we learned that being resource-aware is critical in data science, especially when handling large-scale datasets. The main limitation is not always computational power, but how data is loaded and processed in memory. Instead of loading entire datasets at once, applying techniques such as chunking and data type optimization allowed us to significantly reduce memory usage. Tools like Polars or Dask demonstrated that efficient data handling strategies can outperform traditional approaches, enabling larger datasets to be processed on the same hardware without failure.

### 🔹 Scalability

If this dataset were to grow by 10x, standard Pandas would fail entirely on a local machine. We would be forced to rely exclusively on Dask for cluster computing or Polars to maximize a single powerful machine.

## References
1. Muhammad Bilal. (2025). *Pakistan Carbon Monoxide 2022 - 2025*. Kaggle. https://www.kaggle.com/datasets/muhammadbilal77511/pakistan-carbon-monoxide-2022-2025
2. Pandas Documentation: https://pandas.pydata.org/docs/
3. Dask Documentation: https://docs.dask.org/
4. Polars Documentation: https://pola.rs/
