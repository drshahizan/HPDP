# Airbnb Big Data Analysis: Performance & Memory Optimization

## Project Information

| Item       | Details                                   |
| :--------- | :---------------------------------------- |
| Course     | SECP3133 High Performance Data Processing |
| Assignment | Assignment 2: Mastering Big Data Handling |
| Group Name | **Group Pegasus**                         |
| Member 1   | **LEE YIN SHEN - A23CS0236**              |
| Member 2   | **BRENDAN CHIA YAN FEI - A23CS0211**      |

---

## Project Overview

This project focuses on handling and analysing a large Airbnb listings dataset using different big data processing strategies. The dataset contains listing information such as host details, property types, room types, location details, price, availability, number of reviews, and review scores.

The main objective of this project is to compare traditional data processing using **Pandas** with scalable data processing libraries such as **Dask** and **Polars**. The comparison focuses on memory usage, execution time, and ease of processing.

---

## Dataset Information

| Attribute         | Details                                                                            |
| :---------------- | :--------------------------------------------------------------------------------- |
| Dataset Name      | Airbnb Listings Dataset                                                            |
| File Name         | `airbnb_listings.csv`                                                              |
| Source            | [Airbnb Dataset on Kaggle](https://www.kaggle.com/datasets/joebeachcapital/airbnb) |
| Domain            | Hospitality / Travel Accommodation                                                 |
| File Size         | 1846.24 MB                                                                         |
| Number of Rows    | 494,954                                                                            |
| Number of Columns | 89                                                                                 |
| File Format       | CSV                                                                                |
| Separator         | Semicolon `;`                                                                      |

The dataset is larger than 700 MB, which satisfies the assignment requirement for big data handling.

---

## Libraries Used

| Library | Purpose                                                                   |
| :------ | :------------------------------------------------------------------------ |
| Pandas  | Baseline library for traditional data loading, inspection, and processing |
| Dask    | Scalable library for parallel and partition-based processing              |
| Polars  | High-performance dataframe library with lazy execution                    |

---

## Big Data Handling Strategies

This project applies five big data handling strategies:

1. **Load Less Data**  
   Only selected important columns were loaded instead of all 89 columns to reduce memory usage and loading time.

2. **Chunking**  
   The dataset was processed in chunks of 100,000 rows to avoid loading the full file into memory.

3. **Data Type Optimization**  
   Numeric columns were downcasted and repeated text columns were converted into categorical types to reduce memory usage.

4. **Sampling**  
   A 10% random sample was used for faster exploratory analysis and prototyping.

5. **Parallel and Lazy Processing**  
   Dask and Polars were used to compare scalable processing performance against Pandas.

---

## Key Results

### Memory Usage

| Method                           | Memory Usage |
| :------------------------------- | -----------: |
| Pandas - All Columns Sample      |    649.52 MB |
| Pandas - Selected Columns Sample |    138.69 MB |
| Pandas - Optimized Data Types    |    110.82 MB |
| Pandas - GroupBy with 2 Columns  |     33.46 MB |

### Execution Time

| Method                       | Execution Time |
| :--------------------------- | -------------: |
| Pandas All Columns Load      |         9.85 s |
| Pandas Selected Columns Load |         4.81 s |
| Chunking                     |        25.82 s |
| Sampling                     |        17.25 s |
| Pandas GroupBy               |        26.95 s |
| Dask GroupBy                 |        33.84 s |
| Polars Lazy GroupBy          |         6.09 s |

---

## Charts

### Memory Usage Comparison

![Memory Usage Comparison](images/memory_usage_comparison.png)

### Execution Time Comparison

![Execution Time Comparison](images/execution_time_comparison.png)

---

## Main Findings

The results show that **column selection** was the most effective strategy for reducing memory usage. Loading only 20 selected columns instead of all 89 columns reduced memory usage from 649.52 MB to 138.69 MB for a 100,000-row sample.

Data type optimization further reduced memory usage from 138.69 MB to 110.82 MB.

For execution speed, **Polars** performed the best. It completed the full-dataset groupby operation in 6.09 seconds, compared to 26.95 seconds for Pandas and 33.84 seconds for Dask.

Dask was slower than expected in this experiment because of task scheduling and partitioning overhead. However, Dask remains useful for larger-than-memory datasets and distributed computing environments.

---

## Project Files

| File                                                                           | Description                                                                                     |
| :----------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| [`big_data.md`](big_data.md)                                                   | Main Markdown report containing explanation, code snippets, results, comparison, and reflection |
| [`big_data.ipynb`](big_data.ipynb)                                             | Google Colab notebook containing all Python code and outputs                                    |
| [`README.md`](README.md)                                                       | Project overview and summary                                                                    |
| [`images/memory_usage_comparison.png`](images/memory_usage_comparison.png)     | Memory usage comparison chart                                                                   |
| [`images/execution_time_comparison.png`](images/execution_time_comparison.png) | Execution time comparison chart                                                                 |

---

## Folder Structure

```text
bdm/Group_Pegasus/
├── README.md
├── big_data.md
├── big_data.ipynb
└── images/
    ├── memory_usage_comparison.png
    └── execution_time_comparison.png
```

---

## How to Run the Notebook

1. Open `big_data.ipynb` in Google Colab.
2. Mount Google Drive.
3. Make sure the dataset file `airbnb_listings.csv` is available in the correct Google Drive folder.
4. Run all cells from top to bottom.
5. Check that all outputs, tables, and charts are generated successfully.

---

## Conclusion

This project demonstrates that handling large datasets efficiently requires more than simply loading data with Pandas. Techniques such as loading fewer columns, chunking, data type optimization, and sampling can significantly improve memory efficiency.

Among the scalable libraries tested, **Polars** achieved the fastest execution time for the full-dataset groupby operation. **Dask** provided scalable processing capability but had additional overhead in this experiment.

Overall, the project shows that the best big data strategy depends on the dataset size, available memory, processing task, and computing environment.

---

## References

1. [Airbnb Dataset on Kaggle](https://www.kaggle.com/datasets/joebeachcapital/airbnb)
2. [Pandas Documentation](https://pandas.pydata.org/docs/)
3. [Dask DataFrame Documentation](https://docs.dask.org/en/stable/dataframe.html)
4. [Polars Documentation](https://docs.pola.rs/)
5. [Matplotlib Documentation](https://matplotlib.org/stable/index.html)

