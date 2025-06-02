# Assignment 2: Big Data Handling and Optimization Using NYC Taxi Trip Dataset🚕 
## 👥 Group Members

| Name               | Matric Number |
|--------------------|---------------|
| Muhammad Iman Firdaus Bin Baharuddin        | A22EC0216       |
| Muhammad Ariff Danish Bin Hashnan         | A22EC0204       |

---

## 📌 Project Overview
---

## 📌 Key Observations
### ✅ Benefits & Limitations of Each Method
---

## 🧪 Tasks & Implementation

### Task 1: Dataset Selection
---

### Task 2: Load and Inspect Data
---

### Task 3: Apply Big Data Handling Strategies
---

### Task 4: Comparative Analysis
![image](https://raw.githubusercontent.com/MuhammadImanFirdaus/Photos/refs/heads/main/Screenshot%202025-06-03%20004351.png?token=GHSAT0AAAAAADDVYJY73HAMPXRANPUDRCCE2B54MQQ)

1. Execution Time
Pandas : Completed the task in 34.45 seconds .
Polars : Finished the task in 10.16 seconds , making it the fastest library.
Dask : Executed the task in 32.58 seconds , slightly slower than Polars but faster than Pandas.

2. Memory Usage
Pandas : Consumed 3039.86 MB of memory.
Polars : Used 1949.65 MB , demonstrating significant memory savings compared to Pandas.
Dask : Utilized 1201.98 MB , showing the most efficient memory usage among the three libraries.

📌 Key Observations
 - Polars is the fastest library, showcasing its efficiency in handling large datasets due to its Rust-based implementation.
 - Dask provides scalable computing capabilities while maintaining low memory usage, making it ideal for distributed environments or very large datasets.
 - Pandas , while widely used, struggles with larger-than-GB datasets due to high memory consumption and slower execution times.

## Final Thoughts
This analysis highlights that:

 - Polars excels in speed but uses moderate memory.
 - Dask offers good scalability and low memory usage, making it suitable for distributed 
   computing and very large datasets.
 - Pandas , while versatile, is less efficient for big data processing compared to Polars and 
   Dask.
By selecting the appropriate tool based on specific requirements (e.g., speed, memory, scalability),optimization on data processing workflows can be heightened effectively.
---

### Task 5: Conclusion & Reflection
This assignment provided valuable hands-on experience in managing and optimizing large-scale data processing workflows. Some key takeaways include:

✅ Performance Optimization Techniques
 - Reducing column count (usecols) significantly improves both time and memory efficiency.
 - Data type optimization reduces memory usage by over 70% without losing data fidelity.
 - Chunking is ideal for memory-constrained environments but requires custom logic for full-dataset operations.
 - Sampling is useful during early development but must be used cautiously to avoid misleading insights.
 - Dask enables parallel processing and scalability, especially for files larger than available RAM, though it comes with increased complexity and memory overhead.
   
⚠️ Challenges Faced
 - Measuring accurate memory usage was tricky due to garbage collection and lazy evaluation behavior.
 - Some methods like chunking and Dask require additional logic to perform aggregations or full dataset operations.
 - Type mismatches and missing values required careful preprocessing to ensure smooth execution.

🎯 Thoughts
This exercise highlighted that there is no one-size-fits-all solution when working with big data. The best strategy depends heavily on:

 - The size and structure of the dataset
 - Available system resources (RAM, CPU cores)
 - The goal of the analysis (prototyping vs production)
 - By understanding and applying these techniques, we can make informed decisions about how to handle large-scale data efficiently in real-world scenarios.

📝 Summary
In summary, this assignment emphasized the importance of efficient data handling strategies when working with large datasets. By applying techniques such as selective loading, chunking, data type optimization, sampling, and parallel processing, we can significantly improve performance and reduce resource consumption.

Whether you're analyzing flight delays or tackling any other big data problem, choosing the right approach can make all the difference between a sluggish process and a smooth, scalable workflow.


---
