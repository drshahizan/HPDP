
# 📁 p1/ — Web Crawling & Data Cleaning Scripts

This folder contains all the scripts used for web crawling and cleaning raw data collected from **The Edge** website. It also includes multiple optimized versions of the cleaning pipeline using different performance-enhancing technologies.

## 📄 Files Overview
### 🔍 Web Crawling
- **the-edge-main_crawler.py**  
  The main crawler script used to extract article data from The Edge Malaysia website. This script handles the URL discovery, data parsing, and raw data storage into a JSON or CSV format.

### 🧹 Data Cleaning Scripts
- **theedge_cleaning_pandas.py**  
  A basic data cleaning script using `pandas`. This serves as the baseline method to prepare the dataset by removing nulls, duplicates, and standardizing text.

### ⚡ Optimized Cleaning Scripts
- **optimized_theedge_cleaning_pandas_threaded.py**  
  A multithreaded version of the pandas-based cleaning script. It speeds up processing by distributing row-based operations across multiple threads.

- **optimized_theedge_cleaning_polars.py**  
  An optimized script using the `polars` library, which is a faster DataFrame library than pandas, especially for large datasets.

- **optimized_theedge_cleaning_dask.py**  
  A parallel computing version using `dask`, which enables the script to handle larger-than-memory datasets and utilize multiple CPU cores for data transformation.


