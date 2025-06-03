# 📘 Assignment 2: Mastering Big Data Handling

**Group Members**:  
- Student 1: *Goh Jiale, A22EA0043*  
- Student 2: *Yong Wern Jie, A22EC0121*

---

## 📌 Introduction

*Write a brief overview of the importance of big data handling and what this assignment covers.*

---

## 🎯 Learning Outcomes

1. Identify challenges and limitations in traditional big data processing.
2. Apply strategies to manage and analyze large datasets efficiently.
3. Compare performance between traditional and optimized methods.

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
![image](https://github.com/user-attachments/assets/7c06b263-e209-4469-9211-fc0ecca2b19b)


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
![image](https://github.com/user-attachments/assets/661097a0-6161-4697-904c-ccbb740dbb93)


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
**Explanation**:  
*How Dask helps in parallelizing the workload.*  

**Implementation Summary**:  
*Which operations were parallelized.*

**Output Summary**:  
*Comparison in performance or output.*

---

## 📊 Task 4: Comparative Analysis

| Metric                | Traditional Pandas | Optimized Strategies |
|-----------------------|--------------------|----------------------|
| Memory Usage          | *e.g., 1.5GB*       | *e.g., 300MB*        |
| Execution Time        | *e.g., 120s*        | *e.g., 40s*          |
| Ease of Processing    | *Subjective score or remarks* | *Remarks* |

*You may include charts, plots, or bullet points here for additional analysis.*

---

## 🧠 Task 5: Conclusion & Reflection

### 🔹 Summary of Observations  
*Summarize the main findings from each strategy.*

### 🔹 Benefits & Limitations  
- **Load Less Data**:  
- **Chunking**:  
- **Data Type Optimization**:  
- **Sampling**:  
- **Dask Parallel Processing**:  

### 🔹 Reflection  
*What did you learn about handling big data, and how will it be useful in the future?*

---

## 📁 Folder Structure

```plaintext
bdm/your_group/
├── big_data.md        ← This file
├── readme.md          ← Brief intro and links
└── big_data.ipynb     ← Code notebook
