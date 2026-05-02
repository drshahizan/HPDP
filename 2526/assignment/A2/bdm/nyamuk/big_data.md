# Assignment 2: Mastering Big Data Handling

## Group Members:
<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>Nabil Aflah Boo Binti Mohd Yosuf Boo Yong Chong</td>
    <td>A23CS0252</td>
  </tr>
  <tr>
    <td>Yasmin Batrisyia Binti Zahiruddin</td>
    <td>A23CS0201</td>
  </tr>
</table> 

## 1. Dataset Description
- **Name:** UK Housing Prices Paid </p>
- **Source:** [Kaggle-hm-land-registry](https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid) </p>
- **File size:** 2.41 GB </p>
- **Domain:** Housing </p>
- **Shape:** 22,489,348 rows × 11 columns  </p>

### 📖 Description
This dataset contains comprehensive records of all registered property sales in England and Wales that were sold for full market value. It captures details of reported transactions, legal ownership types, property classifications, and geographical markers. This dataset provide a valuable insights into economic trends, purchasing behaviours, and regional distribution of property values which makes it well-suited for time-series analysis, geospatial mapping, and categorical market trend analysis.

### Data Column Description

| Column Name        | Data Type | Description                                                         |
| ------------------ | --------- | ------------------------------------------------------------------- |
| Transaction unique identifier | object (string) | A unique reference number assigned to each specific sale transaction |
| Price | int64 | the sale price of the property in GBP |
| Date of Transfer | object (date) | The exact date when the sale was completed and the property changed hands |
| Property Type | object | The type of property sold: D= Detached, S= Semi-Detached, T= Terraced, F= Flats/Maisonettes, O= Other |
| Old/New | object | Indicates if the property is newly built (N) or an established residential building (Y) |
| Duration | object | The tenure of the property: F= Freehold, L= Leasehold |
| Town/City | object | The town or city where the property is located |
| Country | object | The country where the property is situated |
| PPDCategory Type | object | Indicates the category of price paid entry: A= Standard price paid entry, B= Additional price paid entry |
| Record Status | object | Indicates the status of the record: A= Addition, C= Change, D= Delete |

## 2. Library Choices
Chosen libraries: </p>
| Library 1 | Library 2 | Library 3 |
|--------- | -----------| ---------- |
| Pandas | Dask | Polars |

- Dask is chosen besides Pandas as it enables to process the data through parallel processing and distributed processing of datasets which divides them into a smaller segments for simultaneous processing. It uses lazy evaluation as it performs calculations only when necessary which leads to reduced memory consumption and increased system operational capacity.

- Polars is chosen as it is a high-performance DataFrame library that is written in Rust which allows to execute the programs more faster while using less memory consumptions. It uses multi-threading method which enables it to perform data operations at a speed that exceeds Pandas when handling large datasets.

## 3. Data Loading and Inspection
<h4> 🔷Load Strategy </h4>
The following steps are taken to efficiently load the dataset in Google Colab: </p>
1. kaggle.json is imported using Google Colab import files feature. </p>

``` python
  from google.colab import files
  files.upload()
```

2. Configured Kaggle API Credentials. </p>

```bash
  !mkdir -p ~/.kaggle
  !cp kaggle.json ~/.kaggle/
  !chmod 600 ~/.kaggle/kaggle.json
```

3. Download the dataset from Kaggle using Kaggle CLI to retrieve dataset directly into Colab. </p>

```bash
  !kaggle datasets download -d hm-land-registry/uk-housing-prices-paid
```

4. Unzipped the dataset file. </p>

```bash
  !unzip uk-housing-prices-paid.zip
```

5. Loaded sample of rows using pd.read_csv() and display first 5 rows of the dataset. </p>

```bash
  df = pd.read_csv('price_paid_records.csv', low_memory=False)
  display(df.head())
  df.info()
```

<h4> 🔷Data Inspection </h4>
Below is the initial loading code and the results of the data inspection. 

#### 📌 First 5 Rows
```python
# Load the dataset
df = pd.read_csv("price_paid_records.csv")

# Display the first 5 rows
df.head(5)
```

![image](https://github.com/yAsmin241/HPDP-A2/blob/e27ef8b724b83bee4fd03356b2bbf082320d2329/Screenshot%202026-05-03%20022530.png)

#### 📐 Shape of the Dataset
```python
print(f"\nDataset Shape:\nRows: {df.shape[0]}, Columns: {df.shape[1]}")
```

![image](https://github.com/yAsmin241/HPDP-A2/blob/ebc86b961c0d93aa6961030f73cb13c65c5857f9/Screenshot%202026-05-03%20023211.png)

#### 🏷️ Column Names and Data Types
```python
display(df.dtypes.to_frame(name='Data Type').T)
```
![image](https://github.com/yAsmin241/HPDP-A2/blob/ad655d7d771f4051c5193e46e3be6004460c3ef6/Screenshot%202026-05-03%20023727.png)

## 4. Big Data Handling Strategies (For each strategy: explanation, code snippet, output or screenshot, and discussion )

### **Part 1: Memory- and Performance-Efficient Techniques**
This part focuses on optimizing data loading using strategies such as selective column loading, chunking, type optimization, sampling, and parallelization.

### 📊 Performance Measurement Setup

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
    # mem_percent_after = (mem_after / total_ram) * 100
    # mem_diff_percent = (mem_diff_mb / total_ram) * 100

    # convert dask to pandas safely
    if isinstance(result, dd.DataFrame):
      result = result.head(100000)

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
**Explanation**:
This code defines a benchmarking wrapper designed to quantify the efficiency of different data-loading methods. It captures a comprehensive snapshot of how a specific function impacts system resources in real-time.

**Implementation Summary**:

* uses the psutil library to identify the current system process and launches a background threading loop.
* Before the target function (func) runs, the code records a "before" timestamp and measures the Resident Set Size (RSS)
* The function executes the data-loading task within a try-except block. This ensures that even if a library (like Dask or Polars) crashes due to an Out-of-Memory (OOM) error, the script captures the failure and the error message rather than stopping entirely.
* After execution, it handles Dask objects by converting a subset to Pandas to prevent infinite processing. It then calculates throughput by dividing the number of records processed by the total execution time

### 1. Load Less Data
**Explain:** </p>
This strategy uses the ``` cols ``` parameter within ``` pd.read_csv() ``` function to restrict to only necessary data to be loaded into the environment. The selected columns are ``` Price, Date of Transfer, Property Type, Old/New, Duration, and Town/City ```. By filtering these columns, the system able to avoids the overhead of parsing and storing irrelevant columns, which also directly minimize the initial memory used.

</p>

**Code:** </p>
```python
  file_path="price_paid_records.csv"

  def load_less_data_pandas(file_path):
    cols = [
        'Price', 'Date of Transfer', 'Property Type', 'Old/New', 'Duration',   'Town/City'
    ]
    return pd.read_csv(file_path, usecols=cols)
  
  
  performance_less_data, df_less_data = measure_performance(
      load_less_data_pandas,
      description="Load Less Data with Pandas",
      file_path=file_path
  )
  
  display(pd.DataFrame([performance_less_data]))

```
</p>

**Output:** </p>
![image](https://github.com/aflahh12/hpdpA2/blob/0633951a2bcd421bec27f10fa8a5c4dc5e1503d8/Screenshot%202026-05-03%20014142.png)

</p>

**Discussion:** </p>
From this strategy, it requires only 1093.57 MB of memory and execution time of 31.8884 seconds. The system also maintain a high throughput of 705251.69 records per seconds which shows that this approach is recommended when the analytical scope is limited to a specific subset of data.

</p>

### 2. Chunking
**Explain:** </p>
This strategy uses an interative loading technique to break a large file into smaller parts using discrete segments that is defined by ``` chunksize ``` parameter. This helps to prevent the system crashes by ensuring that only small portions of file, which is ``` 10,000 ``` to be processed in the limited RAM.

</p>

**Code:** </p>
```bash
  def load_with_chunking(file_path):
    chunks = []
    for chunk in pd.read_csv(file_path, chunksize=10000):
      chunks.append(chunk)
    df = pd.concat(chunks, ignore_index=True)
    return df
  
  performance_chunking, df_chunked = measure_performance(
      load_with_chunking,
      description="Chuncked Load",
      file_path="price_paid_records.csv"
  )
  
  display(pd.DataFrame([performance_chunking]))
```
</p>

**Output:** </p>
![image](https://github.com/aflahh12/hpdpA2/blob/0633951a2bcd421bec27f10fa8a5c4dc5e1503d8/Screenshot%202026-05-03%20014216.png)

</p>

**Discussion:** </p>
The results show a significant increase in memory usage of 5722.25 MB and execution time of 61.0781 seconds compared to load less data strategy. This performance degradation happened as the code appends all chunks into a list and concatenates them which effectively reconstructcs the entire dataset in memory and using a high computational cost during the final merge.
</p>

### 3. Data Type Optimisation
Explain: </p>
The code optimizes memory by selectively loading only the six essential columns and discarding irrelevant data immediately. It assigns specific data types, such as category for repeating text and int32 for numbers, to significantly shrink the memory footprint compared to default settings. The process utilizes chunking to read the file in manageable segments of 100,000 rows, which prevents the system from crashing under a single massive load. Finally, these optimized segments are stitched back together into a high-performance DataFrame ready for analysis.
</p>

Code: </p>
```bash
def optimized_chunked(file_path):
  cols = ['Price', 'Date of Transfer', 'Property Type', 'Old/New', 'Duration', 'Town/City']

  dtype_map = {
      'Price': 'int32',
      'Property Type':'category',
      'Old/New' : 'category',
      'Duration': 'category',
      'Town/City': 'object'
  }

  chunks = []

  for chunk in pd.read_csv(
      file_path,
      usecols=cols,
      dtype=dtype_map,
      parse_dates=['Date of Transfer'],
      chunksize=100000
  ):
        chunks.append(chunk)

  return pd.concat(chunks, ignore_index=True)

performance_opt, df_opt = measure_performance(
    optimized_chunked,
    description="Optimized Load with Dtype",
    file_path=file_path
)

display(pd.DataFrame([performance_opt]))
df_opt.info()
```

Output: </p>
![image](https://github.com/yAsmin241/HPDP-A2/blob/d859e4337390d5d12d0554cf9c5ca1958e2c81a4/Screenshot%202026-05-03%20024801.png)

Discussion: </p>
The code concludes with two diagnostic tools which are measure_performance to quantify the Time vs. Memory trade-off and df_opt.info() where 60% to 80% reduction in memory consumption
</p>

### 4. Sampling
Explain: </p>
The code creates a representative subset of the data by reading the file in blocks of 10,000 rows and immediately extracting a 10% random sample from each segment. By using a fixed random seed, it ensures that this selection is reproducible for consistent testing, while the chunking mechanism prevents the system from overloading its memory with the entire file. This strategy allows you to build and verify your analysis on a statistically balanced version of the full dataset while keeping the hardware requirements extremely low.
</p>

Code: </p>
```bash
def sampling_chunked(file_path, sample_fraction=0.1):
  cols = [
      'Price', 'Date of Transfer', 'Property Type', 'Old/New', 'Duration', 'Town/City'
  ]

  sampled_chunks = []

  for  chunk in pd.read_csv(
      file_path,
      usecols=cols,
      chunksize=10000
  ):

      sampled_chunk = chunk.sample(frac=sample_fraction, random_state=42)
      sampled_chunks.append(sampled_chunk)

  return pd.concat(sampled_chunks, ignore_index=True)


performance_sample, df_sample = measure_performance(
    sampling_chunked,
    description="Sampling",
    file_path=file_path
)

display(pd.DataFrame([performance_sample]))

print("Sample rows:", df_sample.shape[0])
df_sample.head()
```
Output: </p>
![image](https://github.com/yAsmin241/HPDP-A2/blob/c936da7cb8ac7be69255ec5e33d77430bfc47d19/Screenshot%202026-05-03%20025454.png)

Discussion: </p>
The analysis focuses on the practical balance between data integrity and computational speed. By sampling from every chunk across the entire file rather than just the top, the code maintains a statistically representative slice that captures the full chronological and geographical diversity of the records. While this method significantly reduces the final memory footprint for analysis, it doesn't drastically cut the initial loading time because the computer must still scan the entire disk to find the sample rows.
</p>


### 5. Parallel Processing
Explain: </p>
The code implements parallel processing through lazy evaluation, meaning it maps out the data structure without immediately loading it into memory to save resources. By using Dask DataFrames, it partitions the large CSV into smaller virtual pieces that can be processed across multiple CPU cores simultaneously.
</p>

Code: </p>
```bash
def optimized_load_dask(file_path):
  cols = [
      'Price', 'Date of Transfer', 'Property Type', 'Old/New', 'Duration', 'Town/City'
  ]

  ddf = dd.read_csv(
      file_path,
      usecols=cols,
      assume_missing=True,
      on_bad_lines="skip"
  )

  ddf.columns = ddf.columns.str.strip()

  ddf['Date of Transfer'] = dd.to_datetime(
      ddf['Date of Transfer'],
      errors='coerce'
  )

  return ddf

performance_dask, df_dask = measure_performance(
    optimized_load_dask,
    description="Parallel Processing with Dask",
    file_path=file_path
)

display(pd.DataFrame([performance_dask]))

df_dask.head(10)
```

Output: </p>
![image](https://github.com/yAsmin241/HPDP-A2/blob/d20152aa2417aeb5cae82bfb53f2e6cb5c93c0ab/Screenshot%202026-05-03%20030240.png)

Discussion: </p>
By utilizing parallelism, Dask distributes tasks across all available CPU cores, dramatically reducing processing time compared to the one-by-one approach of standard Pandas. This method provides infinite scalability, allowing even modest hardware to handle massive files (e.g., 100GB) without crashing, as it only loads specific data partitions into RAM when needed. However, this comes with a "lazy evaluation" trade-off, where the initial load appears near-instant because the actual computation is deferred until a result is explicitly requested.
</p>

### 🔹 **Part 2: Loading Dataset with Different Libraries**

This section compares how various data libraries handle CSV file loading and performance. Different tools and ecosystems (Pandas, Dask, Polars, Vaex) are explored.

#### 1. Using **Pandas** (Traditional)
```python
def load_with_chunking():
    chunk_size = 100000
    chunks = []
    for chunk in pd.read_csv("price_paid_records.csv", chunksize=chunk_size):
        chunks.append(chunk)
    df = pd.concat(chunks, axis=0)
    return df

# creates the 'performance_chunking' dictionary AND the 'df' variable
performance_chunking, df = measure_performance(load_with_chunking, description="Load with Pandas")

# Convert the performance results to a DataFrame for that pretty GitHub-style table
performance_df = pd.DataFrame([performance_chunking])

# Display the result
display(performance_df)
```

**Explanation**:  
This code defines a function that reads a large CSV file in segments of 100,000 rows to prevent memory overload. Each segment is appended to a list, which is then concatenated into a single, unified DataFrame. To evaluate this method, the function is passed into the measure_performance wrapper, which captures system metrics like RAM usage and execution time. The resulting performance data is then converted into a structured table and displayed to show the efficiency of the chunking strategy.

**Output**:  
![image](https://github.com/yAsmin241/HPDP-A2/blob/bc508c65b19eb2a1da28cc6c67cfbf8a5b1318be/Screenshot%202026-05-03%20033718.png)

#### 2. Using **Polars**
```python
def load_with_polars(filepath):
    df = pl.read_csv(filepath)
    return df

performance_polars, df_polars = measure_performance(
    load_with_polars,
    description="Load with Polars",
    filepath="price_paid_records.csv"
)

performance_polars = pd.DataFrame([performance_polars])
display(performance_polars)
```

**Explanation**:  
This code demonstrates the implementation of the Polars library to perform high-speed data ingestion. By utilizing pl.read_csv(), the script leverages Polars' multi-threaded Rust engine to load the dataset far more rapidly than standard Pandas. The performance metrics are converted into a structured table, providing a clear view of the library's throughput and efficiency for large-scale data tasks.

**Output**:  
![image](https://github.com/yAsmin241/HPDP-A2/blob/dccf9cee104330f6b26b22cb4aa1b8b1145ab454/Screenshot%202026-05-03%20034001.png)

#### 3. Using **Dask**
```python
def load_full_data_dask_and_compute(file_path):
    # Dask setup (lazy)
    ddf = dd.read_csv(
        file_path,
        assume_missing=True,
        quoting=3,
        on_bad_lines='skip',
        dtype=str
    )

    # Trigger computation and return the pandas DataFrame
    # This is where the main memory usage occurs
    df = ddf.compute()
    return df

# Measure the performance of the loading and computation
performance_dask_compute, df_dask_computed = measure_performance(
    load_full_data_dask_and_compute,
    description="Load with Dask",
    file_path="price_paid_records.csv"
)

performance_df_compute = pd.DataFrame([performance_dask_compute])
display(performance_df_compute)
```

**Explanation**: 
This code transitions Dask from a "lazy" planning tool to an active processing engine by explicitly calling the .compute() method, which forces the distributed data partitions into a single, standard Pandas DataFrame. dd.read_csv maps out the file structure to save resources, the .compute() command triggers the actual data ingestion and CPU-intensive calculations across all available cores.

**Output**: 
![image](https://github.com/yAsmin241/HPDP-A2/blob/3076ec3063c7484ea8f3cc095be8a69464a3014f/Screenshot%202026-05-03%20034249.png)

## 5. Comparative Analysis
### 5.1 Comparison of Optimized Loading Strategies
<h4> Summary Table </h4>

| Strategy | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (records/sec) |
| --------- | --------------- | ------------------| ------------| -------------------------|
| Load Less Data | 1093.57 | 31.8884 | 99.12 | 705251.69 |
| Chunking | 5722.25 | 61.0781 | 99.17 | 368206.41 |
| Optimized Data Types | 21.6 | 116.0844 | 102.38 | 193732.73 |
| Sampling | 83.34 | 43.7621 | 96.64 | 51390.02 |
| Parallel with <Dask> | 9.24 | 0.3845 | 17.48 | 260078.02 |

<h4> Visual Comparison </h4>

![image](https://github.com/aflahh12/hpdpA2/blob/61ecc4639aabbe6d8eae8a6e2652e173ade554a9/Screenshot%202026-05-03%20020434.png)

<h4> Interpretation </h4>
From the results, it shows that load less data performed best among others strategies. This is because it achieves the highest throughput and the fastest execution time while maintaining a low memory consumption. By filtered out some unnecessary columns, it minimizes the overhead and allows the CPU to process necessary data with maximum efficiency. 


### 5.2 Comparison Between Libraries

<h4> Summary Table </h4>

| Library | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (records/sec) |
| --------|-----------------|---------------------| ----------- | ------------------------ |
| Pandas |3727.15|65.2052|99.27|344901.14|
| Polars |7412.44|9.2270|181.34|2437341.28|
| Dask |2220.73|80.6522|123.53|278843.58|

<h4> Visual Comparison </h4>

![image](https://github.com/yAsmin241/HPDP-A2/blob/3076ec3063c7484ea8f3cc095be8a69464a3014f/Screenshot%202026-05-03%20031149.png)


<h4> Interpretation: </h4>
The library performance results showcase a strategic trade-off between execution speed and hardware resource management. Polars stands out as the highest-performing library for speed, delivering a throughput of over 2.4 million records per second and completing the task in just 9.2 seconds, though it requires the most memory (7.4 GB) and CPU power (181%) to do so. Dask offers the opposite advantage by being the most memory-efficient, using only 2.2 GB of RAM, about 3.5 times less than Polars while taking the longest time to execute at 80.6 seconds. Pandas occupies the middle ground, providing a balanced performance with moderate memory usage (3.7 GB) and a 65 second execution time, making it the standard choice for general analysis where extreme speed or massive scalability is not the primary concern.

## 6. Conclusion and Reflection
<h4> 🔷Summary of key observations </h4>
- The "Load Less Data" strategy emerged as the most effective optimization for general use because achieving the highest throughput (705,251 records/sec) by simply reducing the analytical scope to essential columns.
- Chunking prevents system crashes during the loading phase, it can lead to significant memory spikes (5,722 MB) during the final concatenation phase if the entire dataset is reconstructed.
- Data Type Optimization and Sampling proved to be the most "RAM-friendly" strategies, drastically reducing memory usage to as low as 21.6 MB
- Polars specialist in speed by using a multi-threaded Rust engine to achieve unprecedented speeds (9.2s total execution)
- Dask specialist in scalability by t is the most memory-efficient library (2.2 GB) for full dataset processing.
- Pandas is the Generalist where it remains the standard for datasets that fit comfortably in memory but lacks the modern multi-core optimizations seen in Polars or the distributed capabilities of Dask.

<h4> 🔷Discussion of scalability </h4>

| Strategy | Benefits | Limitations |
| -------- | -------- | ----------- |
| Load less data | Achieves the highest throughput and fastest execution by filtering only 6 columns at ingestion which make it most performant full-load strategy | Scans all rows sequentially and degrades proportionally as row count grows |
| Chunking | Enables processing of large files to fit in memory at once by 10,000 row increments | Driving peak memory to the highest of all strategies |
| Dtype optimization | Reduce column memory by casting columns to efficient types | Incurs slowest execution and lowest throughput due to overhead of dtype casting and date parsing on every chunk |
| Sampling | Achieves the lowest memory usage and fast execution by retaining only 10% of rows per chunk | Discards 90% of records, make it less suitable for tasks required full dataset accuracy|
| Dask parallel processing | Reads the CSV lazily and defers computation until needed | Low CPU utilization on a local setup |

<h4> 🔷Personal reflection on learning </h4> 

This assignment provide a new experience for me on how to strategically handle the data when standard tools hit their limit. Even though there is some challenges during the data inspections as the system keep crashing due to limitations of RAM, we had successfully changed the data and run without crashing without limiting the rows of the dataset. This hands-on activity also highlights the importance of selecting appropriate methods and libraries based on the dataset size, system resources, and specific analysis goals. Ultimately, I learned on how to balancing the processing speed with memory constraints using all of the strategies. -_Nabil Aflah Boo_

Working with the UK Housing Prices Paid dataset has enhance my practical lesson in handling big data. The primary challenge i faced was managing system crashes caused by RAM exhaustion. However, i do overcome this problem by implementing chunking solution to read the file in manageable segments of 100,000 rows. This allowed to keep the system stable during the ingestion phase. Moreover, i do analyse the differnce between that 3 library which are pandas, polars and dask. Polars offered incredible speed, Dask is good at memory-efficient, and pandas is the general ones. Overal, this project has changed my perspective from just by focusing on the codes to writing code effectively that is resource-aware.

## References
_UK Housing Prices Paid_. (n.d.). Www.kaggle.com. https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid 

The Pandas Development Team. (2024). _pandas-dev/pandas: Pandas 2.2.2_. Zenodo. https://doi.org/10.5281/zenodo.3509134 

Dask Development Team. (2022). _Dask: Library for dynamic task scheduling_. https://dask.org 

Polars Development Team. (2024). _Polars: Fast multi-threaded, hybrid-streaming DataFrame library in Rust | Python_. https://pola.rs 

Google. (n.d.). _Google Colaboratory_. https://colab.research.google.com 
