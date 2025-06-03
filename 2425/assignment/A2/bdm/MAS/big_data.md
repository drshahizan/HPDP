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

### 1.1 Background of the Project


### 1.2 Objectives


### 1.3 Dataset Source
- **Dataset:** 
- **Source:** 
- 

---

## 2. Dataset Overview and Inspection

### 2.1 Dataset Description


### 2.2 Initial Loading


### 2.3 Basic Inspection

**Sample Preview (via df.head())**


**Data Types (via df.dtypes and df.info()):**

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
| **Processing Time (seconds)** | 0            | 0      | 0                | 0       | 114.8009                     |
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
> I have developed a clearer view of big data processing and the importance of selecting the right tools for the job by completing this project. I have learned that while pandas is suitable for small and quick data tasks, libraries like Dask and Polars offer excellent options when dealing with big data. I was especially thrilled to see how Polars with its optimized architecture processed data extremely fast. This project provided me with greater confidence in applying scalable data solutions to future projects, and it further reaffirmed my interest in data engineering and performance optimization.<br>

#### Nadhrah NurSabrina Binti Zulaini
> This project allowed me to learn how to link Kaggle to Google Collab which was very useful because I could never run a 3 GB dataset on my own laptop. We also tried Polars, it is quite new for me but what I found after I started using it is that it is very fast and the code is simple. This project taught me the importance of choosing the right tool for the right task. I learned how to work with large datasets using Pandas, Dask, and Polars, and realized that performance can vary greatly depending on the method used. Most importantly, I learned how to work smarter with big data and the value of deepening my knowledge in my own field.<br>

---
## 6. References




