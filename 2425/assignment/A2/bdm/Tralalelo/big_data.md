# 📘 Assignment 2: Mastering Big Data Handling

**Due Date**: **4 June 2025 5:00 PM**  
**Group Work**: Yes (2 students per group)  
**Submission Platform**: GitHub (via provided structure) and Google Colab

## 📌 Introduction

In the modern data-driven world, organizations face the challenge of managing and extracting insights from *massive datasets* that far exceed the capabilities of traditional data handling tools. This assignment provides hands-on experience in managing such datasets using Python and its scalable libraries.

Students will apply real-world strategies for handling data volumes above **700MB** using techniques such as **chunking**, **sampling**, **type optimization**, and **parallel computing with Dask**.

## 🎯 Learning Outcomes

By the end of this assignment, students should be able to:

1. Identify challenges and limitations in traditional big data processing.
2. Apply strategies to manage and analyze large datasets efficiently.
3. Compare performance between traditional and optimized methods.

## 📝 Assignment Tasks

### Task 1: Dataset Selection

- **Dataset Source**: [Amazon Books Reviews](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews?select=Books_rating.csv)
- **Dataset Size**: 2.07GB (Approximately before zip)
- **Domain**: Book Reviews
- **Number of Records**: 1,010,293

### Task 2: Load and Inspect Data

- The dataset is loaded using the **KaggleHub** library and inspected using **Pandas**. The dataset has 1,010,293 rows and 9 columns. 
- **First 5 Records**:  
    ```plaintext
    review_id         reviewer                          movie  rating  
    rw5704482    raeldor-96879            After Life (2019– )     9.0   
    rw5704483          dosleeb  The Valhalla Murders (2019– )     6.0   
    ```

### Task 3: Apply Big Data Handling Strategies

#### 1. **Load Less Data**
- We loaded only the relevant columns: `Title`, `Price`, `User_id`, `review/score`, `review/time`, `review/text`.
  
#### 2. **Use Chunking**
- The data was processed in 500,000-row chunks using Pandas, preventing memory overload during analysis.

#### 3. **Optimize Data Types**
- Columns like `Title` and `User_id` were converted to the `category` type to save memory, and numerical data was cast to more efficient types (`float32`).

#### 4. **Sampling**
- A 5% random sample was taken from the dataset for faster prototyping and analysis.

#### 5. **Parallel Processing with Dask**
- Dask was used to load and process the data in parallel, significantly improving performance on large datasets.

### Task 4: Comparative Analysis

| Method                     | Memory Usage (MB) | Execution Time (seconds) |
|----------------------------|-------------------|--------------------------|
| **Full Pandas Load**        | 1370.75           | 16.52                    |
| **Polars**                  | 906.20            | 2.19                     |
| **Dask**                    | 967.74            | 22.78                    |

**Findings**:
- **Polars** was the fastest with the lowest memory usage.
- **Dask** allowed for parallel processing, though it was slightly slower than Polars.
- **Pandas** struggled with large datasets but performed adequately with optimized types.

### Task 5: Conclusion & Reflection

- **Pandas** is ideal for small to medium datasets but is limited in performance with large data.
- **Polars** offers superior performance and memory efficiency, especially for larger datasets.
- **Dask** provides scalability for distributed computing and parallel processing but has an overhead that can be a limitation for smaller datasets.

## 📁 File and Folder Structure

Place your files in your respective group folder inside the `bdm/` directory as follows:

