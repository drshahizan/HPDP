# SECP3133 Assignment 2 — Big Data Handling Report

## Group Details

- **Group Name:** Potato
- **Member 1:** Lau Yee Wen (A23CS0099)
- **Member 2:** Chau Ying Jia (A23CS0213)

## Project Files

- `big_data.md` — main report with methodology, results, and reflection.
- `big_data.ipynb` — executable Colab notebook containing code, outputs, and charts.

## Project Summary

This assignment explores the Netflix User Ratings dataset using three Python libraries:

- **Pandas** for the baseline workflow
- **Dask** for partitioned and parallel dataframe processing
- **Polars** for high-performance, Rust-backed computation

The analysis focuses on practical big data strategies such as column selection, chunking, dtype optimisation, sampling, and scalable processing.

## Dataset Details

- **Dataset:** Netflix User Ratings
- **Source:** https://www.kaggle.com/datasets/evanschreiner/netflix-movie-ratings
- **Type:** CSV
- **Size:** 2585.43 MB
- **Rows:** 100,480,507
- **Columns:** 4 (`CustId`, `MovieId`, `Rating`, `Date`)

## What is Included

- A clean introduction and dataset summary.
- A step-by-step inspection of the CSV file.
- Five big data strategies with code and results:
  - Load Less Data
  - Chunking
  - Data Type Optimisation
  - Sampling
  - Parallel/Scalable Processing
- A comparative analysis of Pandas, Dask, and Polars.
- A conclusion with reflection on scalability and tool choice.

## Notes for Running the Notebook

- The notebook is intended for Google Colab.
- Mount Google Drive before accessing the dataset.
- Install any missing libraries at the top of the notebook if necessary.

## Usage

Open `big_data.md` to read the full report, and open `big_data.ipynb` to run the code and review the outputs.

