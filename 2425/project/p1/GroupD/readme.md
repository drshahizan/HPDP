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

## 📁 Project Structure

| No | Folder / File |
|----|----------------|
| 1  | [`data`](./data) |
| 2  | [`p1`](./p1) |
| 3  | [`p2`](./p2) |
| 4  | [`report`](./report) |

---

## 🔍 Quick Links

- **📁 Link to Full Code Folder:** [Google Drive – GroupD Full Code](https://drive.google.com/drive/folders/1LxHqnUEUspyp9mxUi2mLtvIscrrFHdZG?usp=sharing)  
- **🗃️ Link to Datasets:** [GitHub – GroupD Data Folder](https://github.com/drshahizan/HPDP/tree/main/2425/project/p1/GroupD/data)

---

## 🙌 Acknowledgements

- Data collected from [PG Mall](https://pgmall.my/)
- Developed with Python, Google Colab, Beautiful Soup, Requests, Pandas, Polars, and Dask