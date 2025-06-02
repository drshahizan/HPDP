<h1 align="center"> 
  Assignment 2 - MasterData(Amazon Book Review Dataset)
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td>KEK JESSLYN</td>
    <td>A22EC0057</td>
  </tr>
  <tr>
    <td>TAN JUN YUAN</td>
    <td>A22EC0107</td>
  </tr>
</table>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

# <img src="https://github.com/user-attachments/assets/f2e03ef1-27c9-4b8f-9920-8c429eb20bd6" width=40px height=40px> Table of Contents
1. [Introduction](#1-introduction)
2. [Dataset Overview and Inspection](#2-dataset-overview-and-inspection)
3. [Big Data Handling Strategies and Loading Data Using Different Libraries](#3-big-data-handling-strategies-and-loading-data-using-different-libraries)
4. [Comparative Analysis](#4-comparative-analysis)
5. [Conclusion and Reflection](#5-conclusion-and-reflection)
6. [References](#6-references)

<a name="1-introduction"></a>
# <img src="https://github.com/user-attachments/assets/ec2cacd2-740e-4aea-a186-0c35bc115e45" width=43px height=40px> 1. Introduction
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

<a name="2-dataset-overview-and-inspection"></a>
# <img src="https://github.com/user-attachments/assets/7e00a8b0-f6f9-424b-abfb-71d56ac67a1a" width=43px height=40px> 2. Dataset Overview and Inspection
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

<a name="3-big-data-handling-strategies-and-loading-data-using-different-libraries"></a>
# <img src="https://github.com/user-attachments/assets/e5d567b0-8ac4-42a8-94f1-0b7506de87cb" width=43px height=40px> 3. Big Data Handling Strategies and Loading Data Using Different Libraries
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


<a name="4-comparative-analysis"></a>
# <img src="https://github.com/user-attachments/assets/bf9a03a5-df6b-4e8a-8641-46e4b872b83f" width=43px height=40px> 4. Comparative Analysis
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
<table border="1">
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

<a name="5-conclusion-and-reflection"></a>
# <img src="https://github.com/user-attachments/assets/b35663ff-9d7f-4b7c-93b4-c91e8133f547" width=43px height=40px> 5. Conclusion and Reflection
### 5.1 Summary of Findings
It is clear from the evaluation that using the “Load Less Data” method in Pandas provides the best performance and is therefore suitable for tasks that require high speed. Even though “Optimize Data Type” and “Chunking” are not very fast, they use a lot of memory and “Optimize Data Type” also uses the most CPU. The “Sampling” strategy uses less CPU power, but it is not efficient when processing a lot of data because it delivers the weakest throughput. Dask’s parallel approach saves memory, but it generally takes longer and offers less throughput than Pandas’ best techniques which means parallelization may not be necessary for small datasets.

In every important performance metric, Polars is much faster than Pandas and Dask. It has the shortest execution time, requires the least memory and provides the greatest throughput which is perfect for large and fast data workloads. While pandas are useful and used by many, they are not as fast or efficient with memory as other libraries. Dask is designed for parallel and distributed computing and uses less memory than Pandas, but it is slower for most tasks which means its benefits are best seen in very large-scale or distributed environments. In general, Polars is the best library for handling data processing that requires speed, low memory usage and high throughput.

### 5.2 Benefits and Limitations of Each Strategies
<table border="1">
  <tr>
    <th></th>
    <th width=40%>Benefits</th>
    <th width=40%>Limitations</th>
  </tr>
  <tr>
    <td>Load Less Data</td>
    <td>
      <ul>
        <li>Among all strategies, this one took the least time to run.</li>
        <li>The highest throughput makes handling data very efficient.</li>
        <li>Because it uses very little memory, it is suitable for places with limited memory.</li>
        <li>Useful when there is only need to look at a small part of the data.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>May cause insights to be lost if important details are found in the excluded data.</li>
        <li>This approach is not suitable when processing the whole dataset which is necessary (for example, in training models or combining all the data).</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Chunking</td>
    <td>
      <ul>
        <li>Processes big files in sections, so the memory does not get overloaded.</li>
        <li>Less RAM is used when loading the small dataset than when loading the full dataset.</li>
        <li>Prevents crashes that happen because of memory errors.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>The program executes longer because it has to read and process the data more than once.</li>
        <li>The data is processed at a slow rate.</li>
        <li>Makes the code more complicated because it needs to manage and merge the results from different chunks.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Optimize Data Type</td>
    <td>
      <ul>
        <li>Reduces the amount of memory used for future calculations when used properly.</li>
        <li>Improves how well the system works after data has been optimized and less RAM is needed.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>During optimization, the program used a lot of memory which might be because of temporary conversions or copying.</li>
        <li>The high CPU usage indicates that the application uses a lot of system resources.</li>
        <li>May result in losing data or encountering errors when the wrong data type is used (for example, changing float to int).</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Sampling</td>
    <td>
      <ul>
        <li>Analyzing is allowed and testing quickly using a small sample of the data.</li>
        <li>The CPU is being used very little and memory is used less than it is when processing all the data.</li>
        <li>Can be used to create models and test ideas.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Because the throughput is low and the execution time is long, the performance is not efficient.</li>
        <li>If the way samples are chosen is biased, the findings may not reflect the whole population.</li>
        <li>Should not be used for final production or analysis that needs all the data.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Parallel Processing with Dask</td>
    <td>
      <ul>
        <li>Since the model uses very little memory, it is perfect for working with large datasets that RAM cannot handle.</li>
        <li>Can be used in programs that use multiple cores or distributed systems.</li>
        <li>Good for situations where data does not fit in memory and for real-time streaming.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>The longest execution time suggests that there is some overhead involved in setting up the parallelization.</li>
        <li>Because of the low throughput, the system is not efficient for handling small tasks.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Pandas</td>
    <td>
      <ul>
        <li>Many people use and support it and there is a lot of information available.</li>
        <li>Many functions: Allows users to handle, clean, transform and study data in many ways.</li>
        <li>Easy to pick up and work with, especially for those who are just starting to code.</li>
        <li>Easy to use with other Python libraries, including NumPy, Matplotlib and Scikit-learn.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Too much memory is used: Not recommended for datasets that are larger than the system’s RAM.</li>
        <li>It takes more time to execute queries than newer libraries like Polars.</li>
        <li>Default is single-threaded: Does not fully use multi-core processors which can make large-scale operations run slower.</li>
        <li>A lower throughput rate means the system is processing data more slowly.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Polars</td>
    <td>
      <ul>
        <li>Due to its Rust backend, this engine offers the fastest performance: quickest code execution and most rows per second.</li>
        <li>The program uses very little memory: It is designed to use memory efficiently.</li>
        <li>It is multi-threaded by design: All CPU cores are used automatically for better speed.</li>
        <li>Lazy evaluation is available: It helps by carrying out computations only when needed.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Not as mature: There are fewer people in the community and not as many tutorials or tools available as there are in Pandas.</li>
        <li>Limited features (at the moment): It lacks some of the specialized functions found in Pandas.</li>
        <li>API differences: Users who know Pandas will have to learn a bit of the Polars way.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Dask</td>
    <td>
      <ul>
        <li>Can handle both parallel and distributed computing and can be used on a laptop or a cluster.</li>
        <li>The low memory usage makes it good for working with data that is larger than the available RAM.</li>
        <li>Pandas-compatible API: Helps users who already use Pandas make the switch.</li>
        <li>Perfect for streaming and handling big data, as it can also work with cloud storage and distributed file systems.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>The benchmark shows that it takes the longest time to execute.</li>
        <li>The lower throughput is caused by the extra work needed for task scheduling and lazy execution.</li>
        <li>More difficult to learn: People need to know about delayed execution and task graphs.</li>
        <li>Not as helpful for small to medium data sets, as the overhead can be greater than the advantages unless you are working with huge or complex workloads.</li>
      </ul>
    </td>
  </tr>
</table>

### 5.3 Personal Reflection
#### 5.3.1 Kek Jesslyn
By studying these data processing strategies and libraries, I have learned how different ways of working and tools can affect how fast tasks are completed, how much memory is used, how efficient the CPU is and the overall throughput. It was very clear to me that using “Load Less Data” can boost Pandas’ performance, so I learned that being careful with data in the beginning is very important. I found out that Pandas and similar tools help a lot, but they may not be suitable for working with huge datasets. Looking into Polars was very interesting, I realized how much better modern libraries are at handling large datasets. In addition, Dask showed me how parallel and distributed computing can be useful for working with large amounts of data in the future. By doing this assignment, I now see more clearly the trade-offs among usability, speed and scalability which makes me more careful when choosing tools and strategies for data processing. Now, I feel more assured about picking the right solution for different project requirements.

#### 5.2.2 Tan Jun Yuan
This assignment gave us a solid hands-on experience in managing large datasets efficiently using Python. By working with a 2.86GB file containing about 3 million rows, we faced real-world challenges like memory limits and slow processing. We explored techniques such as chunking, sampling, data type optimization, and parallel processing with Dask, and saw how even small changes like converting object types to categories or loading only specific columns can greatly reduce memory use and improve speed. Using Google Colab also highlighted the importance of building scalable solutions within limited resources. Overall, this project improved our problem-solving skills and deepened our understanding of big data handling in real-world scenarios.

<a name="6-references"></a>
# <img src="https://github.com/user-attachments/assets/6f9087b7-2c68-4045-afc9-3f88b11bf29e" width=43px height=40px> 6. References
- McKinney, W. (2022). _Python for data analysis: Data wrangling with pandas, NumPy, and Jupyter_ (3rd ed.). O’Reilly Media.
  (https://wesmckinney.com/book/)
- Dask Development Team. (2024). _Dask documentation_. Dask.
  (https://docs.dask.org/en/stable/)
- MohamedBakhet. (2022). _Amazon books reviews_ [Data set]. Kaggle.
  (https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews)
