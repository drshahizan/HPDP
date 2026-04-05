# <div align='center'>📘 Assignment 2: Mastering Big Data Handling</div>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>LOW JIE SHENG</td>
    <td>A22EC0075</td>
  </tr>
</table>
<br>

# 📝 Assignment Tasks

## 📂 Task 1: Dataset Selection  
We chose a Kaggle dataset with GitHub Issues data that was more over 700 MB in size. The dataset's details and column descriptions are as follows:  

### 📊 Data Details
- **Dataset**: GitHub Issues 
- **Data source**: [Kaggle - GitHub Issues](https://www.kaggle.com/datasets/davidshinn/github-issues/data)  
- **File size**: 2.85GB  
- **Data Shape**: (5,332,153 rows, 3 columns)  
- **Domain**: Software development / Issue tracking

  This dataset contains a large collection of GitHub issue reports, including URLs, titles, and detailed descriptions from various open-source repositories. It captures real-world software development discussions, bug reports, feature requests, and other issue tracking activities. This makes it ideal for exploring text analytics, natural language processing, and understanding patterns in software project management and community collaboration.

### 🧾 Dataset Column Descriptions
Below is a detailed breakdown of the columns in the file:

| Column Name           | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| issue_url             | URL to the GitHub issue                                                     |
| issue_title           | Title of the issue                                                          |
| body                  | Full text body/description of issue                                         |


---

## 🔍 Task 2: Load and Inspect Data  
We begin by loading a manageable sample of the dataset to understand its structure without exhausting system memory.

**Code Snippet** <br>
![Image](https://github.com/jiesheng4616/jiesheng4616/blob/8a60a63e01e1c621df19ebbae046217fbbe66b8d/Screenshot%202025-06-01%20171408%20code%20pandas.png)

**Output**
| **Metric**         | **Value** |
|--------------------|-----------|
| Processing Time (S) | 1.7265    |
| Memory Usage (MB)   | 58.80     |
![image](https://github.com/jiesheng4616/jiesheng4616/blob/8a60a63e01e1c621df19ebbae046217fbbe66b8d/Screenshot%202025-06-01%20170439%20%20pandas.png)

- Column and Datatype <br>
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20171154%20datatype%20for%20pandas.png)


Explanation:
We load only the first 100,000 rows to inspect shape, column names, and datatypes efficiently, tracking time and memory to establish a baseline.

## 🛠️Task 3: Apply Big Data Handling Strategies


### 📉 1. Load Less Data
Large datasets often contain columns irrelevant to the analysis. Loading only necessary columns reduces memory usage and speeds up data loading. <br><br>
We specify columns to load using the usecols parameter in pd.read_csv(). This reduces I/O and memory overhead. <br><br>
**Code Snippets**- <br>
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20172431%20code%20load%20less%20data.png)

<br><br>**Outputs**<br>
|**Metric**|**Value**|
|----------|---------|
|Processing Time (S)|0.9109|
|Memory Usage (MB)|58.80|
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20170509%20load%20less%20data.png) <br>

Significance: 
By focusing only on needed columns, this strategy directly targets data volume, improving efficiency without losing analytic value.


### 📦 2. Use Chunking
Loading very large files can exceed system memory, causing crashes or slowdowns. <br><br>
Using Pandas’ chunksize parameter, data is read in manageable pieces (chunks). Each chunk is processed individually, allowing large datasets to be analyzed sequentially without loading the entire dataset into memory.

<br><br>**Code Snippets**- <br>
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20172613%20code%20chunking1.png)
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20172636%20code%20chunking%202.png)

<br><br>**Outputs**<br>
|**Metric**|**Value**|
|----------|---------|
|Processing Time (S)|7.5677|
|Memory Usage (MB)|0.52|
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20170607%20chunking.png) 

Benefits: 
Chunking balances memory use and processing time, making it a versatile technique for batch data processing.


### 🧮 3. Optimize Data Types
Default data types (e.g., object or float64) can be unnecessarily memory-heavy. <br><br>
Convert columns to appropriate, more efficient types such as categorical for strings with few unique values or downcast numeric columns to smaller types.<br><br>

**Code Snippets**-<br>
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20172729%20optimize%20code%201.png)
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20172749%20optimize%20code%202.png)

<br><br>**Outputs**<br>
|**Metric**|**Value**|
|----------|---------|
|Processing Time (S)|0.0003|
|Memory Usage (MB)|0.52|
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20170644%20optimize%20data%20type.png) 

Impact: 
This step often results in significant memory savings, enabling the handling of larger datasets within limited resources.


### 🔍 4. Sampling
Sampling allows fast prototyping and analysis by working on a smaller, representative subset of the data.<br><br>
We perform random sampling and stratified sampling to maintain distributional characteristics in the smaller dataset.<br><br>

**Code Snippets**-<br>
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20172912%20sampling%201.png)
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20173006%20sampling%202.png)

<br><br>**Outputs**<br>
|**Metric**|**Value**|
|----------|---------|
|Processing Time (S)|0.0011|
|Memory Usage (MB)|0.11| <br>
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20170724%20sampling.png) 

Advantages: 
Sampling reduces computational burden while preserving data representativeness, critical for exploratory analysis.


### 📉 5. Parallel Processing with Dask
Datasets exceeding available memory require distributed or parallel computation. <br><br>
We clean the raw data in chunks with Pandas, then load it with Dask, which handles data partitions in parallel. <br><br>

**Code Snippets**- <br>
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20173256%20code%20dask%20.png)
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20173314%20code%20dask%202.png)

<br><br>**Outputs**<br>
|**Metric**|**Value**|
|----------|---------|
|Processing Time (S)|0.1425|
|Memory Usage (MB)|0.01|
![image](https://github.com/jiesheng4616/jiesheng4616/blob/b125d85283c28f4b4c81b83c26fae5d763d0d8d5/Screenshot%202025-06-01%20170755%20dask.png) <br>

Effectiveness:
Dask enables scalable, parallel data processing beyond single-machine memory limits, ideal for big data scenarios.


## 📊 Task4 : Comparative Analysis

### Part 1: Comparing the Performance of Different Optimized Strategies in Handling Large Dataset

In this section, we evaluate the effectiveness of several optimization techniques applied previously to manage the extensive GitHub Issues dataset. These approaches include:

- **Load Less Data** (Loading only the necessary columns)
- **Chunking** (Reading the dataset in smaller portions)
- **Optimize Data Types** (Converting data types to reduce memory consumption)
- **Sampling** (Working with a smaller, representative subset of the data)
- **Parallel Processing with Dask** (Leveraging Dask for distributed and parallel data processing)

Our comparison focuses on two primary performance indicators:
- **Memory Usage:** The amount of RAM utilized during data loading or processing. 
- **Processing Time:** The duration required to complete data loading or processing tasks.


| Optimized Strategy       | Processing Time (seconds) | Memory Usage (MB) |
|---------------------------|----------------------------|--------------------|
| Load Less Data            | *0.9109*                   | *58.80*            |
| Chunking                  | *7.5677*                   | *0.52*             |
| Optimize Data Types       | *0.0003*                   | *0.52*             |
| Sampling                  | *0.0011*                   | *0.11*             |
| Parallel Processing (Dask)| *0.1425*                   | *0.01*             |

---


<br> **Comparison of Optimized Strategies** <br>
![Chart](https://github.com/jiesheng4616/jiesheng4616/blob/37ba16366f787a6c8edd5162b2b0e0088ef43e11/chart.png)


### Part 2: Comparison of different library for big data

In this section, we evaluate and compare the capabilities and efficiency of three distinct libraries—Pandas, Dask, and Polars—in handling large datasets. For simplicity and consistency, we focus on the fundamental operation of data loading. The performance is measured using two key metrics: **execution time** and **memory consumption**.

<br><br>

Pandas: 
The Pandas library was used to load the dataset with the typical read_csv function, demonstrating a straightforward approach widely used in data analysis workflows.


**Code Snippets**- <br>
![image](https://github.com/jiesheng4616/jiesheng4616/blob/37ba16366f787a6c8edd5162b2b0e0088ef43e11/Screenshot%202025-06-01%20173357%20codepandas%201.png)
![image](https://github.com/jiesheng4616/jiesheng4616/blob/37ba16366f787a6c8edd5162b2b0e0088ef43e11/Screenshot%202025-06-01%20173357%20codepandas%202.png)


<br><br>**Outputs**<br>
|**Metric**|**Value**|
|----------|---------|
|Processing Time (S)|87.15|
|Memory Usage (MB)|4012.66|
![image](https://github.com/jiesheng4616/jiesheng4616/blob/37ba16366f787a6c8edd5162b2b0e0088ef43e11/Screenshot%202025-06-01%20170843%20pandas%20performance.png) <br>


Explanation:
Loading the dataset with Pandas took 87.15 seconds and consumed approximately 4GB of memory. This demonstrates Pandas’ ease of use but also highlights its relatively high resource consumption when handling large datasets.

<br><br>

Polars: 
Polars was used to load the dataset leveraging its efficient Rust-based engine designed for speed and low memory consumption.


**Code Snippets**- <br>
![image](https://github.com/jiesheng4616/jiesheng4616/blob/37ba16366f787a6c8edd5162b2b0e0088ef43e11/Screenshot%202025-06-01%20173615%20polars%202.png)
![image](https://github.com/jiesheng4616/jiesheng4616/blob/37ba16366f787a6c8edd5162b2b0e0088ef43e11/Screenshot%202025-06-01%20173700%20polars%203.png)


<br><br>**Outputs**<br>
|**Metric**|**Value**|
|----------|---------|
|Processing Time (S)|36.17|
|Memory Usage (MB)|3790.27|
![image](https://github.com/jiesheng4616/jiesheng4616/blob/37ba16366f787a6c8edd5162b2b0e0088ef43e11/Screenshot%202025-06-01%20170901%20polars.png) <br>


Explanation:
Polars loaded the dataset faster, taking 36.17 seconds and using about 3.8GB of memory. Although it showed better performance than Pandas, the resource usage suggests there is still room for further optimization depending on dataset characteristics and code implementation.

<br><br>

PyArrow: 
PyArrow was used to load and process the dataset, leveraging its high-performance in-memory columnar data structures optimized for speed and interoperability.


**Code Snippets**- <br>
![image](https://github.com/jiesheng4616/jiesheng4616/blob/37ba16366f787a6c8edd5162b2b0e0088ef43e11/Screenshot%202025-06-01%20173727%20pyarrow%202.png)
![image](https://github.com/jiesheng4616/jiesheng4616/blob/37ba16366f787a6c8edd5162b2b0e0088ef43e11/Screenshot%202025-06-01%20173848%20pyarrow%203.png)
![image](https://github.com/jiesheng4616/jiesheng4616/blob/37ba16366f787a6c8edd5162b2b0e0088ef43e11/Screenshot%202025-06-01%20173848%20pyarrow%204.png)


<br><br>**Outputs**<br>
|**Metric**|**Value**|
|----------|---------|
|Processing Time (S)|1.68|
|Memory Usage (MB)|4858.99|
![image](https://github.com/jiesheng4616/jiesheng4616/blob/37ba16366f787a6c8edd5162b2b0e0088ef43e11/Screenshot%202025-06-01%20170915%20%20pyarrow.png) <br>


Explanation:
PyArrow excelled in processing speed, completing the load in just 1.68 seconds, but consumed more memory at approximately 4.9GB. This indicates PyArrow’s strength in fast data handling with its optimized columnar memory format, albeit at the cost of increased memory usage.

<br>

| Library   | Processing Time (seconds) | Memory Usage (MB) |
|-----------|---------------------------|-------------------|
| Pandas    | 87.15                     | 4012.66           |
| Polars    | 36.17                     | 3790.27           |
| PyArrow   | 1.68                      | 4858.99           |


<br> **Comparison of Data Loading Libraries** <br>
![Chart](https://github.com/jiesheng4616/jiesheng4616/blob/fc4fb1dd146a6acd7fca4e83cacd0f47a98b0b58/chart1.png)

<br><br>

## 📌 Task 5: Conclusion & Reflection

## Task 5: Conclusion & Reflection

### Key Observations
This assignment demonstrated that different big data handling strategies have distinct trade-offs in terms of memory usage and processing speed. Load Less Data and Sampling techniques provided the fastest execution times, while Chunking and Parallel Processing with Dask excelled at minimizing memory consumption. Among libraries, PyArrow offered the quickest data loading, Polars showed balanced performance, and Pandas, while easiest to use, was the most resource-intensive.

### Benefits
- **Load Less Data:** Efficiently reduces memory and processing time when only necessary columns are needed.  
- **Chunking:** Allows processing of datasets too large to fit into memory by reading in manageable portions.  
- **Optimize Data Types:** Significantly lowers memory usage by converting to appropriate data types.  
- **Sampling:** Enables quick prototyping and analysis on smaller, representative subsets of data.  
- **Parallel Processing with Dask:** Offers scalable and memory-efficient processing for very large datasets.  
- **Modern Libraries (PyArrow, Polars):** Provide faster and more memory-efficient alternatives to traditional tools.

### Limitations
- **Load Less Data:** Not suitable if analysis requires the full dataset with all columns.  
- **Chunking:** May increase overall processing time due to overhead in handling multiple chunks.  
- **Optimize Data Types:** Requires careful understanding of data and can introduce complexity.  
- **Sampling:** Risks losing important information present in the full dataset.  
- **Parallel Processing with Dask:** Has a steeper learning curve and setup complexity compared to Pandas.  
- **Library Choices:** Newer libraries might require adaptation and familiarity; compatibility issues may arise.

### Reflection
This assignment provided valuable insights into how strategic data handling can overcome limitations of traditional tools when working with big data. It highlighted the importance of selecting appropriate methods and libraries based on dataset size, system resources, and analysis goals. The hands-on experience reinforced the critical role of memory optimization, efficient processing, and the potential of parallel computing in data science workflows.
