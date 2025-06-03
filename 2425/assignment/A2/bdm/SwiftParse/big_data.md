# 🧠 Big Data Analysis of 2019 Airline Delays with Weather & Airport Detail

This project explores **various strategies** for efficiently handling large-scale datasets and processing data using popular Python libraries: **Pandas**, **Dask**, and **Polars**. Through comparative evaluation, the goal is to identify techniques that improve **execution time** and **memory usage** for both data loading and processing tasks.

The performance evaluation is divided into two parts:

Part 1: Big Data Handling Strategies
<br></br>
**Objective**: Compare five strategic approaches for reading and optimizing large datasets using Pandas and Dask.

- 📌 Load Less Data  
- 📌 Use Chunking  
- 📌 Optimize Data Types  
- 📌 Sampling  
- 📌 Parallel Processing with Dask  

Part 2: Data Processing using 3 different libraries
<br></br>
**Objective**: Benchmark three Python libraries using traditional and optimized data processing pipelines.

- 🐼 **Pandas** (Traditional Processing)  
- 🧵 **Dask**   
- ⚡ **Polars** 
---

## 📂 Dataset Description

The dataset used in this project is full_data_flightdelay.csv (size: 1.27 GB), containing 6489062 of flight records from 2019. It simulates real-world big data challenges by combining flight schedules, weather conditions, and airline operations.

- Dataset: [2019 Airline Delays w/Weather and Airport Detail](https://www.kaggle.com/datasets/threnjen/2019-airline-delays-and-cancellations?resource=download)
- Size: 1.27 GB
- Records in dataset: 6489062

Below is a table describing 26 columns in the dataset:
| Column                          | Description                                                              |
| ------------------------------- | ------------------------------------------------------------------------ |
| `MONTH`                         | Month of the year (1-12)                                                 |
| `DAY_OF_WEEK`                   | Day of the week (1=Monday, 7=Sunday)                                     |
| `DEP_DEL15`                     | **Target:** Binary indicator (1 = Departure delayed over 15 mins)        |
| `DEP_TIME_BLK`                  | Departure time block                                                     |
| `DISTANCE_GROUP`                | Distance group to be flown by the aircraft                               |
| `SEGMENT_NUMBER`                | Segment index of the tail number for the day                             |
| `CONCURRENT_FLIGHTS`            | Flights departing concurrently within the same time block at the airport |
| `NUMBER_OF_SEATS`               | Number of seats on the aircraft                                          |
| `CARRIER_NAME`                  | Name of the airline carrier                                              |
| `AIRPORT_FLIGHTS_MONTH`         | Average monthly flights at the airport                                   |
| `AIRLINE_FLIGHTS_MONTH`         | Average monthly flights by the airline                                   |
| `AIRLINE_AIRPORT_FLIGHTS_MONTH` | Average monthly flights by the airline at the airport                    |
| `AVG_MONTHLY_PASS_AIRPORT`      | Average monthly passengers at the airport                                |
| `AVG_MONTHLY_PASS_AIRLINE`      | Average monthly passengers on the airline                                |
| `FLT_ATTENDANTS_PER_PASS`       | Flight attendants per passenger for the airline                          |
| `GROUND_SERV_PER_PASS`          | Ground service staff per passenger for the airline                       |
| `PLANE_AGE`                     | Age of the aircraft in years                                             |
| `DEPARTING_AIRPORT`             | Airport code for departure                                               |
| `LATITUDE`                      | Latitude of the departing airport                                        |
| `LONGITUDE`                     | Longitude of the departing airport                                       |
| `PREVIOUS_AIRPORT`              | Previous airport that aircraft departed from                                  |
| `PRCP`                          | Precipitation (inches) on the day of departure                           |
| `SNOW`                          | Snowfall (inches) on the day of departure                                |
| `SNWD`                          | Snow depth (inches) on the ground                                        |
| `TMAX`                          | Maximum temperature (°F) on the day of departure                         |
| `AWND`                          | Maximum wind speed (mph) on the day of departure                         |

---
## 🧪 Load and Inspect Data
Before applying the five optimization techniques, the full dataset was loaded using standard pandas.read_csv() to understand the baseline performance and structure of the data. This initial step allowed us to observe the raw resource usage when handling the full 1.27GB CSV file (full_data_flightdelay.csv) without any optimization.

Initial Loading Results:

- Execution Time: 35.45 seconds

- Memory Used: 3961.75 MB

<br></br>
![Data Processing using Pandas](./images/Load.png)

This result highlights the performance limitations of loading large datasets without strategy. It also highlights the need to explore alternative methods for optimizing execution time and memory efficiency.

## 🧪 Strategy Implementations

We implemented **five data-loading and cleaning strategies** with Pandas, and used **Dask and Polars** for parallel and optimized processing:

###  Part 1: Big Data Handling Strategies
In this step-by-step comparison, five different data processing strategies were applied using only the Pandas library to evaluate their effectiveness in terms of execution time and memory usage. 

1. The **"Load Less Data"** strategy focused on minimizing the volume of data read into memory by selecting only necessary columns or filtering rows during import. This approach showed a balanced performance, with moderate execution time and memory usage. 
<br></br>
![Load Less Data](./images/T1.png)
<br></br>
Our approach read only these 9 columns: 'MONTH', 'DAY_OF_WEEK', 'DEP_DEL15', 'CONCURRENT_FLIGHTS', 'CARRIER_NAME', 'AIRPORT_FLIGHTS_MONTH', 'AIRLINE_FLIGHTS_MONTH', 'PREVIOUS_AIRPORT', 'AWND'. Thus, the code loads only the selected columns from the CSV. This approach will make the program faster as it reads less data from disk and uses less memory which it doesn't store unwanted columns. Therefore, it is more efficient than loading the entire file and then dropping columns.

2. The **"Chunking"** method processed data in smaller batches using Pandas' `chunksize` parameter, which resulted in the fastest execution time and nearly zero memory usage, making it highly efficient for very large datasets that cannot be loaded entirely into memory. 
<br></br>
![Chunking](./images/T2.png)
<br></br>
Chunking Process divides the large file by reading the CSV in smaller pieces (chunks) of 100,000 rows at a time instead of loading the entire file into memory at once. It processes each chunk separately and prints the chunk's shape for every 100,000-row chunk. Our approach will only processes first 3 chunks

3. The **"Optimize Data Types"** strategy involved converting data columns to more memory-efficient types (such as changing float64 to float32 or object to category), which significantly reduced memory consumption but incurred a higher execution time due to the computational cost of conversion.
<br></br>
![DOptimize Data Types](./images/T3.png)
<br></br>
This approach loads the CSV file while minimizing memory usage by specifying optimal data types for each column. The code uses a dictionary (dtypes_optimized) to assign compact data types such as:

- Small integers (int8, int16) for numeric columns with limited range
- category type for repetitive text values (like airport codes)
- 32-bit floats (float32) instead of default 64-bit

4. **"Sampling"** involved selecting a subset of the data to work with, reducing the memory footprint dramatically, but similar to data type optimization, it took longer to execute—likely due to the effort needed to create a representative sample.
<br></br>
![Sampling](./images/T4.png)
<br></br>
This approach applied simple random sampling which every row in the original dataset has an equal 1% chance of being selected and the selection is random and unbiased. The code reads the entire CSV file (pd.read_csv(file_path)) and takes a 1% random sample using .sample(frac=0.01). "random_state=42" ensures reproducibility (same random sample each run).

5. **"Parallel with Dask"**, while still using Pandas under the hood, distributed the workload across multiple cores. This led to better speed than loading all data at once, but it consumed the highest amount of memory due to the overhead from parallel processing.
<br></br>
![Parallel with Dask](./images/T5.png)
<br></br>
This approach loads data lazily (doesn't load into memory immediately) and only loads specified columns (memory optimization). .compute() triggers actual loading of data into memory (converts Dask DataFrame → pandas DataFrame). Dask approach does not load data immediately. Instead, it builds a task graph and executes only when .compute() is called.

Overall, each strategy has its trade-offs: chunking stands out as the most memory-efficient and fastest, while others like data type optimization and sampling are useful for long-term performance gains despite longer initial processing times.


### Part 2: Data Processing using 3 different libraries
In this part, the dataset undergoes data cleaning and analysis using Pandas, Dask, and Polars to compare their performance. The cleaning process included checking for null values and duplicates. Duplicated rows were found and removed , while no missing values were detected.

For the analysis, the data processing focused on evaluating airline performance by calculating the departure delay rate specifically the proportion of flights delayed more than 15 minutes. The analysis is grouped by month and carrier. The corresponding delay percentage was computed.

Each library was used to execute the same task, and the execution time and memory usage were recorded to assess their efficiency and identify which library handled the dataset most effectively for this type of analysis.

1. Pandas
<br></br>
![Data Processing using Pandas](./images/Part2_Pandas.png)

What it does:
- Reads the full CSV into memory with pd.read_csv().

- Removes duplicates directly in memory.

- Groups data by MONTH and CARRIER_NAME, then:

- Counts total flights,

- Sums delayed flights (DEP_DEL15 == 1),

- Computes the average delay rate.

- Adds a delay percentage column.

2. Dask
<br></br>
![Data Processing using Dask](./images/Part2_Dask.png)

What it does:
- Reads the CSV using lazy loading (doesn’t load all data at once).

- Drops duplicates in parallelized chunks.

- Groups data the same way as Pandas, but the operation is lazy until .compute() is called.

- Final result is converted to a Pandas DataFrame for output.

3. Polars
<br></br>
![Data Processing using Polars](./images/Part2_Polars.png)

What it does:
- Uses Polars' lazy API for deferred computation.

- Groups and aggregates using efficient Polars expressions.

- Adds a calculated delay_pct column.

- Triggers execution with .collect() (similar to .compute() in Dask).

---

## 📊 Comparative Analysis 

A side-by-side comparison of each technique was conducted based on:

- **Execution Time (s)**
- **Memory Used (MB)**

###  Part 1: Big Data Handling Strategies

### 📈 Technique Comparison Chart
![Comparison Table](./images/Table1.jpg)

![Execution Comparison](./images/Chart1-1.jpg)

![Memory Usage Comparison ](./images/Chart1-2.jpg)


### Part 2: Data Processing using 3 different libraries
### 📈 Library Comparison Chart
![Comparison Chart](./images/Table2.png)

![Execution Comparison](./images/chart2.png)

![Memory Usage Comparison ](./images/chart3.png)


### Discussion
In Part 1, five different strategies were applied to load and prepare a large dataset efficiently. Among these, Chunking delivered the best overall performance by achieving the lowest execution time and memory usage. This is due to its ability to process manageable portions of the dataset sequentially which avoids overwhelming system memory and minimizes runtime. Besides, sampling also showed excellent memory efficiency by working on a reduced subset of the data, but it required slightly more time compared to chunking. This is likely because the sample still needed to be extracted from the full dataset before operations could begin.Next, optimizing data types reduced memory consumption by converting columns to more efficient formats (e.g., int64 to int32, or object to category). While this technique helped in memory reduction, it didn’t significantly improve execution time which suggesting that memory constraints were not the main bottleneck during processing. Parallel Processing using Dask showed moderate improvements in execution time through its task scheduling system and lazy evaluation. However, this came with higher memory usage. The extra memory was likely consumed by task graph creation and intermediate data storage during .compute() execution.Lastly,loading less data is simple but slower due to the selective I/O overhead and lack of optimization during partial reads. In summary, Chunking and Sampling are ideal in resource-constrained environments due to their minimal memory usage, while Dask is better suited for scenarios where more compute power and memory are available.

In Part 2, the same analytical task was executed using three different data processing libraries: Pandas, Dask, and Polars. Polars demonstrated the fastest execution speed that complete the task in under 9 seconds. This impressive performance is attributed to Polars' Rust-based backend and lazy evaluation engine which allows optimized execution plans and efficient use of system resources. However, this speed came at the cost of highest memory consumption. Thus, Polars is more suitable for machines with adequate RAM. Pandas is slower but consumed the least memory. This makes it suitable for smaller datasets or low-memory environments. However, its eager execution model and in-memory operations caused performance to drop significantly with full-scale datasets. Dask provided moderate execution time with the advantage of parallel processing but showed higher memory consumption than Pandas. The tradeoff was due to the overhead of Dask's task scheduling and lazy computation graph which becomes beneficial only for larger distributed systems or scalable environments.

---



## 📌 Conclusion & Reflection

In summary, **Chunking** had the best performance among the 5 big data handling techniques with the lowest exeuction time and memory usage. Meanwhile, **Sampling** was efficient in memory but still took longer time to process. **Parallel Processing** with Dask showed improvement in time but consumed significantly more memory. **Optimize Data Types** helped reduce memory but didn’t significantly improve time. Techniques like chunking and sampling significantly reduce memory usage and load time, making them practical choices for handling large datasets without overwhelming system resources.

For part 2, **Polars** was the fastest, with the execution time under 9 seconds, but required the highest memory. **Pandas** used the least memory, but its performance was noticeably slower.
**Dask** offered parallel processing but suffered in both speed and memory compared to the others, possibly due to overhead and compute operations. In conclusion, Polars is suitable for maximum speed when memory is not a constraint. Pandas should be used when working with smaller datasets or limited RAM while Dask should be applied in distributed environments or for chunk-based workloads where parallel execution is needed but compute power is sufficient.

| Method                         | Benefits                                        | Limitations                                          |
| ------------------------------ | ----------------------------------------------- | ---------------------------------------------------- |
| **Load Less Data**             | - Reduces overall memory usage                  | - Still takes time depending on file read scope      |
| **Chunking**                   | - Fastest loading time<br>- Lowest memory usage | - Mostly beneficial for loading, not full processing |
| **Sampling**                   | - Low memory usage                              | - Slower processing compared to chunking             |
| **Optimize Data Types**        | - Significantly reduces memory usage            | - Minimal impact on execution time                   |
| **Parallel Processing (Dask)** | - Improved loading time via parallel execution  | - Very high memory consumption                       |

### Reflection
This assignment provided valuable insights into various techniques for handling big data. These methods demonstrated how different strategies affect execution time and memory usage, which is crucial when working with large-scale datasets.

Running the experiments on platforms like Google Colab highlighted practical limitations of cloud-based environments — limited resources can sometimes lead to runtime crashes, especially with large files or resource-intensive tasks. This underscores the importance of selecting strategies that align with the capabilities of the execution environment.

The comparison between Pandas, Dask, and Polars revealed that each library has strengths suited to specific use cases. Polars offers exceptional speed but at the cost of higher memory usage. Pandas is memory-efficient and well-suited for smaller datasets, though it is slower. Dask supports parallel processing and is beneficial in distributed settings but may incur additional overhead.

Overall, the experience emphasized the importance of scalable data processing strategies and the thoughtful selection of tools based on task complexity and system limitations.

---

## 🔗 Reference

1. [2019 Airline Delays w/Weather and Airport Detail](https://www.kaggle.com/datasets/threnjen/2019-airline-delays-and-cancellations?resource=download)
2. [Source Code](https://colab.research.google.com/drive/1wUMZHJUkx59CJcZO5pYSnyD-rbPrztir?usp=sharing#scrollTo=7MG1r2tM2sLW)
