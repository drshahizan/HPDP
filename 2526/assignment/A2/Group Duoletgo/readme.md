# Flight Delay Dataset 2024 — Big Data Analysis

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

## Project Summary

This project evaluates the Flight Delay Dataset 2024 using big data processing strategies. It compares a traditional Pandas baseline against scalable libraries such as Dask and Polars.

The goal is to measure memory usage and execution time while demonstrating practical techniques for handling large datasets in Google Colab.

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
