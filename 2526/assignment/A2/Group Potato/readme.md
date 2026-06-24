# 📊 Netflix Movie Ratings Analysis — Project Overview

## 👥 Group Information

### Group Name: Potato

| Member | Matric Number |
|----------|----------|
| Lau Yee Wen | A23CS0099 |
| Chau Ying Jia | A23CS0213 |

---

## 📁 Project Files

| File | Description | Link |
|----------|----------|----------|
| `big_data.md` | Main Markdown report containing methodology, results, comparative analysis, and reflection | [View Report](big_data.md) |
| `big_data.ipynb` | Executable Google Colab notebook containing code implementation, outputs, and visualisations | [Open Notebook](big_data.ipynb) |

---

## 🎬 Project Summary

This project investigates efficient techniques for handling large-scale datasets using the Netflix User Ratings dataset. The analysis evaluates multiple big data processing strategies and compares the performance of traditional and scalable dataframe libraries.

The objective is to measure memory usage, execution time, and scalability while demonstrating practical approaches for processing large datasets in a resource-constrained environment such as Google Colab.

---

## 📊 Dataset Snapshot

- **Dataset:** Netflix User Ratings
- **Source:** https://www.kaggle.com/datasets/evanschreiner/netflix-movie-ratings
- **Domain:** Entertainment / Recommendation Systems
- **Format:** CSV
- **Size:** 2585.43 MB
- **Rows:** 100,480,507
- **Columns:** 4 (`CustId`, `MovieId`, `Rating`, `Date`)

---

## 🚀 Key Techniques Implemented

- **Load Less Data** – Load only the columns required for analysis.
- **Chunking** – Process large files in smaller chunks to minimise memory usage.
- **Data Type Optimisation** – Reduce memory footprint through datatype downcasting.
- **Sampling** – Use representative subsets for faster experimentation.
- **Parallel Processing** – Compare the performance of Pandas, Dask, and Polars.

---

## 🛠️ Libraries Used

- Pandas
- Dask
- Polars
- Matplotlib
- Seaborn
- Memory Profiler

---

## ▶️ Running the Notebook

1. Open `big_data.ipynb` in Google Colab.
2. Mount Google Drive.
3. Verify the dataset path and file location.
4. Run all cells from top to bottom.

---

## 📌 Notes

- The notebook was developed and tested in Google Colab.
- The Netflix User Ratings dataset must be available in Google Drive before execution.
- `big_data.md` contains the complete written report.
- `big_data.ipynb` contains all code, outputs, performance measurements, and visualisations.
