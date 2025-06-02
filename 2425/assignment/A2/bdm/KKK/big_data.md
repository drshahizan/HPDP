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
