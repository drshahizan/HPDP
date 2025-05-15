# 🧼 Folder P1

This repository includes the source code for web scraping and cleaning process before and after as well as data mapping process 

---

## 📁 Folder Structure & File Descriptions



### 🧪 Code Files

#### 🔹 Basic Scraping (Without Optimization)
- `PgmallScraping_withoutOptimization.ipynb`  
  ➤ Performs basic web scraping and data collection without any performance optimization. Saves raw product data.

#### 🔹 Optimized Scraping
- `PgmallScraping_multithreading.ipynb`  
  ➤ Implements web scraping using multithreading to improve performance and reduce total scraping time.

#### 🔹 Scraping by SubCategory
- `PgmallBySubCategory.ipynb.ipynb`  
  ➤ Scrapes product data by subcategory

#### 🔹 Mapping for Product Type
- `Map_ProductType.ipynb`  
  ➤ Maps raw product to product type categories to assist in analysis.

#### 🔹 Basic Cleaning (Without Optimization)
- `Cleaning_Process_withoutOptimization.ipynb`  
  ➤ Step-by-step cleaning using **Pandas** only. Checks for nulls/duplicates, cleans price/product fields, and saves cleaned data.

#### 🔹 Optimized Cleaning
- `Cleaning_Process_withPolar.ipynb`  
  ➤ Cleaning using **Polars** for improved speed and parallelism.

- `Cleaning_Process_withDask.ipynb`  
  ➤ Cleaning using **Dask** for parallelized processing. Designed to test scalability on larger datasets.

---




