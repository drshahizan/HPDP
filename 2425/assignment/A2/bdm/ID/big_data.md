# Assignment 2: Big Data Handling and Optimization Using 2009 Airline On Time Data 
## 👥 Group Members

| Name               | Matric Number |
|--------------------|---------------|
| Muhammad Iman Firdaus Bin Baharuddin        | A22EC0216       |
| Muhammad Ariff Danish Bin Hashnan         | A22EC0204       |

---

## 📌 Project Overview
---

## 📌 Key Observations
### ✅ Benefits & Limitations of Each Method
---

## 🧪 Tasks & Implementation

### Task 1: Dataset Selection
---
- **Dataset Name:** Data Expo 2009: Airline On Time Data  
- **Source:** [Kaggle - wenxingdi/data-expo-2009-airline-on-time-data](https://www.kaggle.com/datasets/wenxingdi/data-expo-2009-airline-on-time-data)  
- **Domain:** Transportation / Aviation  
- **Used File:** `2007.csv`  
- **File Size:** ~2.12 GB  
- **Dimensions:** 7,453,215 rows × 29 columns  
- **Access Method:** Kaggle JSON API

### 🧾 Dataset Schema (2007.csv)

| Column Name           | Data Type | Description |
|------------------------|-----------|-------------|
| Year                  | int64     | Year of the flight (e.g., 2007) |
| Month                 | int64     | Month of the flight (1-12) |
| DayofMonth            | int64     | Day of the month the flight took place |
| DayOfWeek             | int64     | Day of the week (1=Monday, 7=Sunday) |
| DepTime               | float64   | Actual departure time (local, hhmm) |
| CRSDepTime            | int64     | Scheduled departure time (local, hhmm) |
| ArrTime               | float64   | Actual arrival time (local, hhmm) |
| CRSArrTime            | int64     | Scheduled arrival time (local, hhmm) |
| UniqueCarrier         | object    | Airline carrier code |
| FlightNum             | int64     | Flight number |
| TailNum               | object    | Aircraft tail number |
| ActualElapsedTime     | float64   | Total flight time in minutes |
| CRSElapsedTime        | float64   | Scheduled flight time in minutes |
| AirTime               | float64   | Actual time spent in the air |
| ArrDelay              | float64   | Arrival delay in minutes |
| DepDelay              | float64   | Departure delay in minutes |
| Origin                | object    | Origin airport code |
| Dest                  | object    | Destination airport code |
| Distance              | int64     | Distance flown (in miles) |
| TaxiIn                | int64     | Time spent taxiing in (minutes) |
| TaxiOut               | int64     | Time spent taxiing out (minutes) |
| Cancelled             | int64     | 1 if the flight was cancelled, 0 otherwise |
| CancellationCode      | object    | Reason for cancellation (A = carrier, B = weather, C = NAS, D = security) |
| Diverted              | int64     | 1 if the flight was diverted, 0 otherwise |
| CarrierDelay          | int64     | Delay caused by the airline (minutes) |
| WeatherDelay          | int64     | Delay caused by weather (minutes) |
| NASDelay              | int64     | Delay caused by the National Airspace System (minutes) |
| SecurityDelay         | int64     | Delay caused by security issues (minutes) |
| LateAircraftDelay     | int64     | Delay caused by a late-arriving aircraft (minutes) |



## 🧠 Objective

To demonstrate effective big data handling by:
- Working with a multi-million-row dataset
- Preparing the dataset for further analysis
- Exploring patterns and challenges in airline on-time performance data

## 🛠️ Tools & Technologies

- Python / Pandas
- Jupyter Notebook
- Kaggle API
- (You can add more tools here as you progress)
### Task 2: Load and Inspect Data
---
In this task, we focus on importing the large dataset into the environment, tracking performance metrics (execution time and memory usage), and performing a basic inspection of the data structure.


- Import relevant libraries/frameworks
- Load the dataset into Google Colab
- Calculate execution time and memory used

Code Snippet 
```python
import pandas as pd
import time
import psutil
import os

# Start time and memory usage
start_time = time.time()
process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss / 1024 ** 2

# Load the dataset
file_path = '/content/2007.csv'
df = pd.read_csv(file_path)

# End time and memory usage
end_time = time.time()
end_memory = process.memory_info().rss / 1024 ** 2

# Calculate execution time and memory usage
execution_time_normal = end_time - start_time
memory_used_normal = end_memory - start_memory

print(f"Execution Time: {execution_time_normal:.2f} seconds")
print(f"Memory Used: {memory_used_normal:.2f} MB")
```

The output 
```
Performance Metrics
Execution Time: 32.53 seconds
Memory Used: 1636.44 MB
```

- Find relevant information(shape, columns names, datatypes)
```
print("Shape (Rows, Columns):")
print(df.shape)

print()
print("nColumn Names:")
print(df.columns.tolist())

print()
print("nData Types:")
print(df.dtypes)
```

The Output : 
```
Shape (Rows, Columns):
(7453215, 29)

nColumn Names:
['Year', 'Month', 'DayofMonth', 'DayOfWeek', 'DepTime', 'CRSDepTime', 'ArrTime', 'CRSArrTime', 'UniqueCarrier', 'FlightNum', 'TailNum', 'ActualElapsedTime', 'CRSElapsedTime', 'AirTime', 'ArrDelay', 'DepDelay', 'Origin', 'Dest', 'Distance', 'TaxiIn', 'TaxiOut', 'Cancelled', 'CancellationCode', 'Diverted', 'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay']

nData Types:
Year                   int64
Month                  int64
DayofMonth             int64
DayOfWeek              int64
DepTime              float64
CRSDepTime             int64
ArrTime              float64
CRSArrTime             int64
UniqueCarrier         object
FlightNum              int64
TailNum               object
ActualElapsedTime    float64
CRSElapsedTime       float64
AirTime              float64
ArrDelay             float64
DepDelay             float64
Origin                object
Dest                  object
Distance               int64
TaxiIn                 int64
TaxiOut                int64
Cancelled              int64
CancellationCode      object
Diverted               int64
CarrierDelay           int64
WeatherDelay           int64
NASDelay               int64
SecurityDelay          int64
LateAircraftDelay      int64
dtype: object
```


### Task 3: Apply Big Data Handling Strategies
---

In this part, we used five strategies to work with our large dataset to observe the result of the performance of using different strategies applying to handle big dataset. These methods help save time, memory, and make processing faster.

#### 1. Load Less Data
Instead of loading the entire dataset at once, we can read only the necessary columns or rows. This reduces memory usage and speeds up loading time, especially during initial exploration or debugging.
```
columns = [
    'Year', 'Month', 'DayOfWeek', 'DepTime', 'ArrTime',
    'DepDelay', 'ArrDelay', 'UniqueCarrier', 'Origin', 'Dest',
    'Distance', 'Cancelled', 'Diverted'
]

# Start Time
start_time = time.time()
process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss / 1024 ** 2

df1 = pd.read_csv(file_path, usecols=columns)

# End Time
end_time = time.time()
end_memory = process.memory_info().rss / 1024 ** 2

execution_time_1 = end_time - start_time
memory_used_1 = end_memory - start_memory

print(f"Execution Time: {execution_time_1:.2f} seconds")
print(f"Memory Used: {memory_used_1:.2f} MB")
```

The Output :
```
Execution Time: 15.02 seconds
Memory Used: 742.20 MB
```

#### 2. Use Chunking
Chunking involves reading the data in smaller pieces (chunks) instead of all at once. It allows processing large files that wouldn't otherwise fit in memory. This is useful for filtering, aggregating, or saving summarized results from big files.
```
print("Original shape:", df.shape)
print()

chunksize = 100000
chunk_iter = pd.read_csv(file_path, chunksize=chunksize)

# Start Time
start_time = time.time()
process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss / 1024 ** 2

for i, chunk in enumerate(chunk_iter):
    print(f"Chunk {i+1}: {chunk.shape}")
    # Example: summarize a column
    print(chunk['Year'].value_counts().head())
    print()
    if i == 2:
        break

# End Time
end_time = time.time()
end_memory = process.memory_info().rss / 1024 ** 2

execution_time_2 = end_time - start_time
memory_used_2 = end_memory - start_memory

print(f"Execution Time: {execution_time_2:.2f} seconds")
print(f"Memory Used: {memory_used_2:.2f} MB")
```

The Output : 
```
Original shape: (7453215, 29)

Chunk 1: (100000, 29)
Year
2007    100000
Name: count, dtype: int64

Chunk 2: (100000, 29)
Year
2007    100000
Name: count, dtype: int64

Chunk 3: (100000, 29)
Year
2007    100000
Name: count, dtype: int64

Execution Time: 0.76 seconds
Memory Used: 1.05 MB
```

#### 3. Optimize Data Types
Changing data types to more memory-efficient formats (e.g., converting float64 to float32 or object to category) can significantly reduce memory consumption and speed up processing.
```
dtypes_optimized = {
    'Year': 'int16',
    'Month': 'int8',
    'DayofMonth': 'int8',
    'DayOfWeek': 'int8',
    'DepTime': 'float32',
    'CRSDepTime': 'int16',
    'ArrTime': 'float32',
    'CRSArrTime': 'int16',
    'UniqueCarrier': 'category',
    'FlightNum': 'int32',
    'TailNum': 'category',
    'ActualElapsedTime': 'float32',
    'CRSElapsedTime': 'float32',
    'AirTime': 'float32',
    'ArrDelay': 'float32',
    'DepDelay': 'float32',
    'Origin': 'category',
    'Dest': 'category',
    'Distance': 'int16',
    'TaxiIn': 'int8',
    'TaxiOut': 'int8',
    'Cancelled': 'int8',
    'CancellationCode': 'category',
    'Diverted': 'int8',
    'CarrierDelay': 'float32',
    'WeatherDelay': 'float32',
    'NASDelay': 'float32',
    'SecurityDelay': 'float32',
    'LateAircraftDelay': 'float32'
}

# Start Time
start_time = time.time()
process = psutil.Process(os.getpid())
start_memory = process.memory_info().rss / 1024 ** 2

df3 = pd.read_csv(file_path, dtype=dtypes_optimized)

# End time
end_time = time.time()
end_memory = process.memory_info().rss / (1024 * 1024)  # MB

execution_time_3 = end_time - start_time
memory_used_3 = end_memory - start_memory

print(df3.info())
print(df3.head())

print(f"Execution Time: {execution_time_3:.2f} seconds")
print(f"Memory Used: {memory_used_3:.2f} MB")
```

The Output : 
```
[5 rows x 29 columns]
Execution Time: 34.30 seconds
Memory Used: 460.50 MB
```

#### 4. Sampling
Sampling means analyzing a small, representative subset of the dataset instead of the full dataset. It helps in quicker testing and prototyping of models and visualizations without compromising too much on insights.
```
# Start time
process = psutil.Process(os.getpid())
start_time = time.time()
start_memory = process.memory_info().rss / (1024 * 1024)  # MB

sample_fraction = 0.01  # 1%
df4 = pd.read_csv(file_path).sample(frac=sample_fraction, random_state=42)

# End time
end_time = time.time()
end_memory = process.memory_info().rss / (1024 * 1024)  # MB

print(df4.head())
print(f"Shape of Sampled Data: {df4.shape}")

execution_time_4 = end_time - start_time
memory_used_4 = end_memory - start_memory

print(f"Execution Time: {execution_time_4:.2f} seconds")
print(f"Memory Used: {memory_used_4:.2f} MB")
```

The Output : 
```
Shape of Sampled Data: (74532, 29)
Execution Time: 36.62 seconds
Memory Used: -3.36 MB
```

#### 5. Parallel Processing with Dask
Dask allows parallel and distributed computing with a pandas-like interface. It can handle large datasets by breaking them into smaller tasks and executing them in parallel across multiple cores or machines.
```
import dask.dataframe as dd
# Start time
process = psutil.Process(os.getpid())
start_time = time.time()
start_memory = process.memory_info().rss / (1024 * 1024)  # MB

# Load dataset with Dask
df_dask = dd.read_csv(file_path, usecols=columns, assume_missing=True)

df_dask = df_dask.compute()

end_time = time.time()
end_memory = process.memory_info().rss / (1024 * 1024)

# Calculate performance
execution_time_5 = end_time - start_time
memory_used_5 = end_memory - start_memory

print(f"Execution Time: {execution_time_5:.2f} seconds")
print(f"Memory Used: {memory_used_5:.2f} MB")
```

The Output : 
```
Execution Time: 23.13 seconds
Memory Used: 1515.06 MB
```




### Task 4: Comparative Analysis
![image](https://raw.githubusercontent.com/MuhammadImanFirdaus/Photos/refs/heads/main/Screenshot%202025-06-03%20004351.png?token=GHSAT0AAAAAADDVYJY73HAMPXRANPUDRCCE2B54MQQ)

1. Execution Time
Pandas : Completed the task in 34.45 seconds .
Polars : Finished the task in 10.16 seconds , making it the fastest library.
Dask : Executed the task in 32.58 seconds , slightly slower than Polars but faster than Pandas.

2. Memory Usage
Pandas : Consumed 3039.86 MB of memory.
Polars : Used 1949.65 MB , demonstrating significant memory savings compared to Pandas.
Dask : Utilized 1201.98 MB , showing the most efficient memory usage among the three libraries.

📌 Key Observations
 - Polars is the fastest library, showcasing its efficiency in handling large datasets due to its Rust-based implementation.
 - Dask provides scalable computing capabilities while maintaining low memory usage, making it ideal for distributed environments or very large datasets.
 - Pandas , while widely used, struggles with larger-than-GB datasets due to high memory consumption and slower execution times.

## Final Thoughts
This analysis highlights that:

 - Polars excels in speed but uses moderate memory.
 - Dask offers good scalability and low memory usage, making it suitable for distributed 
   computing and very large datasets.
 - Pandas , while versatile, is less efficient for big data processing compared to Polars and 
   Dask.
By selecting the appropriate tool based on specific requirements (e.g., speed, memory, scalability),optimization on data processing workflows can be heightened effectively.
---

### Task 5: Conclusion & Reflection
This assignment provided valuable hands-on experience in managing and optimizing large-scale data processing workflows. Some key takeaways include:

✅ Performance Optimization Techniques
 - Reducing column count (usecols) significantly improves both time and memory efficiency.
 - Data type optimization reduces memory usage by over 70% without losing data fidelity.
 - Chunking is ideal for memory-constrained environments but requires custom logic for full-dataset operations.
 - Sampling is useful during early development but must be used cautiously to avoid misleading insights.
 - Dask enables parallel processing and scalability, especially for files larger than available RAM, though it comes with increased complexity and memory overhead.
   
⚠️ Challenges Faced
 - Measuring accurate memory usage was tricky due to garbage collection and lazy evaluation behavior.
 - Some methods like chunking and Dask require additional logic to perform aggregations or full dataset operations.
 - Type mismatches and missing values required careful preprocessing to ensure smooth execution.

🎯 Thoughts
This exercise highlighted that there is no one-size-fits-all solution when working with big data. The best strategy depends heavily on:

 - The size and structure of the dataset
 - Available system resources (RAM, CPU cores)
 - The goal of the analysis (prototyping vs production)
 - By understanding and applying these techniques, we can make informed decisions about how to handle large-scale data efficiently in real-world scenarios.

📝 Summary

In summary, this assignment emphasized the importance of efficient data handling strategies when working with large datasets. By applying techniques such as selective loading, chunking, data type optimization, sampling, and parallel processing, we can significantly improve performance and reduce resource consumption.

Whether you're analyzing flight delays or tackling any other big data problem, choosing the right approach can make all the difference between a sluggish process and a smooth, scalable workflow.


---
