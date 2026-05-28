# Flight Delay Dataset 2024 — Big Data Analysis

## Project Information

| Item | Details |
| :--- | :--- |
| Course | SECP3133 High Performance Data Processing |
| Assignment | Assignment 2: Mastering Big Data Handling |

## Group Information

### **Group Name: Duoletgo**

| Member | Matric Number |
| :----- | :------------ |
| Gui Kah Sin | A23CS0080 |
| Poh Lok Yee | A23CS0262 |

## Project Files

| File | Description | Open |
| :--- | :--- | :--- |
| `big_data_md.ipynb` | Main report with methodology, results and reflection | [View](big_data_md.ipynb) |
| `big_data.ipynb` | Executable Google Colab notebook with code, outputs and charts | [Open](big_data.ipynb) |
| `README.md`| Project overview and summary |
| `comparison_chart.png` | Execution time and memory usage comparison charts |

## Project Summary

This project focuses on handling and analysing a large flight delay dataset using different big data processing strategies. The dataset contains domestic US flight performance records including departure and arrival times, delays, cancellations, and airline carrier information for the full year of 2024.

The main objective is to compare traditional data processing using **Pandas** with scalable data processing libraries such as **Dask** and **Polars**. The comparison focuses on memory usage, execution time, and ease of processing.

## Dataset Snapshot

- **Dataset:** Flight Delay Dataset 2024
- **Source:** https://www.kaggle.com/datasets/hrishitpatil/flight-data-2024
- **Domain:** Transportation
- **Format:** CSV
- **Size:** 1.22 GB
- **Rows:** 7,079,081
- **Columns:** 35

## Key Techniques Used

- **Load Less Data:** Read only the required columns to save memory.
- **Chunking:** Process the dataset in smaller pieces to avoid out-of-memory errors.
- **Data Type Optimisation:** Downcast numeric fields and convert columns for lower memory footprint.
- **Sampling:** Use a smaller subset for fast prototyping and exploratory analysis.
- **Scalable Processing:** Compare Pandas, Dask, and Polars performance on the same aggregation task.

## Libraries Used

| Library | Purpose |
| :--- | :--- |
| Pandas | Baseline library for traditional data loading, inspection and processing |
| Dask | Scalable library for parallel and partition-based processing |
| Polars | High-performance dataframe library with Rust-based execution engine |

---

## Key Results

### Strategy Performance

| Strategy | Execution Time | Peak Memory |
| :--- | ---: | ---: |
| Pandas Baseline | 37.21s | 6,185.09 MB |
| Load Less Data | 8.03s | 659.67 MB |
| Chunking | 5.45s | 12.28 MB |
| Data Type Optimisation | 14.98s | 696.87 MB |
| Sampling (10%) | 0.55s | 151.23 MB |

### Library Comparison

| Library | Execution Time | Peak Memory |
| :--- | ---: | ---: |
| Pandas | 37.21s | 6,185.09 MB |
| Dask | 155.13s | 843.41 MB |
| Polars | 12.78s | 0.02 MB* |

*Polars memory not fully captured by `tracemalloc` — managed internally by Rust runtime.

## Charts

### Execution Time Comparison
![Execution Time Comparison](comparison_chart.png)

### Memory Usage Comparison
![Memory Usage Comparison](comparison_chart.png)


## Running the Notebook

1. Open `big_data.ipynb` in Google Colab.
2. Mount Google Drive or connect to Kaggle API.
3. Verify the dataset path and file location.
4. Run all cells from top to bottom.

## Notes

- The notebook is built for Google Colab.
- The dataset is downloaded automatically via Kaggle API.
- `big_data_md.ipynb` contains the full written report.
- `big_data.ipynb` contains the executable code and outputs.
