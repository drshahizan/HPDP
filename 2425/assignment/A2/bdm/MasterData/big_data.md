# 1. Introduction
### 1.1 Background of the Project
Nowadays, with big data becoming more common, many companies rely on their ability to process and analyse huge amounts of data to get useful insights. However, the usual data processing tools often can’t cope well with very large datasets, especially when the file size goes beyond a few hundred megabytes due to memory problems and slow processing.

This project looks into how we can handle big data more efficiently using Python. By using a real dataset that’s over 2GB in size, students will get hands-on experience with practical techniques like loading only required data, processing data in chunks, reducing memory usage through data type tweaks, sampling and speeding things up with parallel computing.

The goal is to explore how these different methods can improve performance, especially in terms of memory usage, processing time, and how easy the data is to work with. This kind of project is especially helpful for those aiming to work as data engineers or analysts, where managing large-scale data efficiently is a daily task.

### 1.2 Objectives
- To build hands-on skills in handling large datasets (more than 700MB) using Python.
- To try out and apply different big data techniques like chunking, sampling, data type tuning, and parallel processing.
- To compare how well normal (traditional) methods perform versus more optimized ways of loading and processing data.
- To understand the pros and cons when it comes to memory usage, speed, and coding difficulty while working with large files.
- To come up with useful insights and suggestions that can help improve how we manage big datasets in real work settings.

### 1.3 Target Website and Data to be Extracted
The dataset used for this assignment was taken from Kaggle. The main file we’re working with is <b>Book_rating.csv</b>, which comes from a bigger collection of Amazon book reviews. The file is around <b>2.86GB</b> in size which is big enough to really test out different big data processing methods.
This dataset contains <b>millions of book reviews and ratings</b> made by users, plus extra info like the book title, author name, user ID, and the review text. With all this data, it’s great not just for exploring patterns and trends but also for testing how well different data loading and processing techniques work.

# 2.0 Dataset Overview and Inspection
### 2.1 Dataset Description
- **Source:** [Kaggle (Amazon Books Reviews Dataset)](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews)
- **File Used:** Book_rating.csv
- **Size:** 2.86 GB
- **Domain:** E-commerce / Literature / User Reviews
- **Number of Records:** Over 10 million entries (3000000 rows x 10 columns )
- **Features/Columns:**
  - **Id:** The Id of Book
  - **Title:** Book Title
  - **Price:** The price of Book
  - **User_id:** Id of user who rate the book
  - **profileName:** Name of user who rate the book
  - **review/helpfulness:** Helpfulness rating of the review, e.g. 2/3
  - **review/score:** Rating from 0 to 5 for the book
  - **review/time:** Time of given the review
  - **review/summary:** The summary of text review
  - **review/text:** The full text of a review

### 2.2 Initial Loading
The dataset was initially loaded using **Pandas** in Google Colab.

![image](https://github.com/user-attachments/assets/519748cf-5ff7-4bed-ba7a-b054f35b85b6)

On standard Colab runtimes (≈12GB RAM), it was able to load this large dataset successfully, but it was not optimal and could slow down further processing. Additionally, due to its large size (2.86 GB), direct loading into memory using pd.read_csv() without optimisations typically leads to memory errors or sluggish performance.

### 2.3 Basic Inspection
Once the file was loaded, a basic inspection of the dataset was conducted to understand its structure and contents.

![image](https://github.com/user-attachments/assets/5271456e-474c-464a-8aa3-1b0fc4c6804f)

Output:

![image](https://github.com/user-attachments/assets/2a3a908c-e306-42b9-9f99-2e913a0c9021)

Observations:
- The dataset has about **3 million rows** and **10 columns**, which means there are around **30 million data points** in total.
- Most of the columns (7 out of 10) are **object type** (usually text), which normally take up more memory and might be improved with type optimisation.
- Only **three columns are numeric**:
  - Price and review/score are in **float64**,
  - review/time is in **int64**.
- When loaded fully into **Pandas**, the dataset uses around **229MB of memory**. That’s still okay for most systems, but optimising it can help improve processing speed and efficiency.
- Columns like review/text, review/summary, and profileName have **text data**, which can vary a lot in length and might be sparse

# 3.0 Big Data Handling Strategies and Loading Data Using Different Libraries
### 3.1 Part 1 (5 Big Data Strategies)
In part 1 of handling our dataset, we performed five big data handling strategies by using **Pandas** library to see which strategy has a better performance.

#### 3.1.1 Load Less Data

![image](https://github.com/user-attachments/assets/df007fe2-8a31-4cde-9a59-e726d093fea4)


#### 3.1.2 Chunking

![image](https://github.com/user-attachments/assets/faa26f1d-4005-41a9-8e6e-4c8c4d861547)


#### 3.1.3 Optimize Data Type

![image](https://github.com/user-attachments/assets/2ed92f99-8391-4b68-b070-7f30c35e6f0f)


#### 3.1.4 Sampling

![image](https://github.com/user-attachments/assets/8e6259fd-5093-4a32-a43e-6c5d8f5adb55)


#### 3.1.5 Parallel Processing with Dask

![image](https://github.com/user-attachments/assets/28e5a124-4f57-4b90-a28c-6646802a15e7)


### 3.2 Part 2 (Loading dataset with different libraries)
In part 2 of handling our dataset, we performed the action of loading the dataset by using different libraries such as **Pandas**, **Polars** and **Dask** libraries to see which strategy has a better performance.

#### 3.2.1 Using Pandas library

![image](https://github.com/user-attachments/assets/022eba3d-4475-46a8-a4c3-ed7997317da6)


#### 3.2.2 Using Polars library

![image](https://github.com/user-attachments/assets/724f4aea-9200-407b-a4f4-399214646984)


#### 3.2.3 Using Dask library

![image](https://github.com/user-attachments/assets/94118897-7859-4a76-8db6-68447fc1c75a)


# 4.0 Comparative Analysis
### 4.1 Metrics Used
- Code execution time (s)
- Peak memory usage (MB)
- CPU usage (%)
- Throughput (rows/s)

### 4.2 Results Summary
#### 4.2.1 Part 1 (Comparing Between Strategies)
<table border="1">
  <tr>
    <th rowspan="2">Metrics</th>
    <th colspan="4">Pandas</th>
    <th rowspan="2" width=15%>Parallel Processing with Dask</th>
  </tr>
  <tr>
    <th width=15%>Load Less Data</th>
    <th width=15%>Chunking</th>
    <th width=15%>Optimize Data Type</th>
    <th width=15%>Sampling</th>
  </tr>
  <tr>
    <td>Code Execution Time (s)</td>
    <td align="center">23.3248</td>
    <td align="center">58.7441</td>
    <td align="center">58.0145</td>
    <td align="center">60.2045</td>
    <td align="center">77.7479</td>
  </tr>
  <tr>
    <td>Peak Memory Usage (MB)</td>
    <td align="center">742.9210</td>
    <td align="center">1190.1397</td>
    <td align="center">3856.6556</td>
    <td align="center">3856.7046</td>
    <td align="center">447.7110</td>
  </tr>
  <tr>
    <td>CPU Usage (%)</td>
    <td align="center">13.6</td>
    <td align="center">4.4</td>
    <td align="center">30.6</td>
    <td align="center">4.0</td>
    <td align="center">4.0</td>
  </tr>
  <tr>
    <td>Throughput (rows/s)</td>
    <td align="center">128618.50</td>
    <td align="center">51068.93</td>
    <td align="center">51711.24</td>
    <td align="center">4983.01</td>
    <td align="center">38586.26</td>
  </tr>
</table>

#### 4.2.2 Part 2 (Comparing Between Libraries)
<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Metrics/Libraries</th>
      <th>Pandas</th>
      <th>Polars</th>
      <th>Dask</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Code Execution Time (s)</td>
      <td align="center">55.8117</td>
      <td align="center">13.4898</td>
      <td align="center">81.2019</td>
    </tr>
    <tr>
      <td>Peak Memory Usage (MB)</td>
      <td align="center">3856.6912</td>
      <td align="center">0.0861</td>
      <td align="center">428.5369</td>
    </tr>
    <tr>
      <td>CPU Usage (%)</td>
      <td align="center">20.0</td>
      <td align="center">40.5</td>
      <td align="center">28.0</td>
    </tr>
    <tr>
      <td>Throughput (rows/s)</td>
      <td align="center">53752.17</td>
      <td align="center">222389.96</td>
      <td align="center">36944.93</td>
    </tr>
  </tbody>
</table>

### 4.3 Discussions and Key Observation
#### 4.3.1 Part 1 (Comparing Between Strategies)
Several data processing techniques from Pandas are compared in the Part 1 section and Dask is introduced for parallel processing. The fastest way to execute code is to “Load Less Data” (23.3248s), then to “Optimize Data Type” (58.0145s), then to “Chunking” (58.7441s) and finally to “Sampling” (60.2045s). In this case, Dask takes the longest at 77.7479 seconds which suggests parallelization might not be worth it for smaller or medium-sized datasets.

The strategy of “Load Less Data” uses the least memory (742.9210 MB) compared to the other three Pandas-based approaches which each use about 3856 MB. Dask uses less memory (447.7110 MB) than Pandas which proves how well its chunked computation model works.

The CPU is used the most by the “Optimize Data Type” option (30.6%) and the rest of the options, including “Chunking”, “Sampling” and Dask, use a very small amount (roughly 4% each). Therefore, changing data types can use a lot of CPU power because of the effort needed to convert them.

Among the strategies, “Load Less Data” performs best, handling 128,618.50 rows per second which is more than double the others. Both “Chunking” and “Optimize Data Type” have about the same speed (~51,000 rows/s) and Dask reaches 38,586.26 rows/s which is faster than “Sampling” but slower than most Pandas-based strategies. This suggests Dask is more suitable when memory is more important than speed.

#### 4.3.2 Part 2 (Comparing Between Libraries)
This section looks at how Pandas, Polars and Dask libraries perform compared to each other. Polars is the top performer in most of the key metrics. It finishes the most quickly (13.4898s), uses the least amount of memory (0.0861 MB) and processes the most rows per second (222,389.96). It demonstrates that Polars is faster because its backend is written in Rust and it uses efficient multi-threading.

Pandas is a well-known tool, but it takes the most time (55.8117s) and uses the largest amount of memory (3856.6912 MB). It also uses a moderate amount of CPU (20%) and has low throughput (53752.17 rows/s) which means it struggles with large data or when speed is important.

Dask, which is made for parallel processing, demonstrates a mix of outcomes. Although it uses less memory than Pandas (428.5369 MB), it takes the longest to run (81.2019s) and has the lowest number of rows processed per second (36944.93). The fact that it uses 28% of the CPU means it takes up a lot of resources for handling distributed tasks.

# 5.0 Conclusion and Reflection
### 5.1 Summary of Findings

### 5.2 Benefits and Limitations of Each Strategies

### 5.3 Personal Reflection
#### 5.3.1 Kek Jesslyn

#### 5.2.2 Tan Jun Yuan

# 6.0 Reference
