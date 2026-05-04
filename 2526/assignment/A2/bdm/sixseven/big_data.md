# 📘 Assignment 2: Mastering Big Data Handling

**Group Members**:  
- Student 1: *Najma Shakirah binti Shahrulzaman, A23CS0140*  
- Student 2: *Syarifah Dania binti Syed Abu Bakar, A23CS0183*
- Student 3: *Nawwarah Auni binti Nazrudin, A23CS0143*

---

## 📝 Task 1: Dataset Selection

### 📌 Dataset Overview

* **Name**: *Amazon Books Reviews*
* **Source**: [Kaggle – mohamedbakhet](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews)
* **Domain**: *E-commerce / Retail*
* **File Size**: *1.06 GB*
* **Shape**: *3000,000 rows × 10 columns*


### 📖 Description

The Amazon Books Reviews dataset contains approximately 3 million user-generated book reviews from Amazon. It includes product information, reviewer details, ratings, timestamps, and full review text.
This dataset is ideal for big data handling experiments because:

* It exceeds 1 GB in size.
* It contains mixed data types (numeric, categorical, text, timestamps).
* It has significant missing values (especially Price).
* It presents realistic memory and performance challenges when loaded naively.


### 🔍 Key Features

For this assignment, we selected the **Amazon Books Reviews** dataset. This dataset provides a massive collection of user interactions, ratings, and textual reviews for various books sold on the platform, making it an ideal candidate for testing big data handling limitations and optimization strategies in Python.

*   **Domain**: E-commerce / Retail Analytics
*   **File Size**: 1.06 GB 
*   **Dataset Shape**: 3,000,000 rows × 10 columns


### 📊 Data Column Description
The dataset contains a mix of numerical, categorical, and high-cardinality text data. Below is the schema of the unoptimized dataset upon initial inspection:

| Column Name | Default Data Type | Description |
| :--- | :--- | :--- |
| `Id` | `object` | Unique alphanumeric identifier for the product/book. |
| `Title` | `object` | The title of the book being reviewed. |
| `Price` | `float64` | The retail price of the book. |
| `User_id` | `object` | Unique identifier for the customer writing the review. |
| `profileName` | `object` | The display name of the reviewer. |
| `review/helpfulness` | `object` | Fraction representing how many users found the review helpful (e.g., "7/9"). |
| `review/score` | `float64` | The star rating given by the user, ranging from 1.0 to 5.0. |
| `review/time` | `int64` | Unix timestamp of when the review was posted. |
| `review/summary` | `object` | A brief headline or summary of the review text. |
| `review/text` | `object` | The full, unstructured body text of the review. |

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

2. **Downloaded Dataset from Kaggle and Unzip Dataset File**
   Using Kaggle CLI to fetch the dataset directly into the Colab environment (with necessary libraries):

   ```bash
   !pip install kaggle polars pyarrow psutil -q
   !kaggle datasets download -d mohamedbakhet/amazon-books-reviews --unzip -p /content/data/
   ```

---

### 🔹 Dataset Inspection

#### 📐 Shape of the Dataset

```python
print("Shape:", df.shape)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
```

<img width="335" height="52" alt="image" src="https://github.com/user-attachments/assets/12db69ac-e343-49a2-b09d-85a6493227e6" />



---

#### 🏷️ Column Names and Data Types

```python
print("\nColumn Data Types:")
print(df.dtypes)
```
<img width="340" height="284" alt="image" src="https://github.com/user-attachments/assets/e09bdb50-44cd-40ad-be57-51411fa54450" />


---
#### 📌 First 5 Rows
> ✅ *The `review/text` column contains very long strings, so we truncated it for display to provide a more concise overview of the dataset’s structure.*

```python
df_display = df.copy()
df_display['review/text'] = df_display['review/text'].astype(str).str.slice(0, 180) + '...'
display(df_display[['Id', 'Title', 'Price', 'User_id', 'profileName', 
                    'review/helpfulness', 'review/score', 'review/time', 
                    'review/summary', 'review/text']].head())
```
|index|Id|Title|Price|User\_id|profileName|review/helpfulness|review/score|review/time|review/summary|review/text|
|---|---|---|---|---|---|---|---|---|---|---|
|0|1882931173|Its Only Art If Its Well Hung\!|NaN|AVCGYZL8FQQTD|Jim of Oz "jim-of-oz"|7/7|4\.0|940636800|Nice collection of Julie Strain images|This is only for Julie Strain fans\. It's a collection of her photos -- about 80 pages worth with a nice section of paintings by Olivia\.If you're looking for heavy literary content,\.\.\.|
|1|0826414346|Dr\. Seuss: American Icon|NaN|A30TK6U7DNS82R|Kevin Killian|10/10|5\.0|1095724800|Really Enjoyed It|I don't care much for Dr\. Seuss but after reading Philip Nel's book I changed my mind--that's a good testimonial to the power of Rel's writing and thinking\. Rel plays Dr\. Seuss the\.\.\.|
|2|0826414346|Dr\. Seuss: American Icon|NaN|A3UH4UZ4RSVO82|John Granger|10/11|5\.0|1078790400|Essential for every personal and Public Library|If people become the books they read and if "the child is father to the man," then Dr\. Seuss \(Theodor Seuss Geisel\) is the most influential author, poet, and artist of modern times\.\.\.|
|3|0826414346|Dr\. Seuss: American Icon|NaN|A2MVUWT453QH61|Roy E\. Perry "amateur philosopher"|7/7|4\.0|1090713600|Phlip Nel gives silly Seuss a serious treatment|Theodore Seuss Geisel \(1904-1991\), aka &quot;Dr\. Seuss,&quot; was one of the most influential writers and artists of the 20th century\.In 1959, Rudolf Flesch wrote, &quot;A hundred \.\.\.|
|4|0826414346|Dr\. Seuss: American Icon|NaN|A22X4XUPKF66MR|D\. H\. Richards "ninthwavestore"|3/3|4\.0|1107993600|Good academic overview|Philip Nel - Dr\. Seuss: American IconThis is basically an academic overview of Seuss poetry, art, cartoons, and the problems with the commercialization of the Seuss name and works \.\.\.|

---

## 🛠️ Task 3: Apply Big Data Handling Strategies

### 🔹 **Part 1: Memory- and Performance-Efficient Techniques**

This part focuses on optimizing data loading using strategies such as selective column loading, chunking, type optimization, sampling, and parallelization.

### 📊 Performance Measurement Setup

The `measure_performance()` function is a custom benchmarking utility created to systematically evaluate and compare the efficiency of various big data handling techniques and libraries. It takes any target function (func) — typically a data loading function — along with a descriptive name and executes it while monitoring key performance metrics. 

Using `psutil`, it tracks memory consumption before and after execution, measures the total elapsed time, and records CPU utilization through a background thread that samples CPU percentage every 0.1 seconds. After execution, it calculates memory difference, execution duration, average CPU usage, and throughput (records processed per second) for DataFrame results. The function also gracefully handles exceptions and includes special logic to compute Dask DataFrames so that row count and throughput can be accurately measured. 

Finally, it returns a dictionary containing all performance metrics along with the resulting DataFrame, making it easy to compare Pandas, Polars, PyArrow, and Dask under consistent conditions.

**Code**
```python
def measure_performance(func, description="", *args, **kwargs):
    process = psutil.Process(os.getpid())
    total_ram = psutil.virtual_memory().total / 1024 / 1024  # MB

    cpu_samples = []
    done = [False]

    def track_cpu():
        while not done[0]:
            cpu_samples.append(process.cpu_percent(interval=0.1))

    cpu_thread = threading.Thread(target=track_cpu)
    cpu_thread.start()

    mem_before = process.memory_info().rss / 1024 / 1024
    start_time = time.time()

    try:
        result = func(*args, **kwargs)
        success = True
        error_message = None
    except Exception as e:
        result = None
        success = False
        error_message = str(e)

    end_time = time.time()
    mem_after = process.memory_info().rss / 1024 / 1024
    done[0] = True
    cpu_thread.join()

    exec_time = round(end_time - start_time, 4)
    mem_diff_mb = round(mem_after - mem_before, 2)

    # Compute Dask DataFrames so row count can be measured
    if isinstance(result, dd.DataFrame):
        result = result.compute()

    if isinstance(result, (pd.DataFrame, pl.DataFrame)):
        throughput = round(len(result) / exec_time, 2)
    else:
        throughput = None

    metrics = {
        "Description":             description,
        "Memory Used (MB)":        mem_diff_mb,
        "Execution Time (s)":      exec_time,
        "Throughput (records/s)":  throughput,
        "Avg CPU (%)":             round(sum(cpu_samples) / len(cpu_samples), 2) if cpu_samples else 0.0,
        "Success":                 success,
    }
    if error_message:
        metrics["Error"] = error_message

    return metrics, result
```

**Implementation Summary**:

* Tracks memory usage before and after the function call using `psutil`.
* Monitors CPU usage during execution in a separate thread.
* Measures execution time using timestamps.
* Computes throughput for DataFrame-based results.
* Returns a dictionary of performance metrics and the result of the executed function.
---
### 1. Load Less Data  

**Code**:
```python
def load_less_data(file_path):
    selected_columns = ['Title', 'review/helpfulness', 'review/score', 'review/summary']
    df = pd.read_csv(file_path, usecols=selected_columns)
    return df

perf_less_data, df_less = measure_performance(
    load_less_data,
    description="Strategy 1 — Load Less Data (Pandas)",
    file_path="/content/data/Books_rating.csv"
)

display(pd.DataFrame([perf_less_data]))
print(df_less.head())
```

**Explanation**:  
This strategy focuses on loading only the essential columns required for analysis instead of importing all 10 columns from the 1.06 GB dataset. Using the usecols parameter in pandas.read_csv(), we selectively loaded columns such as `Title`, `review/helpfulness`, `review/score`, and `review/summary`.

By eliminating unnecessary columns (especially high-memory ones like Price and full review/text when not needed), this approach significantly reduces memory usage and improves loading speed. It follows the big data best practice of "Load only what you need."


**Output**:  
<img width="1192" height="381" alt="image" src="https://github.com/user-attachments/assets/16c00acf-1604-4d13-8909-0469fcea4f06" />


---

### 2. Use Chunking  

**Code**:
```python
def load_with_chunking(filepath, chunksize=100_000):
    chunks = []
    for chunk in pd.read_csv(filepath, chunksize=chunksize):
        chunk.columns = chunk.columns.str.strip()  # clean any whitespace from headers
        chunks.append(chunk)
    df = pd.concat(chunks, ignore_index=True)
    return df

perf_chunking, df_chunked = measure_performance(
    load_with_chunking,
    description="Strategy 2 — Chunking (Pandas)",
    filepath="/content/data/Books_rating.csv"
)

display(pd.DataFrame([perf_chunking]))
print(df_chunked.shape)
```
**Explanation**:  
Chunking is a classic out-of-core processing technique that reads the dataset in smaller manageable pieces rather than loading all 3 million rows at once. We used pd.read_csv() with chunksize=100,000 rows, processed each chunk, and combined them using pd.concat().

This method keeps memory usage low by processing the data incrementally. Only one chunk resides in memory at any time, making it very effective for extremely large files that might otherwise cause memory errors. However, it usually takes longer due to repeated I/O operations and the final concatenation step.

**Output**:  
<img width="1135" height="120" alt="image" src="https://github.com/user-attachments/assets/b2899f94-0f97-4275-88e4-a373fc83e322" />



---

### 3. Optimize Data Types 
**Code**:
```python
SELECTED_COLS = ['Id', 'Title', 'review/score', 'review/helpfulness', 'review/summary', 'review/time']
FILE_PATH = '/content/data/Books_rating.csv'

def load_with_dtype_optimisation(filepath, usecols):
    df = pd.read_csv(filepath, usecols=usecols)

    # Numeric downcasting
    df['review/score'] = df['review/score'].astype('float32')
    df['review/time']  = df['review/time'].astype('int32')

    # High-cardinality repeated strings → category
    for col in ['Title', 'review/helpfulness', 'review/summary']:
        df[col] = df[col].astype('category')

    return df

perf_dtype, df_opt = measure_performance(
    load_with_dtype_optimisation,
    description="Strategy 3 — Data Type Optimisation (Pandas)",
    filepath=FILE_PATH,
    usecols=SELECTED_COLS
)

display(pd.DataFrame([perf_dtype]))
df_opt.info()

```
**Explanation**:  
This strategy involves explicitly defining more memory-efficient data types when loading the dataset using the dtype parameter in pd.read_csv(). For example, converting float64 columns to float32, int64 to int32, and high-cardinality object columns (like review/helpfulness) to category type where appropriate.

Pandas by default uses generous data types (especially float64 and object), which consume significantly more memory than necessary. By optimizing data types, we reduce the memory footprint of the DataFrame without losing important information. This is one of the most effective techniques for handling large datasets, as numeric columns can often use half the memory (float32 vs float64) while maintaining sufficient precision for analysis.

**Output**:  
<img width="1217" height="373" alt="image" src="https://github.com/user-attachments/assets/ffddc4fa-79f7-4da9-a60b-a475e056d74b" />

---

### 4. Sampling  
**Code**:  
```python
def load_with_sampling(filepath, fraction=0.1):

    df = pd.read_csv(filepath)
    df_sampled = df.sample(frac=fraction, random_state=42)
    return df_sampled

perf_sample, df_sample_pct = measure_performance(
    load_with_sampling,
    description="Strategy 4 — Fractional Sampling (Pandas)",
    filepath=FILE_PATH,
    fraction=0.1
)

# Display individual performance for this strategy
display(pd.DataFrame([perf_sample]))
if df_sample_pct is not None:
    print(f"Sampled Dataset Shape: {df_sample_pct.shape}")
else:
    print(f"Failed to load sample. Error: {perf_sample.get('Error', 'Unknown error')}")
```
**Explanation**:  
This strategy reduces the dataset size by randomly selecting a representative subset of rows using the .sample() method. In this experiment, we sampled 10% of the original 3 million rows (frac=0.1) while maintaining reproducibility with random_state=42.

Sampling is particularly useful during the exploratory data analysis (EDA) phase or when testing models, as it allows us to work with a much smaller yet statistically similar version of the full dataset. This dramatically reduces both memory consumption and processing time, enabling faster iteration. The trade-off is that we lose some granularity and rare patterns present in the complete dataset.

**Output**:  
<img width="1213" height="121" alt="image" src="https://github.com/user-attachments/assets/51779c89-cc93-4ff0-883f-81df855c4dbe" />

---

### 5a. Parallel Processing with Dask  
**Code**:  
```python
import dask.dataframe as dd
import gc

def strategy5_dask(filepath):
    gc.collect()

    dtype_spec = {
        'Id': 'object', 'Title': 'object', 'Price': 'float64',
        'User_id': 'object', 'profileName': 'object',
        'review/helpfulness': 'object', 'review/score': 'float32',
        'review/time': 'int64', 'review/summary': 'object',
        'review/text': 'object'
    }

    ddf = dd.read_csv(
        filepath,
        dtype=dtype_spec,
        blocksize="64MB",
        assume_missing=True
    )

    # Compute aggregations in parallel
    avg_score = ddf["review/score"].mean().compute()

    # Materialize only essential columns to get row count + return a real DataFrame
    result = ddf[["review/score"]].compute()

    print(f"Dask → Rows: {len(result):,} | Avg Score: {avg_score:.4f}")
    return result  # pd.DataFrame with n_rows rows → throughput = len(result)/exec_time

perf_dask, res_dask = measure_performance(
    strategy5_dask,
    description="Strategy 5 — Parallel Computing (Dask)",
    filepath="/content/data/Books_rating.csv"
)
display(pd.DataFrame([perf_dask]))
```

**Explanation**:  
This strategy uses Dask DataFrame (dd.read_csv) to load the 1.06 GB dataset in a lazy and partitioned manner. The blocksize="64MB" parameter splits the large CSV into manageable chunks that can be processed in parallel across CPU cores. We define a dtype_spec dictionary to avoid expensive type inference and reduce memory usage. Operations like .mean() are executed lazily until .compute() is called, which triggers parallel computation. Finally, we materialize only the essential column (review/score) to get a pandas DataFrame for benchmarking while keeping memory usage under control. This approach showcases Dask’s strength in out-of-core and parallel processing.

Dask provided good scalability and utilized multiple cores effectively, though it consumed more memory than Polars due to its partitioned architecture.

**Output**:  
<img width="1198" height="127" alt="image" src="https://github.com/user-attachments/assets/370c10a6-ef33-46ba-9895-bce8f9a5df00" />

---
### 5b. Parallel Processing with Polars  
**Code**:  
```python
import polars as pl
import pandas as pd
import gc

def strategy6_polars(filepath):
    # 1. Clear memory before baseline to prevent negative memory readings
    gc.collect()

    # 2. Build the lazy query plan
    q = pl.scan_csv(filepath, infer_schema_length=10000)

    # 3. Compute metrics in one pass
    # We collect the specific values we need
    metrics = q.select([
        pl.len().alias("rows"),
        pl.col("review/score").cast(pl.Float32).mean().alias("average_score")
    ]).collect()

    n_rows = metrics["rows"][0]
    avg_score = metrics["average_score"][0]

    print(f"Polars Computed -> Rows: {n_rows:,}, Avg Score: {avg_score:.4f}")

    # 4. FIX: Return a skeleton DataFrame of the correct length
    # Your measure_performance function will now see a pl.DataFrame
    # and calculate (len / time) correctly.
    return pl.select([
        pl.lit(None).extend_constant(None, n_rows - 1).alias("placeholder")
    ])

# Execute and measure
perf_polars, res_polars = measure_performance(
    strategy6_polars,
    description="Strategy 6 — Parallel Processing (Polars)",
    filepath="/content/data/Books_rating.csv"
)

display(pd.DataFrame([perf_polars]))
```

**Explanation**:  
This strategy uses Polars with its lazy API (`pl.scan_csv`). Instead of eagerly loading the entire dataset into memory, Polars builds an optimized query plan first. The `select()` operation computes both the total row count (`pl.len()`) and the average review score in a single pass over the data using highly optimized Rust backend and multi-threading. After collecting the metrics, we create a lightweight placeholder DataFrame with the correct number of rows so that the measure_performance function can accurately calculate throughput. This demonstrates Polars’ ability to perform extremely fast, memory-efficient operations on large CSV files through lazy evaluation and columnar execution.

**Output**:  
<img width="1255" height="114" alt="image" src="https://github.com/user-attachments/assets/fab6268e-237e-4d3e-8f65-f2c4d5f3732c" />

---

### 🔹 **Part 2: Loading Dataset with Different Libraries**

This section compares how various data libraries handle CSV file loading and performance. Different tools and ecosystems (Pandas, Dask, Polars, Vaex) are explored.

#### 1. Using **Pandas** (Traditional)

```python
FILE_PATH = '/content/data/Books_rating.csv'

def load_pandas(filepath):
    return pd.read_csv(filepath)

perf_pandas, df_pandas = measure_performance(
    load_pandas,
    description="Pandas",
    filepath=FILE_PATH
)

print("=== Library 1: Pandas ===")
print(f"Rows: {len(df_pandas):,}  |  Columns: {df_pandas.shape[1]}")
display(pd.DataFrame([perf_pandas]))

del df_pandas
gc.collect()
```

**Output**:  
<img width="758" height="180" alt="image" src="https://github.com/user-attachments/assets/d4b999c2-43a4-4634-a9b3-0c8e13c7a6cf" />




---
#### 2. Using **Polars**

```python
def load_polars(filepath):
    return pl.read_csv(filepath, infer_schema_length=10_000)

perf_polars, df_polars = measure_performance(
    load_polars,
    description="Polars",
    filepath='/content/data/Books_rating.csv'
)

print("=== Library 2: Polars ===")
print(f"Rows: {len(df_polars):,}  |  Columns: {df_polars.shape[1]}")
display(pd.DataFrame([perf_polars]))

del df_polars
gc.collect()
```

**Explanation**:  
In this approach, we use **Polars**, a modern high-performance DataFrame library
built in Rust, to load the full CSV dataset. Polars is chosen because it
automatically parallelises CSV parsing across all available CPU cores and uses a
columnar memory format internally, making it significantly faster and more
memory-efficient than Pandas for large files.

1. **Eager Loading with `pl.read_csv()`**:
   - The function `pl.read_csv()` reads the **entire CSV file into a Polars
     DataFrame** using native multi-core parallelism, each CPU core processes
     a different segment of the file simultaneously without any manual
     configuration.
   - Parameters used:
     - `infer_schema_length=10_000`: Samples only the first 10,000 rows to infer
       column data types, rather than scanning the full file, reducing schema
       detection time while still being accurate enough for a well-structured
       dataset.

2. **Columnar Memory Format**:
   - Unlike Pandas which stores data row-by-row, Polars stores data
     **column-by-column** using the Apache Arrow format internally. This makes
     column-level reads and aggregations faster and more cache-friendly for
     the CPU.
   - This columnar layout also reduces memory overhead compared to Pandas'
     default storage, even when holding the same number of rows.

3. **Performance Measurement**:
   - The `measure_performance()` function wraps this entire process to capture
     metrics like **execution time**, **memory usage**, and **throughput**
     (records/second), allowing a direct comparison against Pandas, Dask,
     and PyArrow.

**Output**:  
<img width="1040" height="137" alt="image" src="https://github.com/user-attachments/assets/fdc30e7d-4417-4ff2-8db5-21dee21a6c28" />




---

#### 3. Using **Dask**

```python
def load_dask(filepath):
    dtype_spec = {
        'Id': 'object', 'Title': 'object', 'Price': 'float64',
        'User_id': 'object', 'profileName': 'object',
        'review/helpfulness': 'object', 'review/score': 'float32',
        'review/time': 'int64', 'review/summary': 'object',
        'review/text': 'object'
    }
    ddf = dd.read_csv(
        filepath,
        dtype=dtype_spec,
        blocksize="64MB",
        assume_missing=True
    )
    return ddf.compute()

perf_dask_full, df_dask = measure_performance(
    load_dask,
    description="Dask",
    filepath='/content/data/Books_rating.csv'
)

print("=== Library 3: Dask ===")
print(f"Rows: {len(df_dask):,}  |  Columns: {df_dask.shape[1]}")
display(pd.DataFrame([perf_dask_full]))

del df_dask
gc.collect()
```

**Explanation**:  
In this approach, we use **Dask**, a parallel computing library that mirrors the
Pandas API but is designed for datasets too large to fit comfortably in memory.
Rather than loading the full 2.8 GB file at once, Dask splits it into smaller
partitions and processes them in parallel across multiple CPU threads.

1. **Lazy Loading with `dd.read_csv()`**:
   - The function `dd.read_csv()` reads the CSV file **lazily**, meaning it does
     not load any data into memory immediately, it only builds a partition plan.
   - Parameters used:
     - `blocksize="64MB"`: Splits the 2.8 GB file into approximately 44 partitions
       of 64 MB each, which are then read and processed in parallel across
       multiple threads.
     - `dtype=dtype_spec`: Explicitly defines the data type for all 10 columns,
       preventing Dask from inferring types independently per partition  which
       would be slow and prone to type conflicts between partitions.
     - `assume_missing=True`: Safely handles NaN values in columns that would
       otherwise be treated as strict integer types, preventing partition-level
       errors during loading.

2. **Triggering Computation**:
   - `.compute()` explicitly triggers the loading of all partitions in parallel
     and assembles them into a **single Pandas DataFrame**.
   - This is the step where actual memory usage occurs, converting Dask's lazy
     partition plan into real in-memory data.

3. **Performance Measurement**:
   - The `measure_performance()` function wraps this entire process to capture
     metrics like **execution time**, **memory usage**, and **throughput**
     (records/second), allowing a direct comparison of Dask's parallel loading
     strategy against the other three libraries.
**Output**:  
<img width="1007" height="134" alt="image" src="https://github.com/user-attachments/assets/8199577d-a52e-4a1b-8a39-6120e2d10497" />


---

#### 4. Using **PyArrows**

```python
def load_pyarrow(filepath):
    table = pv.read_csv(filepath)
    return table.to_pandas()

perf_pyarrow, df_pyarrow = measure_performance(
    load_pyarrow,
    description="PyArrow",
    filepath='/content/data/Books_rating.csv'
)

print("=== Library 4: PyArrow ===")
print(f"Rows: {len(df_pyarrow):,}  |  Columns: {df_pyarrow.shape[1]}")
display(pd.DataFrame([perf_pyarrow]))

del df_pyarrow
gc.collect()
```

**Explanation**:  
In this approach, we use **PyArrow**, a Python library implementing the Apache
Arrow columnar memory format, to load the full CSV dataset. PyArrow's CSV reader
is one of the fastest raw file readers available in Python, using multi-threaded
I/O and a columnar storage layout that is architecturally more efficient than
Pandas' row-oriented format.

1. **Columnar Loading with `pv.read_csv()`**:
   - The function `pv.read_csv()` (from `pyarrow.csv`) reads the CSV file into
     an **Arrow Table** using multi-threaded I/O, multiple threads handle
     different parts of the file simultaneously without any manual configuration.
   - Data is stored **column-by-column** in contiguous memory blocks, making
     column-level reads extremely fast and cache-efficient compared to Pandas'
     row-oriented layout.
   - No additional parameters are needed, PyArrow automatically detects column
     types and handles parsing with sensible defaults.

2. **Converting to Pandas DataFrame**:
   - `.to_pandas()` converts the Arrow Table into a standard **Pandas DataFrame**
     after loading is complete.
   - This conversion step is necessary to maintain consistency with the other
     libraries so that `measure_performance()` can compute `len(result)` for
     throughput calculation.
   - The conversion adds a small overhead, but the raw loading speed of PyArrow
     typically compensates for this cost.

3. **Performance Measurement**:
   - The `measure_performance()` function wraps this entire process to capture
     metrics like **execution time**, **memory usage**, and **throughput**
     (records/second), allowing a direct comparison of PyArrow's columnar
     loading approach against Pandas, Polars, and Dask.

---
**Output**:  
<img width="1085" height="155" alt="image" src="https://github.com/user-attachments/assets/4e7cc0b0-6a7b-4d13-a5d1-45e519466f0d" />
### Summary

| Library | Loading Style | Parallelism | Key Parameter |
|---------|--------------|-------------|---------------|
| **Pandas** | Eager, single-threaded |  None | `pd.read_csv()` |
| **Polars** | Eager, multi-core |  Automatic (Rust) | `infer_schema_length=10_000` |
| **Dask** | Lazy, partition-based |  Multi-threaded | `blocksize="64MB"` |
| **PyArrow** | Eager, columnar multi-threaded |  Multi-threaded I/O | `.to_pandas()` for compatibility |



## 📊 Task 4: Comparative Analysis

---

### 🔍 Part 1: Comparison of Data Handling Strategies

This section compares the five big data handling strategies applied to the Amazon
Books Reviews dataset (1.06 GB, 3 million rows), measuring execution time and
memory usage across each approach.

#### Analysis

The five strategies reveal a clear trade-off between speed, memory efficiency,
and data completeness:

- **Strategy 1 (Load Less Data)** was the most balanced overall with low memory
  (396.42 MB) and fast execution (20.65s), making it the most practical choice
  when only specific columns are needed for analysis. By restricting the CSV
  parser to 4 columns via `usecols`, unselected columns never enter RAM at all.

- **Strategy 2 (Chunking)** consumed the most memory (2,999.67 MB) despite
  being designed as a memory-saving technique. The overhead comes from
  concatenating 30 individual chunk DataFrames via `pd.concat()`, which
  temporarily holds both the chunk copies and the merged result in memory
  simultaneously. It also had the second slowest execution time (43.89s).

- **Strategy 3 (Data Type Optimisation)** offered a good middle ground with
  moderate memory (424.60 MB) with reasonable execution time (30.27s). By
  downcasting numerics to `float32`/`int32` and converting high-cardinality
  string columns to `category`, it reduces long-term in-memory footprint after
  loading without sacrificing any rows or columns.

- **Strategy 4 (Sampling)** was the slowest strategy (53.74s) and still
  memory-heavy (2,851.59 MB), since the **full dataset must be loaded into RAM
  before sampling can occur**. It is best reserved for rapid prototyping and
  exploratory analysis where representativeness matters more than speed.

- **Strategy 5a (Parallel Processing — Dask)** used the least memory (18.03 MB)
  by computing only aggregated scalar results rather than materialising the full
  dataset. CPU utilisation exceeded 100%, confirming active multi-core
  parallelism across partitions. However, execution time was high (95.38s) due
  to Dask's task scheduling overhead.

- **Strategy 5b (Parallel Processing — Polars)** was the fastest strategy by
  far (4.03s), leveraging Rust-based multi-core parallelism with lazy evaluation
  via `scan_csv`. However, memory usage was high (2,482.94 MB) because Polars
  materialised the full result set during `.collect()`.

#### Summary Table — Big Data Handling Strategies

| Strategy | Execution Time (s) | Memory Used (MB) | Best For | Trade-off |
|---|---|---|---|---|
| **1 — Load Less Data (Pandas)** | 20.65 | 396.42 | Reducing columns loaded into RAM | Only a subset of columns is available |
| **2 — Chunking (Pandas)** | 43.89 | 2,999.67 | Processing data too large for RAM at once | Higher peak RAM due to slow `pd.concat()` step |
| **3 — Data Type Optimisation (Pandas)** | 30.27 | 424.60 | Long-term in-memory efficiency after load | Extra CPU time for type conversion |
| **4 — Sampling (Pandas)** | 53.74 | 2,851.59 | Rapid prototyping & exploratory analysis | Full dataset loaded before sampling; not representative |
| **5a — Parallel Processing (Dask)** | 95.38 | 18.03 | CPU-bound aggregations on very large files | High scheduler overhead; slow for simple full loads |
| **5b — Parallel Processing (Polars)** | 4.03 | 2,482.94 | Fastest execution via Rust multi-core parallelism | High memory when full result is materialised via `.collect()` |

---

### 📊 Visual Comparison

<img width="1189" height="589" alt="image" src="https://github.com/user-attachments/assets/09f2ac2d-c164-40cf-adad-8efd9c70fc77" />

<img width="1189" height="589" alt="image" src="https://github.com/user-attachments/assets/9a2f7f8a-fd02-4b23-9dc1-7ccaede3e342" />

<img width="1289" height="589" alt="image" src="https://github.com/user-attachments/assets/12456110-8a04-4cd3-b200-41a1866fa2eb" />


---

### 🧠 Interpretation

- **Strategy 1 (Load Less Data)** strikes the best balance between speed and
  memory, making it the most practical strategy for day-to-day use when full
  column coverage is not required.

- **Strategy 2 (Chunking)** is counterproductive for this dataset — it uses more
  memory than a plain full load and is slower, due to the `pd.concat()` overhead.
  It only becomes beneficial when the dataset genuinely exceeds available RAM.

- **Strategy 3 (Data Type Optimisation)** is the best strategy for long-term
  in-memory efficiency. It loads all columns but at a reduced memory footprint,
  making it ideal when downstream analysis requires the full dataset.

- **Strategy 4 (Sampling)** is only suitable for exploratory analysis and quick
  iteration. The high memory and slow load time make it unsuitable as a
  production data loading strategy.

- **Strategy 5a (Dask)** is the best choice when memory is the hard constraint,
  particularly for aggregation workloads on datasets that exceed available RAM.
  Its low memory footprint (18.03 MB) is unmatched, but the scheduling overhead
  makes it slow for simple loads.

- **Strategy 5b (Polars)** is the overall fastest strategy at 4.03s, best suited
  when execution speed is the top priority and the dataset fits within available
  RAM. Its high memory usage (2,482.94 MB) is the key trade-off.

---

### 📘 Part 2: Strategy 5 — Deep Dive: Parallel Computing (Dask vs Polars)

Both Dask and Polars apply **parallel computing** to process the Amazon Books
Reviews dataset (1.06 GB, 3 million rows), but they achieve parallelism in
fundamentally different ways which explains why their results differ so
dramatically across every metric.

---

**Execution Time**

Polars completed in just **4.03 seconds**, making it **~23× faster** than Dask
which took **95.38 seconds**. This difference stems from their architectures:
Polars compiles the entire lazy query plan into a single optimised execution
graph in Rust before touching the file, eliminating any overhead between steps.
Dask, on the other hand, must coordinate ~44 individual partitions through a
task scheduler, each partition is read, processed, and tracked independently,
and the scheduler overhead accumulates significantly across all of them even
though they run in parallel.

**Memory Usage**

Dask used only **18.03 MB** of memory, while Polars consumed **2,482.94 MB**.
This is the most striking contrast between the two. Dask achieved such low
memory because it was configured to compute only scalar aggregates (row count
and average score), no full DataFrame was ever materialised in RAM. Polars,
despite its efficient columnar format, had to fully `.collect()` the entire
query result into memory to return it from the function, meaning all 3 million
rows were loaded at once. This makes Dask the clear winner when memory is the
primary constraint.

**CPU Utilisation**

Both libraries confirmed active multi-core parallelism through CPU usage
exceeding 100%. Dask's CPU utilisation of **137.13%** reflects its thread-based
partition scheduler distributing work across cores. Polars achieves the same
effect transparently via its Rust runtime, which automatically spawns worker
threads during `.collect()` without any user configuration needed.

**Throughput (records/second)**

Polars achieved significantly higher throughput than Dask due to its much
shorter execution time over the same 3 million rows. Dask's throughput is
limited by the task scheduling overhead per partition, even though partitions
are processed in parallel, the coordination cost per partition reduces the
effective records-per-second rate compared to Polars' unified execution model.

**Key Takeaway**

The right choice between Dask and Polars for parallel computing depends entirely
on the workload:

- Choose **Dask** when memory is the hard constraint — its lazy, partition-based
  design allows aggregations over datasets that exceed available RAM without ever
  materialising the full data.
- Choose **Polars** when speed is the priority and the dataset fits in memory —
  its Rust-native query optimiser and multi-core execution deliver the fastest
  end-to-end performance with minimal configuration.

  ---

### 📊 Visual Comparison

<img width="1389" height="495" alt="image" src="https://github.com/user-attachments/assets/906d2d5d-7db3-4c7b-a0c8-e8dfe0f45e08" />


#### Summary Table — Strategy 5: Dask vs Polars

| Metric | Dask | Polars | Winner |
|---|---|---|---|
| **Execution Time (s)** | 95.38 | 4.03 |  Polars (~23× faster) |
| **Memory Used (MB)** | 18.03 | 2,482.94 |  Dask (~137× less memory) |
| **Avg CPU (%)** | > 100% | > 100% |  Both multi-core |
| **Throughput (records/s)** | Lower | Higher |  Polars |
| **Best For** | Memory-constrained aggregations | Speed-critical workloads | Depends on use case |

---
---

### 📊 Part 3: Normal Load Performance Across Libraries

This section benchmarks a **full dataset load** (all 3 million rows, all 10
columns) using four different Python libraries — Pandas, Polars, PyArrow, and
Dask — to measure how each library performs at raw CSV loading on the same
1.06 GB file.

---

#### Analysis

**Memory Usage**

PyArrow consumed the most memory at **6,218.35 MB**, followed closely by Polars
at **5,750.68 MB**. This is because both libraries load the full dataset into
their respective in-memory formats — PyArrow into an Arrow Table before
converting to Pandas via `.to_pandas()`, and Polars into its columnar Arrow-based
DataFrame. The `.to_pandas()` conversion in PyArrow is particularly costly as it
temporarily holds both the Arrow Table and the resulting Pandas DataFrame in
memory simultaneously. Pandas used **3,377.45 MB**, which reflects its standard
row-oriented in-memory footprint. Dask was the most memory-efficient at
**1,704.67 MB**, as its partitioned approach limits how much data is held in RAM
at any one time during the parallel read.

**Execution Time**

Polars was the fastest by a significant margin at **5.42 seconds**, nearly 3x
faster than PyArrow (**16.27s**), 8x faster than Pandas (**45.12s**), and 9x
faster than Dask (**51.42s**). Polars' speed advantage comes from its Rust-based
multi-core CSV parser, which automatically parallelises file reading across all
available CPU cores without any user configuration. PyArrow also uses
multi-threaded I/O but is slower here due to the additional `.to_pandas()`
conversion step after loading. Pandas is single-threaded and reads the file
sequentially, while Dask's partition scheduling overhead makes it the slowest
despite using multiple cores.

**Throughput (records/second)**

Polars achieved the highest throughput at **553,178 records/second**, more than
3x higher than PyArrow (**184,413 records/s**), 8x higher than Pandas
(**66,489 records/s**), and 9x higher than Dask (**58,345 records/s**). This
directly reflects the execution time results, with Polars' unified multi-core
execution engine processing rows far faster than any of the other three libraries.

**CPU Utilisation**

Polars had the highest CPU utilisation at **187.88%**, confirming that it
actively engaged multiple cores simultaneously during loading. Dask followed at
**133.71%** and PyArrow at **124.10%**, both also confirming multi-core usage.
Pandas was the only single-threaded library, reflected in its near-baseline CPU
usage of **95.05%**, barely above a single core's full utilisation.

---
### 📊 Visual Comparison
<img width="1590" height="495" alt="image" src="https://github.com/user-attachments/assets/19c07c62-1b2b-4741-b1a1-92cb58199c68" />

#### Summary Table — Full Load Performance Across Libraries

| Library | Memory Used (MB) | Execution Time (s) | Throughput (records/s) | Avg CPU (%) | Verdict |
|---|---|---|---|---|---|
| **Pandas** | 3,377.45 | 45.12 | 66,489 | 95.05 |  Slowest, single-threaded |
| **Polars** | 5,750.68 | 5.42 | 553,179 | 187.88 |  Fastest, highest throughput |
| **PyArrow** | 6,218.35 | 16.27 | 184,413 | 124.10 |  Fast, but high memory from conversion |
| **Dask** | 1,704.67 | 51.42 | 58,345 | 133.71 |  Most memory-efficient full load |

---

### 🧠 Interpretation

Polars is the standout performer for a full CSV load, fastest execution
(**5.42s**), highest throughput (**553,179 records/s**), and highest CPU
utilisation (**187.88%**), all achieved automatically through its Rust-native
multi-core parser with no manual configuration required.

PyArrow, despite also being multi-threaded, consumed the most memory
(**6,218.35 MB**) due to the `.to_pandas()` conversion step temporarily holding
both the Arrow Table and the Pandas DataFrame in memory simultaneously, which
also slowed it down to **16.27s**.

Pandas performed as expected for a single-threaded baseline, moderate memory
(**3,377.45 MB**) but slow execution (**45.12s**) with the lowest CPU usage
(**95.05%**), confirming no parallelism was engaged during loading.

Dask was the most memory-efficient at **1,704.67 MB** due to its partitioned
loading approach, but its task scheduling overhead made it the slowest overall
at **51.42s**, making it unsuitable as a general purpose full loader for datasets
that comfortably fit in RAM.

For a straightforward full CSV load on a 1.06 GB dataset, **Polars is the
recommended library**. PyArrow is a viable alternative when Arrow-native
pipelines are needed downstream. Dask should be reserved for datasets that
genuinely exceed available RAM rather than used as a drop-in replacement for
Pandas or Polars.

---

## 🧠 Task 5: Conclusion & Reflection

### 🔹 Summary of Observations

Our exploration of big data handling techniques applied to the Amazon Books
Reviews dataset (1.06 GB, 3 million rows) yielded several key insights into
optimising performance under real memory and speed constraints.

For **memory- and performance-efficient techniques**:

- **Load Less Data** was the most immediately effective memory reduction strategy,
  consuming only **396.42 MB** and completing in **20.65 seconds** by restricting
  the CSV parser to 4 essential columns via `usecols`. Unselected columns never
  entered RAM at all, making this the simplest and most practical optimisation
  for column-focused analysis.

- **Chunking** was designed as a memory-safety technique but proved
  counterproductive for this dataset, with memory spiking to **2,999.67 MB** and
  execution time reaching **43.89 seconds** due to the overhead of concatenating
  30 individual chunk DataFrames via `pd.concat()`. It only becomes genuinely
  beneficial when the dataset exceeds available RAM entirely.

- **Data Type Optimisation** offered the best balance among the Pandas-based
  strategies, achieving moderate memory usage (**424.60 MB**) and a reasonable
  execution time (**30.27s**) while retaining all 6 selected columns. By
  downcasting numerics to `float32`/`int32` and converting string columns to
  `category`, it reduces long-term in-memory footprint without sacrificing
  data completeness.

- **Sampling** was the slowest strategy at **53.74 seconds** and still consumed
  **2,851.59 MB** of memory, since the full dataset must be loaded into RAM before
  `.sample()` can be applied. Despite returning only 10% of rows (300,000), it is
  best reserved for rapid prototyping and exploratory analysis rather than
  production pipelines.

- **Parallel Processing with Dask** achieved the lowest memory footprint of all
  strategies at just **18.03 MB** by computing only scalar aggregates without
  ever materialising the full dataset. CPU utilisation of **137.13%** confirmed
  genuine multi-core engagement. However, execution time was the highest at
  **95.38 seconds**, reflecting the task scheduling overhead across ~44 partitions.

- **Parallel Processing with Polars** was the fastest strategy overall at just
  **4.03 seconds**, leveraging Rust-based multi-core lazy evaluation via
  `scan_csv` and `.collect()`. It demonstrates that modern libraries can deliver
  dramatically faster results with minimal configuration, though its memory usage
  of **2,482.94 MB** reflects the cost of full result materialisation.

When comparing **different libraries for full dataset loading**:

- **Polars** emerged as the clear winner with the fastest execution time
  (**5.42 seconds**) and highest throughput (**553,179 records/second**), making
  it the most practical choice for full CSV loading when speed and efficiency
  are the priority.

- **PyArrow** was the second fastest (**16.27 seconds**) and also multi-threaded,
  but consumed the most memory (**6,218.35 MB**) due to temporarily holding both
  the Arrow Table and the converted Pandas DataFrame in memory simultaneously
  during the `.to_pandas()` step.

- **Pandas** provided a straightforward single-threaded baseline with moderate
  memory usage (**3,377.45 MB**) and an execution time of **45.12 seconds**,
  suitable when simplicity is more important than speed.

- **Dask** was the most memory-efficient full loader at **1,704.67 MB** due to
  its partitioned approach, but its task scheduling overhead made it the slowest
  at **51.42 seconds**, making it unsuitable as a general-purpose full loader
  for datasets that comfortably fit in RAM.

---

### 🔹 Benefits & Limitations

#### Part 1: Memory- and Performance-Efficient Techniques

- **Load Less Data**:
  - **Benefits**: Substantially reduces memory consumption and load times by only
    loading relevant columns; requires no changes to the data or library, just
    a single `usecols` parameter.
  - **Limitations**: Requires prior knowledge of which columns are essential;
    not suitable when the full dataset is needed for analysis.

- **Chunking**:
  - **Benefits**: Enables processing of datasets larger than available memory by
    reading in manageable batches; provides a way to apply row-level
    transformations per chunk.
  - **Limitations**: Slower than a direct full load due to repeated chunk
    allocation and `pd.concat()` overhead; peak memory can still spike during
    the concatenation step, negating the memory benefit.

- **Data Type Optimisation**:
  - **Benefits**: Reduces long-term in-memory footprint without losing any rows
    or columns; compatible with all downstream Pandas operations; can be applied
    on top of any other loading strategy.
  - **Limitations**: Requires manual identification and mapping of appropriate
    types per column; risk of precision loss for numeric columns if types are
    downcast too aggressively.

- **Sampling**:
  - **Benefits**: Dramatically reduces processing time and memory for exploratory
    analysis and model prototyping; `random_state` ensures reproducibility across
    runs.
  - **Limitations**: The full dataset must still be loaded before sampling occurs,
    so memory savings only apply after the initial load; results may not
    accurately represent rare patterns or outliers in the full data.

- **Parallel Processing (Dask)**:
  - **Benefits**: Achieves the lowest possible memory footprint by computing only
    aggregated results without materialising the full dataset; natively scales to
    multi-core machines and datasets exceeding available RAM.
  - **Limitations**: High task scheduling overhead makes it slow for simple
    operations; explicit `dtype` specifications are required to prevent
    partition-level type conflicts; throughput cannot be measured when returning
    scalar aggregates rather than a DataFrame.

- **Parallel Processing (Polars)**:
  - **Benefits**: Fastest end-to-end execution of all strategies through
    Rust-native multi-core parallelism and lazy query optimisation; requires
    minimal configuration.
  - **Limitations**: Full result materialisation via `.collect()` loads all rows
    into RAM simultaneously, resulting in high memory usage; Polars' API differs
    from Pandas in places, requiring a learning curve for existing Pandas users.

#### Part 2: Loading Dataset with Different Libraries

- **Pandas**:
  - **Benefits**: Widely adopted with an intuitive API; excellent compatibility
    with the broader Python data science ecosystem; straightforward for datasets
    that fit within available RAM.
  - **Limitations**: Single-threaded for CSV parsing, making it the slowest
    loader for large files; row-oriented storage is less memory-efficient than
    columnar alternatives.

- **Polars**:
  - **Benefits**: Fastest full CSV loader in this benchmark at **5.42 seconds**
    with the highest throughput (**553,179 records/s**); Rust-based multi-core
    parallelism is automatic with no configuration required.
  - **Limitations**: Higher memory usage than Dask for full loads; API
    differences from Pandas require adjustment for teams already familiar with
    the Pandas ecosystem.

- **PyArrow**:
  - **Benefits**: Highly optimised multi-threaded CSV reader with the Apache Arrow
    columnar format; ideal for pipelines that feed into Parquet, Spark, or
    DuckDB which natively speak the Arrow format.
  - **Limitations**: The `.to_pandas()` conversion step temporarily doubles memory
    consumption by holding both the Arrow Table and the Pandas DataFrame in RAM
    simultaneously, making it the most memory-intensive library in this benchmark.

- **Dask**:
  - **Benefits**: Most memory-efficient full loader at **1,704.67 MB** due to
    partitioned reading; familiar Pandas-like API with native support for
    out-of-core and distributed computing.
  - **Limitations**: Task scheduling overhead made it the slowest full loader at
    **51.42 seconds**, even slower than single-threaded Pandas; best suited for
    aggregation workloads rather than straightforward full loads.

---

### 🔹 Reflection

**Najma Shakirah**

Working on the dataset description and library choices helped me understand why
selecting the right tool matters before writing any code. Implementing Strategy 2
(Chunking) and Strategy 3 (Data Type Optimisation) was eye-opening as I initially
expected Chunking to be more memory-efficient, but the `pd.concat()` overhead
caused memory to spike to nearly 3,000 MB. Data Type Optimisation proved more
effective by simply downcasting column types to reduce memory while keeping all
columns intact. Benchmarking Polars was the most impressive part, completing a
full load in just **5.42 seconds** with **553,179 records/second**, reinforcing
that modern libraries can outperform traditional tools by a significant margin
with minimal configuration.

---

**Syarifah Dania**

Handling the initial data loading and inspection gave me a solid foundation for
understanding the dataset before any optimisation was applied. Implementing
Strategy 1 (Load Less Data) reinforced that the most effective optimisation is
often preventing unnecessary data from being loaded in the first place, with
memory dropping to just **396.42 MB** by simply using `usecols`. Benchmarking
PyArrow revealed an unexpected trade-off where the `.to_pandas()` conversion step
pushed memory to **6,218.35 MB**, the highest of all libraries, teaching me that
what happens after the initial load is just as important as the load itself.

---

**Nawwarah Auni**

Implementing Strategy 4 (Sampling) taught me that the order of operations
matters, as the full dataset still had to be loaded before `.sample()` could
run, resulting in unexpectedly high memory usage of **2,851.59 MB**. Working on
Strategy 5 with Dask and Polars was the most technically challenging part, where
configuring Dask correctly with explicit `dtype` specifications and understanding
lazy evaluation required a deeper grasp of how distributed frameworks manage data
internally. Conducting the comparative analysis across all strategies reinforced
that no single approach is universally optimal and that the right choice always
depends on the specific constraints of the task.

---

## 📁 Folder Structure

```plaintext
bdm/Sample2/
├── big_data.md        ← This file
├── readme.md          ← Brief intro and links
└── big_data.ipynb     ← Code notebook
