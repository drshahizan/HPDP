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
- **Number of Records:** Over 10 millions entries (42448764rows x 9 columns)
- **Features/Columns:** 
  - event_time: Time when event happened at (in UTC).
  - event_type: Only one kind of event: purchase.
  - product_id: ID of a product
  - category_id:Product's category ID
  - category_code: Product's category taxonomy (code name) if it was possible to make it. Usually present for meaningful categories and skipped for different kinds of accessories.
  - brand: Downcased string of brand name. Can be missed.
  - price: Float price of a product. Present.
  - user_id: Permanent user ID.
  - user_session: Temporary user's session ID. Same for each user's session. Is changed every time user come back to online store from a long pause.
---
</div>

## 2. Dataset Overview and Inspection

### 2.1 Dataset Description


### 2.2 Initial Loading


### 2.3 Basic Inspection


---

## 3. Big Data Handling Strategies

### 3.1 Part 1: Strategies with Pandas & Dask
**3.1.1 Load Less Data**<br>

- **Chunking**<br>


- **Optimize Data Types**<br>


- **Sampling**<br>


- **Parallel Processing with Dask**<br>


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




