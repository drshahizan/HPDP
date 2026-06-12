# SECP3133 Assignment 2: Mastering Big Data Handling

## Group 1: High Performance E-Commerce Data Processing

This repository folder contains the submission files for **SECP3133 High Performance Data Processing Assignment 2**, titled **Mastering Big Data Handling**.

The project focuses on handling a large real-world e-commerce logistics dataset using **Pandas**, **Dask**, and **Polars**. The assignment demonstrates big data handling strategies such as loading fewer columns, chunking, data type optimisation, sampling, and scalable parallel processing.

---

## Group Members

| Name | Matric No. | Role |
|---|---|---|
| NEO LI XIN | A23CS0253 | Student A: Baseline & Setup Lead |
| ELIJAH SHE YU SHENG | A23CS0073 | Student B: Scalability & Performance Lead |

---

## Dataset Information

| Item | Description |
|---|---|
| Dataset Name | Shopee Logistics Performance March |
| Source | [[Open] Shopee Code League - Logistics](https://www.kaggle.com/competitions/open-shopee-code-league-logistic) |
| File Used | `delivery_orders_march.csv` |
| Compressed File | `delivery_orders_march.csv.zip` |
| Compressed Size | Approximately 381 MB |
| Extracted CSV Size | Approximately 721 MB |
| Number of Records | 3,176,313 rows |
| Number of Columns | 6 columns |
| Domain | E-Commerce Logistics |

The dataset is suitable for this assignment because the extracted CSV file is larger than the required minimum dataset size of 700 MB.

---

## Libraries Used

| Library | Purpose |
|---|---|
| Pandas | Baseline data loading, inspection, and optimisation strategies |
| Dask | Scalable dataframe processing using partition-based computation |
| Polars | High-performance dataframe processing using Rust engine and lazy execution |

---

## Project Files

| File | Description | Link |
|---|---|---|
| `big_data.ipynb` | Google Colab / Jupyter Notebook containing full code, explanations, outputs, tables, and charts | [Open Notebook](https://github.com/lixinneo04/high-performance-ecommerce-data-processing/blob/main/big_data.ipynb) |
| `big_data.md` | Main Markdown technical report containing dataset description, strategies, comparative analysis, conclusion, and references | [Open Report](https://github.com/lixinneo04/high-performance-ecommerce-data-processing/blob/main/big_data.md) |


---


## Work Distribution

| Student | Responsibility |
|---|---|
| NEO LI XIN | Dataset setup support, Dask and Polars implementation, performance testing, comparison charts, analysis, conclusion and scalability reflection |
| ELIJAH SHE YU SHENG | Dataset preparation, dataset description, Pandas baseline, Pandas big data handling strategies, GitHub setup, report structure, and documentation refinement |

---

## Summary of Implemented Strategies

| Strategy | Description |
|---|---|
| Strategy 1: Load Less Data | Loaded only required columns to reduce memory usage and improve loading speed |
| Strategy 2: Chunking | Processed the large CSV file in smaller chunks to avoid loading the full dataset into memory |
| Strategy 3: Data Type Optimisation | Applied suitable data types to reduce memory footprint |
| Strategy 4: Sampling | Used a smaller sample for fast prototyping and testing |
| Strategy 5: Parallel Processing | Compared scalable processing using Dask and Polars against the Pandas baseline |

---

## Comparative Analysis

The project compares **Pandas**, **Dask**, and **Polars** using the same processing task. The comparison includes:

- Execution time
- RAM usage
- Number of rows processed
- Missing second delivery attempt count
- Average delivery time calculation
- Critical discussion of performance and scalability

---

## Submission Checklist

- ✅ Dataset is larger than 700 MB
- ✅ Pandas is used as the compulsory baseline library
- ✅ Two scalable libraries are used: Dask and Polars
- ✅ Five big data handling strategies are implemented
- ✅ Memory usage and execution time are measured
- ✅ Comparison table and charts are included
- ✅ Notebook contains code, explanations, and visible outputs
- ✅ Markdown report is completed
- ✅ README contains project details and links to required files
- ✅ Required files are placed in the correct GitHub folder

---

## Notes

The results may vary slightly depending on the runtime environment, especially when executed in Google Colab, because available CPU cores and RAM allocation may differ between sessions.

---

## References

- [[Open] Shopee Code League - Logistics](https://www.kaggle.com/competitions/open-shopee-code-league-logistic)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Dask Documentation](https://docs.dask.org/)
- [Polars Documentation](https://docs.pola.rs/)
