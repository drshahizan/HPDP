# Assignment 2: Mastering Big Data Handling

## Group Information

| Name | Matric No. | Role |
|---|---|---|
| NEO LI XIN | A23CS0253 | Student A: Baseline & Setup Lead |
| ELIJAH SHE YU SHENG | A23CS0073 | Student B: Scalability & Performance Lead |

---

## 1. Dataset Description

The dataset used for this assignment is the **Shopee Logistics Performance March** dataset from the **Kaggle Open Shopee Code League Logistics** competition. This dataset was selected because the extracted CSV file is larger than 700 MB, which satisfies the minimum dataset size requirement for this assignment. It is also suitable for big data handling because it contains millions of delivery records and text-heavy address columns that can increase memory usage during processing.

| Item | Description |
|---|---|
| Dataset Name | Shopee Logistics Performance March |
| Source | Kaggle - Open Shopee Code League Logistics |
| File Name | `delivery_orders_march.csv` |
| Compressed File | `delivery_orders_march.csv.zip` |
| Compressed Size | Approximately 381 MB |
| Extracted CSV Size | Approximately 721 MB |
| Number of Records | 3,176,313 rows |
| Number of Columns | 6 columns |
| Domain | E-commerce Logistics |

The dataset contains delivery order records for Shopee logistics operations in March. Each record represents one delivery order and includes the order ID, pickup timestamp, first delivery attempt timestamp, second delivery attempt timestamp, buyer address, and seller address. The dataset is meaningful for performance testing because the timestamp columns support delivery-time analysis, while the address columns create additional memory pressure due to long text values.

| Column | Description |
|---|---|
| `orderid` | Unique order identifier for each delivery order. |
| `pick` | Timestamp showing when the order was picked up. |
| `1st_deliver_attempt` | Timestamp of the first delivery attempt. |
| `2nd_deliver_attempt` | Timestamp of the second delivery attempt, if available. |
| `buyeraddress` | Buyer delivery address. |
| `selleraddress` | Seller address. |

---

## 2. Library Choices

This assignment uses exactly three Python libraries. **Pandas** is used as the compulsory baseline library, while **Dask** and **Polars** are selected as scalable libraries for performance comparison.

| Library | Role | Reason for Selection |
|---|---|---|
| Pandas | Baseline library | Pandas is the compulsory baseline and is widely used for data loading, inspection, and data analysis. |
| Dask | Scalable library | Dask can read large CSV files in partitions and execute dataframe operations using parallel processing. |
| Polars | Scalable library | Polars is designed for high-performance dataframe processing using a Rust-based execution engine and lazy query optimisation. |

Pandas is simple and suitable for baseline analysis, but it normally loads data directly into memory. This becomes a limitation when the dataset grows larger. Dask improves scalability by splitting the dataset into partitions and delaying execution until `.compute()` is called. Polars improves performance through columnar processing, lazy execution, and query optimisation.

---

## 3. Data Loading and Initial Inspection

Before applying optimisation strategies, the dataset was inspected using Pandas. A small sample was loaded first to understand the structure of the dataset without consuming too much memory.

The initial inspection focused on:

- dataset shape;
- column names;
- data types;
- missing values;
- first few records.

```python
import pandas as pd

sample_df = pd.read_csv(csv_path, nrows=10000)
print(sample_df.shape)
print(sample_df.dtypes)
print(sample_df.isnull().sum())
sample_df.head()
```

The full dataset contains **3,176,313 rows** and **6 columns**. The address columns are object/string columns and consume more memory compared with numeric timestamp columns. The `2nd_deliver_attempt` column contains many missing values because not all orders required a second delivery attempt.

This inspection step is important because data type optimisation and column selection should only be applied after understanding the structure and purpose of each column.

---

## 4. Big Data Handling Strategies

Five big data handling strategies were implemented. The first four strategies were implemented using Pandas, while the fifth strategy used the scalable libraries Dask and Polars.

---

### 4.1 Strategy 1: Load Less Data

#### Explanation

The first strategy is to load only the columns needed for the analysis instead of reading the full dataset into memory. The delivery-time analysis only requires the order ID and timestamp columns. Therefore, the text-heavy address columns can be excluded during processing.

This strategy reduces memory usage because long address columns are not loaded into RAM. It can also reduce execution time because fewer columns are read from the CSV file.

#### Code

```python
use_cols = ["orderid", "pick", "1st_deliver_attempt", "2nd_deliver_attempt"]

df_less = pd.read_csv(csv_path, usecols=use_cols)
print(df_less.shape)
print(df_less.memory_usage(deep=True).sum() / (1024 * 1024))
```

#### Output and Discussion

The selected-column dataframe still contains all **3,176,313 rows**, but only **4 required columns** are loaded. This is more efficient than loading all 6 columns because `buyeraddress` and `selleraddress` are not needed for delivery-time analysis. Since address columns are long text fields, excluding them provides a clear memory-saving benefit.

---

### 4.2 Strategy 2: Chunking

#### Explanation

Chunking means reading the dataset in smaller portions instead of loading the whole CSV file at once. This is useful when the dataset is too large to fit comfortably in memory. Each chunk is processed separately, and only the aggregated result is kept.

In this assignment, chunking was used to count the total number of rows, count missing second delivery attempts, and calculate the average delivery time between pickup and first delivery attempt.

#### Code

```python
chunk_size = 100000
total_rows = 0
missing_second_attempt = 0
delivery_hours_sum = 0
valid_delivery_count = 0

for chunk in pd.read_csv(csv_path, usecols=use_cols, chunksize=chunk_size):
    total_rows += len(chunk)
    missing_second_attempt += chunk["2nd_deliver_attempt"].isnull().sum()

    delivery_hours = (chunk["1st_deliver_attempt"] - chunk["pick"]) / 3600
    delivery_hours_sum += delivery_hours.sum()
    valid_delivery_count += delivery_hours.notnull().sum()

average_delivery_hours = delivery_hours_sum / valid_delivery_count

print(total_rows)
print(missing_second_attempt)
print(average_delivery_hours)
```

#### Output and Discussion

| Metric | Result |
|---|---:|
| Total rows processed | 3,176,313 |
| Missing `2nd_deliver_attempt` values | 1,819,311 |
| Average delivery time from pickup to first attempt | 104.449 hours |

Chunking proves that the dataset can be processed without keeping the entire file in memory at the same time. This strategy is especially useful in Google Colab because Colab has limited RAM.

---

### 4.3 Strategy 3: Data Type Optimisation

#### Explanation

Pandas may automatically assign larger data types than necessary, such as `float64` for timestamp columns. Data type optimisation reduces memory usage by assigning smaller but still suitable data types.

In this dataset, timestamp columns can be stored using smaller numeric types. The `orderid` column is kept as `int64` because it represents unique identifiers and should not lose precision.

#### Code

```python
dtype_map = {
    "orderid": "int64",
    "pick": "int32",
    "1st_deliver_attempt": "float32",
    "2nd_deliver_attempt": "float32"
}

df_optimised = pd.read_csv(csv_path, usecols=use_cols, dtype=dtype_map)
print(df_optimised.dtypes)
print(df_optimised.memory_usage(deep=True).sum() / (1024 * 1024))
```

#### Output and Discussion

Data type optimisation reduces the memory footprint of the selected columns by avoiding unnecessary 64-bit numeric types. This allows the same dataset to use less RAM and makes later processing more efficient. This strategy is important because memory optimisation should be applied before large-scale processing begins.

---

### 4.4 Strategy 4: Sampling

#### Explanation

Sampling selects a smaller subset of the dataset for quick testing and exploratory analysis. It is useful during early development because code can be tested faster before being applied to the full dataset.

A chunk-based sampling method was used instead of loading the full dataset first. This is more appropriate for big data because it avoids reading the entire CSV into memory just to create a sample.

#### Code

```python
sample_chunks = []
sample_fraction = 0.05

for chunk in pd.read_csv(csv_path, usecols=use_cols, chunksize=100000):
    sample_chunks.append(chunk.sample(frac=sample_fraction, random_state=42))

df_sample = pd.concat(sample_chunks, ignore_index=True)
print(df_sample.shape)
```

#### Output and Discussion

A 5% sample gives approximately **158,816 rows** from the original 3,176,313 rows. This is large enough for rapid testing but much faster to process than the full dataset. Sampling does not replace full-data processing in the final analysis, but it helps speed up debugging, prototyping, and exploratory analysis.

---

### 4.5 Strategy 5: Parallel Processing with Scalable Libraries

#### Explanation

The fifth strategy uses scalable libraries to process the same analysis task more efficiently. Dask and Polars were compared with the Pandas baseline.

The same operation was performed using all three libraries:

1. load selected columns;
2. count total rows;
3. count missing values in `2nd_deliver_attempt`;
4. calculate average delivery time between pickup and first delivery attempt;
5. measure execution time and RAM usage.

#### Pandas Code

```python
def pandas_analysis():
    df = pd.read_csv(csv_path, usecols=use_cols)
    total_rows = len(df)
    missing_second = df["2nd_deliver_attempt"].isnull().sum()
    avg_delivery_hours = ((df["1st_deliver_attempt"] - df["pick"]) / 3600).mean()
    return total_rows, missing_second, avg_delivery_hours
```

#### Dask Code

```python
import dask.dataframe as dd

def dask_analysis():
    ddf = dd.read_csv(csv_path, usecols=use_cols)
    total_rows = len(ddf)
    missing_second = ddf["2nd_deliver_attempt"].isnull().sum().compute()
    avg_delivery_hours = ((ddf["1st_deliver_attempt"] - ddf["pick"]) / 3600).mean().compute()
    return total_rows, missing_second, avg_delivery_hours
```

#### Polars Code

```python
import polars as pl

def polars_analysis():
    result = (
        pl.scan_csv(csv_path)
        .select(use_cols)
        .select([
            pl.len().alias("total_rows"),
            pl.col("2nd_deliver_attempt").is_null().sum().alias("missing_second_attempt"),
            ((pl.col("1st_deliver_attempt") - pl.col("pick")) / 3600).mean().alias("avg_delivery_hours")
        ])
        .collect()
    )
    return result
```

#### Output and Discussion

Dask processes the file in partitions and can use parallel execution, making it more scalable than Pandas for larger datasets. Polars uses lazy execution and query optimisation, allowing it to avoid unnecessary work and read only the required columns. Both scalable libraries are more suitable than Pandas when the dataset size increases significantly.

---

## 5. Comparative Analysis

The comparative analysis measured the execution time and memory usage of Pandas, Dask, and Polars using the same analytical workload. The workload included loading selected columns, counting total rows, checking missing values in `2nd_deliver_attempt`, calculating the average delivery time from pickup to first delivery attempt, and measuring RAM usage. Each benchmark was executed three times, and the average result was used to make the comparison more reliable.

### 5.1 Benchmark Results

The following results were collected from three benchmark runs. Lower execution time and lower RAM usage indicate better performance.

| Library | Avg Execution Time (s) | Avg RAM Change (MB) | Avg Peak RAM Increase (MB) | Highlight |
|---|---:|---:|---:|---|
| Pandas | 9.671 | **340.352** | **347.371** | Best memory efficiency |
| Dask | 10.618 | 672.445 | 687.837 | Best scalability direction |
| Polars | **1.695** | 734.286 | 749.777 | **Best speed / recommended for this workload** |

**Main highlight:** For this benchmark workload, **Polars is the best choice when execution speed is the main priority** because it completed the task in only **1.695 seconds**. However, **Pandas is the best choice for memory efficiency** because it recorded the lowest RAM change and the lowest peak RAM increase.

---

### 5.2 Standardised Performance Score

To compare the libraries more clearly, all metrics were standardised into scores. Since lower values are better for execution time and memory usage, the best result in each metric is given a score of 100. A higher score means better performance.

| Library | Execution Time Score | RAM Change Score | Peak RAM Score | Equal-Weight Average Score | Result |
|---|---:|---:|---:|---:|---|
| Pandas | 17.53 | **100.00** | **100.00** | **72.51** | Best balanced score if all metrics are equal |
| Dask | 15.96 | 50.61 | 50.50 | 39.03 | Lowest score in this single-machine benchmark |
| Polars | **100.00** | 46.35 | 46.33 | 64.23 | Best speed score |

Based on the equal-weight score, Pandas has the highest average score because it performed strongly in both RAM metrics. However, this does not mean Pandas is always the best. It only means Pandas is more balanced when memory usage and execution time are treated equally.

---

### 5.3 Speed-Weighted Overall Score

For big data processing, execution speed is often more important because large datasets can take a long time to process. Therefore, a second score was calculated using a speed-focused weighting:

- Execution time: 50%
- RAM change: 25%
- Peak RAM increase: 25%

| Library | Speed-Weighted Score | Interpretation |
|---|---:|---|
| Pandas | 58.76 | Good memory usage, but slower execution |
| Dask | 33.26 | More suitable for larger distributed workloads, not the fastest here |
| Polars | **73.17** | **Best overall for this benchmark when speed is prioritised** |

Using this speed-weighted comparison, **Polars becomes the best overall library for this workload**. This is because its execution time is much faster than Pandas and Dask, even though it uses more memory.

---

### 5.4 Execution Time Comparison

| Library | Avg Execution Time (s) | Rank | Discussion |
|---|---:|---:|---|
| Polars | **1.695** | 1 | Fastest library in this benchmark because of lazy execution and query optimisation. |
| Pandas | 9.671 | 2 | Slower than Polars, but still acceptable for a dataset that can fit into memory. |
| Dask | 10.618 | 3 | Slightly slower because task scheduling and partition overhead affected performance. |

Polars achieved the best execution time. It was much faster than Pandas and Dask for this analytical workload. Dask was slower than expected because the dataset could still be processed on one machine, so the overhead of partitioning and task scheduling reduced its advantage.

---

### 5.5 RAM Usage Comparison

| Library | Avg RAM Change (MB) | Avg Peak RAM Increase (MB) | Rank for Memory Efficiency | Discussion |
|---|---:|---:|---:|---|
| Pandas | **340.352** | **347.371** | 1 | Used the least memory in this benchmark. |
| Dask | 672.445 | 687.837 | 2 | Used more memory because of partition and computation overhead. |
| Polars | 734.286 | 749.777 | 3 | Fastest execution, but required the highest RAM increase. |

Pandas recorded the lowest RAM usage, making it the best option when memory is limited. Polars used the most memory, but it provided the fastest processing speed. This shows that faster execution does not always mean lower memory usage.

---

## 6. Critical Analysis

### 6.1 Summary of Strengths and Weaknesses

| Library | Strength | Weakness | Best Use Case |
|---|---|---|---|
| Pandas | Simple syntax and lowest memory usage in this benchmark | Slower than Polars and not ideal for very large datasets | Small to medium datasets and normal analysis |
| Dask | Can process data in partitions and supports scalable processing | Slower in this benchmark due to scheduling overhead | Very large datasets or distributed processing |
| Polars | Fastest execution time and strong query optimisation | Highest RAM usage in this benchmark | Fast single-machine analytics |

The results show that each library has a different advantage. **Polars is the strongest library for speed**, **Pandas is the strongest library for memory efficiency**, and **Dask is the strongest library for scalability when the dataset becomes too large for one machine**.

---

### 6.2 Which Library Is Better?

| Evaluation Focus | Better Library | Reason |
|---|---|---|
| Fastest execution time | **Polars** | It completed the workload in only 1.695 seconds. |
| Lowest RAM usage | **Pandas** | It recorded the lowest RAM change and peak RAM increase. |
| Best equal-weight score | **Pandas** | It performed best when execution time and memory usage were treated equally. |
| Best speed-weighted score | **Polars** | It achieved the highest score when speed was prioritised. |
| Best scalability direction | **Dask** | It is designed for partition-based and distributed processing. |
| Best overall for this benchmark | **Polars** | The execution time improvement was very large, making it the best choice for fast processing. |

**Final decision:** For this assignment benchmark, **Polars should be highlighted as the best overall library** because it achieved the fastest execution time by a large margin. However, the report should also mention that **Pandas is better when RAM usage is the main concern**, while **Dask is better when the dataset becomes too large for one machine**.

---

### 6.3 Scenario-Based Recommendation

| Scenario | Recommended Library | Explanation |
|---|---|---|
| Small dataset that fits easily into memory | Pandas | Pandas is simple, readable, and easy to debug. |
| Medium dataset with limited RAM | Pandas with column selection or chunking | Pandas can still be efficient if only required columns are loaded and chunking is used. |
| Need fastest processing on one machine | **Polars** | Polars is the best choice because it achieved the fastest execution time in this benchmark. |
| Data analysis with many filtering and aggregation operations | Polars | Lazy execution and query optimisation can reduce unnecessary processing. |
| Dataset is larger than available RAM | Dask | Dask can divide the dataset into partitions instead of loading everything at once. |
| Distributed or cluster-based processing | Dask | Dask is designed to scale across multiple cores or multiple machines. |
| Beginner-friendly exploratory data analysis | Pandas | Pandas has simpler syntax and is widely used in data analysis. |
| Production workflow with very large data | Dask or Apache Spark | These tools are more suitable when the data grows from gigabytes to terabytes. |

---

### 6.4 Interpretation of the Benchmark Results

The benchmark results show that **Polars is the fastest library**, but it also used the highest RAM in this experiment. This means Polars is suitable when the machine has enough memory and the main objective is to reduce execution time.

Pandas performed better in memory usage. This makes Pandas suitable for memory-limited environments such as Google Colab or laptops with lower RAM. However, Pandas may become slower or fail when the dataset becomes too large.

Dask did not achieve the fastest result in this experiment, but that does not mean Dask is not useful. Dask is more useful when the dataset is too large to fit into memory or when processing can be distributed across multiple cores or machines. In this benchmark, the dataset was still manageable on a single machine, so Dask's overhead made it slower.

---

## 7. Conclusion and Scalability Reflection

This assignment compared Pandas, Dask, and Polars for big data handling using the Shopee Logistics Performance March dataset. The comparison focused on execution time, RAM change, and peak RAM increase. The results show that **Polars achieved the fastest execution time**, **Pandas achieved the lowest memory usage**, and **Dask provided the strongest scalability direction**.

For this benchmark, **Polars is the best overall library to highlight** because it completed the analytical workload much faster than Pandas and Dask. Polars is especially suitable when the goal is to process data quickly on a single machine. This makes it useful for fast data analysis, feature engineering, and repeated testing where execution speed is important.

However, Pandas is still a strong choice when memory usage and simplicity are more important. In this benchmark, Pandas used the lowest RAM, so it is suitable for smaller datasets, beginner-friendly analysis, and limited-RAM environments. If the dataset is not too large, Pandas is often easier to write and understand.

Dask is not the best based on execution time in this experiment, but it is still important for scalability. When the dataset becomes too large for memory, Dask can process data in partitions and can also support distributed processing. Therefore, Dask is more suitable for larger real-world workloads that cannot be handled efficiently by Pandas alone.

In conclusion, **no single library is best for every situation**. If the priority is **speed**, **Polars is the best choice**. If the priority is **low memory usage and simple coding**, **Pandas is the best choice**. If the priority is **scalability for very large datasets**, **Dask is the best choice**. For this assignment's benchmark result, the final recommended library is **Polars**, while Pandas and Dask remain useful in different scenarios.

---

## References

1. Kaggle Open Shopee Code League Logistics Dataset. (https://www.kaggle.com/competitions/open-shopee-code-league-logistic)
