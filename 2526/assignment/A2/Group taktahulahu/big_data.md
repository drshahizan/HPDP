# Mastering Big Data Handling
### SECP3133 — High Performance Data Processing | Assignment 2

---

## Group Members

| Name | Matric No | Role |
|------|-----------|------|
| Safiya Nursyahadah binti Masnoor | A23CS0176 | Dataset, Data Inspection, Strategies 1–3 |
| Farra Nurzahin binti Zaharil Anuar | A23CS0079 | Strategies 4–5, Comparative Analysis, Report |

---

## Dataset Description

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

## Task 2: Load and Inspect Data

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

## Task 3: Big Data Handling Strategies

---

### Strategy 1: Load Less Data

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

### Strategy 2: Chunking

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

### Strategy 3: Data Type Optimisation

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

