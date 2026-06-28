# 📊 P2 Folder

This folder contains the performance evaluation files for the **BigPotato JobStreet High Performance Data Processing Pipeline** project.

The purpose of this folder is to store the benchmark results, evaluation notebook, and generated charts used to compare the performance of different data processing approaches.

---

## 📌 Folder Purpose

The `p2` folder focuses on evaluating the efficiency of the processing pipelines after the JobStreet dataset has been cleaned.

The evaluation compares:

* Baseline Pandas
* Optimized Pandas
* Polars Lazy Execution
* DuckDB SQL

The comparison is based on execution time, memory usage, CPU usage, and throughput.

---

## 📁 Files in This Folder

| File Name                       | Description                                             |
| ------------------------------- | ------------------------------------------------------- |
| `performance_before.csv`        | Benchmark result for the baseline Pandas implementation |
| `performance_after.csv`         | Benchmark results for optimized processing methods      |
| `evaluation_charts.ipynb`       | Notebook used to generate performance comparison charts |
| `execution_time_comparison.png` | Chart comparing average execution time                  |
| `memory_usage_comparison.png`   | Chart comparing memory usage                            |
| `cpu_usage_comparison.png`      | Chart comparing CPU usage                               |
| `throughput_comparison.png`     | Chart comparing throughput                              |
| `readme.md`                     | Documentation for the `p2` folder                       |

---

## ⚙️ Evaluation Metrics

The performance of each processing method was measured using four main metrics:

| Metric         | Description                                                        |
| -------------- | ------------------------------------------------------------------ |
| Execution Time | Time required to complete the data loading and aggregation process |
| Memory Usage   | Amount of memory consumed during execution                         |
| CPU Usage      | Percentage of CPU resources used during processing                 |
| Throughput     | Number of records processed per second                             |

---

## 📈 Benchmark Results Summary

| Method                | Execution Time (s) | Memory Usage (MB) | CPU Usage (%) | Throughput |
| --------------------- | -----------------: | ----------------: | ------------: | ---------: |
| Baseline Pandas       |               0.31 |              3.92 |         27.99 | 128,736.72 |
| Optimized Pandas      |               0.15 |             0.001 |         44.10 | 178,116.33 |
| Polars Lazy Execution |               0.07 |              0.79 |         16.88 | 400,751.48 |
| DuckDB SQL            |               0.23 |              0.02 |         39.07 | 110,278.38 |

---

## 📊 Generated Charts

### `execution_time_comparison.png`

Shows the average execution time of each processing method.

Polars Lazy Execution achieved the shortest execution time, making it the fastest method in this benchmark.

---

### `memory_usage_comparison.png`

Shows the memory usage comparison between the processing methods.

Optimized Pandas recorded the lowest memory usage due to selective column loading and data type optimization.

---

### `cpu_usage_comparison.png`

Shows the average CPU usage of each method.

Optimized Pandas recorded the highest CPU usage, while Polars achieved strong performance with lower CPU utilization.

---

### `throughput_comparison.png`

Shows the number of records processed per second.

Polars Lazy Execution achieved the highest throughput, showing its strength in fast and efficient data processing.

---

## 🔍 Key Findings

Based on the evaluation results:

* Polars Lazy Execution achieved the fastest processing time.
* Polars Lazy Execution recorded the highest throughput.
* Optimized Pandas achieved the lowest memory usage.
* DuckDB SQL provided efficient SQL-based analytical processing.
* Baseline Pandas was usable but less efficient compared to the optimized methods.

Overall, Polars Lazy Execution showed the best overall performance for this project workload.

---

## 🔄 Suggested Usage

The recommended workflow for this folder is:

```text
1. Open evaluation_charts.ipynb
2. Load performance_before.csv and performance_after.csv
3. Generate comparison charts
4. Review the PNG chart outputs
5. Use the results for report writing and presentation explanation
```

---

## 📌 Related Files

This folder is connected to:

| Folder       | Purpose                                                    |
| ------------ | ---------------------------------------------------------- |
| `../data/`   | Contains the raw and cleaned JobStreet datasets            |
| `../p1/`     | Contains the crawler, cleaning, and optimization notebooks |
| `../report/` | Contains the final project report                          |

---

## 📝 Note

The benchmark results were collected for academic performance evaluation purposes. Results may vary depending on the dataset size, runtime environment, and available computing resources.

