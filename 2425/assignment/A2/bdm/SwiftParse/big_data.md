# 🧠 Big Data Analysis of 2019 Airline Delays with Weather & Airport Detail

This project explores **various strategies** for efficiently handling large-scale datasets and processing data using popular Python libraries: **Pandas**, **Dask**, and **Polars**. Through comparative evaluation, the goal is to identify techniques that improve **execution time** and **memory usage** for both data loading and processing tasks.

The performance evaluation is divided into two parts:

Part 1: Big Data Handling Strategies
**Objective**: Compare five strategic approaches for reading and optimizing large datasets using Pandas and Dask.

- 📌 Load Less Data  
- 📌 Use Chunking  
- 📌 Optimize Data Types  
- 📌 Sampling  
- 📌 Parallel Processing with Dask  

Part 2: Data Processing using 3 different libraries
**Objective**: Benchmark three Python libraries using traditional and optimized data processing pipelines.

- 🐼 **Pandas** (Traditional Processing)  
- 🧵 **Dask**   
- ⚡ **Polars** 
---

## 📂 Dataset Description

The dataset used contains millions of flight records with various features including:

- `MONTH`, `DAY_OF_WEEK`, `DEP_DEL15`, `CONCURRENT_FLIGHTS`, `CARRIER_NAME`, etc.
- Weather data: `AWND`, `PRCP`, `TMAX`, etc.
- The dataset size is substantial enough to simulate real-world big data challenges.

---

## 🧪 Strategy Implementations

We implemented **five data-loading and cleaning strategies** with Pandas, and used **Dask and Polars** for parallel and optimized processing:

###  Part 1: Big Data Handling Strategies
In this step-by-step comparison, five different data processing strategies were applied using only the Pandas library to evaluate their effectiveness in terms of execution time and memory usage. 

1. The **"Load Less Data"** strategy focused on minimizing the volume of data read into memory by selecting only necessary columns or filtering rows during import. This approach showed a balanced performance, with moderate execution time and memory usage. 
2. The **"Chunking"** method processed data in smaller batches using Pandas' `chunksize` parameter, which resulted in the fastest execution time and nearly zero memory usage, making it highly efficient for very large datasets that cannot be loaded entirely into memory. 
3. The **"Optimize Data Types"** strategy involved converting data columns to more memory-efficient types (such as changing float64 to float32 or object to category), which significantly reduced memory consumption but incurred a higher execution time due to the computational cost of conversion.
4. **"Sampling"** involved selecting a subset of the data to work with, reducing the memory footprint dramatically, but similar to data type optimization, it took longer to execute—likely due to the effort needed to create a representative sample. Lastly,
5. **"Parallel with Dask"**, while still using Pandas under the hood, distributed the workload across multiple cores. This led to better speed than loading all data at once, but it consumed the highest amount of memory due to the overhead from parallel processing.

Overall, each strategy has its trade-offs: chunking stands out as the most memory-efficient and fastest, while others like data type optimization and sampling are useful for long-term performance gains despite longer initial processing times.


### Part 2: Data Processing using 3 different libraries
In this part, the dataset undergoes data cleaning and analysis using Pandas, Dask, and Polars to compare their performance. The cleaning process included checking for null values and duplicates. Duplicated rows were found and removed , while no missing values were detected.

For the analysis, the data processing focused on evaluating airline performance by calculating the departure delay rate specifically the proportion of flights delayed more than 15 minutes. The analysis is grouped by month and carrier. The corresponding delay percentage was computed.

Each library was used to execute the same task, and the execution time and memory usage were recorded to assess their efficiency and identify which library handled the dataset most effectively for this type of analysis.

1. Pandas

2. Dask

3. Polars


---

## 📊 Comparative Analysis 

A side-by-side comparison of each technique was conducted based on:

- **Execution Time (s)**
- **Memory Used (MB)**
###  Part 1: Big Data Handling Strategies



### 📈 Technique Comparison Chart
![Technique Comparison Chart](./images/comparison_techniques.png)


### Part 2: Data Processing using 3 different libraries
### 📈 Library Comparison Chart
![Library Comparison Chart](./images/chart2.png)



---



## 📌 Conclusion & Reflection

- **Pandas** is simple but memory-heavy for large files.
- **Chunking and dtype optimization** greatly improved efficiency.
- **Dask** offers excellent parallelism but requires lazy evaluation understanding.
- **Polars** outperformed Pandas and Dask in both time and memory in most scenarios.
- Choosing the right tool depends on the dataset size and available resources.

---

## 🔗 GitHub Submission

📁 Repository Structure:
