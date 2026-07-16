# 📘 Big Data Management Assignment: Mastering Big Data Handling

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>AHMAD ZIYAAD BIN MOHD ABBAS</td>
    <td>A23CS0206</td>
  </tr>
</table>

---

## 🗂️ Project Files

| File Name                     | Description                                                                    | Link |
|------------------------------|--------------------------------------------------------------------------------|------|
| `big_data.md`                | Markdown file with the detailed write-up for this assignment                   | [![Open](https://img.shields.io/badge/View-Markdown-blue?logo=markdown)](big_data.md) |
| `big_data.ipynb`             | Colab notebook exploring big-data loading strategies and library benchmarking  | [![Open](https://img.shields.io/badge/Open-Notebook-green?logo=jupyter)](big_data.ipynb) |

---

## 📖 Introduction

In the era of big data, traditional processing tools often fail when handling large-scale datasets, leading to memory exhaustion and slow execution. This assignment focuses on mastering high-performance data handling techniques by transitioning from theory to practical implementation.

We use the US Accidents (2016–2023) dataset (~3.0 GB, 7,728,394 rows), which is large enough to challenge the limits of a naive `pandas.read_csv()` call. Our objective is to apply five key strategies — loading selective data, chunking, data type optimization, sampling, and parallel processing — to improve efficiency, and to compare Pandas against two scalable alternatives, Polars and Dask, evaluating improvements (and, in one case, surprising results) in execution time, memory usage, CPU utilization, and throughput.

---

## 🚦 Dataset Overview

- **Name**: US Accidents (2016–2023)
- **Source**: [Kaggle – sobhanmoosavi](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
- **Domain**: Transportation / Road Safety
- **File Size**: 3,058.2 MB (~3.0 GB), confirmed directly via `os.path.getsize()` in the notebook
- **Shape**: 7,728,394 rows × 46 columns (full dataset); benchmarks in this notebook used a `MAX_ROWS = 500,000` cap for safe execution on Colab's free-tier RAM

### 📘 Description

The US Accidents dataset is a large-scale, countrywide collection of traffic accident records covering 49 US states from February 2016 to March 2023, sourced from multiple traffic APIs (state DOTs, law-enforcement feeds, traffic cameras, and road sensors). It is primarily used for road-safety analysis, geospatial/time-series exploration, and — as in this assignment — high-performance data processing tasks due to its significant volume.

### ⚠️ Notes

- Several weather-related columns (e.g. `End_Lat`, `End_Lng`) have notable missing-value rates.
- Some benchmark memory readings (see `big_data.md`, Task 4) came out negative or unusually high for Polars/Dask — this is discussed openly in the report as a likely artifact of first-call library initialization and process-level memory measurement noise, not a data quality issue.
- All benchmark numbers in this project were captured on a `MAX_ROWS = 500,000` slice of the full 7.7M-row file, not the entire dataset — see `big_data.md` for why.

### 🔍 Key Features

- Location data: `Start_Lat`, `Start_Lng`, `City`, `County`, `State`, `Zipcode`
- Weather attributes: `Temperature(F)`, `Humidity(%)`, `Visibility(mi)`, `Wind_Speed(mph)`, `Weather_Condition`
- Road-feature flags: `Crossing`, `Junction`, `Traffic_Signal`, `Bump`, and more (boolean)
- Severity rating (1–4) used as the target column throughout the benchmarks
- Time span: February 2016 – March 2023, across 49 US states

---

## ⚙️ Techniques Used

- Selective column loading (`usecols`)
- Data type downcasting (`float32`, `int8`, `category`)
- Chunk-based reading (`chunksize`)
- Random sampling (`.sample()`)
- Parallel processing with Dask (`dask.dataframe`, `map_partitions`)
- High-performance full-load benchmarking with Polars (`pl.read_csv`)

---

## 📊 Library Benchmarking

We evaluated three data-processing libraries on an identical plain full load (500,000-row cap):

| Library | Memory Used (MB) | Execution Time (s) | Avg CPU (%) | Throughput (records/s) |
|---|---|---|---|---|
| **Pandas** | 279.20 | 2.5808 | 96.21 | 193,738.38 |
| **Polars** | 7,299.50 | 9.8531 | 172.43 | 50,745.45 |
| **Dask** | -3,695.73 | 57.9638 | 123.76 | 8,626.07 |

Each library was tested and compared based on: memory consumption, execution time, average CPU usage, and processing throughput (records/second) — see `big_data.md` for the full analysis, including why the Polars/Dask numbers likely reflect one-time initialization overhead rather than their typical steady-state performance.

---

## 🎯 Conclusion

This project allowed us to explore and apply advanced data-handling techniques on a high-volume, real-world dataset. Among the five pandas-based strategies, **Dtype Optimization** gave the best overall balance of speed, throughput, and memory. Comparing libraries directly produced a result worth reflecting on rather than smoothing over: Pandas outperformed Polars and Dask in this specific run, most likely due to first-call runtime initialization costs for the other two libraries — a reminder that a single benchmarking run is one data point, not a universal verdict.

Through this assignment, we took a step closer to how professional data engineers manage, optimize, and honestly report on large-scale data processing in real-world applications.

---

## 📁 Folder Structure

```plaintext
bdm/your_group/
├── big_data.md        ← Full write-up
├── readme.md          ← This file
└── big_data.ipynb     ← Colab notebook
```
