# Assignment 2: Mastering Big Data Handling 📊<br>
This repository presents our journey through efficient big data processing in Python, a core component of the SECP3133 High Performance Data Processing course. Our goal was to conquer large datasets by implementing and comparing various optimization strategies and powerful data processing libraries.

## 📌 Introduction
This project tackles the challenge of efficiently processing large datasets (exceeding 700MB) using Python. We explored various optimization strategies and data processing libraries to manage and analyze a 2.57 GB [School Donation Dataset](https://www.kaggle.com/datasets/perkymaster/school-donations?select=Projects.csv) from Kaggle, focusing on performance metrics like execution time and memory consumption.

## 🎯 Project Focus
Our core objective was to gain hands-on experience with real-world big data handling techniques. We systematically implemented and benchmarked different approaches to identify their strengths, weaknesses and optimal use cases.

## ✨ Big Data Handling Strategies Explored ✨
We explored and benchmarked five key strategies to handle the data efficiently:
1.  **Load Less Data 🤏:** Selectively loading only essential columns or a subset of rows to minimize memory overhead.
2.  **Chunking 📦:** Processing the dataset in smaller, sequential chunks to handle files larger than available RAM.
3.  **Optimize Data Types 🧠:** Converting data columns to more memory-efficient types (e.g., `object` to `category`, downcasting numeric types).
4.  **Sampling 🎲:** Using a representative subset of the data for rapid analysis and prototyping.
5.  **Parallel Processing with Dask ⚡:** Leveraging Dask DataFrames for parallel and out-of-core computation.

## 📚 Libraries Conducted 📚
In addition to the strategies, we conducted a comparative analysis of three prominent Python libraries for big data processing:
-   **Pandas 🐼:** Serving as our baseline for traditional, sequential data manipulation.
-   **Polars 🐻‍❄️:** A modern, high-performance DataFrame library built in Rust, known for its speed and memory efficiency.
-   **Dask ⚙️:** A flexible library for parallel computing, enabling scalable processing of large datasets.

## 📈 Performance Summary 📉
Our experiments yielded significant insights into the effectiveness of each strategy and library.
<h3>Optimized Strategies Performance</h3>
<table style="width:100%; border-collapse: collapse;">
    <thead>
        <tr style="background-color:#f2f2f2;">
            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Strategy</th>
            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Execution Time (seconds)</th>
            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Memory Used (MB)</th>
            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Memory Used (%)</th>
            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">CPU Usage (%)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Strategy 1: Load Less Data</td>
            <td style="border: 1px solid #ddd; padding: 8px;">25.61</td>
            <td style="border: 1px solid #ddd; padding: 8px;">83.61</td>
            <td style="border: 1px solid #ddd; padding: 8px;">0.64</td>
            <td style="border: 1px solid #ddd; padding: 8px;">12.65</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Strategy 2: Chunking</td>
            <td style="border: 1px solid #ddd; padding: 8px;">40.23</td>
            <td style="border: 1px solid #ddd; padding: 8px;">699.82</td>
            <td style="border: 1px solid #ddd; padding: 8px;">5.39</td>
            <td style="border: 1px solid #ddd; padding: 8px;">5.00</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Strategy 3: Optimize Data Types</td>
            <td style="border: 1px solid #ddd; padding: 8px;">43.07</td>
            <td style="border: 1px solid #ddd; padding: 8px;">553.51</td>
            <td style="border: 1px solid #ddd; padding: 8px;">4.26</td>
            <td style="border: 1px solid #ddd; padding: 8px;">47.60</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Strategy 4: Sampling</td>
            <td style="border: 1px solid #ddd; padding: 8px;">19.43</td>
            <td style="border: 1px solid #ddd; padding: 8px;">0.00</td>
            <td style="border: 1px solid #ddd; padding: 8px;">0.00</td>
            <td style="border: 1px solid #ddd; padding: 8px;">28.20</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Strategy 5: Dask Parallel</td>
            <td style="border: 1px solid #ddd; padding: 8px;">61.51</td>
            <td style="border: 1px solid #ddd; padding: 8px;">43.58</td>
            <td style="border: 1px solid #ddd; padding: 8px;">0.34</td>
            <td style="border: 1px solid #ddd; padding: 8px;">38.00</td>
        </tr>
    </tbody>
</table>

**Key Findings (Strategies):**
-   **Sampling** proved to be the most efficient for quick exploration due to minimal data processing.
-   **Load Less Data** and **Optimize Data Types** are highly effective for reducing memory and improving speed when more of the data is required.
-   **Dask** showed its strength in memory management, though its overhead made it slower for simpler read operations compared to specialized strategies on this specific task.

<br>

<h3>Data Processing Libraries Performance</h3>
<table style="width:100%; border-collapse: collapse;">
    <thead>
        <tr style="background-color:#f2f2f2;">
            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Library</th>
            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Execution Time (seconds)</th>
            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Memory Used (%)</th>
            <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">CPU Usage (%)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Pandas</td>
            <td style="border: 1px solid #ddd; padding: 8px;">55.76</td>
            <td style="border: 1px solid #ddd; padding: 8px;">75.20</td>
            <td style="border: 1px solid #ddd; padding: 8px;">58.00</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Dask</td>
            <td style="border: 1px solid #ddd; padding: 8px;">73.76</td>
            <td style="border: 1px solid #ddd; padding: 8px;">45.30</td>
            <td style="border: 1px solid #ddd; padding: 8px;">39.00</td>
        </tr>
        <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Polars</td>
            <td style="border: 1px solid #ddd; padding: 8px;">8.86</td>
            <td style="border: 1px solid #ddd; padding: 8px;">39.13</td>
            <td style="border: 1px solid #ddd; padding: 8px;">38.00</td>
        </tr>
    </tbody>
</table>

**Key Findings (Libraries):**
-   **Polars** demonstrated superior speed and memory efficiency for reading the entire large dataset on a single node.
-   **Dask** excels in scenarios requiring distributed computing or handling datasets far exceeding system memory, though it has startup/coordination overhead.

## Conclusion
The choice of data handling strategy or library is highly dependent on the specific task, dataset size, available resources, and analytical goals. For rapid insights, sampling is highly effective. For single-node processing of large files, Polars offers remarkable performance. For truly out-of-core or distributed computations, Dask remains the go-to solution despite its overhead for simpler tasks. Understanding these trade-offs is crucial for efficient big data processing.
