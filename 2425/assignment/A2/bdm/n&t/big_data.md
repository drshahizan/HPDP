# 🎧 Big Data Handling Report: Spotify Charts Dataset

## 1. 📁 Dataset Overview  

### 🎵 Dataset: **Spotify Charts - Global & Regional**  
- **Source:** [Kaggle - Spotify Charts Dataset](https://www.kaggle.com/datasets/dhruvildave/spotify-charts)  
- **File Size:** ~3.48 GB  
- **Entries:** `26,173,514` rows and `9` columns  
- **Domain:** Music Streaming, Time Series  
- **Date Range:** Spanning from 2017 onward  

This dataset contains daily rankings for Spotify’s **Top 200** and **Viral 50** charts across multiple regions. Each row represents a song's rank on a specific chart in a specific region on a given date. It is ideal for exploring trends in music popularity and practicing large-scale data handling techniques.

---

### 📊 Dataset Snapshot

| Column Name | Description |
|-------------|-------------|
| `title`     | Name of the song as listed on Spotify. |
| `rank`      | The position of the song on the chart for the specific day and region. |
| `date`      | The chart date (daily granularity). |
| `artist`    | Name of the artist(s) of the song. |
| `url`       | Direct URL to the Spotify track. |
| `region`    | The geographical region (e.g., US, Global, Brazil). |
| `chart`     | The chart type – either **top200** or **viral50**. |
| `trend`     | Indicates if the song’s ranking is **new**, **re-entry**, or unchanged. |
| `streams`   | Number of times the song was streamed on that day in the region. |

> 📌 **Observation:**  
> The dataset includes a mix of categorical (`region`, `chart`, `trend`) and numerical (`rank`, `streams`) data. The text-heavy columns such as `title` and `artist` consume memory due to their string nature.


## 2. ⏱️📊 Measurement Techniques: Time & Memory

To evaluate and compare the performance of various big data handling strategies, we consistently measured both **execution time** and **memory usage**.

### 🧪 Tools Used

- **`time` module** – to track how long each strategy took to run.
- **`pandas.DataFrame.memory_usage(deep=True)`** – to calculate the full memory footprint of the loaded data.

### ⏱️ Time Measurement Snippet

```python
import time

start_time = time.time()
# Data loading or processing code here
end_time = time.time()

print("Time Taken:", (end_time - start_time:.2f), "seconds")
```

### 🧠 Memory Usage Snippet

```python
memory_usage = df.memory_usage(deep=True).sum() / (1024**3)
print("Memory Usage:", (memory_usage:.2f), "GB")
```

These tools were used after each strategy to benchmark improvements in resource efficiency and processing speed.


## 3. 🐼 Traditional Data Load (Baseline)
As a baseline, we loaded the full dataset using the most common method — reading **all rows** and **all columns** into memory without any optimization. This represents the default approach many users take when first working with large CSV files.

### ✅ What Was Done

- Loaded the full dataset with **no column filtering** or **data type optimization**.
- Used standard `pandas.read_csv()` on the entire file.

### 🧾 Code Snippet

```python
df = pd.read_csv("spotify_data/charts.csv")
````

### 📈 Results

| Metric             | Value                         |
| ------------------ | ----------------------------- |
| 🔹 Load Time       | **81.13 seconds**             |
| 🔹 Memory Usage    | **13,431.49 MB** (\~13.43 GB) |
| 🔹 DataFrame Shape | `(26,173,514, 9)`             |

> 🧠 **Data Types**
> All columns loaded in default types — most strings default to `object`, and numbers as `int64` or `float64`.


### 📌 Observation

This baseline method is **simple but very inefficient** for large-scale data.
The **full 9-column load** puts immense pressure on memory (13+ GB), especially due to multiple `object` columns (`title`, `artist`, `url`, etc.).
> ⚠️ While convenient for exploration, this method is **impractical** for use on machines with limited RAM or when working within platforms like **Google Colab**, where session crashes are common with datasets this size.


## 4. ⚙️ Big Data Handling Strategies

## 4.1 🧃 Load Less Data

One of the simplest yet most effective strategies for handling large datasets is to **load only the necessary columns** rather than the entire file. This reduces both **memory usage** and **I/O overhead** during the reading process.

### ✅ What Was Done

- Selected **only 5 relevant columns**: `title`, `rank`, `date`, `artist`, and `region`.
- Used the `usecols` parameter in `pandas.read_csv()` to load a subset of the data.

### 🧾 Code Snippet

```python
use_cols = ['title', 'rank', 'date', 'artist', 'region']
df_less = pd.read_csv('spotify_data/charts.csv', usecols=use_cols)
````

### 📈 Results

| Metric             | Value                      |
| ------------------ | -------------------------- |
| 🔹 Load Time       | **69.64 seconds**          |
| 🔹 Memory Usage    | **7266.65 MB** (\~7.27 GB) |
| 🔹 DataFrame Shape | `(26,173,514, 5)`          |

> 🧠 **Data Types**
> `title`, `artist`, `date`, `region` → `object` (string)
> `rank` → `int64`

---

### 📌 Observation

Column filtering offers a quick memory improvement and simplifies analysis by removing irrelevant data. However, the **massive row count (26M+)** and presence of **string-heavy columns** still result in **significant memory consumption**.
This step is a solid first move, but further strategies are needed to make the dataset more manageable.

## 4.2 🍰 Chunking

Instead of loading the entire dataset at once, **chunking** allows reading large files in smaller, manageable parts. This approach improves performance and makes it possible to **process datasets that might not fit in memory** all at once — especially useful in limited environments like Google Colab.

### ✅ What Was Done

- Used `pandas.read_csv()` with `chunksize=500000` to read the file in 53 smaller parts.
- Each chunk was stored in memory temporarily and concatenated after timing.
- Total row count and memory usage were tracked post-concatenation.

### 🧾 Code Snippet

```python
chunk_size = 500000
chunks = []
for chunk in pd.read_csv('spotify_data/charts.csv', chunksize=chunk_size):
    chunks.append(chunk)

df_full = pd.concat(chunks, ignore_index=True)
````

### 📈 Results

| Metric                  | Value                         |
| ----------------------- | ----------------------------- |
| 🔹 Chunks Processed     | **53**                        |
| 🔹 Total Rows Processed | **26,173,514**                |
| 🔹 Load Time            | **77.43 seconds**             |
| 🔹 Memory Usage         | **13,431.49 MB** (\~13.43 GB) |

> 🧠 **Data Types**
> Same as full load: `object` for strings, `int64`/`float64` for numbers.

---

### 📌 Observation

Chunking breaks the load process into smaller pieces, helping avoid **immediate memory spikes** and reducing the chance of **crashes or kernel failures**.
However, **concatenating all chunks at once** still results in high memory usage — similar to the traditional full load.
To fully benefit, chunking should ideally be combined with **streamed processing**, where each chunk is processed (e.g., filtered, aggregated) before moving to the next — avoiding full memory build-up.

This method is best when you want to **incrementally process** or **conditionally load** massive datasets.

## 4.3 ⚙️ Optimized During Load

This strategy involves specifying **data types explicitly during the CSV load** to reduce memory usage. Converting some columns to **categorical types** and using smaller numeric types can significantly optimize RAM consumption.

### ✅ What Was Done

- Defined specific `dtype` mappings for columns (`int16` for `rank`, `category` for `region` and `chart`, `float32` for `streams`).
- Parsed the `date` column as a datetime object to optimize date handling.
- Loaded the entire dataset with these optimized data types.

### 🧾 Code Snippet

```python
dtypes = {
    'rank': 'int16',
    'chart': 'category',
    'region': 'category',
    'streams': 'float32'
}

df_opt = pd.read_csv(
    'spotify_data/charts.csv',
    dtype=dtypes,
    parse_dates=['date']
)
````

### 📈 Results

| Metric             | Value                      |
| ------------------ | -------------------------- |
| 🔹 Load Time       | **191.54 seconds**         |
| 🔹 Memory Usage    | **8557.44 MB** (\~8.56 GB) |
| 🔹 DataFrame Shape | `(26,173,514, 9)`          |

> 🧠 **Data Types**
> Key optimized columns:
>
> * `rank` → `int16`
> * `region`, `chart` → `category`
> * `streams` → `float32`
> * `date` → `datetime64[ns]`
>   Other columns remain as `object`.

---

### 📌 Observation

Explicitly defining data types during load **substantially reduces memory usage** (\~36% reduction compared to full traditional load).
However, this optimization comes at the cost of **longer load times**, likely due to type conversions and parsing overhead.
This method is effective for large datasets where memory is a bottleneck and **accurate type representation** benefits downstream processing or querying.

## 4.4 🎲 Sampling

Sampling involves loading a **random subset of rows** instead of the full dataset, which drastically reduces memory use and load time. This approach is useful for exploratory analysis when working with very large datasets.

### ✅ What Was Done

- Used a **5% random sample** of rows from the CSV file during loading.
- Employed the `skiprows` parameter with a lambda function and `random.random()` to randomly skip rows.

### 🧾 Code Snippet

```python
import random

df_sample = pd.read_csv(
    'spotify_data/charts.csv',
    skiprows=lambda i: i > 0 and random.random() > 0.05
)
````

### 📈 Results

| Metric             | Value             |
| ------------------ | ----------------- |
| 🔹 Load Time       | **36.32 seconds** |
| 🔹 Memory Usage    | **672.75 MB**     |
| 🔹 DataFrame Shape | `(1,311,034, 9)`  |

---

### 📌 Observation

Random sampling offers a representative subset of the full dataset, maintaining the overall data distribution and key patterns. This makes it effective for exploratory analysis and prototyping while keeping resource use low. However, since it's only a fraction of the data, rare events or outliers may be underrepresented or missed entirely.

---


## 5. 📊 Comparative Analysis
![Strategy Comparison Graph](strategy_comparison.png)

*Figure: Load Time and Memory Usage across different data loading strategies.*

| Strategy            | Time Taken (seconds) | Memory Usage (MB) | Ease of Processing                | Notes                                                                                 |
| ------------------- | -------------------- | ----------------- | -------------------------------- | ------------------------------------------------------------------------------------- |
| Traditional Load    | 81.13                | 13431.49          | Moderate                         | Loads entire dataset; high memory and time usage due to full data size               |
| Load Less Data      | 69.64                | 7266.65           | Easier                          | Loads only selected columns, reducing memory and load time significantly             |
| Chunking            | 77.43                | 13431.49          | Harder                         | Loads data in chunks to handle large data, but total memory usage similar to full load |
| Optimize Data Types | 191.54               | 8557.44           | Moderate to Hard                | Longer load time due to type conversion but memory reduced from full load             |
| Sampling            | 36.32                | 672.75            | Easiest                        | Loads small representative sample, drastically reducing time and memory               |

> **Note:**  
> - Ease of processing reflects how straightforward it is to handle and manipulate the data after loading, with Sampling being easiest and Chunking requiring more manual effort.  
> - Sampling offers the benefit of a representative subset for faster experimentation or prototyping but may not capture all variability in data.



## 6. 🧠 Conclusion & Reflection

* Key takeaways
* Benefits vs limitations
* What you learned from this assignment

