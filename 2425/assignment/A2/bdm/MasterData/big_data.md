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


# 3.0 Big Data Handling Strategies and Loading Data Using Different Libraries
### 3.1 Part 1 (5 Big Data Strategies)

#### 3.1.1 Load Less Data

#### 3.1.2 Chunking

#### 3.1.3 Optimize Data Type

#### 3.1.4 Sampling

#### 3.1.5 Parallel Processing with Dask

### 3.2 Part 2 (Loading dataset with different libraries)

#### 3.2.1 Using Pandas library

#### 3.2.2 Using Polars library

#### 3.2.3 Using Dask library

# 4.0 Comparative Analysis
### 4.1 Metrics Used

### 4.2 Results Summary
#### 4.2.1 Part 1 (Comparing Between Strategies)

#### 4.2.2 Part 2 (Comparing Between Libraries)

### 4.3 Discussions and Key Observation
#### 4.3.1 Part 1 (Comparing Between Strategies)

#### 4.3.2 Part 2 (Comparing Between Libraries)

# 5.0 Conclusion and Reflection
### 5.1 Summary of Findings

### 5.2 Benefits and Limitations of Each Strategies

### 5.3 Personal Reflection
#### 5.3.1 Kek Jesslyn

#### 5.2.2 Tan Jun Yuan

# 6.0 Reference
