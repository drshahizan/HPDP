# 🅿️ Assignment 2: Mastering Big Data Handling
### SECP3133 – High Performance Data Processing

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>Muhammad Adam bin Razali</td>
    <td>A23CS0116</td>
  </tr>
  <tr>
    <td>Afif Shaqir Irfan bin Arqam</td>
    <td>A23CS</td>
  </tr>
</table>

---

## 📂 Repository Contents

| File | Purpose | Open |
|------|---------|------|
| `big_data.md` | Full written report covering all tasks, strategies, analysis, and reflection | [![View](https://img.shields.io/badge/View-Report-blue?logo=markdown)](big_data.md) |
| `big_data.ipynb` | Executed Jupyter notebook with annotated Python code and all outputs | [![Open](https://img.shields.io/badge/Open-Notebook-green?logo=jupyter)](big_data.ipynb) |

---

## 🗃️ Dataset

| Field | Details |
|-------|---------|
| **Name** | NYC Parking Violations Issued – Fiscal Year 2017 |
| **Source** | [Kaggle – New York City](https://www.kaggle.com/datasets/new-york-city/nyc-parking-tickets) |
| **Domain** | Transportation / Urban Governance / Law Enforcement |
| **File Size** | ~2.1 GB |
| **Records** | ~10.8 Million rows × 43 columns |

The dataset captures every parking ticket issued by the NYC Department of Finance throughout Fiscal Year 2017. It includes a rich mix of column types — numeric IDs, categorical state codes, free-text street names, and date fields — which makes it well-suited for testing a range of big data handling strategies, particularly data type optimisation and parallel processing.

---

## 🐍 Libraries Used

| # | Library | Role |
|---|---------|------|
| 1 | **Pandas** | Baseline — standard single-threaded DataFrame processing |
| 2 | **Polars** | Scalable — Rust-based engine with automatic multi-core execution |
| 3 | **Dask** | Scalable — lazy, partitioned parallel processing for out-of-memory data |

Polars was chosen for its exceptional raw speed on CSV loading and filtering thanks to its columnar Rust engine. Dask was selected for its memory efficiency — processing data across partitions rather than loading the full file into RAM — making it the most viable option as dataset size scales beyond available memory.

---

## 🛠️ Strategies Implemented

| # | Strategy | Core Technique |
|---|----------|---------------|
| 1 | **Load Less Data** | `usecols` — load only 7 of 43 columns |
| 2 | **Chunking** | `chunksize=100,000` — sequential chunk aggregation |
| 3 | **Data Type Optimisation** | Downcasting numerics; `category` for low-cardinality strings |
| 4 | **Sampling** | `nrows=1,000,000` in Pandas & Polars; `frac=0.1` in Dask |
| 5 | **Parallel Processing** | Full pipeline benchmarked across all three libraries |

---
## 🔍 How to Run

1. Open `big_data.ipynb` in [Google Colab](https://colab.research.google.com/).
2. Mount Google Drive and place the dataset CSV at the path defined in the notebook.
3. Run all cells top to bottom — all outputs are pre-executed and visible.

> Required libraries: `pandas`, `polars`, `dask` — install any missing ones via `!pip install <library>` at the top of the notebook.
