<h1 align="center"> 
  Assignment 2 - MAS(eCommerce Behavior Data from Multi Category Store)
</h1>

| Name              | Matric No       |
|-------------------|-----------------|
| MAISARAH BINTI RIZAL   | A22EC0192      |
| NADHRAH NURSABRINA BINTI ZULAINI  | A22EC0224    |

---

## 📚 Table of Contents
1. [Introduction](#1-introduction)
2. [Dataset Overview and Inspection](#2-dataset-overview-and-inspection)
3. [Big Data Handling Strategies](#3-big-data-handling-strategies)
4. [Comparative Analysis](#4-comparative-analysis)
5. [Conclusion and Reflection](#5-conclusion-and-reflection)
6. [References](#6-references)

---

## 1. Introduction

<div align="justify">
  
### 1.1 Background of the Project
In a data-driven world, the ability to manipulate large datasets is essential to transforming raw data into useful insights. Traditional tools, such as Pandas, can run into memory problems when working with large files. This project uses contemporary modules written in Python, such as Dask, Pandas, and Polars to evaluate the various ways of optimizing data loading, processing, and analysis. The aim is to know the performance of all options based on the speed, memory usage, and ease of implementation of each approach based on a real e-commerce dataset.

### 1.2 Objectives
This project's key aims include:

 1. To inspect and analyze a huge e-commerce dataset.
 2. To put various large data handling techniques into practice and evaluate them:
- Load Less Data
- Use Chunking
- Optimize Data Types
- Apply Sampling
 - Dask and Polars are used for parallel processing.
 3. To measure performance using throughput, memory use, and execution time.

### 1.3 Dataset Source
- **Dataset:** eCommerce behavior data from multi category store
- **Source:** [Kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)
- **Size:** 5.67GB (2019-Oct.csv)
- **Domain:** The dataset falls under the E-Commerce / Retail domain, focusing on user behavior tracking in an online multi-category store. It provides insights into how users interact with products across different categories and brands. 
- **Number of Records:** Over 10 millions entries (42448764rows x 9 columns)
- **Features/Columns:**

| Column Name       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `event_time`      | Time when event happened (in UTC)                                           |
| `event_type`      | Only one kind of event: purchase                                            |
| `product_id`      | ID of a product                                                             |
| `category_id`     | Product's category ID                                                       |
| `category_code`   | Product's category taxonomy (code name). Usually present for meaningful categories and skipped for different kinds of accessories. |
| `brand`           | Downcased string of brand name. Can be missing.                             |
| `price`           | Float price of a product. Always present.                                   |
| `user_id`         | Permanent user ID                                                           |
| `user_session`    | Temporary session ID. Same for each session, changed after long pause.      |

---
</div>

## 2. Dataset Overview and Inspection

### 2.1 Initial Loading

  ```
 🔽 STEP 1: Install kaggle CLI
!pip install -q kaggle

# 🔽 STEP 2: Upload kaggle.json API token
from google.colab import files
print("Please upload your kaggle.json file:")
files.upload()

# 🔽 STEP 3: Set up Kaggle CLI config
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# 🔽 STEP 4: Download your desired dataset
# Replace with your actual competition or dataset name
!kaggle datasets download mkechinov/ecommerce-behavior-data-from-multi-category-store

!unzip ecommerce-behavior-data-from-multi-category-store.zip
!ls

```

### 2.2 Basic Inspection

  ```
import pandas as pd

# Only load first 10,000 rows to avoid crash
filename = '2019-Oct.csv'
df_sample = pd.read_csv(filename)

print("📊" + "="*40)
print("     🔍 DATASET INSPECTION REPORT")
print("📊" + "="*40 + "\n")

# Shape
print("🧾 Shape (Rows, Columns):")
print(f"    ➤ {df_sample.shape[0]} rows, {df_sample.shape[1]} columns\n")

# Column Names
print("📌 Column Names:")
print("    ➤ " + "\n    ➤ ".join(df_sample.columns.tolist()) + "\n")

# Data Types
print("⚙️ Data Types:")
for col, dtype in df_sample.dtypes.items():
    print(f"    ➤ {col.ljust(20)} : {dtype}")
print()

# Memory Usage
print("💾 Memory Usage (MB):")
mem_usage = df_sample.memory_usage(deep=True) / (1024 ** 2)
for col, usage in mem_usage.items():
    print(f"    ➤ {col.ljust(20)} : {usage:.4f} MB")
print(f"\n    🧮 Total Memory : {mem_usage.sum():.4f} MB")

```

Output:
![image](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/MAS/RawDataOutput.png)

---

## 3. Big Data Handling Strategies

### 3.1 Part 1: Strategies with Pandas & Dask
**3.1.1 Load Less Data**<br>

- **Chunking**<br>


- **Optimize Data Types**<br>


- **Sampling**<br>


- **Parallel Processing with Dask**<br>

```
start_time = time.time()

# Read CSV with Dask
ddf = dd.read_csv(filename, usecols=['event_type', 'price'])

# Filter and compute mean
mean_price_after = ddf[ddf['event_type'] == TARGET_EVENT_TYPE][MEASUREMENT_COLUMN].mean().compute()

shape_after = (len(ddf), len(ddf.columns))
time_after = time.time() - start_time
mem_after = ddf.memory_usage(index=True, deep=True).sum().compute() / (1024 ** 2)
throughput_after = shape_after[0] / time_after if time_after > 0 else 0

print(f"Shape: {shape_after}")
print(f"Memory Usage: {mem_after:.2f} MB")
print(f"Processing Time: {time_after:.2f} seconds")
print(f"Throughput: {throughput_after:.0f} rows/sec")
print(f"Mean Purchase Price: {mean_price_after:.2f}")
print("-" * 50)

```

```
Shape: (42448764, 2)
Memory Usage: 812.49 MB
Processing Time: 157.33 seconds
Throughput: 269811 rows/sec
Mean Purchase Price: 309.56
--------------------------------------------------

```

### 3.2 Part 2: Comparing Libraries Reading Raw Data


| Library | Visualization |
|---------|---------------|
| Pandas  |  |  
| Dask    |  | 
| Polars  |  |

---

## 4. Comparative Analysis

### 4.1 Metrics Used


### 4.2 Results Summary

#### Part 1: Strategy Comparison

| **Strategies / Metrics**      | **Load Less Data** | **Chunking** | **Optimise Data Type** | **Sampling** | **Parallel Processing with Dask** |
|------------------------------|--------------------|--------------|------------------------|--------------|-------------------------------|
| **Processing Time (seconds)** | 0            | 0      | 0                | 0       | 0                    |
| **Memory Usage (MB)**        | 0            | 0      | 0                | 0        | 0                      |
| **Throughput (records/sec)** | 0         | 0    | 0             | 0    | 0                    |


#### Part 2: Library Comparison

| Library  | Time (s) | Memory (MB) | Throughput (records/sec)       |
|----------|----------|-------------|--------------------------------|
| Pandas   | 0 | 0     | 0                    |
| Dask     | 0   | 0     | 0                 |
| Polars   | 0   | 0      |                      |

### 4.3 Discussion

---

## 5. Conclusion and Reflection

### 5.1 Summary of Findings


### 5.2 Benefits & Limitations

| Tool     | Benefits                                  | Limitations                                |
|----------|-------------------------------------------|--------------------------------------------

### 5.3 Personal Reflection

#### Maisarah Binti Rizal


#### Nadhrah NurSabrina Binti Zulaini


---
## 6. References




