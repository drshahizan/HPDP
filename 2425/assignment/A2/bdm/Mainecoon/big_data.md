<h1 align="center"> 
  Mastering Big Data Handling
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>MULYANI BINTI SARIPUDDIN</td>
    <td>A22EC0223</td>
  </tr>
  <tr>
    <td width=80%>ALIATUL IZZAH BINTI JASMAN</td>
    <td>A22EC0136</td>
  </tr>
</table>

# 📊 Mastering Big Data Handling

This project focuses on efficiently managing large datasets using Python and scalable libraries. We applied various strategies to handle datasets exceeding 700MB, specifically the NYC Parking Tickets dataset from Kaggle.

---

## 📂 Project Files

| File Name                     | Description                                | Link |
|------------------------------|--------------------------------------------|------|
| **Raw Dataset**              | Original dataset with parking tickets data | [![Download](https://img.shields.io/badge/Download-Drive-blue?logo=google-drive)](https://drive.google.com/file/d/1eK8V7xZXzvBDPVBAppC2TzItXCjdHnkr/view?usp=sharing) |
| **Google Collab**      | Code to load and inspect data              | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](notebooks/data_loading.ipynb) |


---

## 📚 Libraries Used

| Library | Description |
|--------|-------------|
| `Pandas` | A popular library for data manipulation and analysis, ideal for smaller datasets. |
| `Dask`   | A parallel computing library that scales Pandas operations for larger datasets. |
| `Polars` | A high-performance DataFrame library optimised for speed and memory efficiency. |

---

## 🔗 Data Details

- **Original Dataset**: Contains over **10,803,028 rows** of data and **43 columns** related to parking violations in NYC.

### Columns

---

## 📊 Key Observations

1. **Efficiency Gains**: Using Dask and Polars significantly reduced memory usage and execution time compared to traditional Pandas methods.
2. **Scalability**: Dask’s ability to handle large datasets in parallel allowed for smoother processing.
3. **Data Integrity**: Data cleaning improved data quality, ensuring reliable analysis.

---

## 📈 Benefits and Limitations of Each Method

### Pandas
- **Benefits**: 
  - Easy to use and well-documented.
  - Great for exploratory data analysis on smaller datasets.
- **Limitations**: 
  - Struggles with memory management for very large datasets.
  - Slower execution times compared to optimized libraries.

### Dask
- **Benefits**:
  - Handles larger-than-memory datasets effectively.
  - Parallel processing capabilities enhance performance.
- **Limitations**:
  - Slightly steeper learning curve than Pandas.
  - Overhead can be significant for smaller datasets.

### Polars
- **Benefits**:
  - Extremely fast and memory-efficient.
  - Excellent performance for large-scale data manipulation.
- **Limitations**:
  - Less mature ecosystem compared to Pandas and Dask.
  - May require adjustments for compatibility with existing Pandas-based workflows.

---

## ✅ Reflection

This assignment enhanced our understanding of big data handling techniques. We learned the importance of choosing the right tools for specific tasks, especially when dealing with large datasets. The experience reinforced the need for efficient data processing strategies to extract meaningful insights without compromising performance. Overall, mastering these techniques equips us with essential skills for navigating the data-driven landscape more effectively.
