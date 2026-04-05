# 📘 Assignment 2: Mastering Big Data Handling

**Group Members**:  
- Student 1: *Goh Jiale, A22EA0043*  
- Student 2: *Yong Wern Jie, A22EC0121*

---

## 📝 Task 1: Dataset Selection

### 📌 Dataset Overview

* **Name**: *🎹 960K Spotify Songs With Lyrics Data 🎵*
* **Source**: [Kaggle – bwandowando](https://www.kaggle.com/datasets/bwandowando/spotify-songs-with-attributes-and-lyrics)
* **Domain**: *Music / Entertainment*
* **File Size**: *1.54 GB*
* **Shape**: *955,320 rows × 17 columns*


### 📖 Description

This dataset is an enriched compilation built by combining multiple large-scale Spotify-related datasets, including:

* *Spotify 1M+ Tracks*,
* *Spotify + Genius Dataset*,
* *30K Spotify Songs*,
* *6K Spotify Playlists*, and more.

From over 3.3 million tracks submitted to the Spotify Lyrics API, about **960,000** were matched with usable lyrics. These tracks include audio attributes (like tempo, energy, and acousticness), metadata (such as artist and album), and lyrical content—making the dataset ideal for both **audio signal processing** and **natural language processing** applications.

> ⚠️ Note:
>
> * Some songs do **not** have album information.
> * A portion of the lyrics lack properly annotated `startTimeMs` values.
> * Not every track contains lyrics.


### 🔍 Key Features

* **Track metadata**: name, artist(s), album
* **Audio features**: danceability, energy, tempo, loudness, valence, etc.
* **Lyrics**: complete song lyrics with optional timestamp annotations
* **Merged sources**: enriched using data from multiple Kaggle contributors and lyric APIs


### 📊 Data Column Description

| Column Name        | Data Type | Description                                                         |
| ------------------ | --------- | ------------------------------------------------------------------- |
| `id`               | object    | Unique Spotify track ID                                             |
| `name`             | object    | Name of the song                                                    |
| `album_name`       | object    | Name of the album (may be missing for some entries)                 |
| `artists`          | object    | Artist(s) who performed the song                                    |
| `danceability`     | float64   | Suitability for dancing (0.0 = low, 1.0 = high)                     |
| `energy`           | float64   | Intensity and activity level (0.0 = calm, 1.0 = energetic)          |
| `key`              | object    | Musical key (e.g., C, D#, F#)                                       |
| `loudness`         | float64   | Loudness in decibels (typically -60 to 0 dB)                        |
| `mode`             | object    | Modality of the song: major or minor                                |
| `speechiness`      | float64   | Presence of spoken words (higher = more speech-like)                |
| `acousticness`     | float64   | Confidence score of acoustic quality (0.0 to 1.0)                   |
| `instrumentalness` | float64   | Likelihood that the track is instrumental (0.0 to 1.0)              |
| `liveness`         | float64   | Probability that the track was performed live                       |
| `valence`          | float64   | Musical positivity (0.0 = sad, 1.0 = happy/upbeat)                  |
| `tempo`            | float64   | Tempo in beats per minute (BPM)                                     |
| `duration_ms`      | float64   | Length of the track in milliseconds                                 |
| `lyrics`           | object    | Full lyrics of the song (may include timestamps like `startTimeMs`) |

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
   !kaggle datasets download -d bwandowando/spotify-songs-with-attributes-and-lyrics
   ```

4. **Unzipped the Dataset File**
   Extracted the dataset ZIP file:

   ```bash
   !unzip spotify-songs-with-attributes-and-lyrics.zip
   ```

5. **Loaded a Sample (100 Rows) Using `pandas.read_csv()`**
   This is to allow quicker inspection without overloading memory:

   ```python
   import pandas as pd
   df = pd.read_csv('songs_with_attributes_and_lyrics.csv', nrows=1000000)
   ```

---

### 🔹 Dataset Inspection

#### 📌 First 5 Rows

```python
df['lyrics_short'] = df['lyrics'].astype(str).str.slice(0, 100) + '...'

print("First 5 rows of the dataset:")
display(df.drop(columns=['lyrics']).head())
df = df.drop(columns=['lyrics_short'])
```
> ✅ *The `lyrics` column contains very long strings, so we truncated it for display to provide a more concise overview of the dataset’s structure.*

|index|id|name|album\_name|artists|danceability|energy|key|loudness|mode|speechiness|acousticness|instrumentalness|liveness|valence|tempo|duration\_ms|lyrics\_short|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0|0Prct5TDjAnEgIqbxcldY9|\!|UNDEN\!ABLE|\['HELLYEAH'\]|0\.415|0\.605|7|-11\.157|1|0\.0575|0\.00116|0\.838|0\.471|0\.193|100\.059|79500\.0|He said he came from Jamaica, he owned a couple acres A couple fake visas 'cause he never got his \.\.\.|
|1|2ASl4wirkeYm3OWZxXKYuq|\!\!|NaN|Yxngxr1|0\.788|0\.648|7|-9\.135|0|0\.315|0\.9|0\.0|0\.176|0\.287|79\.998|114000\.0|Fucked a bitch, now she running with my kids And you said I never listen, yeah, yeah Yeah, yeah, y\.\.\.|
|2|69lcggVPmOr9cvPx9kLiiN|\!\!\! - Interlude|Where I Belong EP|\['Glowie'\]|0\.0|0\.0354|7|-20\.151|0|0\.0|0\.908|0\.0|0\.479|0\.0|0\.0|11413\.0|Oh, my God, I'm going crazy \.\.\.|
|3|4U7dlZjg1s9pjdppqZy0fm|\!\!De Repente\!\!|Un Palo Al Agua \(20 Grandes Canciones\)|\['Rosendo'\]|0\.657|0\.882|5|-6\.34|1|0\.0385|0\.0074|1\.27e-05|0\.0474|0\.939|123\.588|198173\.0|Continuamente se extraña la gente si no puede ser verdad que de repente tan fácilmente material sin\.\.\.|
|4|4v1IBp3Y3rpkWmWzIlkYju|\!\!De Repente\!\!|Fuera De Lugar|\['Rosendo'\]|0\.659|0\.893|5|-8\.531|1|0\.0411|0\.0922|1\.91e-05|0\.0534|0\.951|123\.6|199827\.0|Continuamente se extraña la gente si no puede ser verdad que de repente tan fácilmente material sin\.\.\.|
---

#### 📐 Shape of the Dataset

```python
print(f"\nDataset Shape:\nRows: {df.shape[0]}, Columns: {df.shape[1]}")
```

![image](https://github.com/user-attachments/assets/1fb696c5-2295-4e68-bbec-ffd07d719fc4)


---

#### 🏷️ Column Names and Data Types

```python
display(df.dtypes.to_frame(name='Data Type').T)
```
![image](https://github.com/user-attachments/assets/5112b408-7ca5-41de-8339-6b2e3141c67b)

---

#### 📋 Summary Info

```python
df.info()
```

![image](https://github.com/user-attachments/assets/e2610d93-51b2-4d7a-849a-6e085e14f41e)


---

## 🛠️ Task 3: Apply Big Data Handling Strategies

### 🔹 **Part 1: Memory- and Performance-Efficient Techniques**

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
    mem_percent_after = (mem_after / total_ram) * 100
    mem_diff_percent = (mem_diff_mb / total_ram) * 100

    if isinstance(result, pd.DataFrame):
        num_records = len(result)
        throughput = round(num_records / exec_time, 2) if exec_time > 0 else None
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
To evaluate the effectiveness of different big data handling strategies, a custom `measure_performance` function was implemented. This function captures key performance metrics such as memory usage, CPU load, execution time, and throughput (records per second). This allows for objective comparison between various optimization techniques.

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
def load_less_data_pandas(file_path):
    selected_columns = [
        'danceability', 'energy', 'loudness', 'speechiness',
        'acousticness', 'instrumentalness', 'liveness',
        'valence', 'tempo', 'duration_ms'
    ]

    df = pd.read_csv(file_path, usecols=selected_columns)
    return df

performance_less_data, df_less_data = measure_performance(
    load_less_data_pandas,
    description="Load Less Data with Pandas",
    file_path="songs_with_attributes_and_lyrics.csv"
)

performance_df = pd.DataFrame([performance_less_data])
display(performance_df)
```

**Explanation**:  
When working with large datasets, it's often unnecessary to load all available columns into memory. By selecting only the relevant columns required for the task, memory usage and load time can be significantly reduced.

**Implementation Summary**:  
Only these columns were loaded from the CSV:

* `danceability`, `energy`, `loudness`, `speechiness`,
  `acousticness`, `instrumentalness`, `liveness`,
  `valence`, `tempo`, `duration_ms`

**Output Summary**:  
![image](https://github.com/user-attachments/assets/11870680-f399-4d76-ae5a-e38e9cfec9e7)



---

### 2. Use Chunking  

**Code**:
```python
# Read and concatenate chunks of 10,000 rows
def load_with_chunking(filepath):
    chunks = []
    for chunk in pd.read_csv(filepath, chunksize=10000):
        chunk.columns = chunk.columns.str.strip()
        chunks.append(chunk)
    df = pd.concat(chunks, ignore_index=True)
    return df

performance_chunking, df_chunked = measure_performance(
    load_with_chunking, 
    description="Chunked Load", 
    filepath="songs_with_attributes_and_lyrics.csv"
)

performance_df = pd.DataFrame([performance_chunking])
display(performance_df)
```

**Explanation**:  
Chunking is a memory-efficient strategy where large datasets are loaded in smaller parts (chunks) instead of all at once. This approach prevents memory overload and allows processing of datasets that may not fit entirely into memory. It’s especially useful for big data scenarios where performance and resource management are critical.

**Implementation Summary**:  
The dataset was loaded in chunks of 10,000 rows using `pandas.read_csv()` with the chunksize parameter. Each chunk was processed and then concatenated into a single DataFrame using pd.concat(). Column names were also stripped of leading/trailing whitespace for consistency.

**Output Summary**:  
![image](https://github.com/user-attachments/assets/3155b298-3912-430c-808a-ad18667e3942)


---

### 3. Optimize Data Types 
**Code**:
```python
def optimized_load(filepath, usecols=None, dtype_map=None):
    df = pd.read_csv(filepath, usecols=usecols, dtype=dtype_map)
    return df

# Define arguments for optimized_load
load_args = {
    "filepath": "songs_with_attributes_and_lyrics.csv",
    "usecols": [
        'danceability', 'energy', 'loudness', 'speechiness',
        'acousticness', 'instrumentalness', 'liveness',
        'valence', 'tempo', 'duration_ms'
    ],
    "dtype_map": {
        'danceability': 'float32',
        'energy': 'float32',
        'loudness': 'float32',
        'speechiness': 'float32',
        'acousticness': 'float32',
        'instrumentalness': 'float32',
        'liveness': 'float32',
        'valence': 'float32',
        'tempo': 'float32',
        'duration_ms': 'float32'
    }
}

performance_optimize_load, df_optimize_load = measure_performance(
    optimized_load, 
    description="Optimized Load with Dtype",
    **load_args
)

performance_df = pd.DataFrame([performance_optimize_load])
display(performance_df)

df_optimize_load.info()

```

**Explanation**:  
In large datasets, memory usage can become a major bottleneck, especially when working on machines with limited resources. By default, pandas uses data types like `float64`, which consume more memory than necessary.
This strategy focuses on optimizing memory by explicitly converting numeric columns to more memory-efficient types, such as `float32`. This can significantly reduce memory consumption without compromising the precision required for analysis.

**Implementation Summary**:  
Only the numeric audio feature columns were loaded, and each was explicitly cast to `float32` using the `dtype` argument in `pd.read_csv`.
The selected columns include:

* `'danceability'`, `'energy'`, `'loudness'`, `'speechiness'`, `'acousticness'`, `'instrumentalness'`, `'liveness'`, `'valence'`, `'tempo'`, `'duration_ms'`

This reduces their memory footprint compared to the default `float64`.

**Output Summary**:  
![image](https://github.com/user-attachments/assets/734cfc66-170c-4d8c-8a17-43b52a76321d)

---

### 4. Sampling  
**Code**:  
```python
def sampling(filepath, sample_fraction=0.1, usecols=None, dtype_map=None):
    df = pd.read_csv(filepath, usecols=usecols, dtype=dtype_map)
    sampled_df = df.sample(frac=sample_fraction, random_state=42)
    return sampled_df

# Define arguments for sampling
load_args = {
    "filepath": "songs_with_attributes_and_lyrics.csv",
    "sample_fraction": 0.1,
}

performance_sampling, df_sampling = measure_performance(
    sampling, 
    description="Sampling",
    **load_args
)

performance_df = pd.DataFrame([performance_sampling])
display(performance_df)

print(f"\nRows: {df_sampling.shape[0]}")
```
**Explanation**:  
Sampling is a technique used to reduce the size of a dataset by selecting a smaller, representative subset of the data. This is particularly useful for exploratory data analysis or testing models, as it reduces memory usage and speeds up computations. In this case, we randomly sampled **10%** of the dataset to work with a smaller, yet statistically representative, portion of the full data.


**Implementation Summary**:  
We applied **random sampling** using `pandas.DataFrame.sample()` with `frac=0.1`, which selects 10% of the rows from the dataset. A fixed `random_state=42` was used to ensure the sample is reproducible. No stratification or grouping was applied, making this a simple random sample across the entire dataset.

**Output Summary**:  
![image](https://github.com/user-attachments/assets/0314bde3-8368-4f9c-b09e-0236bd1e8e94)

---

### 5. Parallel Processing with Dask  
**Code**:  
```python
def load_with_dask(filepath):
    dtype_spec = {'key': 'object', 'mode': 'object', 'danceability': 'object'}
    ddf = dd.read_csv(filepath, on_bad_lines='skip', engine='python', dtype=dtype_spec)
    df = ddf.compute()
    return df

performance_dask, ddf_loaded = measure_performance(
    load_with_dask,
    description="Full Load with Dask (Lazy)",
    filepath="songs_with_attributes_and_lyrics.csv"
)

performance_df = pd.DataFrame([performance_dask])
display(performance_df)
```

**Explanation**:  
Dask enables parallel processing by breaking large datasets into smaller chunks and processing them concurrently across multiple CPU cores. In this implementation, `dask.dataframe.read_csv` is used to **load a large CSV file in parallel**, allowing faster data ingestion compared to pandas—especially for very large datasets. Dask handles memory more efficiently by **lazy-loading** the data and only computing the final result when explicitly instructed, which helps avoid memory overload on limited-resource machines.

**Implementation Summary**:  
* `dd.read_csv` reads the file in parallel chunks using multiple cores.
* The `on_bad_lines='skip'` and `engine='python'` options ensure robustness against malformed rows.
* A simplified `dtype_spec` is passed to avoid type inference errors.
* The `.compute()` method triggers the actual execution, combining all partitions into a standard pandas DataFrame.

This approach significantly improves performance for large datasets while maintaining flexibility and compatibility with the pandas ecosystem.

**Output Summary**:  
![image](https://github.com/user-attachments/assets/69449004-8cf8-48a6-adfb-de75e1b94f31)


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
