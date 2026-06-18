# 📘 Assignment 2: Mastering Big Data Handling

<div align="center">

|Name|Matric Number|
|----|-----|
|Evelyn Goh Yuan Qi|A23CS0222|
|Lim Yu Han| A23CS0241|
</div>

## 📂 Project Structure

| File Name         | Explanation                                                                                                   | Link                                                                                                                                 |
|----------|-------------|---------------|
| `big_data.md`     | Main report with explanations, code snippets, tables | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](https://github.com/sean-seah/HPDP/blob/main/2526/assignment/A2/Group%20EL/big_data.md) |
| `big_data.ipynb`  | Full Colab notebook with working code | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](https://github.com/sean-seah/HPDP/blob/main/2526/assignment/A2/Group%20EL/big_data.ipynb) |

## 📊 Dataset Overview
-   Name: IMDb Review Dataset
-   Source: [Kaggle - IMDB Review Dataset](https://www.kaggle.com/datasets/ebiswas/imdb-review-dataset)
-   File Size: 1.07 GB
-   Records: Over 1 million movie reviews.
-   Shape: 1,010,293 rows x 9 columns
-   Domain: The dataset contains movie review data, including review text, ratings, reviewer information, and spoiler tags.

## 📄 Description

This project investigates efficient big data handling strategies using the **IMDB Review Dataset** (~1GB, over 1 million records). The objective is to evaluate and compare the performance of three prominent Python data processing libraries — **Pandas**, **Polars**, and **PyArrow** — when working with large-scale datasets.

To evaluate efficient approaches for processing large-scale datasets, this project implemented and benchmarked the following five big data handling strategies:

- **Load Less Data** – Load only the necessary columns from the dataset to reduce memory consumption and improve processing efficiency.

- **Chunking** – Process the dataset in smaller chunks instead of loading the entire file into memory, enabling scalable handling of large datasets.

- **Data Type Optimization** – Convert columns to more memory-efficient data types such as `float32`, `int8`, `category`, and `datetime` to reduce overall memory usage.

- **Sampling** – Extract a representative subset of the dataset to support faster exploratory analysis and prototyping while maintaining meaningful analytical results.

- **Parallel Processing with Polars** – Utilize Polars' parallel execution engine to perform data aggregation and analysis more efficiently on large datasets.
    

The project is divided into two comparative analyses:

1. **Big Data Handling Strategy Comparison** – Evaluates the impact of five data processing strategies (Load Less Data, Chunking, Data Type Optimization, Sampling, and Parallel Processing with Polars) on execution time and memory usage when handling a large IMDb review dataset.

2. **Library Performance Comparison** – Compares the performance of Pandas, Polars, and PyArrow when performing the same analytical task on the dataset, focusing on execution speed and memory efficiency.

