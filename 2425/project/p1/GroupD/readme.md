<h1 align="center"> 
  Group D - PG Mall
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>WAN NUR SOFEA BINTI MOHD HASBULLAH</td>
    <td>A22EC0115</td>
  </tr>
  <tr>
    <td width=80%>LOW YING XI</td>
    <td>A22EC0187</td>
  </tr>
  <tr>
    <td width=80%>MUHAMMAD ARIFF DANISH BIN HASHNAN</td>
    <td>A22EC0204</td>
  </tr>
  <tr>
    <td width=80%>MUHAMMAD IMAN FIRDAUS BIN BAHARUDDIN</td>
    <td>A22EC0216</td>
  </tr>
</table>

# 🧹 Optimizing High-Performance Data Processing for Large-Scale Web Crawlers – PG Mall

![Project Overview](https://cloud.shopback.com/c_scale,c_auto,q_70,f_webp/media-production-aps1/VwBgbmofqVg/aHR0cHM6Ly9pbWFnZXMuYmFubmVyYmVhci5jb20vZGlyZWN0L0VHQnFwQVo1T2U5MTg5VkROSi9yZXF1ZXN0cy8wMDAvMDQ3LzI0My83ODEvWndWYktsRGU5WThwWlo4MVk4bW9hM2pQTS8xM2UyNDY3NzA5MDY1ZDM3M2QzODU5NjU4NjE4NWViODhhODdlNGQ0LnBuZw.jpg)

This project focuses on collecting product data from **PG Mall**, cleaning it, and evaluating different Python libraries for performance (Pandas, Polars, and Dask). The goal is to optimize scraping speed and data transformation for better scalability and analysis.

---

## 🔧 How This Project Works

This project is structured in 4 main stages:

1. **Web Scraping**  
   Data is scraped from PG Mall using both basic and optimized (multithreaded) techniques. One variant also scrapes data by product subcategories.

2. **Product Type Mapping**  
   Raw products are mapped into defined product types using keyword matching to prepare the data for categorization and visualization.

3. **Data Cleaning**  
   The raw scraped data undergoes cleaning using three different libraries: **Pandas**, **Polars**, and **Dask**. This includes:
   - Removing duplicates
   - Filling missing values
   - Standardizing product names and prices

4. **Performance Evaluation of Optimization**  
   Each method is evaluated based on:
   - Execution time
   - Memory usage
   - CPU utilization
   - Throughput (records per second)

---


## 📁 Project File Structure

| No | Folder / File | Description |
|----|---------------|-------------|
| 1  | [`data`](./data) | Folder containing all datasets (raw, cleaned, optimized). |
|    | [`Item_list.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/data/Item_list.csv) | Raw product dataset collected from PG Mall before cleaning. Contains product name, price, location, and link with some duplicates, null values, and uncleaned fields. |
|    | [`merged_product_list.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/data/merged_product_list.csv) | Merged dataset of all raw subcategory data from `Item_By_Category`. |
|    | [`updated_item_list.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/data/updated_item_list.csv) | Raw dataset with product name, price, location, link, and product type. |
|    | [`Item_list_cleaned.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/data/Item_list_cleaned.csv) | Cleaned dataset using Pandas. |
|    | [`Item_list_cleaned_optimized.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/data/Item_list_cleaned_optimized.csv) | Cleaned dataset using Polars. |
|    | [`Item_list_cleaned_dask.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/data/Item_list_cleaned_dask.csv) | Cleaned dataset using Dask. |
| 2  | [`p1`](./p1) | Folder containing scraping and cleaning notebooks. |
|    | [`PgmallScraping_withoutOptimization.ipynb`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/p1/PgmallScraping_withoutOptimization.ipynb) | Basic web scraping and data collection without performance optimization. |
|    | [`PgmallScraping_multithreading.ipynb`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/p1/PgmallScraping_multithreading.ipynb) | Web scraping using multithreading to improve performance. |
|    | [`PgmallBySubCategory.ipynb`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/p1/PgmallBySubCategory.ipynb) | Scrapes product data by subcategory. |
|    | [`Map_ProductType.ipynb`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/p1/Map_ProductType.ipynb) | Maps raw products to product type categories. |
|    | [`Cleaning_Process_withoutOptimization.ipynb`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/p1/Cleaning_Process_withoutOptimization.ipynb) | Cleaning using Pandas (nulls, duplicates, fields). |
|    | [`Cleaning_Process_withPolar.ipynb`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/p1/Cleaning_Process_withPolar.ipynb) | Cleaning using Polars for better performance. |
|    | [`Cleaning_Process_withDask.ipynb`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/p1/Cleaning_Process_withDask.ipynb) | Cleaning using Dask for scalability. |
| 3  | [`p2`](./p2) | Folder containing performance evaluation and visualization. |
|    | [`Chart.ipynb`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/p2/Chart.ipynb) | Bar chart visualization for performance metrics. |
|    | [`performance_log_scraping.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/p2/performance_log_scraping.csv) | Performance data before scraping optimization. |
|    | [`performance_log_scrapingoptimized.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/p2/performance_log_scrapingoptimized.xlsx) | Performance data after scraping optimization. |
| 4  | [`report`](./report) | Final reports and presentations for the project. |
|    | [`HPDP - PROJECT 1 REPORT.pdf`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/report/HPDP%20-%20PROJECT%201%20REPORT.pdf) | Detailed written report documenting the background, implementation, and findings of the project. |
|    | [`Presentation Project 1.pdf`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/report/Presentation%20Project%201.pdf) | Slide deck used during the project presentation summarizing key insights, approach, and results. |
|    | [`Turnitin_PROJECT 1.pdf`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/report/Turnitin_PROJECT%201.pdf) | Turnitin plagiarism report for the submitted project documentation. |




---

## 🔍 Quick Links

- **📁 Link to Full Code Folder:** [Google Drive – GroupD Full Code](https://drive.google.com/drive/folders/1LxHqnUEUspyp9mxUi2mLtvIscrrFHdZG?usp=sharing)  
- **🗃️ Link to Datasets:** [GitHub – GroupD Data Folder](https://github.com/drshahizan/HPDP/tree/main/2425/project/p1/GroupD/data)

---

## 🙌 Acknowledgements

- Data collected from [PG Mall](https://pgmall.my/)
- Developed with Python, Google Colab, Beautiful Soup, Requests, Pandas, Polars, and Dask