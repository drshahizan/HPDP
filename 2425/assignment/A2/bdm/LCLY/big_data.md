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
Traditional data processing tools like Pandas face challenges with large datasets. This project addresses those limitations by applying big data strategies and leveraging Dask for parallel processing on the **UK Housing Prices Paid** dataset (>700MB).

### 1.2 Objectives
- Understand the limitations of Pandas
- Apply strategies like chunking, sampling, data type optimization
- Implement parallel processing using Dask
- Compare Pandas, Dask, and Polars using:
  - Shape
  - Processing Time
  - Memory Usage
  - Throughput

### 1.3 Dataset Source
- **Dataset:** UK Housing Prices Paid  
- **Source:** [Kaggle](https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid)  
- Over 25 million entries, 11 columns, >800MB

---

## 2. Dataset Overview and Inspection

### 2.1 Dataset Description
The dataset contains records of residential property sales in the UK with fields like price, transfer date, property type, location, and metadata.

### 2.2 Initial Loading
To begin the data analysis, the UK Housing Prices Paid dataset was loaded directly into the Colab environment using basic file handling methods. The dataset was obtained from Kaggle and extracted within the environment prior to analysis.
<br><br>
The following code snippet was used to list the dataset contents after ensuring the files were available:
![Screenshot 2025-06-02 120412](https://github.com/user-attachments/assets/ac89a356-673d-4e91-b0b2-5b41a2c7014c)

### 2.3 Basic Inspection
- Shape: 10 rows × 11 columns  
- Processing Time: 0.0065s  
- Memory Usage: 0.01 MB  
- Throughput: 1,545.77 records/sec  
- Most fields are object types; "Price" is numeric
