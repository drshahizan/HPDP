
---

## 📄 big_data.md – Complete Markdown Report

---

# 🧠 Big Data Handling Strategies: MyAnimeList Anime Dataset

## 🎯 Assignment Overview

This report presents our implementation of **Assignment 2: Mastering Big Data Handling**, where we explored five different strategies to efficiently work with large datasets using three Python libraries:
- 🐼 **Pandas**
- 🦖 **Polars**
- 🚀 **Dask**

We used the **MyAnimeList final_animedataset.csv** dataset (size: ~4.5GB) to compare execution time and memory usage across these strategies.

---

## 📁 Dataset Details

| Property | Description |
|---------|-------------|
| **Name** | [MyAnimeList Dataset](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset) |
| **Source** | Kaggle |
| **File Used** | `final_animedataset.csv` |
| **Size** | ~4.5 GB (full file), ~3+ GB usable data |
| **Columns Used** | `username`, `anime_id`, `my_score`, `genre`, `type`, `score` |
| **Domain** | Anime user reviews, ratings, and metadata |

### 🔍 Sample Schema
```python
['username', 'anime_id', 'my_score', 'user_id', 'gender', 'title', 'type',
 'source', 'score', 'scored_by', 'rank', 'popularity', 'genre']
```

---

## 🔧 Applied Big Data Handling Strategies

We applied the following five strategies to manage the large dataset effectively:

---

## 🧪 Tools Used

| Tool/Library | Purpose |
|--------------|---------|
| 🐼 **Pandas** | For basic loading and processing |
| 🦖 **Polars** | For high-performance data loading and manipulation |
| 🚀 **Dask** | For out-of-core computation and parallel processing |
| 📊 **Matplotlib** | For visualizing execution time and memory usage |
| 🧮 **psutil** | For measuring memory consumption during operations |

---

### 1️⃣ Load Less Data (Only Required Columns)

Instead of loading all columns, we selected only relevant ones for analysis:
```python
cols_to_use = ['username', 'anime_id', 'my_score', 'genre', 'type', 'score']
```

**Libraries Tested**: Pandas, Polars, Dask  
**Result**: Reduced memory usage and faster load times.

---

### 2️⃣ Use Chunking (Pandas Only)

Processed the dataset in smaller batches using Pandas' chunking feature:
```python
for chunk in pd.read_csv('final_animedataset.csv', chunksize=100_000):
    process(chunk)
```

**Use Case**: Ideal for streaming or batch processing when RAM is limited.

---

### 3️⃣ Optimize Data Types

Reduced memory footprint by converting column types:
```python
dtypes = {
    'username': 'category',
    'anime_id': 'int32',
    'my_score': 'int8',
    'genre': 'category',
    'type': 'category',
    'score': 'float32'
}
```

**Libraries Tested**: Pandas, Polars  
**Result**: Significant memory savings without compromising usability.

---

### 4️⃣ Sampling

Used random sampling for fast prototyping and testing:
```python
df_sample = pd.read_csv('final_animedataset.csv', nrows=100_000)
```

**Use Case**: Great for early-stage development and model testing.

---

### 5️⃣ Parallel Processing with Dask

Used Dask for lazy evaluation and parallel processing:
```python
ddf = dd.read_csv('final_animedataset.csv', usecols=cols_to_use)
mean_score = ddf['score'].mean().compute()
```

**Use Case**: For out-of-core computation and distributed data handling.

---

## 📊 Performance Comparison Table

| Strategy              | Library     | Execution Time (s) | Memory Used (MB) |
|-----------------------|-------------|--------------------|------------------|
| Load Less Data        | Pandas      | 74.03              | 4771.56          |
| Load Less Data        | Polars      | 26.33              | 8521.61          |
| Load Less Data        | Dask        | 0.24               | 8523.00          |
| Chunking              | Pandas      | 77.15              | 1016.05          |
| Optimize Types        | Pandas      | 90.25              | 2312.83          |
| Optimize Types        | Polars      | 18.88              | 6067.03          |
| Sampling              | Pandas      | 0.31               | 6077.17          |
| Sampling              | Polars      | 0.95               | 5742.82          |
| Dask Full Processing  | Dask        | 87.14              | 3212.63          |

> ⚠️ Note: Dask's fast time (0.24s) reflects lazy evaluation. Use `.compute()` to measure real load time.

---

## 📈 Charts

Below are visual comparisons of the performance metrics.

### ⏱️ Execution Time (seconds)

![Execution Time Chart](executionTime.png)

### 💾 Memory Usage (MB)

![Memory Usage Chart](memoryUsage.png)

These charts were generated using `matplotlib` inside the Colab notebook and saved as PNG files.
You can find the Python code to generate these charts inside **Task 4 notebook**.

---

## 🧠 Comparative Analysis

### ⏱️ Execution Time Insights

- **Fastest Single Load**: `Polars` (26.33s for selective columns)
- **Slowest Method**: `Pandas` with type optimization (90.25s)
- **Best for Prototyping**: `Pandas` sampling (0.31s)

### 💾 Memory Usage Insights

- **Most Efficient**: `Pandas chunking` (~1GB peak)
- **High RAM Usage**: `Polars` (due to in-memory optimizations)
- **Lazy Evaluation**: `Dask` showed high memory but didn’t fully load until `.compute()`

---

## 🧾 Final Reflection

Through this assignment, we explored various big data handling strategies and compared their efficiency in terms of **execution time** and **memory usage**. We learned that:

- **Polars** offers the best performance in most scenarios due to its speed and optimized memory use.
- **Dask** is excellent for handling datasets larger than available RAM but requires understanding of lazy evaluation.
- **Pandas** remains user-friendly but struggles with large files unless combined with optimization techniques like column filtering or type conversion.
- **Chunking** and **sampling** are effective for early development and prototyping.

This hands-on experience helped us understand the trade-offs between different libraries and strategies when dealing with large-scale data.

---

## 🧑‍💻 Developed by

**Solo Squad**  
A single-member team working on high-performance data processing using modern tools.

📌 *Made with ❤️ for HPDP Class — C.Mrhumi*

---
