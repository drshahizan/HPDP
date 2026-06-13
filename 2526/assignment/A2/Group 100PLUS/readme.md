# Assignment 2: Mastering Big Data Handling

**Course:** High Performance Data Processing (HPDP)
**Group Name:** Boeing 737
**Section:** 02

| Member | Student ID |
|---|---|
| Sabrina Heng Wei Qi | A23CS0265 |
| Woo Cheng Shuan | A23CS0283 |

---

## 📊 Dataset

| Field | Details |
|---|---|
| **Name** | Flight Delay Dataset 2024 |
| **Source** | [Kaggle](https://www.kaggle.com/datasets/hrishitpatil/flight-data-2024) |
| **File** | flight_data_2024.csv |
| **Size** | ~1.22 GB |
| **Rows** | ~7.2 million |
| **Columns** | 35 |

> The dataset is not included in this repository due to its size (1.22 GB). Download it from the Kaggle link above and place it in your Google Drive before running the notebook.

---

## 🛠️ Libraries Used

| Role | Library | Version |
|---|---|---|
| Baseline | Pandas | 2.2.2 |
| Scalable (Parallel) | Dask | 2026.3.0 |
| Scalable (High Performance) | Polars | 1.35.2 |

---

## 📝 Strategies Implemented

| Strategy | Description | Peak Memory | Time |
|---|---|---|---|
| Baseline | Full Pandas load, no optimisation | 6,193.62 MB | 72.13s |
| S1: Load Less Data | Select 10 columns only | 1,577.94 MB | 29.90s |
| S2: Chunking | Process in 500,000-row chunks | 151.39 MB | 30.29s |
| S3: Type Optimisation | Downcast dtypes + category encoding | 229.59 MB | ~22s |
| S4: Sampling | 200,000-row random sample | 1,577.93 MB | 25.20s |
| S5a: Dask | Parallel processing with Dask | 406.81 MB | 26.09s |
| S5b: Polars | Rust-native lazy execution | 0.02 MB | 3.73s |

---

## 🚀 Key Results

- **Fastest library:** Polars at **3.73 seconds** (19.33× faster than Pandas)
- **Most memory efficient:** Polars at **0.02 MB** Python-visible memory
- **Best Pandas-based memory saving:** Chunking at **151 MB** (97.5% reduction)
- **Best Pandas-based memory optimisation:** Type optimisation at **87% reduction**

---

## ▶️ How to Run

1. Open [Google Colab](https://colab.research.google.com)
2. Upload or open `big_data.ipynb` from Google Drive
3. Download the dataset from Kaggle and place it in your Drive at: /content/drive/MyDrive/HPDP_A2/flight_data_2024.csv
4. Run all cells from top to bottom (**Runtime → Run all**)

---

## 🔗 Alternative Access

All files including the notebook, report, and charts are accessible via Google Drive:

📂 **[Click here to access our work on Google Drive](https://drive.google.com/drive/folders/1zbW9-g6d645kbzcM8EGtGw7sUcpnG2dT?usp=sharing)**

---

## 📚 References

1. Patil, H. (2025). *Flight Delay Dataset — 2024*. Kaggle. https://www.kaggle.com/datasets/hrishitpatil/flight-data-2024
2. McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
3. Dask Development Team. (2024). *Dask Documentation*. https://docs.dask.org
4. Polars Development Team. (2024). *Polars User Guide*. https://docs.pola.rs
5. Apache Software Foundation. (2024). *Apache Arrow*. https://arrow.apache.org
6. Rocklin, M. (2015). *Dask: Parallel Computation with Blocked Algorithms and Task Graphs*. Proceedings of the 14th Python in Science Conference.
