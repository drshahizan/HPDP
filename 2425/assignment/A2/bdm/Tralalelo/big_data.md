
# 📘 Assignment 2: Mastering Big Data Handling

**Group Members**:
- **M1**: LEE YIK HONG (A21BE0376)
- **M2**: WONG JUN JI (A22EC0117)

**Due Date**: **4 June 2025 5:00 PM**  
**Submission Platform**: GitHub and Google Colab

## 📌 Introduction

In the modern data-driven world, organizations are faced with the challenge of managing and extracting meaningful insights from vast datasets that often exceed the capabilities of traditional data handling tools. This assignment offers hands-on experience in dealing with large datasets (>700MB) using Python and its scalable libraries.

Students will explore and implement strategies such as **chunking**, **sampling**, **data type optimization**, and **parallel computing** with Dask to efficiently handle datasets of this magnitude.

## 🎯 Learning Outcomes

By the end of this assignment, students should be able to:

1. Identify the challenges and limitations of traditional big data processing methods.
2. Implement scalable techniques to handle large datasets efficiently.
3. Compare the performance of traditional and optimized big data handling methods.

## 📝 Assignment Tasks

### Task 1: Dataset Selection

- **Dataset Source**: [Amazon Books Reviews](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews?select=Books_rating.csv)
- **Dataset Size**: 700MB+
- **Domain**: Book Reviews
- **Number of Records**: 3,000,000 records

---

### Task 2: Load and Inspect Data

The dataset was loaded using **KaggleHub** and inspected with **Pandas**. It contains 3 million rows and 10 columns, representing information about books, their ratings, reviews, and other relevant details.

#### Code Snippet for Task 2:

```python
# Task 1: Load the dataset using KaggleHub
start_time = time.time()

# Load the dataset into a Pandas DataFrame (ensure df is defined here)
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "mohamedbakhet/amazon-books-reviews",
    "Books_rating.csv"  # Specify the file name within the Kaggle dataset
)

# Calculate execution time for loading
load_time = time.time() - start_time

# Memory usage for full load (in MB)
memory_usage = df.memory_usage(deep=True).sum() / (1024**2)  # Convert to MB

# Print execution time and memory usage for the traditional method
print(f"Full Pandas Load Execution Time: {load_time:.2f} seconds")
print(f"Full Pandas Load Memory Usage: {memory_usage:.2f} MB")
```

**Findings**:
- **Dataset Shape**: `(3000000, 10)`  
- **Columns and Data Types**:
  - `Id`: object
  - `Title`: object
  - `Price`: float64
  - `review/score`: float64
  - `review/time`: int64
  - `review/summary`: object
  - `review/text`: object

This task helped us load and inspect the dataset. The **Pandas** method is quick but not optimized for large datasets in terms of memory usage.

---

### Task 3: Apply Big Data Handling Strategies

#### **1. Load Less Data**

We reduced memory usage by selecting only the relevant columns, which include `Title`, `Price`, `User_id`, `review/score`, `review/time`, and `review/text`.

#### Code Snippet for Load Less Data:

```python
# Task 3 - Load Less Data: Select only the relevant columns to reduce memory usage
start_time = time.time()
df_load_less = df[['Title', 'Price', 'User_id', 'review/score', 'review/time', 'review/text']]
load_less_time = time.time() - start_time

# Memory usage for Load Less Data
load_less_mem_usage = df_load_less.memory_usage(deep=True).sum() / (1024**2)  # in MB

print(f"Load Less Data Execution Time: {load_less_time:.2f} seconds")
print(f"Load Less Data Memory Usage: {load_less_mem_usage:.2f} MB")
```

**Findings**:
- **Execution Time**: 0.17 seconds  
- **Memory Usage**: 3037.54 MB

By selecting fewer columns, we reduced memory usage significantly, making it easier to work with the data.

---

#### **2. Use Chunking**

We processed the dataset in chunks of 500,000 rows using **Pandas'** `chunksize`. This method allows us to handle large datasets by loading them in smaller portions, preventing memory overload.

#### Code Snippet for Chunking:

```python
# **Chunking with Pandas**: Process the data in smaller chunks
chunk_size = 500_000  # You can adjust chunk size to your needs
total_rows = 0
chunk_memory_usage = 0
first_chunk_preview = None
first_chunk_memory = 0

# Start processing in chunks
start_time = time.time()

# Generate the chunks (simulating chunking from the already-loaded KaggleHub DataFrame)
chunks = (df.iloc[i:i + chunk_size] for i in range(0, len(df), chunk_size))

# Process each chunk
for i, chunk in enumerate(chunks):
    print(f"Processing Chunk {i + 1}: {chunk.shape}")
    print(chunk.head(2))
    print("-" * 50)

    total_rows += chunk.shape[0]

    # Store preview and memory usage from first chunk only
    if i == 0:
        first_chunk_preview = chunk.head()
        first_chunk_memory = chunk.memory_usage(deep=True).sum() / (1024**2)

# Finished processing all chunks
chunk_time_end = time.time()
chunk_execution_time = chunk_time_end - start_time

# Execution time
print(f"Total rows processed: {total_rows}")
print("
First 5 records from first chunk:
", first_chunk_preview)
print(f"
Memory usage of first chunk: {first_chunk_memory:.2f} MB")
print(f"Total execution time: {chunk_execution_time:.2f} seconds")
```

**Findings**:
- **Execution Time**: 1.01 seconds  
- **Memory Usage (First Chunk)**: 695.05 MB

Chunking helped break down the data into smaller, manageable parts. This method is particularly useful when working with datasets that exceed available memory.

---

#### **3. Optimize Data Types**

We optimized memory usage by converting columns to more efficient data types, such as converting `Title` and `User_id` to `category` and `review/score` to `float32`.

#### Code Snippet for Optimizing Data Types:

```python
# **Memory Optimization**: Convert columns with high cardinality to 'category' to reduce memory usage
start_time = time.time()
df['Title'] = df['Title'].astype('category')
df['User_id'] = df['User_id'].astype('category')
df['review/score'] = df['review/score'].astype('float32')
df['review/time'] = pd.to_datetime(df['review/time'], errors='coerce')
df['review/text'] = df['review/text'].astype('string')
optimize_time = time.time() - start_time

# Memory usage after optimization
optimize_mem_usage = df.memory_usage(deep=True).sum() / (1024**2)  # in MB

print(f"Optimize Data Types Execution Time: {optimize_time:.2f} seconds")
print(f"Optimize Data Types Memory Usage: {optimize_mem_usage:.2f} MB")
```

**Findings**:
- **Execution Time**: 10.66 seconds  
- **Memory Usage**: 3519.70 MB

By optimizing data types, we reduced memory usage without losing essential information, making data handling more efficient.

---

#### **4. Sampling**

We used random sampling to select 5% of the dataset for quicker analysis. This method is useful for prototyping and testing hypotheses on smaller subsets of data.

#### Code Snippet for Sampling:

```python
# **Sampling**: Take a 5% random sample for quicker analysis
start_time = time.time()
sample_df = df.sample(frac=0.05, random_state=42)
sampling_time = time.time() - start_time

# Memory usage after sampling
sampling_mem_usage = sample_df.memory_usage(deep=True).sum() / (1024**2)  # in MB

print(f"Sampling Execution Time: {sampling_time:.2f} seconds")
print(f"Sampling Memory Usage: {sampling_mem_usage:.2f} MB")
```

**Findings**:
- **Execution Time**: 0.25 seconds  
- **Memory Usage**: 300.21 MB

Sampling is a quick method to test analysis and generate insights without working with the full dataset.

---

#### **5. Parallel Processing with Dask**

Dask enables parallel processing, which allows large datasets to be handled across multiple cores or distributed systems.

#### Code Snippet for Parallel Processing with Dask:

```python
# **Parallel Processing with Dask**: Use Dask to handle the large dataset in parallel
start = time.time()
df_dd = dd.from_pandas(df, npartitions=4)
df_dd_computed = df_dd.compute()  # Trigger computation
dask_time = time.time() - start

# Check memory usage for Dask
process = psutil.Process(os.getpid())
dask_memory = process.memory_info().rss / (1024 ** 2)  # in MB

print(f"Dask Execution Time: {dask_time:.2f} seconds")
print(f"Dask Memory Usage: {dask_memory:.2f} MB")
```

**Findings**:
- **Execution Time**: 30.43 seconds  
- **Memory Usage**: 9082.52 MB

Dask improved performance for large datasets, but it can introduce some overhead for smaller datasets.

---

### Task 4: Comparative Analysis

| Method                     | Memory Usage (MB) | Execution Time (seconds) |
|----------------------------|-------------------|--------------------------|
| **Full Pandas Load**        | 3831.14           | 53.44                    |
| **Polars**                  | 906.20            | 2.19                     |
| **Dask**                    | 9082.52           | 30.43                    |

**Findings**:
- **Polars** is the fastest and most memory-efficient, handling large datasets significantly better than Pandas.
- **Dask** allowed for parallel processing, which improved performance on a large scale but was slower than Polars.
- **Pandas** performed well with small to medium datasets but struggled with larger datasets due to high memory consumption and longer execution times.

---

### Task 5: Conclusion & Reflection

- **Pandas** remains a powerful tool for small to medium-sized datasets but has performance limitations with large datasets.
- **Polars** emerged as the most efficient tool for handling large datasets, offering faster execution and lower memory consumption compared to both Pandas and Dask.
- **Dask** is best suited for distributed computing and parallel processing, making it ideal for extremely large datasets, but the overhead can result in slower performance for smaller datasets.

**Key Takeaways**:
- **Load Less Data** and **Chunking** are essential for working with datasets that exceed memory limits.
- **Memory Optimization** techniques like converting to `category` type are crucial for reducing memory usage, especially for high-cardinality columns.
- **Sampling** is helpful for quickly testing hypotheses without working with the full dataset.
- **Dask** and **Polars** offer scalable solutions for big data, with **Polars** being the most efficient for large datasets.

---

### References

- **Pandas Documentation**: [https://pandas.pydata.org/pandas-docs/stable/](https://pandas.pydata.org/pandas-docs/stable/)
- **Dask Documentation**: [https://docs.dask.org/en/stable/](https://docs.dask.org/en/stable/)
- **Polars Documentation**: [https://pola-rs.github.io/polars-book/](https://pola-rs.github.io/polars-book/)
- **Amazon Books Reviews Dataset**: [https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews](https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews)


### 📁 File and Folder Structure

Place your files in your respective group folder inside the `bdm/` directory as follows:

```
bdm/your_group/
├── 📄 big_data.md        ← The main Markdown report
├── 📄 readme.md          ← Brief introduction and links
└── 📄 big_data.ipynb     ← Colab Notebook with code
```
