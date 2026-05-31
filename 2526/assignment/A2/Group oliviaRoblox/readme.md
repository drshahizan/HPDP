# SECP3133 Assignment 2 — Big Data Handling

## Group Members

| Name | Matric No |
|------|-------------|
| Ain Nurnabila binti Mohd Azhar | A23CS0207 |
| Dayang Farah Farzana binti Abang Idham | A23CS0071 |

---

## Dataset

| Field | Details |
|-------|---------|
| Name | California Google Local Reviews |
| Source | [Kaggle — mexwell/california-google-local-data](https://www.kaggle.com/datasets/mexwell/california-google-local-data) |
| Format | JSON Lines (.json) |
| Full File Size | ~12 GB (11,929 MB) |
| Rows Used | 2,000,000 |
| Columns Used | rating, text, gmap_id, time |

---

## Libraries Used

- Pandas (baseline)
- Dask
- Polars

---

## Strategies Implemented

| Strategy | Description | Person |
|----------|-------------|--------|
| Pandas Baseline | Load 2M rows with default Pandas settings. Records load time and peak memory as reference. | Person 1 |
| Strategy 1: Load Less Data | Load only 4 of 8 columns using column selection. Reduces memory at point of loading. | Person 1 |
| Strategy 2: Chunking | Read file in 100,000-row chunks. Filters high-rated reviews (≥4) per chunk without loading full file. | Person 1 |
| Strategy 3: Data Type Optimisation | Downcast `rating` to int8, `time` to int32, `gmap_id` to category. Reduces in-memory footprint. | Person 1 |
| Dask | Convert DataFrame to Dask with 4 partitions. Uses lazy evaluation and parallel computation. | Person 1 |
| Strategy 4: Sampling | [Dayang] | Person 2 |
| Strategy 5: Parallel Processing | [Dayang] | Person 2 |
| Polars | [Dayang] | Person 2 |

---

## Results

| Approach | Load Time (s) | Peak Memory (MB) |
|----------|--------------|-----------------|
| Pandas Baseline | 266.09 | 4490.03 |
| Strategy 1: Load Less Data | 218.06 | 4490.03 |
| Strategy 2: Chunking | 142.92 | 564.77 |
| Strategy 3: dtype Optimisation | — | 282.85 |
| Dask | 56.16 | 1298.07 |
| Polars | [Dayang] | [Dayang] |

---

## Files

| File | Description |
|------|-------------|
| big_data.ipynb | Full annotated notebook with all strategies and outputs |
| big_data.md | Main report with analysis and findings |
| README.md | This file |

---

## Links

- [Open Notebook in Colab](https://colab.research.google.com/drive/1bKriHSQa9r76Fx0EmT9C84hfD8O8ntl5?usp=sharing#scrollTo=2tbYlbATSrxK)

---

## How to Run

1. Upload `review-California_10.json` to Google Drive under `HPDP_A2/`
2. Open `big_data.ipynb` in Google Colab
3. Run **Runtime → Run All**

---

## Course Information

| Field | Details |
|-------|---------|
| Course | High Performance Data Processing (SECP3133) |
| Institution | Universiti Teknologi Malaysia (UTM) |
