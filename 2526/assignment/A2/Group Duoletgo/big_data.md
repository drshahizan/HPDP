# 📘 Assignment 2: Mastering Big Data Handling

## **Group Members**:  
- Student 1: *Gui Kah Sin, A23CS0080*  
- Student 2: *Poh Lok Yee, A23CS0262*

# 📝 **1. Dataset Description**
## 📌 Dataset Overview

* **Name**: *Flight Delay Dataset 2024*
* **Source**: [Kaggle – Hrishit Patil](https://www.kaggle.com/datasets/hrishitpatil/flight-data-2024)
* **Domain**: *Transportation*
* **File Size**: *1.22 GB*
* **Shape**: *7,079,081 rows × 35 columns*
<br>

## 📖 Description

This dataset contains comprehensive domestic flight performance and delay records within the United States for the full calendar year of 2024. It is an aggregated compilation built by downloading monthly on-time performance files from the Bureau of Transportation Statistics (BTS) TranStats database and merging them into a unified, cleaned repository.

From the monthly data pools, **35 relevant analytical columns** were structured and standardized into a uniform schema. Spanning over **7.07 million records**, this dataset tracks critical flight timeline sequences which including operational schedule checkpoints, carrier breakdowns, distances, and categorized cancellation roots that making it highly ideal for both predictive machine learning tasks and large-scale data processing/benchmarking infrastructure.

<br>

⚠️Note:
*   Negative delay values (e.g., -10) means early flight operations.
*   Non-cancelled flights will not contain an annotated cancellation_code value (recorded as nulls/blanks).
*   Delay reason breakdowns (like weather_delay or carrier_delay) are only populated if the arrival delay exceeds 15 minutes.

<br>

🔍Key Features
*  **Flight Identity Metadata:** scheduled flight date, unique operating carrier code, and flight number.

*  **Network Trajectory Nodes**: three-letter IATA airport codes, city naming descriptions, and state boundaries for both origin and destination points.

*  **Temporal Checkpoints:** precise times for wheels-off, wheels-on, taxiing, and official arrival/departure matrices.

*  **Operational Blockages:** multi-variable metric tracking for cancellations, diversions, and minutes lost across 5 major delay vectors (Carrier, Weather, NAS, Security, and Late Aircraft).

<br>

## 📊 Data Column Description

| Column Name          | Data Type | Description                                                                         |
| -------------------- | --------- | ----------------------------------------------------------------------------------- |
| `year`               | int64     | Year of the scheduled flight (2024)                                                 |
| `month`              | int64     | Month of the flight (represented from 1 to 12)                                      |
| `day_of_month`       | int64     | Day of the month                                                                    |
| `day_of_week`        | int64     | Day of the week (1 = Monday to 7 = Sunday)                                          |
| `fl_date`            | object    | Flight date in standard ISO string format (YYYY-MM-DD)                              |
| `op_unique_carrier`  | object    | Unique airline carrier identification code (e.g., AA, DL, WN)                       |
| `op_carrier_fl_num`  | int64     | Specific flight tracking number assigned by the reporting airline                   |
| `origin`             | object    | Three-letter IATA identifier code for the departure airport                         |
| `origin_city_name`   | object    | Name of the origin city                                                             |
| `origin_state_nm`    | object    | Full state name of the origin airport                                               |
| `dest`               | object    | Three-letter IATA identifier code for the destination airport                       |
| `dest_city_name`     | object    | Name of the destination city                                                        |
| `dest_state_nm`      | object    | Full state name of the destination airport                                          |
| `crs_dep_time`       | int64     | Scheduled departure time in local format (hhmm)                                     |
| `dep_time`           | float64   | Actual departure time in local format (hhmm)                                        |
| `dep_delay`          | float64   | Departure delay calculated in minutes (negative value indicates early departure)    |
| `taxi_out`           | float64   | Taxi out time duration measured in minutes                                          |
| `wheels_off`         | float64   | Local time checkpoint when wheels left the runway (hhmm)                            |
| `wheels_on`          | float64   | Local time checkpoint when wheels touched down on the runway (hhmm)                  |
| `taxi_in`            | float64   | Taxi in time duration measured in minutes                                           |
| `crs_arr_time`       | int64     | Scheduled arrival time in local format (hhmm)                                       |
| `arr_time`           | float64   | Actual arrival time in local format (hhmm)                                          |
| `arr_delay`          | float64   | Arrival delay calculated in minutes (negative value indicates early arrival)        |
| `cancelled`          | float64   | Binary indicator flag tracking flight status (0.0 = No, 1.0 = Yes)                  |
| `cancellation_code`  | object    | Specific reason identifier code for the cancellation (A, B, C, D)                    |
| `diverted`           | float64   | Binary indicator flag tracking flight diversion (0.0 = No, 1.0 = Yes)               |
| `crs_elapsed_time`   | float64   | Scheduled total gate-to-gate travel time in minutes                                 |
| `actual_elapsed_time`| float64   | Actual recorded gate-to-gate travel time in minutes                                 |
| `air_time`           | float64   | Net flight time spent strictly airborne in minutes                                  |
| `distance`           | float64   | Total distance separating origin and destination airports in miles                  |
| `carrier_delay`      | float64   | Delay time directly caused by the airline operator in minutes                       |
| `weather_delay`      | float64   | Delay time caused by hazardous meteorological conditions in minutes                 |
| `nas_delay`          | float64   | Delay time caused by National Aviation System constraints in minutes               |
| `security_delay`     | float64   | Delay time caused by security line breaches or re-boarding events                   |
| `late_aircraft_delay`| float64   | Delay

# 📝 **2. Library Choices**

## Selected Libraries

Three libraries were selected for this assignment: **Pandas** as the baseline library and **Dask** and **Polars** as the two scalable libraries.

## **Why Dask and Polars?**

| Factor | Pandas | Dask | Polars |
| :--- | :--- | :--- | :--- |
| Speed | Moderate | Slow on single node | Fastest |
| Memory Efficiency | Loads all into RAM | Partition-based | Rust-managed |
| Ease of Use | Easiest | Moderate | Moderate |
| Scalability | Limited to RAM | Distributed | Single-node |
| Best For | Small-medium data | Distributed clusters | Large single-node data |

<br>

**Pandas (Baseline Library)**

Pandas is selected as the compulsory baseline library as it is the most widely used data processing library in Python. It provides a simple and familiar API for loading, inspecting, and processing structured data. However, Pandas loads the entire dataset into RAM at once using a single thread, making it memory-intensive and slow for large datasets exceeding available system RAM.

**Dask (Scalable Library 1)**

Dask was selected because it extends Pandas with parallel and distributed computing capabilities. Dask uses lazy evaluation — it builds a task graph without loading data immediately, only executing when `.compute()` is called. This allows it to process datasets larger than available RAM by splitting them into partitions across multiple CPU cores, making it suitable for large-scale distributed workloads.

**Polars (Scalable Library 2)**

Polars was selected because it is built entirely in Rust, offering significantly faster execution than Pandas. Polars uses a vectorised columnar execution engine with SIMD (Single Instruction Multiple Data) CPU instructions, allowing it to process entire columns simultaneously. Its architecture makes it highly efficient for large single-machine datasets where speed is the priority.

These three libraries cover different big data scenarios, from simple prototyping with Pandas, to distributed processing with Dask, to high-performance single-machine processing with Polars.

# 📝 **3. Data Loading and Inspection**

## 🔹 **Loading Strategy**
The data loading stage is structured into three main components: environment configuration, an automated download/extraction pipeline, and an unoptimized baseline execution benchmark.
1. Environment & API Configuration


```
os.environ['KAGGLE_API_TOKEN'] = "KGAT_5653b27870231087291d5cda1e303d2c"
LOCAL_FILE = "flight_data_2024.csv"
```
Instead of forcing the user to manually upload a kaggle.json file or use a separate configuration step, this line passes the API token directly into the system's environment variables. This lets the notebook talk to Kaggle's servers automatically.The file name define as `LOCAL_FILE` so the script knows what to look for on the disk.

2. Automated Directory Verification and Extraction


```
if not os.path.exists(LOCAL_FILE):
    print("Dataset not found locally. Initiating automated cloud-to-cloud API download...")
    !kaggle datasets download -d hrishitpatil/flight-data-2024
    with zipfile.ZipFile("flight-data-2024.zip", 'r') as zip_ref:
        zip_ref.extractall(".")
    print("Extraction complete! Dataset is ready.")
else:
    print("Dataset already exists in workspace. Skipping download.")
```
This logic operates as an automated gatekeeper to prevent redundant data transfers. It scans the local storage to verify if the uncompressed 1.6 GB CSV file is present.

*   If the file is **absent**, the script automatically runs a command to pull the zipped dataset down from Kaggle and uses Python's built-in `zipfile` library to unzip it right away.

*   If the file is **areadly exist** in the environment, the download sequence is completely bypassed, saving network bandwidth and execution time.

3. Measuring the Baseline Performance (Pandas Load)


```
tracemalloc.start()
start = time.time()

df = pd.read_csv(DATASET_PATH)
pandas_mean = df['arr_delay'].mean()

end = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
```
This segment executes a standard, unoptimized file load using Pandas (`pd.read_csv`). To collect precise hardware utilization metrics required for the subsequent comparative analysis, the execution code is wrapped inside two tracking utilities:



*   `time.time()` captures the total clock duration in seconds required to parse the file from disk into RAM.
*   `tracemalloc` monitors low-level system memory behaviors to capture the maximum RAM allocation spike encountered during data ingestion.


This creates the essential performance baseline needed to measure the optimization efficiency of the upcoming big data strategies.


## 🔹 **Inspect Strategy**
This inspection part is used to check the structure of the dataset, look at the data rows, find the total size, and locate any missing values.

1. Checking the Top 5 Rows


```
print("First 5 rows of the dataset:")
display(df.head())
```
| | year | month | day_of_month | day_of_week | fl_date | op_unique_carrier | op_carrier_fl_num | origin | origin_city_name | origin_state_nm | ... | diverted | crs_elapsed_time | actual_elapsed_time | air_time | distance | carrier_delay | weather_delay | nas_delay | security_delay | late_aircraft_delay |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **0** | 2024 | 1 | 1 | 1 | 2024-01-01 | 9E | 4814.0 | JFK | New York, NY | New York | ... | 0.0 | 136.0 | 122.0 | 84.0 | 509.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| **1** | 2024 | 1 | 1 | 1 | 2024-01-01 | 9E | 4815.0 | MSP | Minneapolis, MN | Minnesota | ... | 0.0 | 130.0 | 114.0 | 88.0 | 622.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| **2** | 2024 | 1 | 1 | 1 | 2024-01-01 | 9E | 4817.0 | JFK | New York, NY | New York | ... | 0.0 | 106.0 | 90.0 | 61.0 | 288.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| **3** | 2024 | 1 | 1 | 1 | 2024-01-01 | 9E | 4817.0 | RIC | Richmond, VA | Virginia | ... | 0.0 | 111.0 | 76.0 | 51.0 | 288.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| **4** | 2024 | 1 | 1 | 1 | 2024-01-01 | 9E | 4818.0 | DTW | Detroit, MI | Michigan | ... | 0.0 | 79.0 | 70.0 | 45.0 | 237.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |


2. Checking Column Names and Data Types

```
display(df.info())
```
![Dataset information](images/df(info).png)

3. Getting the Exact Size of the Data

```
print(f"\nDataset Shape:\nRows: {df.shape[0]}, Columns: {df.shape[1]}")
```
![Dataset shape](images/shape.png)

4. Counting Missing Values
```
print(df.isnull().sum())
```
![Count Null](images/null.png)
# 📝**4. Big Data Handling Strategies**

## 📉 **4.1 Load Less Data**
**Code:**
```
load to targeted analysis domains
tracemalloc.start()
start_s1 = time.time()

target_columns = ['month', 'op_unique_carrier', 'origin', 'dest', 'dep_delay', 'arr_delay']
df_less = pd.read_csv(DATASET_PATH, usecols=target_columns)

end_s1 = time.time()
_, peak_s1 = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Strategy 1 Load Time : {end_s1 - start_s1:.2f}s")
print(f"Strategy 1 Peak Memory: {peak_s1 / 1024**2:.2f} MB")
```
#### **Explanation:**
When working with large datasets, it is often unnecessary to load all available columns into memory. By selecting only the relevant columns required for the analysis task, memory usage and load time can be significantly reduced.

#### **Implementation Summary:**
Only these columns were loaded from the CSV:
`month`, `op_unique_carrier`, `origin`, `dest`, `dep_delay`, `arr_delay`

#### **Output:**
![Strategy 1 output](images/Strategy1.png)

**Performance Insight:** Dropping the other 29 unneeded columns allowed the dataset to load much faster and kept the peak RAM footprint significantly lower than the full baseline load.

## 📉 **4.2 Chunking**
**Code:**

```
tracemalloc.start()
start_s2 = time.time()

# Process data in chunks to handle workloads without memory spikes
chunk_iterator = pd.read_csv(DATASET_PATH, chunksize=500000, usecols=['arr_delay'])
row_accumulator = 0

for chunk in chunk_iterator:
    # Perform standard light aggregations on current memory block
    row_accumulator += chunk['arr_delay'].count()

end_s2 = time.time()
_, peak_s2 = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Strategy 2 Process Time: {end_s2 - start_s2:.2f}s")
print(f"Strategy 2 Peak Memory : {peak_s2 / 1024**2:.2f} MB")
```
#### **Explanation:**
Loading massive datasets all at once can easily overwhelm system memory and cause runtime crashes. By breaking the file into smaller, fixed-size subsets (chunks), data can be loaded and processed sequentially. This sequential processing stream keeps memory usage uniformly low regardless of how large the total dataset grows.

#### **Implementation Summary:**
The dataset was processed in sequential iterations using these parameters:

* Chunk Size: 500,000 rows per iteration block.

* Target Column Extracted: arr_delay

* Operation: Iterated through the dataset using a for loop to accumulate total counts sequentially.

#### **Output:**
![Strategy 2 output](images/Strategy2.png)

**Performance Insight:** Processing the file block-by-block prevents memory spikes, maintaining a flat and safe memory footprint throughout the execution loop.

## 📉 **4.3 Optimize Data Types**
**Code:**

```
# Define optimized schema properties
optimized_schema = {
    'month': 'int8',
    'day_of_week': 'int8',
    'op_unique_carrier': 'category',
    'origin': 'category',
    'dest': 'category',
    'cancelled': 'int8',
    'distance': 'int16',
    'cancellation_code': 'category'
}
target_cols = list(optimized_schema.keys())

# BEFORE
# Force cancellation_code to 'str' initially to prevent the mixed-type warning
df_before = pd.read_csv(DATASET_PATH, usecols=target_cols, dtype={'cancellation_code': 'str'})

# Capture 'Before' metrics
dtypes_before = df_before.dtypes
mem_by_col_before = df_before.memory_usage(deep=True) / 1024**2
total_mem_before = df_before.memory_usage(deep=True).sum() / 1024**2

# AFTER
tracemalloc.start()
start_s3 = time.time()

# Load and optimize types directly at read-time
df_optimized = pd.read_csv(DATASET_PATH, usecols=target_cols, dtype=optimized_schema)

end_s3 = time.time()
current, peak_s3 = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Capture 'After' metrics
dtypes_after = df_optimized.dtypes
mem_by_col_after = df_optimized.memory_usage(deep=True) / 1024**2
total_mem_after = df_optimized.memory_usage(deep=True).sum() / 1024**2

#Comparison DataFrame
comparison_df = pd.DataFrame({
    'Data Type (Before)': dtypes_before,
    'Data Type (After)': dtypes_after,
    'Memory Before (MB)': mem_by_col_before.drop('Index'),
    'Memory After (MB)': mem_by_col_after.drop('Index')
})

# Calculate individual row reduction percentages
comparison_df['Reduction (%)'] = (1 - (comparison_df['Memory After (MB)'] / comparison_df['Memory Before (MB)'])) * 100

print("\n--- SCHEMA & MEMORY COMPARISON TABLE ---")
display(comparison_df.round(2))
print("-" * 60)

print(f"Total Memory BEFORE Optimization : {total_mem_before:.2f} MB")
print(f"Total Memory AFTER Optimization  : {total_mem_after:.2f} MB")
print(f"Overall Dataset RAM Reduction    : {100 * (1 - total_mem_after / total_mem_before):.1f}%")
print(f"Optimized Read Execution Time    : {end_s3 - start_s3:.2f}s")
print(f"Peak Runtime System Memory Spike : {peak_s3 / 1024**2:.2f} MB")
```
#### **Explanation:**
By default, Pandas assigns heavy 64-bit memory types (like int64, float64, or generic object strings) to newly loaded columns, which wastes significant system RAM. Downcasting numbers to smaller bit sizes (such as int8 or int16) and converting repeating text strings into categorical codes drastically shrinks the memory footprint right at read-time.

#### **Implementation Summary:**
An optimized schema blueprint was defined and enforced directly inside pd.read_csv:

* Downcasted Integers (int8 / int16): Applied to month, day_of_week, cancelled, and distance.

* Categorical Mapping (category): Applied to highly repetitive text fields including op_unique_carrier, origin, dest, and cancellation_code.

#### **Output:**
Schema & Memory Comparison Table

| Column Name | Data Type (Before) | Data Type (After) | Memory Before (MB) | Memory After (MB) | Reduction (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `month` | int64 | int8 | 54.01 | 6.75 | 87.50% |
| `day_of_week` | int64 | int8 | 54.01 | 6.75 | 87.50% |
| `op_unique_carrier` | object | category | 344.31 | 6.75 | 98.04% |
| `origin` | object | category | 351.06 | 13.53 | 96.15% |
| `dest` | object | category | 351.06 | 13.53 | 96.15% |
| `cancelled` | int64 | int8 | 54.01 | 6.75 | 87.50% |
| `cancellation_code` | object | category | 217.69 | 6.75 | 96.90% |
| `distance` | float64 | int16 | 54.01 | 13.50 | 75.00% |


* Total Memory BEFORE Optimization: 1,480.15 MB
* Total Memory AFTER Optimization: 74.31 MB
* Overall Dataset RAM Reduction: 95.0%
* Optimized Read Execution Time: 14.98s
* Peak Runtime System Memory Spike: 696.87 MB

**Performance Insight:** By shrinking the "memory boxes" before the data is loaded, columns like `origin` and `dest` see a massive **RAM drop of over 80% to 90%**. This optimization allows the computer to process all 7 million rows at maximum speed while using only a small fraction of the system memory.

## 📉 **4.4 Sampling**
**Code:**

```
tracemalloc.start()
start_s4 = time.time()

#Pull a statistically valid 10% random sample from our full DataFrame
# 'random_state' ensures that the exact same rows are picked every time run it
df_sampled = df.sample(frac=0.1, random_state=50)

end_s4 = time.time()
current, peak_s4 = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Sampling Execution Time : {end_s4 - start_s4:.4f}s ")
print(f"Peak System Memory Spike: {peak_s4 / 1024**2:.2f} MB")
print(f"Original Dataset Shape  : {df.shape}")
print(f"Sampled Dataset Shape   : {df_sampled.shape}")
```
#### **Explanation:**
During the initial phases of data exploration or model prototyping, analyzing millions of rows is unnecessary and slows down development. By extracting a smaller, statistically representative random fraction of the dataset, code logic can be tested and verified instantly while using minimal system resources.This approach provides the benefit of rapid prototyping, allowing developers to experiment with complex visual charts and analytical pipelines with zero lag before deploying them on the entire dataset.

#### **Implementation Summary:**
A random subset was extracted from the main loaded DataFrame using these parameters:

* Sampling Fraction (`frac`): 0.1 (Extracts a random 10% sample of the total records).

* Reproducibility Key (`random_state`): Set to 50 to ensure the exact same rows are picked every time the notebook is executed.

The method successfully isolates a smaller data shape for high-speed prototyping while maintaining the statistical characteristics of the full dataset.

#### **Output:**
![Strategy 4 output](images/Strategy4.png)

**Performance Insight:** By reducing the data size down to 10% of the original records, operations run almost instantly. This strategy allows developers to build and test analytical pipelines rapidly with near-zero memory strain before scaling up to the full dataset.

## 📉 **4.5 Parallel Processing**
**Code:**

```
import dask.dataframe as dd

tracemalloc.start()
start_s5 = time.time()

# Initiate the parallel framework blueprint
dask_df = dd.read_csv(DATASET_PATH, dtype={'cancellation_code': 'object'})

# Force execution across CPU cores silently (No print output assigned)
dask_mean_delay = dask_df['arr_delay'].mean().compute()

end_s5 = time.time()
current, peak_s5 = tracemalloc.get_traced_memory()
tracemalloc.stop()

# 3. ONLY print your hardware performance metrics
print(f"Execution time : {end_s5 - start_s5:.2f}s")
print(f"Peak memory    : {peak_s5 / 1024**2:.2f} MB")
print(f"Partitions used: {dask_df.npartitions}")
```
#### **Explanation:**
Dask enables parallel processing by breaking large datasets into smaller block partitions and processing them concurrently across multiple CPU cores. This architecture provides the massive benefit of horizontal scalability, allowing data handling to bypass the single-threaded limits of traditional pandas. Furthermore, Dask manages hardware memory much more efficiently by lazy-loading the data and building an execution graph. For instance, when calculating the mean arrival delay, the engine does not load the whole dataset; it analyzes individual partitions in parallel, calculates their internal metrics, and combines them into a final average, avoiding memory overload.

#### **Implementation Summary:**
* `dd.read_csv()` initializes a lazy loading blueprint of the dataset, mapping its partitions across CPU cores without pulling the actual rows into RAM.

* A custom `dtype` parameter is passed for the `cancellation_code` column to prevent mixed-type inference errors during partition scanning.

* The `.compute()` method is explicitly called on the `arr_delay.mean()` calculation to trigger parallel execution across all CPU cores, processing multiple partitions concurrently to extract the final average arrival delay.

#### **Output:**
![Strategy 5 output](images/Strategy5.png)

**Performance Insight:** While coordinating multiple data partitions can add a small time overhead, Dask keeps memory usage completely safe. It splits the workload across multiple CPU cores to compute complex metrics , streaming data chunk-by-chunk so the system never encounters an "Out of Memory" crash.

# 📝 **5. Comparative Analysis**

## 📊 **5.1: Evaluation of Big Data Handling Strategies**

### **5.1.1 Performance Metric Summary Table and Visuals**

| Evaluation Strategy | Execution Time (s) | Peak Memory Usage (MB) | Execution Speedup (vs. Baseline) | Memory Reduction % (vs. Baseline) |
| :--- | :---: | :---: | :---: | :---: |
| **Pandas Baseline** | 49.41 | 6,185.09 | *Reference* | *Reference* |
| **1. Load Less Data** | 14.70 | 659.68 | ~3.36x Faster | 89.34 |
| **2. Chunking** | 11.65 | **12.28** | ~4.24x Faster | **99.80** |
| **3. Data Type Optimisation** | 28.47 | 696.89 | ~1.74x Faster | 88.73 |
| **4. Sampling** | **1.82** | 248.45 | **~27.15x Faster** | 95.98 |
| **5. Parallel Processing**| 155.13 | 843.41 | 0.32x Slower | 86.36 |

![execution chart](images/exe.png)
![memory usage chart](images/memory.png)
---

### **5.1.2 Key Metrics Analysis**
#### 1. Execution Time Analysis
* **Fastest Speed:** **Strategy 4 Sampling method** achieved the absolute lowest runtime at just **1.82 seconds**. By isolating a 10% representative slice of the dataset, it eliminated 90% of the computational overhead, providing a massive **27.15x speedup** over the baseline.
* **The Parallel Bottleneck:** **Strategy 5 parallel processing** recorded the longest runtime at **155.13 seconds**, which is roughly 3 times slower than the single-threaded Pandas baseline. Dask was slower because managing 20 different data pieces and planning the parallel tasks created too much administrative overhead for a single computer to handle efficiently.


#### 2. Peak Memory Usage Analysis
* **Least Memory:** **Strategy 2 Chunking** demonstrated unparalleled resource efficiency, peaking at an incredibly low **12.28 MB of RAM**. Because it sequentially streams data in blocks of 250,000 rows rather than dumping the entire file into memory at once, it achieved a spectacular **99.80% reduction** in memory consumption compared to the baseline.
* **The Baseline Vulnerability:** The **Unoptimized Baseline** choked systems with a massive peak memory footprint of **6,185.09 MB**. This extreme resource draw represents a dangerous threshold in limited cloud environments, taking up over half of the runtime's capacity just to read the raw data before running any processing.

## 📊 **5.2: Cross-Library Benchmarking**

### 📊 **5.2.1: Memory Usage**
**Code:**
```
libraries = ['Pandas', 'Dask', 'Polars']
memory = [pandas_peak_memory, peak_s5 / 1024**2, peak_polars / 1024**2]

print(f"{'Library':<20} {'Peak Memory (MB)'}")
print("-" * 40)
for lib, m in zip(libraries, memory):
    note = " *" if lib == "Polars" else ""
    print(f"{lib:<20} {m:.2f}{note}")
print("\n* Polars memory is Python-level only (Rust-managed memory not captured)")
```
#### **Explanation:**
Memory usage is one of the most critical metrics when evaluating big data libraries. Each library was tested loading and processing the same 1.22 GB Flight Delay Dataset 2024 using `tracemalloc` to capture the peak RAM allocation spike during execution.

#### **Implementation Summary:**
* **Tool used:** `tracemalloc` — captures peak RAM allocation in megabytes.
* **Operation measured:** Full dataset load + mean arrival delay computation.
* **All three libraries** performed the same task on the same dataset for a fair comparison.


#### **Output:**
| Library | Peak Memory (MB) | vs Pandas Baseline |
| :--- | :--- | :--- |
| **Pandas** | 6,185.09 MB | Baseline |
| **Dask** | 843.41 MB | 86.4% less RAM |
| **Polars** | 0.02 MB* | N/A (see note) |

<br>

![Execution Time Comparison](images/memory_usage_chart.png)

<br>

* Notes: Polars memory tracked by `tracemalloc` is near zero because Polars manages memory internally through Rust — Python cannot observe it. The actual RAM used by Polars is not captured by this measurement tool.


#### **Performance Insight:**
Pandas consumed the most memory at **6,185.09 MB**, nearly loading the entire dataset into RAM at once. Dask significantly reduced this to **843.41 MB** by lazily partitioning the dataset across 20 blocks and processing them without fully materializing the whole file in memory. Polars, while unmeasurable via `tracemalloc`, is architecturally designed to use Apache Arrow columnar memory format which is highly memory-efficient by nature.


### 📊 **5.2.2 Execution Time**
**Code:**
```
libraries = ['Pandas', 'Dask', 'Polars']
times = [pandas_load_time, end_s5 - start_s5, end_polars - start_polars]

print(f"{'Library':<20} {'Execution Time (s)'}")
print("-" * 40)
for lib, t in zip(libraries, times):
    print(f"{lib:<20} {t:.2f}s")
```
#### **Explanation:**
Execution time measures how long each library takes to fully load and process the dataset. The same operation — loading the full CSV and computing the mean arrival delay — was executed across all three libraries using `time.time()` to capture total wall-clock duration in seconds.

#### **Implementation Summary:**
* **Tool used:** `time.time()` — captures total wall-clock execution duration in seconds.
* **Operation measured:** Full CSV load + mean arrival delay computation (`arr_delay.mean()`).
* The same operation was run on all three libraries to ensure a fair and consistent comparison.

#### **Output:**

| Library | Execution Time (s) | vs Pandas Baseline |
| :--- | :--- | :--- |
| **Pandas** | 37.21s | Baseline |
| **Dask** | 155.13s | 4.2x slower  |
| **Polars** | 12.78s | 2.9x faster  |

<br>

![Execution Time Comparison](images/execution_chart.png)

<br>

#### **Performance Insight:**
Polars was the fastest library at **12.78 seconds**, outperforming even the Pandas baseline by nearly 3x. This is attributed to Polars' Rust-based engine and multi-threaded query execution which processes column data in parallel without any Python overhead. Dask was significantly slower at **155.13 seconds** due to the coordination overhead of splitting the dataset into 20 partitions and managing parallel workers on Google Colab's limited CPU environment. On a production-grade multi-core server, Dask's performance would improve substantially


### 🔍 **5.2.3 Critical Discussion**

#### **Why is Polars the Fastest?**
Polars is built entirely in **Rust**, a systems programming language that executes at near-machine-code speed with zero garbage collection overhead. Unlike Pandas, which processes data through Python's interpreter one operation at a time, Polars uses a **vectorized columnar execution engine** that processes entire columns simultaneously using SIMD (Single Instruction Multiple Data) CPU instructions. This architectural difference explains the nearly 3x speed advantage over Pandas on a 7-million-row dataset. As discussed in Section 5.2.1, Polars' actual memory consumption is estimated to be higher than Dask in absolute terms. However, this reveals an important insight — **higher memory consumption does not necessarily translate to slower performance**. Its Rust-based vectorised execution engine enables substantially faster processing, demonstrating that memory usage and execution speed are independent metrics that must be evaluated separately.

#### **Why is Dask Slower on Colab?**
Dask's parallel framework is designed for **distributed computing environments** with many CPU cores or multiple machines. On Google Colab, which provides limited CPU resources (typically 2 cores), the overhead of splitting the dataset into 20 partitions, scheduling tasks across workers and merging results outweighs the benefit of parallelism. In a real production environment with 16–32 CPU cores, Dask would likely outperform both Pandas and Polars on this dataset size.

#### **Why Does Pandas Use 6 GB of RAM?**
Pandas loads the **entire dataset into RAM at once** using its default `int64` and `object` data types, which are memory-inefficient for large datasets. With 7 million rows and 35 columns of mixed types, this results in a massive 6,185 MB memory spike. This makes Pandas unsuitable for datasets larger than available system RAM without applying optimisation strategies such as those demonstrated in Task 3.

#### **Processing Efficiency Comparison:**

| Factor | Pandas | Dask | Polars |
| :--- | :--- | :--- | :--- |
| Ease of Use |Easiest | Medium | Medium |
| Syntax Familiarity | Very familiar | Similar to Pandas | Different syntax |
| Special Workarounds Needed | RAM crash — required `del df` and `gc.collect()` to free memory | `dtype` fix for mixed columns | `infer_schema_length` needed |
| Memory Measurability | Full tracemalloc support | Full tracemalloc support | Rust memory not captured |
| Scalability | Limited to RAM size | Scales beyond RAM | Very fast on single node |
| Best For | Small-medium datasets | Datasets larger than RAM | Large single-node datasets |

<br>

**Performance Insight:** Pandas remains the most beginner-friendly option with the richest ecosystem, but it is fundamentally limited by available system RAM. Dask provides true horizontal scalability and its real strength emerges on distributed cluster environments. Polars offers the best single-machine performance but has a steeper learning curve and a memory measurement limitation when benchmarking inside Python environments.

# 📝 **6. Conclusion**

In this assignment, the 1.22 GB Flight Delay Dataset 2024 containing 7 million rows and 35 columns was used to demonstrate five practical big data handling strategies, alongisde with a comparison between three popular libraries: Pandas, Dask and Polars.

Among the five strategies, **Chunking** achieved the lowest peak memory usage at only **12.28 MB**, making it the most memory-efficient method because the dataset was processed in smaller sequential blocks of 500,000 rows. Meanwhile, **Sampling** recorded the fastest execution time at **1.82 seconds**, showing that it is highly suitable for quick testing and exploratory analysis. **Data Type Optimisation** provided the biggest memory reduction, successfully decreasing RAM usage by around **95%**, from 1,480 MB to only 74 MB without removing any rows from the dataset.

For the library comparison, **Polars** showed the best performance for single-machine execution by completing the loading and computation process in just **12.78 seconds**, which was almost three times faster than Pandas. Its Rust-based architecture and columnar processing engine make it a strong choice for high-performance data processing pipelines. Although **Dask** performed slower in the Colab environment due to limited CPU resources, it is still the most scalable option for handling datasets that exceed available RAM or require distributed processing across multiple machines.

Overall, this assignment shows that choosing the right strategy and library is important in big data processing. Combining **Data Type Optimisation** with **Chunking** is recommended to reduce memory usage efficiently, while **Polars** is more suitable for faster single-node performance. In contrast, **Dask** is a better option for large-scale distributed workloads and future scalability.

# 📝 **7. Reflection**

Throughout the course of this assignment, a deeper understanding of how different libraries and strategies handle large-scale data processing under real memory and time constraints was developed.

The most unexpected finding was **Dask's underperformance on Google Colab**. As a parallel processing framework, Dask was expected to significantly outperform Pandas. However, the result of 155 seconds versus Pandas' 37 seconds proved otherwise. Further investigation revealed that Dask's parallel scheduling overhead is only beneficial when sufficient CPU cores are available. Google Colab's limited CPU environment exposed Dask's coordination cost rather than its parallel strength, reinforcing the understanding that **choosing the right tool depends heavily on the execution environment**, not just the dataset size.

Another key insight was the **Polars memory measurement limitation**. The near-zero tracemalloc reading of 0.02 MB initially appeared to be an error. However, this revealed an important concept — Python's memory tracking tools can only observe Python-level memory allocations. Since Polars operates through its own Rust runtime, its memory consumption is effectively invisible to tracemalloc. This highlighted the importance of understanding the underlying architecture of a tool, rather than relying solely on its surface-level API output.

#### **Scalability Discussion:**

| Dataset Size | Recommended Approach |
| :--- | :--- |
| **< 1 GB** | Pandas with Data Type Optimisation is sufficient |
| **1 GB – 10 GB** | Polars for speed; Chunking if RAM is limited |
| **10 GB – 100 GB** | Dask on a multi-core machine; Polars with lazy evaluation |
| **> 100 GB / 1 TB** | Apache Spark on a distributed cluster (e.g. Databricks, AWS EMR) |

As datasets grow beyond 10 GB, single-node solutions such as Pandas and Polars begin to struggle regardless of optimisation strategies applied. At the 100 GB–1 TB scale, distributed frameworks such as **Apache Spark** become necessary, as they distribute both computation and storage across multiple machines. Cloud platforms such as **Amazon Web Services (AWS)**, **Microsoft Azure** and **Google Cloud Platform (GCP)** provide scalable computing environments that can handle petabyte-scale datasets efficiently.

This assignment provided a foundational understanding of the big data processing landscape and the practical trade-offs between ease of use, speed, memory efficiency and scalability are the knowledge that will directly applicable to real-world data engineering and data science practices.

## 8. References

1. [Flight Delay Dataset 2024 on Kaggle](https://www.kaggle.com/datasets/hrishitpatil/flight-data-2024)
2. [Pandas Documentation](https://pandas.pydata.org/docs/)
3. [Dask DataFrame Documentation](https://docs.dask.org/en/stable/dataframe.html)
4. [Polars Documentation](https://docs.pola.rs/)
5. [Matplotlib Documentation](https://matplotlib.org/stable/index.html)

