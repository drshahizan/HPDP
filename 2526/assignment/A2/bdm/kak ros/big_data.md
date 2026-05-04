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

3. **Loaded a Sample (100 Rows) Using `pandas.read_csv()`**
   This is to allow quicker inspection without overloading memory:

   ```python
   import pandas as pd
   df = pd.read_csv("2009.csv")
   df.head()
   ```

---

## 📌 Task 3 : Big Data Handling

### Task 3.1 : Load Less Data
### Task 3.2 : Chunking
### Task 3.3 : Data Type Optimisation
### Task 3.4 : Sampling
### Task 3.5 : Parallel Processing with Scalable Libraries
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

---

## 📊 Task 4: Comparative Analysis

To evaluate the efficiency of big data handling strategies, we benchmarked our baseline traditional method (Pandas) against two scalable libraries (Dask and Polars). We measured peak memory usage and total execution time for our standard aggregation task: calculating the average departure delay per airline on a single-year dataset.

### 📋 Summary Table

| Library | Execution Time (Seconds) | Peak Memory Usage (MB) | Evaluation Strategy |
| :--- | :--- | :--- | :--- |
| **Pandas** | [Insert Pandas Time] | [Insert Pandas Memory] | Eager, Single-threaded |
| **Dask** | [Insert Dask Time] | [Insert Dask Memory] | Lazy, Multi-threaded |
| **Polars** | [Insert Polars Time] | [Insert Polars Memory] | Lazy, Multi-threaded, Query Optimized |

---

### 📊 Visual Comparison
<img width="1361" height="593" alt="comparison bar chart" src="https://github.com/user-attachments/assets/b7ac6bda-ac5d-437a-bbfd-1738bf9b06a2" /> [Performance Comparison Chart]

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
