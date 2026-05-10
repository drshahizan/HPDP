# Assignment 2: Mastering Big Data Handling

## Group Information
* **Group Name:** youtube_trending_video
* **Members:** CHOH JING YI & TAN ZHI MING

---

## 1. Dataset Description
* **Dataset Name:** YouTube Trending Video Dataset
* **Source URL:** https://www.kaggle.com/datasets/rsrishav/youtube-trending-video-dataset
* **File Size:** > 700 MB (Combined regional files including BR, CA, DE, FR)
* **Domain:** Social Media / Entertainment
* **Number of Records:** 1,075,056 rows
* **Description:** This dataset contains daily records of the top trending YouTube videos across multiple regions. It includes high-cardinality string data (titles, channel names, tags, descriptions) alongside heavy numerical engagement metrics (views, likes, dislikes, comment counts), making it an ideal candidate for memory optimization and parallel processing benchmarks.

---

## 2. Library Choices
To fulfill the core technical requirements, we selected the following libraries:
1. **Pandas (Library 1 - Compulsory Baseline):** Used as the standard, single-threaded reference point to measure memory consumption and execution time.
2. **Polars (Library 2 - Scalable):** Selected for its extremely fast, multi-threaded Rust backend and its "lazy evaluation" architecture, which optimizes query plans before executing them.
3. **Dask (Library 3 - Scalable):** Selected to demonstrate distributed computing. Dask mirrors the Pandas API but breaks massive datasets into out-of-core partitions, spreading tasks across multiple CPU cores.

---

## 3. Data Loading and Inspection
To establish a baseline, we loaded four regional CSV files and concatenated them into a single massive DataFrame using standard Pandas functions.

```python
import pandas as pd
import glob
import os

# 1. Define the folder path and find all CSV files
folder_path = '/content/drive/MyDrive/youtube_trending_video/'
all_files = glob.glob(os.path.join(folder_path, "*.csv"))

# 2. Load and concatenate
df_list = [pd.read_csv(file) for file in all_files]
df_baseline = pd.concat(df_list, ignore_index=True)

# 3. Inspect
print(f"Shape: {df_baseline.shape[0]:,} rows and {df_baseline.shape[1]} columns.")
memory_mb = df_baseline.memory_usage(deep=True).sum() / (1024 * 1024)
print(f"Baseline Memory Usage: {memory_mb:.2f} MB")
