# Assignment 2: Mastering Big Data Handling 📊<br>
This repository presents our journey through efficient big data processing in Python, a core component of the SECP3133 High Performance Data Processing course. Our goal was to conquer large datasets by implementing and comparing various optimization strategies and powerful data processing libraries.

## 🎯 Project Focus
We delved into a massive 2.57 GB "School Donation Dataset" from Kaggle, analyzing how different approaches impact crucial performance metrics like execution time and memory consumption.

## ✨ Our Big Data Strategies ✨
We explored and benchmarked five key strategies to handle the data efficiently:
- Load Less Data 🤏: Only loading the columns that truly matter, significantly cutting down memory usage.
- Chunking 📦: Processing the dataset in smaller, manageable pieces to avoid overwhelming memory.
- Optimize Data Types 🧠: Smartly converting data types (e.g., object to category, downcasting numbers) for a leaner memory footprint.
- Sampling 🎲: Taking a representative slice of the data for quick insights and rapid prototyping.
- Parallel Processing with Dask ⚡: Harnessing Dask's power for out-of-core and parallel computations on distributed data.

## 📚 Libraries Conducted 📚
In addition to the strategies, we conducted a comparative analysis of three prominent Python libraries for big data processing:
- Pandas 🐼: The widely used library for data manipulation, serving as our sequential baseline.
- Polars 🐻‍❄️: A high-performance DataFrame library written in Rust, designed for speed and memory efficiency.
- Dask ⚙️: A flexible library for parallel computing, extending Pandas and NumPy to larger-than-memory datasets.

## 📈 Performance at a Glance 📉
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
