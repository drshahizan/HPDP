# SECP3133 Assignment 2 — Big Data Handling

## Group Members

| Name | Matric No |
|------|-------------|
| Farra Nurzahin binti Zaharil Anuar | A23CS0079 |
| Safiya Nursyahadah binti Masnoor | A23CS0176 |

---

## Dataset
| Field | Details |
|-------|---------|
| Name | Amazon Product Data |
| Source | [Kaggle — piyushjain16/amazon-product-data](https://www.kaggle.com/datasets/piyushjain16/amazon-product-data) |
| Domain | Cloud & E-Commerce |
| Description | Large-scale cloud-based analytics and fulfilment |
| Format | CSV |
| File Size | ~1.6 GB |
| Columns Used | PRODUCT_ID, TITLE, PRODUCT_TYPE_ID, PRODUCT_LENGTH |

---

## Libraries Used

- Pandas (baseline)
- Dask
- Polars

---

## Strategies Implemented

| Strategy | Description |
|----------|-------------|
| Strategy 1: Load Less Data | Load only 4 required columns using `usecols`, skipping irrelevant fields to reduce memory at read time. |
| Strategy 2: Chunking | Read the full 1.6 GB file in 100,000-row chunks to keep peak memory low across the entire load. |
| Strategy 3: Data Type Optimisation | Downcast `PRODUCT_ID` and `PRODUCT_TYPE_ID` to smaller int types, `PRODUCT_LENGTH` to float32. |
| Strategy 4: Sampling | Draw a 5% random sample (`~50,000 rows`) for rapid prototyping and exploratory analysis. |
| Strategy 5: Parallel Processing | Run the same aggregation using Dask and Polars. |

---

## Results
| Approach | Memory Used (MB) | Execution Time (s) |
|----------|-----------------|-------------------|
| S1: Load Less Data |550.09|19.5451|
| S2: Chunking | 2022.24 | 30.3484 |
| S3: Type Optimisation | 106.54 | 0.5971 |
| S4: Sampling | 0.06 |1.1167|
| S5: Dask | 298.69 | 30.3788 |
| S5: Polars | 99.25| 2.0729 |
| Pandas (Library Comparison) | 1819.9 |39.3038 |
| Dask (Library Comparison) | 433.32 | 41.0228|
| Polars (Library Comparison) | 0.01 | 1.2993 |

---

## Files

| File | Description |
|------|-------------|
| big_data.ipynb | Full annotated notebook with all strategies and outputs |
| big_data.md | Main report with analysis and findings |
| README.md | This file |

---

## Links
- [Open Notebook in Colab](https://colab.research.google.com/drive/1Aa34tgteu6RMYrFBlIMMrwHrIXqNXisH#scrollTo=GNb9pa0OHlKA)

---

## How to Run

1. Upload `product_amazon_data.csv` to Google Drive under `HPDP_A2/`
2. Open `big_data.ipynb` in Google Colab
3. Run **Runtime → Run All**

---

## Course Information
| Field | Details |
|-------|---------|
| Course | High Performance Data Processing (SECP3133) |
| Institution | Universiti Teknologi Malaysia (UTM) |
