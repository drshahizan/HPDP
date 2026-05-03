# 📘 Assignment 2: Mastering Big Data Handling

**Group Members**:  
- Student 1: *Muhammad Syahmi Faris bin Rusli, A23CS0138*  
- Student 2: *Ng Yu Hin, A23CS0148*

---

## 📝 Task 1: Dataset Selection

### 📌 Dataset Overview

* **Name**: *🚕 NYC Yellow Taxi Trip Data 🗽*
* **Source**: [Kaggle – Elemento](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data)
* **Domain**: *Transportation / Urban Analytics*
* **File Size**: *~1.99 GB (January 2015 subset)*
* **Shape**: *~12.7 Million rows × 19 columns*


### 📖 Description

🔍 Key Features

- **Temporal**: Pickup and drop-off timestamps.
- **Geospatial**: Longitude and latitude coordinates for trip start and end.
- **Financial**: Fare amount, mta_tax, tip_amount, and total_amount.
- **Trip Metadata**: Passenger count, trip distance, and payment type.

This dataset contains records of yellow medallion taxicab trips in New York City. The data was collected and provided to the NYC Taxi and Limousine Commission (TLC). Each record includes fields capturing pick-up and drop-off dates/times, locations, distances, itemized fares, rate types, and payment types.

### 📊 Data Column Description

| Column Name              | Data Type | Description                                                                     |
| -------------------------| --------- | ------------------------------------------------------------------------------- |
| `VendorID`               | int64     | A code indicating the TPEP provider that provided the record                    |
| `tpep_pickup_datetime`   | object    | The date and time when the meter was engaged                                    |
| `tpep_dropoff_datetime`  | object    | The date and time when the meter was disengaged                                 |
| `passenger_count`        | int64     | The number of passengers in the vehicle. This is a driver-entered value         |
| `trip_distance`          | float64   | The elapsed trip distance in miles reported by the taximeter                    |
| `pickup_longitude`       | float64   | Longitude where the meter was engaged                                           |
| `pickup_latitude`        | float64   | Latitude where the meter was engaged                                            |
| `RatecodeID`             | int64     | The final rate code in effect at the end of the trip                            |
| `store_and_fwd_flag`     | object    | This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka "store and forward"                                                                           |
| `dropoff_longitude`      | float64   | Longitude where the meter was disengaged                                        |
| `dropoff_latitude`       | float64   | Latitude where the meter was disengaged                                         |
| `payment_type`           | int64     | A numeric code signifying how the passenger paid for the trip                   |
| `fare_amount`            | float64   | The time-and-distance fare calculated by the meter                              |
| `extra`                  | float64   | Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges                                                                                       |
| `mta_tax`                | float64   | $0.50 MTA tax that is automatically triggered based on the metered rate in use  |
| `tip_amount`             | float64   | This field is automatically populated for credit card tips. Cash tips are not included                                                                                                                 |
| `tolls_amount`           | float64   | Total amount of all tolls paid in trip                                          |
| `improvement_surcharge`  | float64   | $0.30 improvement surcharge assessed on trips at the flag drop                  |
| `total_amount`           | float64   | The total amount charged to passengers. Does not include cash tips              |

---


## 📝 Task 2: Load and Inspect Data

### 🔹 Loading Strategy

To load the dataset efficiently in [Google Colab](https://colab.research.google.com/), the following steps were taken:

1. **Imported `kaggle.json`**
   Uploaded via the Colab file upload feature:

   ```python
   from google.colab import files
   files.upload()  # Upload kaggle.json
   ```

2. **Configured Kaggle API Credentials**
   Moved the uploaded file to the `.kaggle` directory and set proper permissions:

   ```bash
   !mkdir -p ~/.kaggle
   !cp kaggle.json ~/.kaggle/
   !chmod 600 ~/.kaggle/kaggle.json
   ```

3. **Downloaded Dataset from Kaggle**
   Using Kaggle CLI to fetch the dataset directly into the Colab environment:

   ```bash
   !kaggle datasets download -d elemento/nyc-yellow-taxi-trip-data
   ```

4. **Unzipped the Dataset File**
   Extracted the dataset ZIP file:

   ```bash
   !unzip nyc-yellow-taxi-trip-data.zip
   ```

5. **Loaded a Sample (100 Rows) Using `pandas.read_csv()`**
   This is to allow quicker inspection without overloading memory:

   ```python
   import pandas as pd
   df = pd.read_csv('yellow_tripdata_2016-03.csv', nrows=1000000)
   ```

---

### 🔹 Dataset Inspection

#### 📌 First 5 Rows

```python
df['taxi_short'] = df['total_amount'].astype(str).str.slice(0, 100) + '...'

print("First 5 rows of the dataset:")
display(df.drop(columns=['total_amount']).head())
df = df.drop(columns=['taxi_short'])
```

| index | VendorID | tpep_pickup_datetime | tpep_dropoff_datetime | passenger_count | trip_distance | pickup_longitude | pickup_latitude | RatecodeID | store_and_fwd_flag | dropoff_longitude | dropoff_latitude | payment_type | fare_amount | extra | mta_tax | tip_amount | tolls_amount | improvement_surcharge | taxi_short |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 2016-03-01 00:00:00 | 2016-03-01 00:07:55 | 1 | 2.50 | -73.976746 | 40.765152 | 1 | N | -74.004265 | 40.746128 | 1 | 9.0 | 0.5 | 0.5 | 2.05 | 0.00 | 0.3 | 12.35... |
| 1 | 1 | 2016-03-01 00:00:00 | 2016-03-01 00:11:06 | 1 | 2.90 | -73.983482 | 40.767925 | 1 | N | -74.005943 | 40.733166 | 1 | 11.0 | 0.5 | 0.5 | 3.05 | 0.00 | 0.3 | 15.35... |
| 2 | 2 | 2016-03-01 00:00:00 | 2016-03-01 00:31:06 | 2 | 19.98 | -73.782021 | 40.644810 | 1 | N | -73.974541 | 40.675770 | 1 | 54.5 | 0.5 | 0.5 | 8.00 | 0.00 | 0.3 | 63.8... |
| 3 | 2 | 2016-03-01 00:00:00 | 2016-03-01 00:00:00 | 3 | 10.78 | -73.863419 | 40.769814 | 1 | N | -73.969650 | 40.757767 | 1 | 31.5 | 0.0 | 0.5 | 3.78 | 5.54 | 0.3 | 41.62... |
| 4 | 2 | 2016-03-01 00:00:00 | 2016-03-01 00:00:00 | 5 | 30.43 | -73.971741 | 40.792183 | 3 | N | -74.177170 | 40.695053 | 1 | 98.0 | 0.0 | 0.0 | 0.00 | 15.50 | 0.3 | 113.8... |
---

#### 📐 Shape of the Dataset

```python
print(f"\nDataset Shape:\nRows: {df.shape[0]}, Columns: {df.shape[1]}")
```

![image](https://github.com/user-attachments/assets/ad35f73a-8f2d-4915-b5d1-12a08f6231a4)


---

#### 🏷️ Column Names and Data Types

```python
display(df.dtypes.to_frame(name='Data Type').T)
```
![image](https://github.com/user-attachments/assets/6e39e229-0074-474e-820f-c0a66341a62b)

---

#### 📋 Summary Info

```python
df.info()
```

![image](https://github.com/user-attachments/assets/8edde355-d89b-4ad9-9843-a91942abedf2)


---

## 🛠️ Task 3: Apply Big Data Handling Strategies

### 🔹 **Part 1: Memory- and Performance-Efficient Techniques**
In this notebook, we apply five effective strategies to handle large datasets using traditional pandas for part 1, and compare three library pandas, polars and dask in part 2:

Part 1:

Load Less Data
Use Chunking
Optimize Data Types
Sampling
(Simulated) Parallel Processing Strategy with Chunk Aggregation
Part 2:

Pandas
Polars
Dask

### 📊 Function used to get memory usage
**Code**
```python
def measure_performance(func, description="", *args, **kwargs):
    process = psutil.Process(os.getpid())
    total_ram = psutil.virtual_memory().total / 1024 / 1024  # MB

    cpu_percent = []

    def track_cpu():
        while not done[0]:
            cpu_percent.append(process.cpu_percent(interval=0.1))

    done = [False]
    cpu_thread = threading.Thread(target=track_cpu)
    cpu_thread.start()

    mem_before = process.memory_info().rss / 1024 / 1024  # MB
    start_time = time.time()

    try:
        result = func(*args, **kwargs)
        success = True
    except Exception as e:
        result = None
        success = False
        error_message = str(e)

    end_time = time.time()
    mem_after = process.memory_info().rss / 1024 / 1024  # MB
    done[0] = True
    cpu_thread.join()

    exec_time = round(end_time - start_time, 4)
    mem_diff_mb = mem_after - mem_before
    mem_percent_after = (mem_after / total_ram) * 100
    mem_diff_percent = (mem_diff_mb / total_ram) * 100

    if isinstance(result, dd.DataFrame):
      result = result.compute()

    if isinstance(result, (pd.DataFrame, pl.DataFrame)):
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

### Strategy 1: Load Less Data
Load only the necessary columns or filter relevant rows during the data reading process to minimize memory consumption.

**Code**:
```python
import pandas as pd

def load_less_data_pandas(file_path):

    actual_col_names = pd.read_csv(file_path, nrows=0).columns.tolist()

    # Define the columns needed
    target_cols = [
        'tpep_pickup_datetime',
        'tpep_dropoff_datetime',
        'passenger_count',
        'trip_distance',
        'RatecodeID',
        'total_amount'
    ]

    # Filter target_cols to only include those that actually exist in the file
    # This prevents the "Usecols do not match" error from crashing the script
    valid_cols = [col for col in target_cols if col in actual_col_names]

    df = pd.read_csv(file_path, usecols=valid_cols)
    return df

# Execute and measure
performance_s1, df_s1 = measure_performance(
    load_less_data_pandas,
    description="Strategy 1: Load Less Data (Column Projection)",
    file_path="yellow_tripdata_2016-03.csv"
)

# Display Results
performance_df_s1 = pd.DataFrame([performance_s1])
display(performance_df_s1)
```
**Output Summary**: 
<img width="772" height="99" alt="image" src="https://github.com/user-attachments/assets/40a05aff-2e63-4a06-9000-1b990df5addd" />

---

### Strategy 2: Chunking
Process the data in small chunks using pandas.read_csv(chunksize=100000).

**Code**:
```python
import tracemalloc
import time
import psutil
import threading

#helper to track peak memory (same pattern as Strategy 1)
def measure_performance_chunking(func, description, **kwargs):
    tracemalloc.start()
    process = psutil.Process()
    cpu_samples = []
    stop_flag = threading.Event()

    def sample_cpu():
        while not stop_flag.is_set():
            cpu_samples.append(psutil.cpu_percent(interval=0.5))
    cpu_thread = threading.Thread(target=sample_cpu, daemon=True)
    cpu_thread.start()

    start_time = time.time()
    result = func(**kwargs)
    elapsed = time.time() - start_time

    stop_flag.set()
    cpu_thread.join()

    _, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    peak_mem_mb = round(peak_mem / (1024 ** 2), 2)
    avg_cpu = round(sum(cpu_samples) / len(cpu_samples), 2) if cpu_samples else 0.0
    total_records = result.get("total_records", 0)
    throughput = round(total_records / elapsed, 2) if elapsed > 0 else 0

    return {
        "Description": description,
        "Memory Used (MB)": peak_mem_mb,
        "Execution Time (s)": round(elapsed, 4),
        "Success": True,
        "Average CPU (%)": avg_cpu,
        "Throughput (records/sec)": throughput,
    }, result


#  chunked processing function
def load_with_chunking(file_path, chunk_size=100_000):
    """
    Reads the CSV in chunks and computes:
      - total number of records
      - total fare amount across the full dataset
    Only one chunk occupies memory at a time.
    """
    total_records = 0
    total_fare    = 0.0
    chunk_count   = 0

    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        total_records += len(chunk)
        total_fare    += chunk["fare_amount"].sum()
        chunk_count   += 1

    return {
        "total_records": total_records,
        "total_fare":    round(total_fare, 2),
        "chunk_count":   chunk_count,
        "chunk_size":    chunk_size,
    }


# run & measure
performance_s2, result_s2 = measure_performance_chunking(
    load_with_chunking,
    description="Strategy 2: Chunking (100k rows/chunk)",
    file_path="yellow_tripdata_2016-03.csv",
    chunk_size=100_000,
)

# display performance table
performance_df_s2 = pd.DataFrame([performance_s2])
display(performance_df_s2)

# display chunking results
print(f"   Chunking Summary:")
print(f"   Chunk size      : {result_s2['chunk_size']:,} rows")
print(f"   Number of chunks: {result_s2['chunk_count']}")
print(f"   Total records   : {result_s2['total_records']:,}")
print(f"   Total fare amt  : ${result_s2['total_fare']:,.2f}")
```
**Output Summary**:  
<img width="779" height="93" alt="image" src="https://github.com/user-attachments/assets/1380b5af-f4fb-4b42-affe-8b62bc2b481c" />

---

### Strategy 3: Optimized Data Type
Process the data in by convert the data with specific data type.

**Code**:
```python
import pandas as pd
import tracemalloc
import time
import psutil
import gc

FILE_PATH  = "yellow_tripdata_2016-03.csv"
CHUNK_SIZE = 200_000
total_rows = 12227456

optimized_dtypes = {
    "VendorID":              "int8",
    "passenger_count":       "int8",
    "RatecodeID":            "int8",
    "payment_type":          "int8",
    "store_and_fwd_flag":    "category",
    "trip_distance":         "float32",
    "pickup_longitude":      "float32",
    "pickup_latitude":       "float32",
    "dropoff_longitude":     "float32",
    "dropoff_latitude":      "float32",
    "fare_amount":           "float32",
    "extra":                 "float32",
    "mta_tax":               "float32",
    "tip_amount":            "float32",
    "tolls_amount":          "float32",
    "improvement_surcharge": "float32",
    "total_amount":          "float32",
}

# Step 1: Default types via chunking
print("-- Step 1: Default Types --")
tracemalloc.start()
start = time.time()

default_mem_total = 0
default_col_mem   = None
default_dtypes    = None
chunk_count       = 0

for chunk in pd.read_csv(FILE_PATH, chunksize=CHUNK_SIZE):
    chunk_mem = chunk.memory_usage(deep=False)   # ← removed deep=True
    default_mem_total += chunk_mem.sum()
    if default_col_mem is None:
        default_col_mem = chunk_mem.drop("Index").copy()
        default_dtypes  = chunk.dtypes.copy()
    del chunk
    chunk_count += 1

gc.collect()
elapsed_default  = round(time.time() - start, 4)
_, peak_default  = tracemalloc.get_traced_memory()
tracemalloc.stop()
inmem_default_mb = round(default_mem_total / (1024**2), 2)
peak_default_mb  = round(peak_default / (1024**2), 2)
default_col_sizes = (default_col_mem / (1024**2) * chunk_count).round(2)

print(f"   Chunks     : {chunk_count}")
print(f"   Full size  : {inmem_default_mb} MB")
print(f"   Peak mem   : {peak_default_mb} MB")
print(f"   Time       : {elapsed_default} s")

#  Step 2: Optimized types via chunking
print("\n-- Step 2: Optimized Types --")
tracemalloc.start()
start = time.time()

optimized_mem_total     = 0
optimized_col_mem       = None
optimized_dtypes_result = None

for chunk in pd.read_csv(FILE_PATH, chunksize=CHUNK_SIZE, dtype=optimized_dtypes):
    chunk_mem = chunk.memory_usage(deep=False)   # ← removed deep=True
    optimized_mem_total += chunk_mem.sum()
    if optimized_col_mem is None:
        optimized_col_mem       = chunk_mem.drop("Index").copy()
        optimized_dtypes_result = chunk.dtypes.copy()
    del chunk

gc.collect()
elapsed_optimized  = round(time.time() - start, 4)
_, peak_optimized  = tracemalloc.get_traced_memory()
tracemalloc.stop()
inmem_optimized_mb = round(optimized_mem_total / (1024**2), 2)
peak_optimized_mb  = round(peak_optimized / (1024**2), 2)
optimized_col_sizes = (optimized_col_mem / (1024**2) * chunk_count).round(2)

print(f"   Full size  : {inmem_optimized_mb} MB")
print(f"   Peak mem   : {peak_optimized_mb} MB")
print(f"   Time       : {elapsed_optimized} s")

# Step 3: Column breakdown
print("\n-- Step 3: Column Breakdown --")
comparison_df = pd.DataFrame({
    "Default Type":       default_dtypes,
    "Optimized Type":     optimized_dtypes_result,
    "Default Mem (MB)":   default_col_sizes,
    "Optimized Mem (MB)": optimized_col_sizes,
})
comparison_df["Reduction (%)"] = (
    (comparison_df["Default Mem (MB)"] - comparison_df["Optimized Mem (MB)"])
    / comparison_df["Default Mem (MB)"] * 100
).round(1)
display(comparison_df)

# Step 4: Summary
reduction_pct = round((inmem_default_mb - inmem_optimized_mb) / inmem_default_mb * 100, 1)

performance_s3 = {
    "Description":              "Strategy 3: Optimized Data Types",
    "Memory Used (MB)":         peak_optimized_mb,
    "Execution Time (s)":       elapsed_optimized,
    "Success":                  True,
    "Average CPU (%)":          round(psutil.cpu_percent(interval=1), 2),
    "Throughput (records/sec)": round(total_rows / elapsed_optimized, 2),
}
display(pd.DataFrame([performance_s3]))

print(f"\n Memory Reduction Summary:")
print(f"   Before : {inmem_default_mb} MB")
print(f"   After  : {inmem_optimized_mb} MB")
print(f"   Saved  : {reduction_pct}%")
```
**Output Summary**:  
<img width="244" height="200" alt="image" src="https://github.com/user-attachments/assets/5c34e0ce-e633-408a-8937-110c4c2f94fb" />
<img width="779" height="720" alt="image" src="https://github.com/user-attachments/assets/559a6b01-41bd-4f29-a6b5-731d724d61ad" />
<img width="205" height="74" alt="image" src="https://github.com/user-attachments/assets/0d00f641-1f5f-4a6b-8bfc-3a4291a28d3b" />

---

### Strategy 4: Sampling
Reduce the dataset size to reduce processing time

**Code**:
```python
def load_with_sampling(file_path):
    p = 0.1  # 10% sampling

    # We use a lambda to skip rows randomly, keeping the header (index 0)
    df = pd.read_csv(
        file_path,
        header=0,
        skiprows=lambda i: i > 0 and random.random() > p
    )
    return df

# Execute and measure
performance_s4, df_s4 = measure_performance(
    load_with_sampling,
    description="Strategy 4: Sampling (Approx. 10%)",
    file_path="yellow_tripdata_2016-03.csv"
)

# Display Results
performance_df_s4 = pd.DataFrame([performance_s4])
display(performance_df_s4)
```
**Output Summary**:  
<img width="776" height="104" alt="image" src="https://github.com/user-attachments/assets/751cc4cc-6bac-457a-8b7f-ed725684342d" />

---

### Strategy 5: Parallel Processing with Dask
Process parallel using dask (used multiple core.)
**Code**:  
```python
def load_with_dask(file_path):
    # 'assume_missing' handles columns with mixed nulls/numbers
    # 'low_memory=False' or specific dtypes help with Dask's strict type checking
    ddf = dd.read_csv(
        file_path,
        assume_missing=True,
        dtype={'store_and_fwd_flag': 'object'}
    )
    return ddf

# Execute and measure
performance_s5, df_s5 = measure_performance(
    load_with_dask,
    description="Strategy 5: Parallel Processing (Dask)",
    file_path="yellow_tripdata_2016-03.csv"
)

# Display Results
performance_df_s5 = pd.DataFrame([performance_s5])
display(performance_df_s5)
```
**Output Summary**:  
<img width="781" height="101" alt="image" src="https://github.com/user-attachments/assets/7a71d245-85af-40bd-9b2c-7b91eacde0a9" />

---

## 🛠️ Task 4: Comparative Analysis

### 🔹 **Part 2: Loading Dataset with Different Libraries**
This section compares how various data libraries handle CSV file loading and performance. Different tools and ecosystems (Pandas, Dask, Polars, Vaex) are explored.

```python
import pandas as pd
import numpy as np
import os
import dask.dataframe as dd
from IPython.display import display # Just use for display purposes
import psutil
import time
import random
import csv
import polars as pl
import threading
import matplotlib.pyplot as plt
import seaborn as sns

def measure_performance(func, description="", *args, **kwargs):
    process = psutil.Process(os.getpid())
    total_ram = psutil.virtual_memory().total / 1024 / 1024  # MB

    cpu_percent = []

    def track_cpu():
        while not done[0]:
            cpu_percent.append(process.cpu_percent(interval=0.1))

    done = [False]
    cpu_thread = threading.Thread(target=track_cpu)
    cpu_thread.start()

    mem_before = process.memory_info().rss / 1024 / 1024  # MB
    start_time = time.time()

    try:
        result = func(*args, **kwargs)
        success = True
    except Exception as e:
        result = None
        success = False
        error_message = str(e)

    end_time = time.time()
    mem_after = process.memory_info().rss / 1024 / 1024  # MB
    done[0] = True
    cpu_thread.join()

    exec_time = round(end_time - start_time, 4)
    mem_diff_mb = mem_after - mem_before
    mem_percent_after = (mem_after / total_ram) * 100
    mem_diff_percent = (mem_diff_mb / total_ram) * 100

    if isinstance(result, dd.DataFrame):
      result = result.compute()

    if isinstance(result, (pd.DataFrame, pl.DataFrame)):
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

#### 1. Using **Pandas** (Traditional)

```python
def load_full_data():
    df = pd.read_csv("yellow_tripdata_2016-03.csv")
    return df

performance, df = measure_performance(load_full_data, description="Load with Pandas")

performance_df = pd.DataFrame([performance])
display(performance_df)
```
**Output**:  
<img width="774" height="83" alt="image" src="https://github.com/user-attachments/assets/1194f6ee-aa53-4b97-8cde-178a5e8f1453" />

---

#### 2. Using **Polars**

```python
import polars as pl

def load_full_data_polars():
    df = pl.read_csv("yellow_tripdata_2016-03.csv", infer_schema_length=10000)
    return df

performance_polars, df_polars = measure_performance(
    load_full_data_polars,
    description="Load with Polars"
)

performance_df_polars = pd.DataFrame([performance_polars])
display(performance_df_polars)
```

1. **Reading the CSV with `pl.read_csv()`**:

2. **Simplicity and Speed**:

3. **Performance Measurement**:
  
**Output**:  
<img width="763" height="68" alt="image" src="https://github.com/user-attachments/assets/a709af24-d8ee-4240-ac55-c1fb9e365bab" />

---

#### 3. Using **Dask**

```python
import dask.dataframe as dd

def load_full_data_dask():
    df = dd.read_csv("yellow_tripdata_2016-03.csv").compute()
    return df

performance_dask, df_dask = measure_performance(
    load_full_data_dask,
    description="Load with Dask"
)

performance_df_dask = pd.DataFrame([performance_dask])
display(performance_df_dask)
```

**Explanation**:  

1. **Lazy Loading with `dd.read_csv()`**:

2. **Triggering Computation**:

3. **Performance Measurement**:

**Output**:  
<img width="763" height="79" alt="image" src="https://github.com/user-attachments/assets/d455433f-90ba-468d-ba07-cfe19b977164" />

---

## 🛠️ Compare Performance

### 🔹 **Part 1: Comparison of Optimized Loading Strategies**
This section compares five different optimization techniques used to improve CSV loading performance in terms of **Memory Used**, **Execution Time**, **Average CPU Usage**, and **Throughput**.

#### Compare between 5 strategies:
1. Load Less Data
2. Use Chunking
3. Optimize Data Types
4. Sampling
5. (Simulated) Parallel Processing Strategy with Chunk Aggregation

### 📋 Summary Table
| Strategy            | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (records/sec) |
| ------------------- | ---------------- | ------------------ | ----------- | ------------------------ |
| Load Less Data      | 973.72           | 48.6298	           | 93.62	    | 251100.19                |
| Use Chunking        | 72.62            | 81.4862            |72.46        | 149852.95                |
| Optimize Data Types | 105.06           | 271.9356           | 28.1        | 44964.53                 |
| Sampling            | 221.85           | 29.6481            | 95.8        | 41157.11                 |
| Parallel with Dask  | 4.65             |  0.1865            | 29.3        | 6547473.46               |

---

### 📊 Visual Comparison
<img width="808" height="555" alt="image" src="https://github.com/user-attachments/assets/fcccab84-911e-47d4-9e01-a8d4c6806bf6" />

### 🧠 Interpretation:
**Parellel with Dask** performed best in overall.

---

### 📘 Part 2: Comparison Between Pandas, Dask, and Polars
In this section, we compare the performance of three major data-processing libraries: **Pandas**, **Dask**, and **Polars**.

### 📋 Summary Table

| Library | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (records/sec) |
| ------- | ---------------- | ------------------ | ----------- | ------------------------ |
| Pandas  | 3665.21          | 74.4024            | 96.43       | 164120.40                |
| Dask    | 4343.52          | 16.0955            | 141.66      | 758656.27                |
| Polars  | 3044.03          | 66.8097            | 133.67      | 182772.14                |

---

### 📊 Visual Comparison
<img width="809" height="548" alt="image" src="https://github.com/user-attachments/assets/dedbbfa3-0845-44ae-a497-f283468f2b2b" />

### 🧠 Interpretation:

---

## 🧠 Task 5: Conclusion & Reflection
***MUHAMMAD SYAHMI FARIS BIN RUSLI:***

***My Parts:*** Strategy 2 (Chunking), Strategy 3 (Optimized Data Types), Lobrary 2 (Polars), Library 3 (Dask), and Compare 3 Libraries

***My Observartions:***
* Chunking was the most memory efficient strategy at only 72.62 MB peak memory, though slower at 81.49 seconds due to sequential chunk processing
* Optimized data types reduced memory significantly by downcasting int64->int8 and flot64->float32, reduced the dataset from 1770.09mb to 803.53mb and took 271.94s.
* Polars was the fastest library at 16.10 seconds which is 4.62x faster than Pandas 74.04s becasue due to its Rust-based engine and automatic multi-core processing.
* Dask at 66.81s performed similarly to Pandas 74.40s showing that Dask advantage only appears at larger scales or distributed environment.
  
***What Suprised Me:*** I expected Dask to outperform Pandas since it supports parellel processing, but it performed almost identically. I learned that dask scheduling overhead cancels out its parellelism benefits on a single machine with a dataset that still fits in RAM. I would have used Polars from the start if I knew how fast it was.

***Scalability*** At 10GB, Polars and chunking would still work. At 100GB, Dask becomes necessary to distribute across cores. At 1TB, cloud solutions like Apache Spark would be required as no single machine could handle it in memory.

---

***NG YU HIN:***

***My Parts:*** Strategy 1 (Load Less Data), Strategy 4 (Sampling), Strategy 5 (Parallel Processing), Library 1 (Pandas), and Compare 5 Strategies.

***My Observations:***
* Load Less Data is the most effective. By only loading the necessary columns, memory usage dropped to 1001.87 MB and execution time fell to 36.97 seconds, proving that minimizing I/O operations is critical.
* Sampling was incredibly fast. This strategy is invaluable for Exploratory Data Analysis (EDA) and pipeline testing before committing compute resources to the full dataset.
* Parallel Processing achieved the highest throughput by far but requires writing slightly more complex, framework-specific code to manage the map-reduce aggregations.
* Pandas is highly intuitive and easy to write, but its eager loading is exceptionally heavy on RAM during peaking at around 2.4 GB for a full load and is severely bottlenecked by Python's single-core execution limit.

***What Surprised Me:*** I was surprised by how quickly standard Pandas consumes memory—often using significantly more RAM than the actual file size on disk. I also didn't expect that simply dropping a few unused columns,Strategy 1 would yield such a massive, immediate improvement in both speed and memory without changing any core logic.

***Overall Strategy Comparison:*** There is no single perfect strategy.The choice depends entirely on the system's constraints. If RAM is the bottleneck, Chunking and Optimizing Types are required. If time is the bottleneck, Parallel Processing and Loading Less Data are the solutions.
