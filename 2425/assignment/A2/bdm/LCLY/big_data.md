---

## 📚 Table of Contents
1. [Introduction](#1-introduction)
2. [Dataset Overview and Inspection](#2-dataset-overview-and-inspection)
3. [Big Data Handling Strategies](#3-big-data-handling-strategies)
4. [Comparative Analysis](#4-comparative-analysis)
5. [Conclusion and Reflection](#5-conclusion-and-reflection)
6. [References](#6-references)

---

## 1. Introduction

### 1.1 Background of the Project
Traditional data processing tools like Pandas face challenges with large datasets. This project addresses those limitations by applying big data strategies and leveraging Dask for parallel processing on the **UK Housing Prices Paid** dataset (>700MB).

### 1.2 Objectives
- Understand the limitations of Pandas
- Apply strategies like chunking, sampling, data type optimization
- Implement parallel processing using Dask
- Compare Pandas, Dask, and Polars using:
  - Shape
  - Processing Time
  - Memory Usage
  - Throughput

### 1.3 Dataset Source
- **Dataset:** UK Housing Prices Paid  
- **Source:** [Kaggle](https://www.kaggle.com/datasets/hm-land-registry/uk-housing-prices-paid)  
- Over 25 million entries, 11 columns, >800MB

---

## 2. Dataset Overview and Inspection

### 2.1 Dataset Description
The dataset contains records of residential property sales in the UK with fields like price, transfer date, property type, location, and metadata.

### 2.2 Initial Loading
To begin the data analysis, the UK Housing Prices Paid dataset was loaded directly into the Colab environment using basic file handling methods. The dataset was obtained from Kaggle and extracted within the environment prior to analysis.
<br><br>
The following code snippet was used to list the dataset contents after ensuring the files were available:
![Screenshot 2025-06-02 120412](https://github.com/user-attachments/assets/ac89a356-673d-4e91-b0b2-5b41a2c7014c)

### 2.3 Basic Inspection
Once identified, the primary data file which is price_paid_records.csv was loaded using pandas for inspection:<br>
![image](https://github.com/user-attachments/assets/c1f76e76-a657-4cc0-9836-f36c30c2dc8f)
To gain an initial understanding of the dataset, a sample of 10 rows was loaded using pandas.read_csv() with the nrows=10 parameter. This small subset was used to inspect the structure, column data types, and basic memory and performance metrics.
<br>
- Shape: 10 rows × 11 columns  
- Processing Time: 0.0065s  
- Memory Usage: 0.01 MB  
- Throughput: 1,545.77 records/sec  
- Most fields are object types; "Price" is numeric<br>

**Sample Preview (via df.head())**

The dataset consists of various features related to property transactions in the UK. Key fields include:
- **Transaction unique identifier:** Unique ID for each transaction
- **Price:** The transaction price (in integer format)
- **Date of Transfer:** Date when the property was sold
- **Property Type, Old/New, Duration:** Categorical descriptors of the property
- **Town/City, District, County:** Geographical location fields
- **PPDCategory Type, Record Status:** Metadata about the transaction entry

**Data Types (via df.dtypes and df.info()):**
- Only Price is in numeric format (int64).
- All other columns are of object type, indicating strings or categorical data.
- All columns contain 10 non-null entries, suggesting no missing values in this sample.
- The Date of Transfer column, though it contains date information, is currently stored as a string (object), and may require conversion to datetime format for future processing or analysis.<br><br>

This initial inspection helps confirm that the dataset is well-structured and provides a strong foundation for further cleaning, transformation, and performance optimization.
This step ensured the dataset was correctly loaded and ready for further processing, including memory optimization and big data handling strategies using Pandas, Dask, and Polars.

---

## 3. Big Data Handling Strategies

### 3.1 Part 1: Strategies with Pandas & Dask
**3.1.1 Load Less Data**<br>
![image](https://github.com/user-attachments/assets/f1bc26ea-4365-467a-b005-b7e7fdbf9579)

- **Chunking**<br>
![image](https://github.com/user-attachments/assets/957700d3-e998-46ca-af6e-e7bbba59bfef)

- **Optimize Data Types**<br>
![image](https://github.com/user-attachments/assets/1d083f1b-c363-46a8-8bec-1f5339376b1a)

- **Sampling**<br>
![image](https://github.com/user-attachments/assets/a9b05f8e-0a27-4599-9580-2d9560496fef)

- **Parallel Processing with Dask**<br>
![image](https://github.com/user-attachments/assets/3779b30a-b649-4141-8f9c-d35c2d5dfc12)

### 3.2 Part 2: Comparing Libraries Reading Raw Data
In Part 2, we conducted a performance comparison of three selected Python libraries—Pandas, Dask, and Polars—by measuring their efficiency in reading the entire dataset.<br>

| Library | Visualization |
|---------|---------------|
| Pandas  | ![image](https://github.com/user-attachments/assets/ba0a6aac-853e-49ed-bfa1-c4ce213975f4) |  
| Dask    | ![image](https://github.com/user-attachments/assets/66f2fde1-7db0-4031-a471-4b99224b1dd9) | 
| Polars  | ![image](https://github.com/user-attachments/assets/fb00b800-01be-4d25-8ac2-5ef03a7a285d) |

---

## 4. Comparative Analysis

### 4.1 Metrics Used
- Processing Time  
- Memory Usage  
- Throughput  
- Shape

### 4.2 Results Summary

#### Part 1: Strategy Comparison

| **Strategies / Metrics**      | **Load Less Data** | **Chunking** | **Optimise Data Type** | **Sampling** | **Parallel Processing with Dask** |
|------------------------------|--------------------|--------------|------------------------|--------------|-------------------------------|
| **Processing Time (seconds)** | 20.7744            | 24.6773      | 14.3979                | 0.2308       | 114.8009                     |
| **Memory Usage (MB)**        | 5634.09            | 5634.09      | 4154.21                | 58.06        | 3824.82                      |
| **Throughput (records/sec)** | 1082549.73         | 911337.90    | 1561993.18             | 974246.76    | 195898.72                    |


#### Part 2: Library Comparison

| Library  | Time (s) | Memory (MB) | Throughput (records/sec)       |
|----------|----------|-------------|--------------------------------|
| Pandas   | *(crashed)* | 3824.82     | 178,308.34                     |
| Dask     | 126.13   | 2109.01     | 209,049,160.62                 |
| Polars   | 0.0108   | 2.1 GB      | ~2 billion                     |

### 4.3 Discussion
In Part 1, we observed the individual tasks using Pandas. The sampling process was the fastest followed by data type optimization due to the simplicity of the task and the optimized operations. While chunking and loading less data were slower. This is because it processes each chunk separately, and repeats operations in every chunk. Moreover, the in-memory processing model of Pandas where it will undergo data copying into RAM thus makes it inefficient in doing such operation. Dask took an overall processing time of 114.80s due to its lazy evaluation and created a task graph for optimization which adds extra overhead for task management before the .compute() is being called. <br>

Since we’ve observed that the unoptimized Pandas is suitable for simple operations, there is other evidence from memory usage that we investigated. In processing heavy data, Pandas consumed 5.63 GB of memory due to its eager execution model where all data is loaded into memory at once without partitioning. However, after we optimized the data types, the memory consumption dropped to 4.15 GB, and the sampling process used only 58 MB. These optimizations also improved throughput of the overall execution, enhancing the effectiveness and processing speed. In comparison, Dask uses less memory than unoptimized Pandas because it processes data in chunks that avoids full data loading. However it still consumed more than the optimized Pandas (with optimized data type and sampling), as parallelism processing required additional overhead.<br>

In terms of ease of processing, Pandas’s code is simple and easy from its familiar API and some built-in features. It remains the easiest for small to medium-sized datasets that fit comfortably in memory. If the large scale dataset is unoptimised, Pandas may crash. In this case, Dask is more capable when the size of the dataset exceeds memory.<br>

Part 2 compared how well the three libraries perform in loading an entire dataset. Polar uses 2.1 GB of memory and loads the entire dataset in 0.011 seconds which is significantly fast. This is being benefited from its architecture that is based on Rust and designed for zero-copy memory that allows it to process more than two billion records per second. Dask took 126.13s, which is about 10000 times slower than polars. However, Dask still handles 180K records per second with a moderate memory consumption, which is adequate for many applications. On the other hand, the execution of the traditional Pandas library crashes and displays a memory exhaustion result with no output. This proves that it is not suitable for processing large scale full data without any preprocessing.

---

## 5. Conclusion and Reflection

### 5.1 Summary of Findings
In conclusion, Polar is the most efficient library in executing, Dask is powerful for massive datasets with distributed data and Pandas is fast for smaller data but can crash large workloads. This also highlights the ability of Dask and Polars in handling large volumes of data effectively. Apart from that, Polars achieve the greatest throughput, proving that it is ideally suited for processing large datasets and potential for real-time processing with a learning curve. <br>

After the investigation on each of the libraries above, this research highlights the importance of choosing the right tools and optimization methods that are adapted to the size of the dataset and the resources. The selection of these libraries ultimately relies on the particular needs of the project, such as the size of the dataset, performance objectives, existing codebases and the member’s familiarity with various DataFrame APIs. For both speed and memory efficiency with extensive datasets, Polars is inevitably the champion, it provides excellent processing speeds and memory optimization with its Rust-based architecture. Dask is an ideal option to scale current Pandas workflows to extensive or distributed datasets as it facilitates out-of-core and parallel processing. It is good at connecting single-machine Pandas with genuine distributed computing. For a smaller dataset that can be accommodated within the available RAM, Pandas continues to be a strong choice. It is also remarkable with its wide range of features and community backing.


### 5.2 Benefits & Limitations

| Tool     | Benefits                                  | Limitations                                |
|----------|-------------------------------------------|--------------------------------------------|
| Pandas   | - Large community support<br> - Highly mature and a well-understood API<br> - Minimal setup required<br> - Suitable for users that are already familiar with data manipulation in Python.| - Loads the entire dataset into memory before processing<br> - Lead to memory errors or extremely slow performance if the dataset size is more than the available RAM.|
| Dask     | - Automates parallelization and task scheduling<br> - Designed to scale Pandas workflows to large and distributed datasets<br> - Its API is similar to Pandas so it makes the transition relatively smooth for Pandas users.   | - More complex due to lazy evaluation, task graphs, and potential distributed computing overhead<br>- Challenging on debugging process<br> - Requires more setup than Pandas (Dask cluster)  |
| Polars   | - Code structure is more concise and readable in complex operations- Memory efficient- Integrates well with tools that handle distributed storage | - Different API with pandas<br> - Require a learning curve<br> - Not a distributed computing library |

### 5.3 Personal Reflection

#### Bernice Lim Jing Xuan
> I have developed a clearer view of big data processing and the importance of selecting the right tools for the job by completing this project. I have learned that while pandas is suitable for small and quick data tasks, libraries like Dask and Polars offer excellent options when dealing with big data. I was especially thrilled to see how Polars with its optimized architecture processed data extremely fast. This project provided me with greater confidence in applying scalable data solutions to future projects, and it further reaffirmed my interest in data engineering and performance optimization.<br>

#### Chai Yu Tong
> This project allowed me to learn how to link Kaggle to Google Collab which was very useful because I could never run a 3 GB dataset on my own laptop. We also tried Polars, it is quite new for me but what I found after I started using it is that it is very fast and the code is simple. This project taught me the importance of choosing the right tool for the right task. I learned how to work with large datasets using Pandas, Dask, and Polars, and realized that performance can vary greatly depending on the method used. Most importantly, I learned how to work smarter with big data and the value of deepening my knowledge in my own field.<br>

---
## 6. References
- Gen. Devin DL. (June 21, 2024). [Several Methods for Efficiently Handling Large Datasets in Pandas](https://medium.com/@tubelwj/several-methods-for-efficiently-handling-large-datasets-in-pandas-b37e4db8256a). *Medium*.

- Vijaykumar Koppoju. (December 6, 2024). [Outpacing Pandas: The DataFrame Library That's 16X Faster](https://www.aptuz.com/blog/outpacing-pandas-the-dataframe-library-thats-16x-faster/). *Aptus Technology Solutions*.

- Vikas Rahar. (September 11, 2024). [Python Tip: Efficiently Handle Large Datasets with Dask](https://medium.com/@vikasrahar007/python-tip-efficiently-handle-large-datasets-with-dask-095054549f90). *Medium*.


