# 🐾 Big Data Handling Project: Efficient Techniques for Large-Scale Datasets

## 🚀 Project Overview

This project investigates efficient strategies and tools for handling large-scale datasets using Python. It benchmarks the performance of traditional and modern data processing libraries — including **Pandas**, **Dask**, and **Polars** — on a real-world dataset that exceeds **1.4 GB** in size with **over 10 million rows**.

## 📄 Included Files

| 📁 File | 📝 Description |
|--------|----------------|
| [`big_data.ipynb`](./big_data.ipynb) | Jupyter Notebook with all analysis and benchmarking |
| [`big_data.md`](./big_data.md) | Project summary and documentation |
| [NYC Parking Violations 2017 – Dataset](https://www.kaggle.com/datasets/new-york-city/nyc-parking-tickets) | Real-world dataset used for benchmarking |

## 🎯 Objectives

- Compare big data processing techniques for efficiency and scalability.
- Measure memory usage and execution time across different tools.
- Identify the best practices for handling datasets that challenge system memory limits.

## 🧰 Tools & Libraries Used

| Library | Purpose |
|--------|---------|
| **Pandas** | Standard data manipulation (in-memory processing) |
| **Dask** | Scalable, parallel, and out-of-core computing |
| **Polars** | High-performance processing with Rust backend |

## ⚙️ Techniques Implemented

- **Selective Loading**: Load only required columns/rows to reduce memory footprint.
- **Chunking**: Process the dataset in parts rather than loading all at once.
- **Data Type Optimization**: Convert columns to more memory-efficient formats (e.g., `category`, `int8`).
- **Sampling**: Analyze a representative subset of the data.
- **Parallel & Lazy Execution**: Use Dask to defer computations and utilize multiple cores.

## 📦 Dataset Details

- **Dataset**: NYC Parking Violations Issued – Fiscal Year 2017  
- **Source**: [NYC Open Data via Kaggle](https://www.kaggle.com/datasets/new-york-city/nyc-parking-tickets)  
- **File Size**: ~1.4 GB (CSV, uncompressed)  
- **Domain**: Transportation / Government / Urban Analytics  
- **Records**: 10+ million rows  
- **Columns**: 43  
- **Format**: CSV

### 🔍 Why Dask Over Pandas?

Pandas attempts to load the entire dataset into memory, which led to a `RuntimeError: You have used all available RAM` in Google Colab (12–25 GB RAM).  
**Dask**, however:

- Loads data in **chunks**, avoiding full memory usage
- Uses **lazy evaluation**, only computing when required
- Prevents crashes in constrained environments
- Supports **parallelism and out-of-core processing** for better performance

## 👩‍🎓 Student Information

- **Group Name**: Mainecoon  
- **Subject**: High Performance Data Processing  
- **Assignment**: Mastering Big Data Handling

### 👥 Team Members

- Aliatul Izzah Binti Jasman  
- Mulyani Binti Saripuddin  

## 📈 Key Outcomes

- Benchmarked Pandas, Dask, and Polars for large dataset processing
- Identified memory bottlenecks and how to overcome them
- Demonstrated scalable data processing methods ideal for big data environments
  


> 📦 These resources provide everything you need to explore and reproduce the analysis.



## ⭐️ Support

If you found this project useful or insightful, please consider giving it a ⭐️ on GitHub!
