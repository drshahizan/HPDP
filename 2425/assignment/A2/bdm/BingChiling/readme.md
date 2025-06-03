
﻿
# Big Data Assignment 2: Mastering Big Data Handling with IMDB Review Dataset


## 🧑‍💻 Team Members

-   Member 1: CHEN PYNG HAW A22EC0042
    

## 📂 Project Structure

| File Name         | Explanation                                                                                                   | Link                                                                                                                                 |
|----------|-------------|---------------|
| `big_data.md`     | Main report with explanations, code snippets, tables | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/BingChiling/big_data.md) |
| `big_data.ipynb`  | Full Colab notebook with working code | [![Open in GitHub](https://img.shields.io/static/v1?label=&message=Open%20in%20GitHub&labelColor=grey&color=blue&logo=github)](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/BingChiling/big_data.ipynb) |


## 📄 Description

This project investigates efficient big data handling strategies using the **IMDB Review Dataset** (~1GB, over 1 million records). The objective is to evaluate and compare the performance of three prominent Python data processing libraries — **Pandas**, **Polars**, and **Dask** — when working with large-scale datasets.

To achieve this, we applied and benchmarked the following five data handling techniques:

-   **Load Less Data** – Load only relevant columns to reduce memory usage and improve efficiency.
    
-   **Use Chunking** – Process the dataset in smaller chunks to prevent memory overload.
    
-   **Optimize Data Types** – Convert data columns to more memory-efficient types (e.g., `category`, `float32`, `int8`).
    
-   **Sampling** – Randomly sample a subset of the data to enable faster prototyping (not supported natively in Dask).
    
-   **Parallel Processing with Dask** – Leverage Dask’s partitioned and parallel execution model for scalable data processing.
    

The project is divided into two comparative analyses:

1.  **Strategy-level comparison** (using Pandas and Dask) to measure how each technique affects performance.
    
2.  **Library-level comparison** of Pandas, Polars, and Dask focusing on the performance of normal full dataset loading.

## 📦 Dataset

-   Source: [Kaggle - IMDB Review Dataset](https://www.kaggle.com/datasets/ebiswas/imdb-review-dataset)
    
-   Size: ~1.07 GB (JSON format)
    


