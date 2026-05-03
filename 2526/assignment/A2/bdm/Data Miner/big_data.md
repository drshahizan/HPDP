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


