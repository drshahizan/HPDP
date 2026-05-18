# 📘 Assignment 2: Mastering Big Data Handling

<div align="center">

|Name|Matric Number|
|----|-----|
|Chua Jia Lin|A23CS0069|
|Joanne Ching Yin Xuan| A23CS0227|
</div>

## 📁 Project Files

<div align="center">

| File Name        | Description                                             | Link |
|------------------|---------------------------------------------------------|------|
| `big_data.md`    | Markdown file with detailed write-up for Assignment 2   |<a href="big_data.md"><img src="https://img.shields.io/badge/View-Markdown-blue?logo=markdown&logoColor=white" /></a>|
| `big_data.ipynb` | Colab notebook exploring various data loading and optimization techniques |<a href="big_data.ipynb"><img src="https://img.shields.io/badge/Open-Notebook-green?logo=jupyter&logoColor=white" /></a>|
</div>

## 📖 Introduction
In the modern era of digital payments and online commerce, financial institutions generate massive volumes of transaction data every day. This data is essential for identifying suspicious behavior and preventing fraud. Efficiently handling this kind of data requires specialized tools and techniques.

Our project focuses on mastering scalable big data techniques using tools such as Pandas, Dask, and Polars. We applied various optimization strategies to load and process a large real-world dataset, then conducted performance benchmarking on memory usage and execution time.

## 📊 Dataset Overview
- **Name:** Transaction  
- **Source:** [Kaggle – ismetsemedov](https://www.kaggle.com/datasets/ismetsemedov/transactions)
- **Domain:** Finance
- **File Size:** 2.73GB
- **Shape:** 7,483,766 rows x 24 columns

## 📄 Description
This project examines efficient big data handling strategies using the Transaction Dataset (2.73GB, over 7 million records). The objective is to evaluate and compare the performance of three popular Python data processing libraries which are Pandas, Dask, and Polars when working with large-scale datasets.

To achieve this, we applied and benchmarked the following big data handling strategies:
- **Load Less Data:** Load only relevant columns to reduce memory usage and improve efficiency.
- **Use Chunking:** Process the dataset in smaller chunks to prevent memory overload.
- **Optimize Data Types:** Convert data columns' data types to more memory-efficient data types (e.g., category, float32, int8).
- **Sampling:** Randomly sample a subset of the data to enable faster prototyping.
- **Parallel Processing with Polars:** Leverage Polars’ built-in multithreading and columnar execution engine for fast and scalable data processing.
- **Parallel Processing with Dask:** Use a task-based parallel computing framework that enables lazy evaluation and scalable processing through distributed-like execution using .compute().

The project is divided into two comparative analyses:
- Strategy-level comparison (using Pandas, Polars, and Dask) to measure how each strategy affects performance.
- Library-level comparison of Pandas, Dask, and Polars focusing on the performance of full dataset loading.

