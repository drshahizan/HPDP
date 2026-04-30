# 📘 Assignment 2: Mastering Big Data Handling

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>Muhammad Afiq Danish bin Mohd Hazni</td>
    <td>A23CS0118</td>
  </tr>
</table>

---

## 🗂️ Project Files

| File Name        | Description                                                              | Link |
|------------------|--------------------------------------------------------------------------|------|
| `big_data.md`    | Detailed report containing strategies, benchmarking, and analysis        | [![Open](https://img.shields.io/badge/View-Markdown-blue?logo=markdown)](big_data.md) |
| `big_data.ipynb` | Google Colab notebook with Python code, outputs, charts, and comparison | [![Open](https://img.shields.io/badge/Open-Notebook-green?logo=jupyter)](big_data.ipynb) |

---

## 📖 Introduction

In the modern telecommunications industry, massive amounts of infrastructure data are generated to support mobile connectivity across countries and regions. Cell tower datasets are an excellent example of real-world big data, containing millions of records with location coordinates, network information, and operational metadata.

This project focuses on mastering scalable big data handling techniques using **Pandas**, **Dask**, and **Polars**. Various optimisation strategies were applied to efficiently load, process, and analyse a large dataset while comparing performance in terms of memory usage, execution time, and scalability.

---

## 📡 Dataset Overview

- **Name**: Cell Towers Worldwide Location Data by Continent (Asia Towers)
- **Source**: [Kaggle Dataset](https://www.kaggle.com/datasets/zakariaeyoussefi/cell-towers-worldwide-location-data-by-continent)
- **Domain**: Telecommunications / Geospatial Analytics
- **Selected File**: `Asia towers.csv`
- **File Size**: ~1.56GB
- **Shape**: 13.37 Million rows x 18 columns

### 📘 Description

This dataset contains mobile cell tower records across Asian countries. Each row represents a tower location with related metadata such as country, network provider, radio type, latitude, longitude, and technical identifiers.

### 🔍 Key Features

- **Geospatial Data**: Latitude and longitude of tower locations  
- **Country Information**: Tower distribution across Asia  
- **Network Operators**: Telecom service providers  
- **Radio Technology**: GSM, LTE, UMTS, NR, and others  
- **Infrastructure Scale**: Millions of real-world tower records  

---

## ⚙️ Strategies Applied

- **Strategy 1: Load Less Data**  
  Selected only required columns using `usecols`.

- **Strategy 2: Chunking**  
  Loaded data in smaller chunks to reduce RAM usage.

- **Strategy 3: Data Type Optimisation**  
  Converted columns into smaller numeric types and categorical data types.

- **Strategy 4: Sampling**  
  Used a subset of rows for faster exploratory analysis.

- **Strategy 5: Parallel Processing**  
  Used scalable libraries to speed up large file operations.

---

## 📊 Library Benchmarking

Three Python libraries were benchmarked:

- **Pandas** – Standard library for structured data analysis  
- **Dask** – Parallel and scalable processing for large datasets  
- **Polars** – High-performance DataFrame library built in Rust  

### Comparison Metrics

- Memory usage (MB)
- Execution time (seconds)
- Ease of implementation
- Scalability for larger datasets

---

## 🎯 Conclusion

This project demonstrates how large-scale datasets can be efficiently managed using modern data processing libraries and optimisation techniques. While Pandas is easy to use, Dask and Polars offer better scalability and performance for big data workloads. Through this assignment, practical skills in handling real-world large datasets were developed, which are highly relevant in data engineering and analytics careers.
