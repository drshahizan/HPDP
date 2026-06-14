# Mastering Big Data Handling
### SECP3133 — High Performance Data Processing | Assignment 2

---

## Group Members

| Name | Matric No | Role |
|------|-----------|------|
| Safiya Nursyahadah binti Masnoor | A23CS0176 | Dataset, Data Inspection, Strategies 1–3 |
| Farra Nurzahin binti Zaharil Anuar | A23CS0079 | Strategies 4–5, Comparative Analysis, Report |

---

## 1. Dataset Description

| Field | Details |
|-------|---------|
| **Name** | Amazon Product Data |
| **Source** | [Kaggle — piyushjain16](https://www.kaggle.com/datasets/piyushjain16/amazon-product-data) |
| **File** | product_amazon_data.csv |
| **Format** | CSV |
| **Size** | ~1.6 GB |
| **Records** | ~1,000,000+ rows |
| **Domain** | Cloud & E-Commerce |
| **Columns Used** | `PRODUCT_ID`, `TITLE`, `PRODUCT_TYPE_ID`, `PRODUCT_LENGTH` |

This dataset contains Amazon product listings including product IDs, titles, product type classifications, and physical product dimensions. It represents large-scale cloud-based analytics and e-commerce fulfilment data. The size of the dataset makes it an ideal candidate for big data handling techniques, as loading it naively with Pandas causes excessive memory consumption on standard hardware.

---

## 2. Library Choices

In this assignment, we used three Python libraries to handle and process the Amazon Product dataset.

### 2.1 Pandas (Library 1 – Compulsory)

Pandas is the most widely used data processing library in Python. It loads the entire dataset into memory at once and runs on a single CPU core. We used it as our **baseline**, meaning all other strategies are compared against how Pandas performs by default.

### 2.2 Dask (Library 2 – Scalable)

Dask is designed to handle datasets that are too large to fit in RAM. It splits the data into smaller chunks and processes them in parallel across multiple CPU cores. Dask does not run immediately, it builds a plan first and only executes when `.compute()` is called. We chose it to see how a chunk-based parallel approach compares to Pandas on a large dataset.

### 2.3 Polars (Library 3 – Scalable)

Polars is a newer and much faster alternative to Pandas. It is built in Rust and uses all CPU cores automatically without any extra setup. Like Dask, it is lazy by default. It only reads the data it actually needs. We chose it to test whether a modern high-performance library could outperform both Pandas and Dask on the same task.

---

## Environment Setup

# Install Kaggle and download dataset
```python
from google.colab import files
files.upload()  # upload kaggle.json

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d piyushjain16/amazon-product-data
!unzip amazon-product-data.zip

# Move file from subfolder to working directory
import os
if os.path.exists("dataset/train.csv"):
    os.rename("dataset/train.csv", "product_amazon_data.csv")
    print("Success: File is now product_amazon_data.csv and ready to use!")

# Imports
import pandas as pd
import numpy as np
import dask.dataframe as dd
import polars as pl
import tracemalloc
import psutil
import time
import threading
import os
import gc
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

FILE_PATH = "product_amazon_data.csv"
print(f"File size: {os.path.getsize(FILE_PATH) / (1024**2):.2f} MB")
```
---

## 3. Data Loading and Inspection

Initial inspection was performed by loading the full dataset using Pandas with `low_memory=False` to correctly infer column types. A basic inspection was then carried out to understand the structure of the dataset before applying any strategies.

```python
df_copy = pd.read_csv("product_amazon_data.csv", low_memory=False)
df = df_copy.copy()

# Preview the first 5 rows
df.head()
```
**Output Screenshot:**

<img width="1732" height="342" alt="Screenshot 2026-06-14 214205" src="https://github.com/user-attachments/assets/d1643f90-5790-4605-82e7-aea0c5a8d182" />

```python
# Column names and data types
df.info()
```
**Output Screenshot:**

<img width="652" height="310" alt="image" src="https://github.com/user-attachments/assets/2c218104-a0e0-497c-9de7-1cdf87ab26f8" />


```python
# Count of non-null values per column
df.count()
```
**Output Screenshot:**

<img width="390" height="342" alt="image" src="https://github.com/user-attachments/assets/7a529b63-ac92-4102-b302-6c702a5d711a" />

```python
# Shape of the dataset
rows, cols = df.shape
print(f"Rows: {rows}, Columns: {cols}")
```

**Output Screenshot:**

<img width="507" height="122" alt="image" src="https://github.com/user-attachments/assets/bdec2309-8f58-44ec-88b7-b22acc395c43" />


> The default Pandas data types are over-allocated for this dataset. For example, `PRODUCT_ID` and `PRODUCT_TYPE_ID` are stored as `int64` despite their values fitting in smaller integer types, and `PRODUCT_LENGTH` uses `float64` when `float32` is sufficient. This motivates Strategy 3.

---

## Performance Measurement Function

A shared `measure_performance()` function is used consistently across all strategies to ensure fair and comparable measurements of memory usage, execution time, and CPU utilisation.

```python
def measure_performance(func, description="", *args, **kwargs):
    process = psutil.Process(os.getpid())

    cpu_percent = []
    done = [False]

    def track_cpu():
        while not done[0]:
            cpu_percent.append(process.cpu_percent(interval=0.1))

    cpu_thread = threading.Thread(target=track_cpu)
    cpu_thread.start()

    mem_before = process.memory_info().rss / 1024 / 1024
    start_time = time.time()

    try:
        result = func(*args, **kwargs)
        success = True
    except Exception as e:
        result = None
        success = False
        error_message = str(e)

    end_time = time.time()
    mem_after = process.memory_info().rss / 1024 / 1024

    done[0] = True
    cpu_thread.join()

    exec_time = round(end_time - start_time, 4)
    mem_diff_mb = mem_after - mem_before

    if isinstance(result, pd.DataFrame):
        num_records = len(result)
        throughput = round(num_records / exec_time, 2)
    else:
        throughput = None

    performance = {
        "Description": description,
        "Memory Used (MB)": round(mem_diff_mb, 2),
        "Execution Time (s)": exec_time,
        "Success": success,
        "Average CPU (%)": round(sum(cpu_percent) / len(cpu_percent), 2) if cpu_percent else 0.0,
        "Throughput (records/sec)": throughput
    }

    if not success:
        performance["Error"] = error_message

    return performance, result
```

---

## 4. Big Data Handling Strategies

---

### 4.1 Load Less Data

Instead of reading all columns from the CSV, we use the `usecols` parameter to load only the 4 columns required for analysis. This prevents unnecessary data from ever entering memory.

```python
def load_less_data_pandas(file_path):
    cols = ['PRODUCT_ID', 'TITLE', 'PRODUCT_TYPE_ID', 'PRODUCT_LENGTH']
    return pd.read_csv(file_path, usecols=cols)

file_path = "product_amazon_data.csv"

performance_less_data, df_less_data = measure_performance(
    load_less_data_pandas,
    description="Load Less Data with Pandas (Amazon Dataset)",
    file_path=file_path
)

display(pd.DataFrame([performance_less_data]))
```
**Output Screenshot:**

<img width="1375" height="107" alt="image" src="https://github.com/user-attachments/assets/857b3070-f306-4e53-8954-333a6059b319" />

**Explanation:**

By specifying only the 4 columns required using `usecols`, Pandas skips parsing and storing all other columns entirely. This reduces both memory usage and I/O time since fewer bytes are read from disk. This strategy is most effective when the dataset has many columns but the analysis only needs a small subset. It should always be the first line of defence before loading any large file.

---

### 4.2 Chunking

Instead of loading the entire dataset in a single operation, we use `chunksize=100,000` to process the file in smaller portions. Each chunk is loaded, processed, and concatenated into a final DataFrame.

```python
def load_with_chunking(file_path):
    chunks = []
    for chunk in pd.read_csv(file_path, chunksize=100000, low_memory=False):
        chunks.append(chunk)

    df = pd.concat(chunks, ignore_index=True)
    return df

performance_chunking, df_chunked = measure_performance(
    load_with_chunking,
    description="Chunked Load (Amazon Dataset)",
    file_path="product_amazon_data.csv"
)

display(pd.DataFrame([performance_chunking]))
```
**Output Screenshot:**

<img width="1215" height="110" alt="image" src="https://github.com/user-attachments/assets/ab7e4feb-af98-46bc-9f7d-d157ef6e0113" />


**Explanation:**

Chunking ensures that only 100,000 rows occupy RAM at any given moment. Each chunk is processed and appended to a list before the next chunk is loaded. Without chunking, loading the full ~1.6 GB dataset into Pandas in a single call risks exceeding the available memory on Google Colab's free tier. This strategy is especially important for aggregate operations on datasets larger than available RAM, as it allows the full file to be processed without a single large memory spike.

---

### 4.3 Data Type Optimisation

Pandas assigns default data types when reading CSVs, which are often wasteful. `PRODUCT_ID` and `PRODUCT_TYPE_ID` are stored as `int64` by default, but their values fit within smaller unsigned integer types. `PRODUCT_LENGTH` defaults to `float64` when `float32` precision is sufficient.

```python
def optimize_data_types(df_input):
    df_opt = df_input.copy()

    df_opt['PRODUCT_ID'] = pd.to_numeric(df_opt['PRODUCT_ID'], downcast='unsigned')
    df_opt['PRODUCT_TYPE_ID'] = pd.to_numeric(df_opt['PRODUCT_TYPE_ID'], downcast='unsigned')
    df_opt['PRODUCT_LENGTH'] = pd.to_numeric(df_opt['PRODUCT_LENGTH'], downcast='float')

    return df_opt

performance_opt, df_optimized = measure_performance(
    optimize_data_types,
    description="Data Type Optimization (Downcasting)",
    df_input=df
)

display(pd.DataFrame([performance_opt]))

print("\nFinal Optimised Data Types:")
display(df_optimized.dtypes.to_frame(name='New Data Type'))
```
**Output Screenshot:**

<img width="1328" height="432" alt="image" src="https://github.com/user-attachments/assets/c98069d8-2e20-46db-866f-183b965b5bfe" />


**Type changes applied:**

| Column | Before | After | Reason |
|--------|--------|-------|--------|
| `PRODUCT_ID` | int64 | uint32 or smaller | Product IDs are non-negative and fit within 32-bit unsigned range |
| `PRODUCT_TYPE_ID` | int64 | uint32 or smaller | Category IDs are non-negative and small in range |
| `PRODUCT_LENGTH` | float64 | float32 | Physical dimensions do not require double precision |

**Explanation:**

Downcasting reduces the number of bytes used to store each value. An `int64` column uses 8 bytes per value; downcasting to `uint8` or `uint16` reduces this to 1–2 bytes, cutting memory by up to 75% for that column. `float64` to `float32` halves the per-value storage from 8 bytes to 4 bytes. Applied across one million rows, these reductions translate to hundreds of megabytes of savings. This strategy should be applied after initial inspection, once the value ranges of each column are understood, so that all subsequent operations benefit from the reduced memory footprint.

---

### 4.4 Sampling

Instead of processing the full dataset, a representative 5% random sample is drawn using `df.sample(frac=0.05)`. This drastically reduces the number of rows in memory while still preserving the statistical distribution of the data.

```python
def run_sampling(df_input):
    return df_input.sample(frac=0.05, random_state=42)

performance_sampling, df_sample = measure_performance(
    run_sampling,
    description="Sampling (5% of Dataset)",
    df_input=df
)

display(pd.DataFrame([performance_sampling]))
print(f"Original Row Count : {len(df):,}")
print(f"Sampled Row Count  : {len(df_sample):,}")
print(f"Rows removed       : {len(df) - len(df_sample):,} ({(1 - len(df_sample)/len(df))*100:.0f}% reduction)")
```

**Output Screenshot:**

<img width="1114" height="166" alt="image" src="https://github.com/user-attachments/assets/0f52a6ee-89a9-4673-ad9e-f8de25368e5a" />

**Explanation:**

Sampling is useful for exploratory analysis, prototyping, and model development where working with the full dataset is unnecessary. By randomly selecting 5% of rows with a fixed `random_state`, the sample is reproducible and representative. The trade-off is that sampling introduces a loss of information — rare events or minority categories may be underrepresented or missing entirely. It is not suitable for tasks that require complete data, such as full aggregations or reporting, but significantly speeds up iteration during the development phase.

---

### 4.5 Parallel Processing with Dask and Polars

Two parallel processing libraries are applied to the same groupby aggregation task to compare their performance against Pandas.

#### 4.5a: Dask

Dask splits the CSV into partitions and processes them in parallel using a lazy task graph, only computing when `.compute()` is called.

```python
def run_dask_parallel(file_path):
    ddf = dd.read_csv(file_path, low_memory=False, assume_missing=True)

    result = (
        ddf
        .groupby("PRODUCT_TYPE_ID")["PRODUCT_LENGTH"]
        .mean()
        .reset_index()
        .compute()
        .sort_values("PRODUCT_LENGTH", ascending=False)
    )
    return result

performance_dask, result_dask = measure_performance(
    run_dask_parallel,
    description="Strategy 5: Parallel Processing (Dask)",
    file_path="product_amazon_data.csv"
)

display(pd.DataFrame([performance_dask]))
```

**Output Screenshot:**

<img width="1209" height="99" alt="image" src="https://github.com/user-attachments/assets/5fefae5a-5e25-4122-b210-1dbc78e3cb27" />

#### 4.5b: Polars

Polars uses lazy evaluation via `scan_csv`, builds an optimised query plan, and executes it with `.collect()` using all available CPU cores.

```python
def run_polars_parallel(file_path):
    result = (
        pl.scan_csv(file_path, infer_schema_length=10000)
        .group_by("PRODUCT_TYPE_ID")
        .agg(pl.col("PRODUCT_LENGTH").mean().alias("PRODUCT_LENGTH"))
        .sort("PRODUCT_LENGTH", descending=True)
        .collect()
        .to_pandas()
    )
    return result

performance_polars, result_polars = measure_performance(
    run_polars_parallel,
    description="Strategy 5: Parallel Processing (Polars)",
    file_path="product_amazon_data.csv"
)

display(pd.DataFrame([performance_polars]))
```

**Output Screenshot:**

<img width="1219" height="100" alt="image" src="https://github.com/user-attachments/assets/da9fa70b-e236-48dc-9823-9ad9f924a517" />


**Explanation:**

Both Dask and Polars use parallelism to speed up processing, but in different ways. Dask partitions the data and distributes work across threads, making it ideal for datasets too large to fit in RAM. Polars, built in Rust, processes data in-memory using all CPU cores with a columnar format and lazy execution, making it significantly faster when the data fits in memory. For this dataset, Polars outperforms Dask because the coordination overhead of Dask's task scheduler adds cost that Polars avoids entirely.

---
# 5.0 Comparative Analysis

## 5.1 Comparison Between Strategies

The chart below compares all five strategies across four metrics: execution time, memory usage, average CPU usage, and throughput.

```python
all_strategies = pd.DataFrame([
    performance_less_data,
    performance_chunking,
    performance_opt,
    performance_sampling,
    performance_dask,
    performance_polars,
])

all_strategies["Label"] = [
    "S1: Load\nLess Data",
    "S2: Chunking",
    "S3: Type\nOptimise",
    "S4: Sampling",
    "S5: Dask",
    "S5: Polars",
]
```

**Output Screenshot:**

<img width="880" height="623" alt="image" src="https://github.com/user-attachments/assets/66539391-e918-41dc-838c-d846c1bc088a" />


---

## 5.2 Comparison Between Libraries (Pandas vs. Dask vs. Polars)

Each library was benchmarked over 3 runs on the same groupby aggregation task. Load time, process time, total time, and peak memory were averaged across runs to ensure fair comparison.

```python
library_table = pd.DataFrame({
    "Library"              : ["Pandas", "Dask", "Polars"],
    "Avg Load Time (s)"    : [metrics_pandas["Avg Load Time (s)"],
                              metrics_dask["Avg Load Time (s)"],
                              metrics_polars["Avg Load Time (s)"]],
    "Avg Process Time (s)" : [metrics_pandas["Avg Process Time (s)"],
                              metrics_dask["Avg Process Time (s)"],
                              metrics_polars["Avg Process Time (s)"]],
    "Avg Total Time (s)"   : [metrics_pandas["Avg Total Time (s)"],
                              metrics_dask["Avg Total Time (s)"],
                              metrics_polars["Avg Total Time (s)"]],
    "Peak Memory (MB)"     : [metrics_pandas["Peak Memory (MB)"],
                              metrics_dask["Peak Memory (MB)"],
                              metrics_polars["Peak Memory (MB)"]],
})

display(library_table)
```

**Output Screenshot:**

<img width="889" height="199" alt="image" src="https://github.com/user-attachments/assets/033cc0b1-4a17-4010-b33f-7c9324065a91" />


**Output Screenshot:**

<img width="1168" height="832" alt="image" src="https://github.com/user-attachments/assets/e38f25b4-8649-4408-9a3f-d13bf45b97c9" />


### 5.3 Critical Discussion

**Why Polars is fastest:** Polars uses lazy evaluation — it builds a query plan first and only reads the data it needs when `.collect()` is called. It is also built in Rust with multi-threading by default, using all CPU cores automatically. Combined with columnar Arrow memory storage, this makes both loading and processing significantly faster than the other libraries.

**Why Pandas is slowest:** Pandas loads the entire file into memory at once and runs on a single thread. It cannot take advantage of multiple CPU cores, which becomes a clear bottleneck on large datasets. That said, Pandas remains the easiest to use and has the widest ecosystem support, making it a reasonable choice for smaller data.

**Why Dask falls in between:** Dask is designed for data that is too large to fit in RAM, splitting work into chunks processed in parallel. However, this coordination has overhead. Since the Amazon dataset fits in memory, Dask's chunking mechanism adds cost rather than benefit — making it slower than Polars and only marginally better than Pandas here.

**Trade-off:** The core trade-off is performance vs simplicity. Polars wins on speed and memory efficiency, Pandas wins on ease of use and ecosystem, and Dask is best suited for truly out-of-memory workloads — not for datasets like this one.

## 6. Conclusion

This assignment explored five big data handling strategies applied to the Amazon Product dataset (~1.6 GB). Each strategy targeted a different bottleneck — whether it was reducing the amount of data loaded, managing memory through chunking, optimising data types, shrinking the dataset through sampling, or leveraging parallel processing libraries.

Among all strategies, Sampling was the fastest due to the sheer reduction in data volume, while Data Type Optimisation offered memory savings with no data loss. For parallel processing, Polars proved to be the most efficient library overall — outperforming both Pandas and Dask in speed and memory usage thanks to its Rust-based engine and lazy evaluation design. Dask, while suitable for truly out-of-memory workloads, showed overhead costs that made it less competitive when the dataset fits in RAM.

> Overall, no single strategy is universally best. The right approach depends on the size of the data, the task at hand, and the available resources. Combining strategies — such as loading less data and then downcasting types — would likely yield the best real-world performance.

---

## Reflection

### Safiya Nursyahadah binti Masnoor (A23CS0176)

Through this assignment, I gained a much better understanding of how to handle large datasets efficiently using Python. Working on the dataset setup, initial inspection and the first three strategies taught me that performance improvements do not always require complex tools. Sometimes loading only the columns you need or adjusting data types is enough to make a significant difference. I was surprised by how much memory could be saved just by downcasting `int64` to a smaller type across a million rows. This experience made me realise the importance of understanding your data before writing any code and it has made me more careful and intentional about memory usage in my future work.

---

### Farra Nurzahin binti Zaharil Anuar (A23CS0079)

Working on the more advanced parts of this assignment including Sampling, parallel processing with Dask and Polars and the comparative analysis, gave me a new perspective on how data tools are designed and why they perform differently. Understanding concepts like lazy evaluation, columnar storage and multi-threading made the numbers feel meaningful rather than just results on a table. The critical discussion was the most challenging part, as it required me to explain architectural differences clearly but it was also the most valuable. This assignment changed how I approach tool selection. I now think about why a tool fits a problem not just whether it works.

---

## References

1. Amazon Product Dataset. Kaggle. Retrieved from: https://www.kaggle.com/datasets/piyushjain16/amazon-product-data
