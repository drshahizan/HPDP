#  Big Data Handling with Carrier On-Time Performance Dataset

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>DHESHIEGHAN A/L SARAVANA MOORTHY</td>
    <td>A23CS0072</td>
  </tr>
  <tr>
    <td width=80%>PRAVINRAJ A/L SIVABATHI</td>
    <td>A23CS0171</td>
  </tr>
</table>

## Abstract

This report details a project focused on mastering big data handling techniques using the Carrier On-Time Performance Dataset. Various strategies were explored using Pandas, including loading selective data, employing chunking, optimizing data types, and sampling. Additionally, Dask was used to demonstrate parallel processing capabilities, while Polars was tested as a high-performance DataFrame library.

The performance of these strategies was evaluated based on execution time and memory usage. The dataset used in this project was `airline_2m.csv`, which has a file size of approximately 841.30 MB, 2,000,000 rows, and 109 columns. The findings indicate that Polars provided the fastest execution time, while chunking and selective loading helped manage memory usage effectively. This project provided valuable insights into choosing appropriate tools and strategies based on dataset size, available memory, and processing requirements.

## 1. Introduction

The growth of large datasets, also known as "big data", presents challenges in storage, processing, and analysis. Efficiently handling big data is important for extracting meaningful insights and building scalable data processing workflows.

This project aims to explore and evaluate various strategies for handling large datasets through practical implementation and performance comparison. We utilized the Carrier On-Time Performance Dataset, a large aviation dataset containing airline flight records, delay information, cancellation status, route details, and carrier information.

The primary libraries employed were Pandas for general data analysis, Dask for parallel and scalable data processing, and Polars for high-performance data manipulation. This report outlines the dataset used, the methodologies applied for handling and processing the data, the results obtained from the experiments, and a reflection on the learning outcomes.

## 2. Dataset Description

The primary dataset used for this assignment is the **Carrier On-Time Performance Dataset**.

-   **Source**: Kaggle ([https://www.kaggle.com/datasets/mexwell/carrier-on-time-performance-dataset](https://www.kaggle.com/datasets/mexwell/carrier-on-time-performance-dataset))
-   **Size**: Approximately 841.30 MB.
-   **Records**: 2,000,000 flight records.
-   **Columns**: 109 columns.
-   **Domain**: Airline / Transportation Analytics.
-   **File Format**: The data was provided in CSV format (`airline_2m.csv`).
-   **Dataset Features Description**:

| **Content** | **Details** |
|-------------|-------------|
| `Year` | Year of the flight record |
| `Quarter` | Quarter of the year |
| `Month` | Month of the flight |
| `DayofMonth` | Day of the month |
| `DayOfWeek` | Day of the week |
| `FlightDate` | Date of the flight |
| `Reporting_Airline` | Airline carrier code |
| `DOT_ID_Reporting_Airline` | Department of Transportation airline ID |
| `IATA_CODE_Reporting_Airline` | IATA airline code |
| `Tail_Number` | Aircraft tail number |
| `Flight_Number_Reporting_Airline` | Flight number reported by the airline |
| `Origin` | Origin airport code |
| `OriginCityName` | Origin city name |
| `OriginState` | Origin state code |
| `Dest` | Destination airport code |
| `DestCityName` | Destination city name |
| `DestState` | Destination state code |
| `CRSDepTime` | Scheduled departure time |
| `DepTime` | Actual departure time |
| `DepDelay` | Departure delay in minutes |
| `DepDelayMinutes` | Positive departure delay minutes |
| `DepDel15` | Indicator for departure delay of 15 minutes or more |
| `CRSArrTime` | Scheduled arrival time |
| `ArrTime` | Actual arrival time |
| `ArrDelay` | Arrival delay in minutes |
| `ArrDelayMinutes` | Positive arrival delay minutes |
| `ArrDel15` | Indicator for arrival delay of 15 minutes or more |
| `Cancelled` | Indicates whether the flight was cancelled |
| `CancellationCode` | Reason code for flight cancellation |
| `Diverted` | Indicates whether the flight was diverted |
| `CRSElapsedTime` | Scheduled elapsed time |
| `ActualElapsedTime` | Actual elapsed time |
| `AirTime` | Time spent in the air |
| `Flights` | Number of flights |
| `Distance` | Flight distance |
| `DistanceGroup` | Distance category group |
| `CarrierDelay` | Delay caused by airline carrier |
| `WeatherDelay` | Delay caused by weather |
| `NASDelay` | Delay caused by National Airspace System |
| `SecurityDelay` | Delay caused by security issues |
| `LateAircraftDelay` | Delay caused by late aircraft arrival |

- **Dataset Statistics**:
  - **# total records** = 2,000,000
  - **# total columns** = 109
  - **# file size** = 841.30 MB
  - **# selected columns used for analysis** = 8
  - **# delayed flights** = 859,554
  - **# delayed flights percentage** = 42.98%

This dataset was selected because of its substantial size and rich structure, making it suitable for testing and comparing various big data handling strategies.

## 3. Initial Data Loading and Inspection

The first step involved setting up the environment in Google Colab, accessing the dataset from Kaggle, and performing an initial inspection to understand the dataset structure.

### 3.1. Kaggle API Configuration

To download the dataset, the Kaggle API credentials were configured:
!pip install kaggle dask[dataframe] polars pyarrow memory_profiler psutil -q

from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json


### 3.2. Dataset Download and File Selection

The dataset was downloaded from Kaggle and extracted into the `/content/data` directory.
DATASET_SLUG = "mexwell/carrier-on-time-performance-dataset"

!mkdir -p /content/data
!kaggle datasets download -d {DATASET_SLUG} -p /content/data --unzip


**Dataset File Output:**

-   `/content/data/airline_2m.csv`: 841.30 MB
-   Total dataset size: 841.30 MB
-   Dataset requirement satisfied: above 700 MB
-   Main dataset selected: `/content/data/airline_2m.csv`
-   Main file size: 841.30 MB

### 3.3. Loading and Initial Inspection with Pandas

A preview of 10,000 rows was loaded using Pandas to inspect the dataset structure before applying big data handling techniques.

import pandas as pd

main_file = "/content/data/airline_2m.csv"

df_preview = pd.read_csv(main_file, nrows=10000)

print("Preview shape:", df_preview.shape)
print("Total columns:", len(df_preview.columns))
print(df_preview.columns.tolist())


**Initial Inspection Output:**

-   **Preview shape**: (10000, 109)
-   **Total columns**: 109
-   **Main file**: `airline_2m.csv`
-   **Full dataset shape**: 2,000,000 rows × 109 columns

The preview confirmed that the dataset contains many flight-related attributes, including date information, airline carrier details, origin and destination airports, delay metrics, cancellation status, diversion details, and distance-related features.

## 4. Big Data Handling Strategies and Library Comparisons

Several strategies were applied to manage and process the large dataset. Pandas was used for most strategies, while Dask and Polars were used to compare parallel and high-performance processing capabilities.

### 4.1. Pandas-based Strategies

These strategies focused on reducing memory footprint and improving processing efficiency using Pandas.

**4.1.1. Load Less Data**

Loading only essential columns can significantly reduce memory usage and improve processing efficiency, especially when not all 109 columns are required for analysis.

-   **Explanation**: Instead of loading all columns, only 8 important columns were selected: `Year`, `Month`, `DayOfWeek`, `Reporting_Airline`, `Origin`, `Dest`, `DepDelay`, and `ArrDelay`.

-   **Code Snippet (Pandas)**:

    ```
    import pandas as pd

    selected_cols = [
        "Year",
        "Month",
        "DayOfWeek",
        "Reporting_Airline",
        "Origin",
        "Dest",
        "DepDelay",
        "ArrDelay"
    ]

    df_selected = pd.read_csv(main_file, usecols=selected_cols)

    print(df_selected.head())
    print(df_selected.info())
    ```

-   **Results**:
    -   Selected columns: 8
    -   Execution time: 26.19 seconds
    -   Memory change: 261.09 MB

-   **Analysis**: This strategy reduced unnecessary data loading by selecting only relevant columns. It is useful when the analysis does not require every column in the dataset.

**4.1.2. Use Chunking**

Chunking allows a large file to be processed in smaller segments. This prevents memory overload because only one chunk is processed at a time.

-   **Explanation**: The dataset was read in chunks, and each chunk was used to calculate total rows, average departure delay, average arrival delay, and delayed flights.

-   **Code Snippet (Pandas)**:

    ```
    import pandas as pd

    chunk_size = 100000
    total_rows = 0
    delayed_flights = 0
    total_dep_delay = 0
    total_arr_delay = 0
    valid_dep_count = 0
    valid_arr_count = 0

    for chunk in pd.read_csv(main_file, usecols=selected_cols, chunksize=chunk_size):
        total_rows += len(chunk)
        delayed_flights += (chunk["ArrDelay"] > 0).sum()

        total_dep_delay += chunk["DepDelay"].sum(skipna=True)
        total_arr_delay += chunk["ArrDelay"].sum(skipna=True)

        valid_dep_count += chunk["DepDelay"].count()
        valid_arr_count += chunk["ArrDelay"].count()

    avg_dep_delay = total_dep_delay / valid_dep_count
    avg_arr_delay = total_arr_delay / valid_arr_count
    delayed_percentage = (delayed_flights / total_rows) * 100

    print("Total Rows Processed:", total_rows)
    print("Average Departure Delay:", avg_dep_delay)
    print("Average Arrival Delay:", avg_arr_delay)
    print("Delayed Flights Count:", delayed_flights)
    print("Delayed Flights Percentage:", delayed_percentage)
    ```

-   **Results**:
    -   Total rows processed: 2,000,000
    -   Average departure delay: 8.59 minutes
    -   Average arrival delay: 6.21 minutes
    -   Delayed flights count: 859,554
    -   Delayed flights percentage: 42.98%
    -   Execution time: 12.15 seconds
    -   Memory change: 19.47 MB

-   **Analysis**: Chunking was effective because it processed the entire dataset with a small memory change. This technique is suitable for large files because it avoids loading the full dataset into memory at once.

**4.1.3. Optimize Data Types**

Converting columns to more memory-efficient data types can reduce memory usage significantly.

-   **Explanation**: The selected dataset was optimized by converting integer columns into smaller integer types, float columns into smaller float types, and repeated text columns into categorical data types.

-   **Code Snippet (Pandas)**:

    ```
    import pandas as pd

    before = df_selected.memory_usage(deep=True).sum() / (1024 ** 2)

    for col in ["Year", "Month", "DayOfWeek"]:
        df_selected[col] = pd.to_numeric(df_selected[col], downcast="integer")

    for col in ["DepDelay", "ArrDelay"]:
        df_selected[col] = pd.to_numeric(df_selected[col], downcast="float")

    for col in ["Reporting_Airline", "Origin", "Dest"]:
        df_selected[col] = df_selected[col].astype("category")

    after = df_selected.memory_usage(deep=True).sum() / (1024 ** 2)
    reduction = ((before - after) / before) * 100

    print("Memory before optimisation: {:.2f} MB".format(before))
    print("Memory after optimisation: {:.2f} MB".format(after))
    print("Memory reduction: {:.2f}%".format(reduction))
    print(df_selected.dtypes)
    ```

-   **Results**:
    -   Memory before optimisation: 371.95 MB
    -   Memory after optimisation: 32.50 MB
    -   Memory reduction: 91.26%
    -   Execution time: 1.85 seconds
    -   Memory change: 0.00 MB

-   **Analysis**: Optimizing data types produced a major memory reduction from 371.95 MB to 32.50 MB. This shows that data type optimization is highly effective when a dataset contains repeated categorical values and columns that can be downcasted.

**4.1.4. Sampling**

Sampling allows a smaller representative subset of the dataset to be used for faster exploration and testing.

-   **Explanation**: A sample of 30,000 rows was selected from the loaded data for quick analysis.

-   **Code Snippet (Pandas)**:

    ```
    sample_df = df_selected.sample(n=30000, random_state=42)

    avg_dep_sample = sample_df["DepDelay"].mean()
    avg_arr_sample = sample_df["ArrDelay"].mean()

    print("Sample shape:", sample_df.shape)
    print("Average Departure Delay:", avg_dep_sample)
    print("Average Arrival Delay:", avg_arr_sample)
    ```

-   **Results**:
    -   Sample shape: (30000, 8)
    -   Average departure delay: 8.49 minutes
    -   Average arrival delay: 6.07 minutes
    -   Execution time: 1.65 seconds
    -   Memory change: 0.00 MB

-   **Analysis**: Sampling was useful for quick exploratory analysis. The sample result was close to the full dataset result, showing that sampling can provide a fast approximation before running full-scale processing.

### 4.2. Dask for Parallel Processing

Dask enables parallel computation on large datasets by splitting the data into partitions and processing them efficiently.

-   **Explanation**: Dask DataFrame was used to read selected columns from the CSV file and calculate delay-related metrics.

-   **Code Snippet (Dask)**:

    ```
    import dask.dataframe as dd

    ddf = dd.read_csv(main_file, usecols=selected_cols, assume_missing=True)

    total_rows = len(ddf)
    avg_dep_delay = ddf["DepDelay"].mean().compute()
    avg_arr_delay = ddf["ArrDelay"].mean().compute()
    delayed_flights = (ddf["ArrDelay"] > 0).sum().compute()
    delayed_percentage = (delayed_flights / total_rows) * 100

    print("Total Rows:", total_rows)
    print("Average Departure Delay:", avg_dep_delay)
    print("Average Arrival Delay:", avg_arr_delay)
    print("Delayed Flights Count:", delayed_flights)
    print("Delayed Flights Percentage:", delayed_percentage)
    ```

-   **Results**:
    -   Total rows processed: 2,000,000
    -   Average departure delay: 8.59 minutes
    -   Average arrival delay: 6.21 minutes
    -   Delayed flights count: 859,554
    -   Delayed flights percentage: 42.98%
    -   Execution time: 37.74 seconds
    -   Memory change: 1.13 MB

-   **Analysis**: Dask showed low memory change and successfully processed the full dataset. However, it was slower than Pandas and Polars in this experiment due to task scheduling overhead. Dask is still beneficial for larger-than-memory datasets and distributed processing.

### 4.3. Comparative Performance of Libraries

To compare library performance, Pandas, Dask, and Polars were used to calculate the same delay-related metrics.

**4.3.1. Pandas Baseline Processing**

-   **Code Snippet**:

    ```
    df_pandas = pd.read_csv(main_file, usecols=selected_cols)

    total_rows = len(df_pandas)
    avg_dep_delay = df_pandas["DepDelay"].mean()
    avg_arr_delay = df_pandas["ArrDelay"].mean()
    delayed_flights = (df_pandas["ArrDelay"] > 0).sum()
    delayed_percentage = (delayed_flights / total_rows) * 100

    print("Total Rows:", total_rows)
    print("Average Departure Delay:", avg_dep_delay)
    print("Average Arrival Delay:", avg_arr_delay)
    print("Delayed Flights Count:", delayed_flights)
    print("Delayed Flights Percentage:", delayed_percentage)
    ```

-   **Results**:
    -   Total rows processed: 2,000,000
    -   Average departure delay: 8.59 minutes
    -   Average arrival delay: 6.21 minutes
    -   Delayed flights count: 859,554
    -   Delayed flights percentage: 42.98%
    -   Execution time: 12.09 seconds
    -   Memory change: 0.00 MB

**4.3.2. Polars Processing**

-   **Explanation**: Polars is a DataFrame library implemented in Rust and designed for fast performance.

-   **Code Snippet**:

    ```
    import polars as pl

    result = (
        pl.scan_csv(main_file)
        .select(selected_cols)
        .select([
            pl.len().alias("Total Rows"),
            pl.col("DepDelay").mean().alias("Average Departure Delay"),
            pl.col("ArrDelay").mean().alias("Average Arrival Delay"),
            (pl.col("ArrDelay") > 0).sum().alias("Delayed Flights"),
            (((pl.col("ArrDelay") > 0).sum() / pl.len()) * 100).alias("Delayed Flights Percentage")
        ])
        .collect()
    )

    print(result)
    ```

-   **Results**:
    -   Total rows processed: 2,000,000
    -   Average departure delay: 8.59 minutes
    -   Average arrival delay: 6.21 minutes
    -   Delayed flights count: 859,554
    -   Delayed flights percentage: 42.98%
    -   Execution time: 1.21 seconds
    -   Memory change: 546.69 MB

**4.3.3. Dask Processing**

-   **Explanation**: Dask loads the dataset into partitions and performs calculations using parallel processing.

-   **Code Snippet**: Same as Section 4.2.

-   **Results**:
    -   Total rows processed: 2,000,000
    -   Average departure delay: 8.59 minutes
    -   Average arrival delay: 6.21 minutes
    -   Delayed flights count: 859,554
    -   Delayed flights percentage: 42.98%
    -   Execution time: 37.74 seconds
    -   Memory change: 1.13 MB

## 5. Results and Analysis

This section summarizes the performance metrics collected from applying various data handling techniques and comparing library efficiency.

### 5.1. Comparison of Data Handling Techniques

The `big_data.ipynb` notebook includes comparisons of execution time and memory change for the strategies: Load Less Data, Chunking, Optimized Data Types, Sampling, Pandas Baseline, Dask, and Polars.

| Technique / Library | Execution Time (s) | Memory Change (MB) |
| :------------------ | :----------------- | :----------------- |
| Load Less Data | 26.19 | 261.09 |
| Use Chunking | 12.15 | 19.47 |
| Optimize Data Types | 1.85 | 0.00 |
| Sampling | 1.65 | 0.00 |
| Pandas Baseline | 12.09 | 0.00 |
| Dask | 37.74 | 1.13 |
| Polars | 1.21 | 546.69 |

-   **Execution Time**: Polars was the fastest method with an execution time of 1.21 seconds. Sampling and optimized data types were also fast because they worked on already loaded or reduced data. Dask was the slowest in this experiment due to parallel processing overhead.
-   **Memory Usage**: Optimized data types reduced memory usage significantly from 371.95 MB to 32.50 MB. Chunking also performed well by keeping memory change low at 19.47 MB. Polars had the highest memory change in this run, but it achieved the fastest execution time.
-   **Overall Performance**: Polars was best for speed, chunking was best for memory-safe full processing, and Pandas remained easy to use for baseline analysis.

### 5.2. Comparison of Library Performance

The following table summarizes the performance of Pandas, Polars, and Dask when performing the same delay analysis task:

| Library | Execution Time (s) | Memory Change (MB) |
|---------|---------------------|--------------------|
| Pandas | 12.09 | 0.00 |
| Polars | 1.21 | 546.69 |
| Dask | 37.74 | 1.13 |

-   **Polars** demonstrated the fastest performance with 1.21 seconds due to its optimized query engine and lazy execution.
-   **Pandas** completed the processing in 12.09 seconds and was straightforward to implement.
-   **Dask** completed the task in 37.74 seconds. Although slower in this test, it is useful for larger datasets that may not fit into memory.

### 5.3. Delay Analysis Results

The full dataset was analyzed to understand flight delay patterns.

| Metric | Result |
|--------|--------|
| Total Rows Processed | 2,000,000 |
| Average Departure Delay | 8.59 minutes |
| Average Arrival Delay | 6.21 minutes |
| Delayed Flights Count | 859,554 |
| Delayed Flights Percentage | 42.98% |

The analysis shows that 859,554 flights experienced arrival delays, representing 42.98% of the dataset. The average departure delay was higher than the average arrival delay, indicating that some flights may have recovered part of the delay during flight.

## 6. Conclusion and Reflection

### 6.1. Summary of Findings

-   **Polars** performed best in terms of execution time, completing the analysis in 1.21 seconds.
-   **Pandas** was easy to use and provided reliable baseline performance, completing the analysis in 12.09 seconds.
-   **Dask** showed its ability to process the full dataset with low memory change, but it introduced overhead and was slower in this experiment.
-   **Chunking** was effective for processing the full dataset while controlling memory usage.
-   **Optimized data types** produced a major memory reduction from 371.95 MB to 32.50 MB.

### 6.2. Effectiveness of Strategies

-   **Load Less Data** helped reduce unnecessary data loading by selecting only 8 important columns from 109 columns.
-   **Chunking** was effective for processing large files without loading the entire dataset into memory.
-   **Data Type Optimization** was highly effective in reducing memory usage by 91.26%.
-   **Sampling** was useful for quick exploratory analysis and testing.
-   **Dask Parallel Processing** demonstrated scalability but required careful implementation to avoid overhead.
-   **Polars Processing** provided the best execution speed in this project.

### 6.3. Limitations

-   Some memory change values were recorded as 0.00 MB because the Google Colab runtime may reuse memory that was already allocated.
-   The main comparison focused on selected columns instead of processing all 109 columns for every strategy.
-   Dask performance may improve for even larger datasets or distributed computing environments.
-   The results may vary depending on hardware, runtime memory, CPU availability, and library versions.

### 6.4. Learning Reflection

This assignment provided practical experience in handling large datasets using different tools and strategies. The key learning points include:

-   The importance of selecting only necessary columns when working with large datasets.
-   The impact of data types on memory usage.
-   The usefulness of chunking when a dataset is too large to load at once.
-   The difference between ease of use, memory efficiency, and execution speed across Pandas, Dask, and Polars.
-   The need to choose the right tool based on the size of the dataset, available resources, and the purpose of the analysis.

Through this project, we gained a better understanding of how memory usage, execution time, and parallel processing affect big data workflows.

## 7. References

-   **Dataset**: Kaggle: Carrier On-Time Performance Dataset - [https://www.kaggle.com/datasets/mexwell/carrier-on-time-performance-dataset](https://www.kaggle.com/datasets/mexwell/carrier-on-time-performance-dataset)
-   **Pandas Documentation**: [https://pandas.pydata.org/pandas-docs/stable/](https://pandas.pydata.org/pandas-docs/stable/)
-   **Dask Documentation**: [https://docs.dask.org/en/latest/](https://docs.dask.org/en/latest/)
-   **Polars Documentation**: [https://docs.pola.rs/](https://docs.pola.rs/)

## Appendix: Code and Visualizations

For all detailed Python code, execution outputs, and generated visualizations such as bar charts comparing execution time and memory usage, please refer to the accompanying Jupyter Notebook: [big_data.ipynb](big_data.ipynb).

----------

**Academic Integrity Note:** All work presented in this report and the accompanying notebook is original. Academic integrity has been strictly adhered to.
