# 📘 Assignment 2: Mastering Big Data Handling

**Group Members**:  
- Student 1: *Harini A/P Sangaran, A23CS0081*  
- Student 2: *Nurul Adriana Binti Kamal Jefri, A23CS0258*

---

## 📝 Task 1: Dataset Selection

### 📌 Dataset Overview

* **Name**: *Airline Delay and Cancellation Data, 2009 - 2018*
* **Source**: [Kaggle – yuanyuwendymu](https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018)
* **Domain**: *Transportation / Aviation*
* **File Size**: *7.62 GB (Uncompressed)*
* **Shape**: *61,556,964 rows × 28 columns*


### 📖 Description

This dataset is a comprehensive compilation of flight tracking records collected over a ten-year period. It contains over 61 million flight logs detailing domestic operations across the United States. Efficiently handling this scale of data requires specialized tools and techniques that go beyond standard memory limits.

> ⚠️ Note:
>
> * Cancelled or diverted flights will naturally be missing arrival times and airborne durations.
> * Specific delay reason columns (e.g., Weather Delay, Carrier Delay) contain null values if the flight departed on time.
> * The sheer size of the uncompressed data (7.62 GB) exceeds standard RAM capacities, requiring strategic loading methods.


### 🔍 Key Features

* **Flight Metadata**: Date, Airline Carrier Code (`OP_CARRIER`), Flight Number, Tail Number.
* **Location Data**: Origin Airport, Destination Airport, Distance.
* **Time Metrics**: Scheduled Departure/Arrival, Actual Departure/Arrival.
* **Performance Attributes**: Departure Delay (`DEP_DELAY`), Arrival Delay, Cancellation Codes.

---

## 📝 Task 2: Load and Inspect Data

### 🔹 Loading Strategy

To load the dataset efficiently in Google Colab without crashing the kernel, we pulled the data directly via the Kaggle API.

1. **Downloaded Dataset from Kaggle**
   Using Kaggle CLI to fetch the dataset directly into the Colab environment:
   ```bash
   !kaggle datasets download -d yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018
   ```

2. **Unzipped the Dataset File**
   Extracted the dataset ZIP file:
   ```bash
   !unzip airline-delay-and-cancellation-data-2009-2018.zip
   ```

3. **Loaded a Sample Using `pandas.read_csv()`**
   This is to allow quicker inspection without overloading memory:

   ```python
   import pandas as pd
   df = pd.read_csv("2009.csv")
   ```

---

### 🔹 Dataset Inspection

#### 📌 First 5 Rows

```python
pd.set_option('display.max_columns', None)
df.head()
```

|index|FL_DATE|OP_CARRIER|OP_CARRIER_FL_NUM|ORIGIN|DEST|CRS_DEP_TIME|DEP_TIME|DEP_DELAY|TAXI_OUT|WHEELS_OFF|WHEELS_ON|TAXI_IN|CRS_ARR_TIME|ARR_TIME|ARR_DELAY|CANCELLED|CANCELLATION_CODE|DIVERTED|CRS_ELAPSED_TIME|ACTUAL_ELAPSED_TIME|AIR_TIME|DISTANCE|CARRIER_DELAY|WEATHER_DELAY|NAS_DELAY|SECURITY_DELAY|LATE_AIRCRAFT_DELAY|Unnamed:27|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0|2009-01-01|XE|1204|DCA|EWR|1100|1058.0|-2.0|18.0|1116.0|1158.0|8.0|1202|1206.0|4.0|0.0|NaN|0.0|62.0|68.0|42.0|199.0|NaN|NaN|NaN|NaN|NaN|NaN|
|1|2009-01-01|XE|1206|EWR|IAD|1510|1509.0|-1.0|28.0|1537.0|1620.0|4.0|1632|1624.0|-8.0|0.0|NaN|0.0|82.0|75.0|43.0|213.0|NaN|NaN|NaN|NaN|NaN|NaN|
|2|2009-01-01|XE|1207|EWR|DCA|1100|1059.0|-1.0|20.0|1119.0|1155.0|6.0|1210|1201.0|-9.0|0.0|NaN|0.0|70.0|62.0|36.0|199.0|NaN|NaN|NaN|NaN|NaN|NaN|
|3|2009-01-01|XE|1208|DCA|EWR|1240|1249.0|9.0|10.0|1259.0|1336.0|9.0|1357|1345.0|-12.0|0.0|NaN|0.0|77.0|56.0|37.0|199.0|NaN|NaN|NaN|NaN|NaN|NaN|
|4|2009-01-01|XE|1209|IAD|EWR|1715|1705.0|-10.0|24.0|1729.0|1809.0|13.0|1900|1822.0|-36.0|0.0|NaN|0.0|105.0|77.0|40.0|213.0|NaN|NaN|NaN|NaN|NaN|NaN|

---

#### 🏷️ Column Names and Data Types

```python
display(df.dtypes.to_frame(name='Data Type').T)
```

| Column Name           | Data Type |
| --------------------- | --------- |
| `FL_DATE`             | object    |
| `OP_CARRIER`          | object    |
| `OP_CARRIER_FL_NUM`   | int64     |
| `ORIGIN`              | object    |
| `DEST`                | object    |
| `CRS_DEP_TIME`        | int64     |
| `DEP_TIME`            | float64   |
| `DEP_DELAY`           | float64   |
| `TAXI_OUT`            | float64   |
| `WHEELS_OFF`          | float64   |
| `WHEELS_ON`           | float64   |
| `TAXI_IN`             | float64   |
| `CRS_ARR_TIME`        | int64     |
| `ARR_TIME`            | float64   |
| `ARR_DELAY`           | float64   |
| `CANCELLED`           | float64   |
| `CANCELLATION_CODE`   | object    |
| `DIVERTED `           | float64   |
| `CRS_ELAPSED_TIME`    | float64   |
| `ACTUAL_ELAPSED_TIME` | float64   |
| `AIR_TIME`            | float64   |
| `DISTANCE`            | float64   |
| `CARRIER_DELAY`       | float64   |
| `WEATHER_DELAY`       | float64   |
| `NAS_DELAY`           | float64   |
| `SECURITY_DELAY`      | float64   |
| `LATE_AIRCRAFT_DELAY` | float64   |
| `Unnamed:27`          | float64   |

---

#### 📋 Summary Info

```python
df.info()
```
<img width="326" height="572" alt="image" src="https://github.com/user-attachments/assets/42248717-8b37-47e0-b533-0e3589cce730" />

---

## 📌 Task 3 : Big Data Handling

### Task 3.1 : Load Less Data
**Code**:
```python
import pandas as pd

# List all yearly files
files = [f"{year}.csv" for year in range(2009, 2019)]

# Columns we actually need
columns_needed = [
    "FL_DATE",
    "OP_CARRIER",
    "ORIGIN",
    "DEST",
    "DEP_DELAY",
    "ARR_DELAY"
]
dfs = []

for file in files:
    df = pd.read_csv(file, usecols=columns_needed)
    dfs.append(df)

df_all = pd.concat(dfs, ignore_index=True)

print(df_all.head())
print(df_all.info())
```

**Explanation**:  
Instead of loading all 28 columns from the dataset, only 6 relevant columns required for analysis are selected using the `usecols` parameter in Pandas.

**Implementation Summary**:  

* `FL_DATE`, `OP_CARRIER`, `ORIGIN`, `DEST`, `DEP_DELAY`, `ARR_DELAY` *

Only these columns were loaded from the CSV because they are directly relevant to:
- Flight frequency analysis
- Delay calculations
- Route-based insights

**Output Summary**:
<img width="398" height="339" alt="image" src="https://github.com/user-attachments/assets/18795792-88d6-464d-9122-7e72d7790783" />

### Task 3.2 : Chunking
3 examples were given to show the use of datain chunks in different instances. The airline along with the total number of flights operated, average delay and cancelled flight ratio per year was calculated using `chunk` function.

**📚 Example 1: Airlines and Its Total Flights Operated**

**Code**:
```python
airline_counts = {}

for file in files:
    for chunk in pd.read_csv(file, usecols=["OP_CARRIER"], chunksize=100000):
        counts = chunk["OP_CARRIER"].value_counts()

        for airline, count in counts.items():
            airline_counts[airline] = airline_counts.get(airline, 0) + count

print("Airline, Total Flights Operated: ", sorted(airline_counts.items(), key=lambda x: x[1], reverse=True)[:10])
```

**Explanation**:  
1. A dictionary airline_counts is created to store total flight counts for each airline.
2. The dataset is processed file by file and chunk by chunk. Only the `"OP_CARRIER"` column is loaded and each chunk contains 100,000 rows.
3. For each chunk, `value_counts()` counts how many times each airline appears.
4. Existing counts are updated using:
```python
airline_counts.get(airline, 0) + count
```
5. Finally, results are sorted in descending order and top 10 airlines are displayed.

**Output Summary**:
<img width="677" height="30" alt="image" src="https://github.com/user-attachments/assets/ef14cd78-703e-4690-a9d5-ef938a39c4c2" />
<img width="657" height="30" alt="image" src="https://github.com/user-attachments/assets/cdeac773-08d9-4800-a558-e6d66fa61979" />
<img width="649" height="30" alt="image" src="https://github.com/user-attachments/assets/82c83e8b-6595-41d0-9f03-1de4e20615b0" />



**📚 Example 2: Average Delay**

**Code**:
```python
total_delay = 0
total_count = 0

for file in files:
    for chunk in pd.read_csv(file, usecols=["DEP_DELAY"], chunksize=100000):
        total_delay += chunk["DEP_DELAY"].sum()
        total_count += chunk["DEP_DELAY"].count()

print("Average Delay:", total_delay / total_count)
```

**Explanation**:  
1. `total_delay` stores sum of all delays and `total_count` stores number of valid delay entries.
2. The dataset is read in chunks with only "DEP_DELAY" column is loaded
3. For each chunk:
   - `.sum()` adds all delay values in that chunk
   - `.count()` counts non-missing values
4. Final average is computed using `total_delay`/`total_count`.

**Output Summary**:
<img width="323" height="25" alt="image" src="https://github.com/user-attachments/assets/8b96fd12-5266-48be-a35b-f69ab60ef878" />



**📚 Example 3: Cancelled Flights Ratio Per Year**

**Code**:
```python
year_stats = {}

for file in files:
    year = file.split(".")[0]

    total = 0
    cancelled = 0

    for chunk in pd.read_csv(file, usecols=["CANCELLED"], chunksize=100000):
        total += len(chunk)
        cancelled += chunk["CANCELLED"].sum()

    year_stats[year] = cancelled / total

print("Cancelled flights ratio per year: ", year_stats)
```

**Explanation**:  
1. A dictionary year_stats stores cancellation ratios for each year.
2. For each chunk:
   - `len(chunk)` stores the total flights
   - "CANCELLED" column contains values 1 which means cancelled and 0 which means not cancelled
   - `.sum()` counts total cancelled flights
3. Cancellation ratio is computed using `cancelled`/`total`, whereby `cancelled` contains the total number of flights cancelled for the year and `total` contains the total number of flights operated in the year.

**Output Summary**:
<img width="755" height="26" alt="image" src="https://github.com/user-attachments/assets/497be76a-a9d2-497a-8f2a-f4a19437d8ab" />
<img width="793" height="30" alt="image" src="https://github.com/user-attachments/assets/762cf874-3821-4d27-a56d-3e7b995be5cf" />
<img width="795" height="29" alt="image" src="https://github.com/user-attachments/assets/2894f0ff-3ceb-4b6a-b7e5-1485cf306c7f" />
<img width="806" height="31" alt="image" src="https://github.com/user-attachments/assets/63a241eb-3809-4acc-bc26-92c96629c9f8" />
<img width="808" height="31" alt="image" src="https://github.com/user-attachments/assets/e17cafd0-14db-4ed9-a9f2-db2c6f480100" />
<img width="393" height="30" alt="image" src="https://github.com/user-attachments/assets/68421a10-c298-4bab-9e2c-8d5f60a5255a" />



### Task 3.3 : Data Type Optimisation
Thecolumns used in all 3 examples were assigned a much more efficient data type to reduce the memory usage, improve computation speed and to allow larger data to be processed within limited resources.


**📚 Example 1: Airlines and Its Total Flights Operated**

**Code**:
```python
for chunk in pd.read_csv(file, usecols=["OP_CARRIER"], chunksize=100000, dtype={"OP_CARRIER": "category"}): #Optimised dtype
```

**📚 Example 2: Average Delay**

**Code**:
```python
for chunk in pd.read_csv(file, usecols=["DEP_DELAY"], chunksize=100000, dtype={"DEP_DELAY": "float32"}): #Optimised dtype
```

**📚 Example 3: Cancelled Flights Ratio Per Year**

**Code**:
```python
for chunk in pd.read_csv(file, usecols=["CANCELLED"], chunksize=100000, dtype={"CANCELLED": "int8"}): #Optimised dtype
```


### Task 3.4 : Sampling
**Consolidate and Measure Dataset** : Exports the fully combined DataFrame (df_all) into a single, consolidated CSV file to be used for subsequent processing. It then utilizes the os module to retrieve the physical file size on the disk, displaying the final megabytes alongside the total row and column counts for verification.
```python
import pandas as pd
import os

# Save as a single CSV for your strategies to use
FILE_PATH = "/content/combined.csv"
df_all.to_csv(FILE_PATH, index=False)

size_mb = os.path.getsize(FILE_PATH) / 1024**2
print(f"Total rows    : {df_all.shape[0]:,}")
print(f"Total columns : {df_all.shape[1]}")
print(f"Combined size : {size_mb:.1f} MB")
```
Output:
<img width="217" height="57" alt="image" src="https://github.com/user-attachments/assets/fcd0016c-8ccd-4717-86d1-c640a77a6f64" />


### Task 3.5 : Parallel Processing with Scalable Libraries
**Benchmark Library Performance** : Executes a comparative performance test using Pandas, Dask, and Polars to calculate the average departure delay per airline on a single-year dataset. It utilizes time and tracemalloc to actively record and output the execution speed and peak memory consumption for each library, establishing a direct baseline comparison.
```python
import time
import tracemalloc
import pandas as pd
import dask.dataframe as dd
import polars as pl

# We will benchmark using one year so Pandas doesn't crash
filename = "2009.csv"
columns = ['OP_CARRIER', 'DEP_DELAY']

print("--- BENCHMARKING STARTED ---\n")

# 1. PANDAS (The Baseline)
print("Running Pandas...")
tracemalloc.start()
start_time = time.time()

df_pd = pd.read_csv(filename, usecols=columns)
pd_result = df_pd.groupby('OP_CARRIER')['DEP_DELAY'].mean()

pd_time = time.time() - start_time
_, pd_peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Pandas -> Time: {pd_time:.4f} sec | Peak Memory: {pd_peak / 10**6:.2f} MB\n")

# 2. DASK
print("Running Dask...")
tracemalloc.start()
start_time = time.time()

# Dask uses lazy evaluation, so .compute() triggers the execution
df_dask = dd.read_csv(filename, usecols=columns)
dask_result = df_dask.groupby('OP_CARRIER')['DEP_DELAY'].mean().compute()

dask_time = time.time() - start_time
_, dask_peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Dask -> Time: {dask_time:.4f} sec | Peak Memory: {dask_peak / 10**6:.2f} MB\n")

# 3. POLARS
print("Running Polars...")
tracemalloc.start()
start_time = time.time()

# Polars lazy scanning
q = (
    pl.scan_csv(filename)
    .select(columns)
    .group_by('OP_CARRIER')
    .agg(pl.col('DEP_DELAY').mean())
)
polars_result = q.collect()

polars_time = time.time() - start_time
_, polars_peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Polars -> Time: {polars_time:.4f} sec | Peak Memory: {polars_peak / 10**6:.2f} MB\n")
```
Output:
<img width="421" height="184" alt="image" src="https://github.com/user-attachments/assets/e2fa6587-3f0d-40fe-b262-19fa28f33c9e" />


---

## 📊 Task 4: Comparative Analysis

To evaluate the efficiency of big data handling strategies, we benchmarked our baseline traditional method (Pandas) against two scalable libraries (Dask and Polars). We measured peak memory usage and total execution time for our standard aggregation task: calculating the average departure delay per airline on a single-year dataset.

### 📋 Summary Table

| Library | Execution Time (Seconds) | Peak Memory Usage (MB) | Evaluation Strategy |
| :--- | :--- | :--- | :--- |
| **Pandas** | 13.3988 | 373.16 | Eager, Single-threaded |
| **Dask** | 15.2439 | 305.21 | Lazy, Multi-threaded |
| **Polars** | 2.5356 | 0.05 | Lazy, Multi-threaded, Query Optimized |
---

### 📊 Visual Comparison
<img width="1390" height="635" alt="lalala" src="https://github.com/user-attachments/assets/095d27f4-5ba5-4505-8954-850728c3774f" /> [Performance Comparison Chart]

### 🧠 Interpretation:
The performance comparison reveals key differences in execution behavior:

* **Polars** outperformed the others heavily. Written in Rust, it leverages parallel execution and vectorization. By utilizing `pl.scan_csv()`, we activated Polars' lazy API, allowing the query engine to optimize our request before execution.
* **Dask** mitigates memory issues by partitioning the dataframe into smaller chunks under the hood and processing them in parallel. Its lazy evaluation meant it did not consume massive memory spikes until `.compute()` was explicitly called.
* **Pandas** attempts to load the entire dataset into memory simultaneously and operates on a single CPU core, resulting in the highest memory footprint and slower execution times. 

---

## 🧠 Task 5: Conclusion & Reflection

### 🔹 Summary of Observations  
Our exploration of big data handling techniques yielded critical insights into optimizing performance for a 7.6 GB aviation dataset. While Pandas is highly accessible for small-scale operations, its eager loading and single-core architecture make it inherently unsuitable for raw big data. By applying strategies like selective loading (`usecols`), chunking, and data type downcasting, we successfully reduced the dataset's memory footprint to function within Google Colab.

### 🔹 Reflection & Scalability 
This assignment proved that there is no one-size-fits-all solution; the best strategy depends on dataset characteristics and computational resources. 

**Thinking Ahead: Scaling to 100 GB and Beyond**
While chunking and multi-core processing (Polars/Dask) allowed us to manage 61 million rows on a single machine, these methods have strict physical limits. If this telemetry dataset scaled to 100 GB or 1 TB, relying on a single Colab instance would create severe bottlenecks. At that scale, we would need to migrate to a distributed computing cluster. Solutions like deploying Apache Spark across a cloud environment would become necessary, decoupling processing power from the limits of a single computer's RAM.

---

## 6. References

* Kaggle. (2019). *Airline Delay and Cancellation Data, 2009 - 2018*. Retrieved from https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018
* Gorelik, A. (2019). *The Enterprise Data Lake*. O'Reilly Media.
* Polars Documentation. (n.d.). *User Guide*. Retrieved from https://pola.rs/
* Dask Documentation. (This is a fantastic template your group found. It is highly structured, visually appealing, and hits every single requirement of your assignment.
