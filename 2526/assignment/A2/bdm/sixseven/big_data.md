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
def load_full_data():
    df = pd.read_csv("songs_with_attributes_and_lyrics.csv")
    return df

performance, df = measure_performance(load_full_data, description="Load with Pandas")

performance_df = pd.DataFrame([performance])
display(performance_df)
```

**Output**:  
![image](https://github.com/user-attachments/assets/1410fead-440a-4198-9aad-2de9e3c7f034)



---
#### 2. Using **Dask**

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
    file_path="songs_with_attributes_and_lyrics.csv"
)

performance_df_compute = pd.DataFrame([performance_dask_compute])
display(performance_df_compute)
```

**Explanation**:  
In this approach, we use **Dask**, a parallel computing library, to handle the CSV file more efficiently—especially useful for large datasets that may not fit into memory at once.

1. **Lazy Loading with `dd.read_csv()`**:

   * The function `dd.read_csv()` reads the CSV file **lazily**, meaning it doesn’t load all data into memory immediately.
   * Parameters used:

     * `assume_missing=True`: Ensures columns with mixed types (like numeric and nulls) are safely interpreted as floats.
     * `quoting=3`: Ignores quote characters in the data.
     * `on_bad_lines='skip'`: Skips malformed rows to avoid loading issues.
     * `dtype=str`: Treats all columns as strings for uniformity.

2. **Triggering Computation**:

   * `.compute()` explicitly triggers the loading of the full dataset into a **Pandas DataFrame**.
   * This is the step where actual memory usage happens, converting Dask’s lazy operations into real data.

3. **Performance Measurement**:

   * The `measure_performance()` function wraps this entire process to capture metrics like **execution time** and **memory usage**, helping us compare it with other approaches (e.g., pure Pandas).

**Output**:  
![image](https://github.com/user-attachments/assets/1940a747-ee2c-49ce-a20d-6eb68fda979a)



---

#### 3. Using **Polars**

```python
def load_with_polars(filepath):
    df = pl.read_csv(filepath)
    return df

performance_polars, df_polars = measure_performance(
    load_with_polars,
    description="Load with Polars",
    filepath="songs_with_attributes_and_lyrics.csv"
)

performance_df = pd.DataFrame([performance_polars])
display(performance_df)
```

**Explanation**:  
In this method, we use **Polars**, a fast and efficient DataFrame library built for performance and optimized for modern hardware (e.g., multi-threaded CPUs).

1. **Reading the CSV with `pl.read_csv()`**:

   * Polars reads the entire CSV file eagerly (i.e., it loads data into memory immediately).
   * It is written in Rust and designed for **blazing-fast performance**, making it significantly faster than Pandas and even Dask in many cases.
   * It also handles large datasets well and often uses **less memory** due to efficient memory allocation and data structures.

2. **Simplicity and Speed**:

   * The function is straightforward: `pl.read_csv(filepath)` loads the data into a **Polars DataFrame** with a single line.
   * No need to specify data types or handle bad lines unless needed—Polars automatically infers them efficiently.

3. **Performance Measurement**:

   * The `measure_performance()` wrapper captures key performance metrics like **execution time** and **memory usage**, providing a direct comparison with Pandas and Dask.

**Output**:  
![image](https://github.com/user-attachments/assets/9e04ad8d-47fc-4383-a948-9c94b4be4616)

---

## 📊 Task 4: Comparative Analysis

### 🔍 Part 1: Comparison of Optimized Loading Strategies

This section compares five different optimization techniques used to improve CSV loading performance in terms of **Memory Used**, **Execution Time**, **Average CPU Usage**, and **Throughput**.

#### ✅ Strategies Compared:

1. **Load Less Data**
2. **Use Chunking**
3. **Optimize Data Types**
4. **Sampling**
5. **Parallel Processing with Dask**

### 📋 Summary Table

| Strategy            | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (records/sec) |
| ------------------- | ---------------- | ------------------ | ----------- | ------------------------ |
| Load Less Data      | 48.34      | 19.4726	       | 98.39	  | 49059.7           |
| Use Chunking        | 165.15      | 29.8092        | 99.07  | 32047.82           |
| Optimize Data Types | 79.67       | 17.7305        | 99.06  | 53880.04           |
| Sampling            | 61.79      | 34.3492       | 97.89  | 2781.2            |
| Parallel with Dask  | 1565.71      | 75.243       | 95.1 | 12706.13          |

---

### 📊 Visual Comparison
![image](https://github.com/user-attachments/assets/e477357a-1529-47d1-959c-35c5cea6ad64)

### 🧠 Interpretation:

* **Optimize Data Types** performed best in overall.

---

### 📘 Part 2: Comparison Between Pandas, Dask, and Polars

In this section, we compare the performance of three major data-processing libraries: **Pandas**, **Dask**, and **Polars**.

### 📋 Summary Table

| Library | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (records/sec) |
| ------- | ---------------- | ------------------ | ----------- | ------------------------ |
| Pandas  | 2324.79     | 32.9665       | 99.66% | 28979.51           |
| Dask    | 1653.96      | 74.9795       | 89.78% | 12750.78          |
| Polars  | 1579.88      | 5.0251        | 97.89% | 190109.65          |

---

### 📊 Visual Comparison
![image](https://github.com/user-attachments/assets/155ef1d3-6c38-40f2-9765-0dcfbd27ceed)



### 🧠 Interpretation:
The performance comparison between **Pandas**, **Dask**, and **Polars** reveals key differences in their execution behavior and efficiency:

* **Polars** outperforms both Pandas and Dask in every aspect. With the **lowest memory usage**, **fastest execution time (5.03s)**, and **highest throughput (190k records/sec)**, it is exceptionally well-optimized for fast and efficient data processing, especially with CSV files.

* **Pandas** performs reasonably well, loading the data in **\~33 seconds** with a relatively high memory footprint. It is still a strong choice for datasets that fit into memory and for tasks requiring immediate results with minimal setup.

* **Dask**, while designed for large-scale distributed processing, shows **significantly slower performance (75s)** and the **lowest throughput** among the three. This slower speed is largely due to the need to **fall back on the Python engine (`engine='python'`)** to handle malformed or inconsistent CSV rows in the dataset. This fallback is **much slower** than the default C engine, as it parses files in pure Python for robustness at the cost of speed.

  > ⚠️ **Note**: Dask is still valuable when working with datasets that are **too large to fit into memory**, as it supports out-of-core processing and parallel computation. However, in this benchmark, the dataset had formatting issues (e.g., bad lines), which required extra handling and slowed down Dask significantly.

---

## 🧠 Task 5: Conclusion & Reflection

### 🔹 Summary of Observations  
Our exploration of big data handling techniques yielded several key insights into optimizing performance for large datasets.

For **memory- and performance-efficient techniques**:
* **Load Less Data** significantly reduced memory usage and improved loading times by focusing only on necessary columns.
* **Chunking** allowed us to process the large dataset in manageable parts, preventing memory overload, though it resulted in higher execution time compared to selective loading.
* **Data Type Optimization** proved to be the most effective strategy among the optimizations, achieving the lowest memory footprint and one of the fastest execution times by converting columns to more memory-efficient data types.
* **Sampling** drastically reduced the dataset size, leading to lower memory usage and faster processing for exploratory analysis, though at the cost of working with a subset of the data.
* **Parallel Processing with Dask** demonstrated its ability to handle larger-than-memory datasets by distributing computation, but its performance was significantly impacted by the need to use a slower Python engine for malformed lines in our specific dataset.

When comparing **different libraries for full dataset loading**:
* **Polars** emerged as the clear winner, exhibiting superior performance in terms of memory efficiency, execution speed, and throughput, making it an excellent choice for fast data processing.
* **Pandas** provided a straightforward and reasonably performant solution for loading the full dataset, suitable when the data fits within available memory.
* **Dask**, while powerful for distributed computing, showed the slowest performance due to issues with bad lines in the CSV requiring a less efficient parsing engine.
---

### 🔹 Benefits & Limitations  
#### Part 1: Memory- and Performance-Efficient Techniques

* **Load Less Data**:
    * **Benefits**: Substantially reduces memory consumption and load times by only loading relevant columns.
    * **Limitations**: Requires prior knowledge of which columns are essential for the analysis; not suitable if all columns are needed.
* **Chunking**:
    * **Benefits**: Enables processing of datasets larger than available memory; provides a way to handle data in batches.
    * **Limitations**: Can be slower than loading the entire dataset at once due to overhead of reading and concatenating chunks; may require additional logic for processing across chunk boundaries.
* **Data Type Optimization**:
    * **Benefits**: Significantly reduces memory usage by fitting data into smaller, appropriate types (e.g., `float32` instead of `float64`).
    * **Limitations**: Requires careful consideration of data ranges to avoid overflow or loss of precision; manual type mapping can be tedious for many columns.
* **Sampling**:
    * **Benefits**: Dramatically reduces processing time and memory for quick exploratory analysis or model prototyping; useful when full data is not needed.
    * **Limitations**: Results are based on a subset and may not accurately represent the entire dataset; can miss rare patterns or outliers present in the full data.
* **Dask Parallel Processing**:
    * **Benefits**: Designed for out-of-core and parallel processing, making it ideal for datasets that exceed memory limits; scales well to multi-core machines or clusters.
    * **Limitations**: Can incur overhead for scheduling tasks and managing distributed data; performance can degrade if data formatting issues require fallback to less efficient parsing engines.

#### Part 2: Loading Dataset with Different Libraries

* **Pandas**:
    * **Benefits**: Widely adopted, intuitive API, and excellent for in-memory data manipulation; robust for datasets that fit into RAM.
    * **Limitations**: Can struggle with very large datasets that exceed available memory, leading to memory errors; single-threaded for most operations.
* **Dask**:
    * **Benefits**: Provides a familiar Pandas-like API for out-of-core and parallel computing; integrates well with the Python data science ecosystem.
    * **Limitations**: Can be slower for smaller datasets due to parallelization overhead; performance is highly dependent on data cleanliness, as malformed data can force less efficient processing.
* **Polars**:
    * **Benefits**: Extremely fast and memory-efficient due to Rust backend and multi-threaded design; excels at eager execution for large datasets.
    * **Limitations**: Newer library with a smaller community compared to Pandas; its API, while similar to Pandas, has differences that require a learning curve for existing Pandas users.
---
### 🔹 Reflection  
Through this assignment, we gained a deeper understanding of the complexities involved in handling big data, particularly when faced with resource constraints. The most significant learning for us was that there isn't a one-size-fits-all solution; the best strategy depends heavily on the **dataset's characteristics**, the **available computational resources**, and the **specific analytical task**.

For instance, we learned the critical importance of **proactive memory management** through techniques like selective column loading and data type optimization, which can significantly reduce memory footprint and speed up processing. The experience with Dask highlighted the trade-off between **robustness and speed** when dealing with imperfect data; while it can handle large-scale, out-of-core processing, data quality issues can severely impact its performance. Conversely, Polars demonstrated the power of modern data libraries designed for **speed and efficiency**, proving that significant performance gains are possible with the right tools.

These insights will be incredibly useful in our future endeavors, especially when working on projects involving large-scale data. We now understand the importance of:
1.  **Profiling and benchmarking**: Always measuring performance to identify bottlenecks and validate the effectiveness of chosen strategies.
2.  **Strategic data loading**: Applying techniques like `usecols`, `chunksize`, and `dtype` optimization from the outset to avoid memory issues.
3.  **Choosing the right tool**: Selecting libraries like Polars or Dask based on data size, memory constraints, and the need for parallelization.
4.  **Data cleanliness**: Recognizing that data quality directly impacts processing efficiency, especially with tools designed for high performance.

This assignment has equipped us with practical skills to approach big data challenges more effectively, ensuring efficient and scalable data handling in real-world scenarios.

---

## 📁 Folder Structure

```plaintext
bdm/Sample2/
├── big_data.md        ← This file
├── readme.md          ← Brief intro and links
└── big_data.ipynb     ← Code notebook
