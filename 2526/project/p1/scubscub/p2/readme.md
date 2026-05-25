<h1 align="center">
  Group scubscub — Performance Comparison
  <br>
  Pandas vs Polars vs PyArrow
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>IMAN ABADI BIN MOHD NIZWAN</td>
    <td>A23CS0084</td>
  </tr>
  <tr>
    <td width=80%>MOHAMED ALIF FATHI BIN ABDUL LATIF</td>
    <td>A23CS0112</td>
  </tr>
  <tr>
    <td width=80%>DHESHIEGHAN A/L SARAVANA MOORTHY</td>
    <td>A23CS0072</td>
  </tr>
</table>

<br>

<h3 align="center">Libraries Compared</h3>
<p align="center">
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas">
  &nbsp;
  <img src="https://img.shields.io/badge/polars-0075FF?style=for-the-badge&logo=polars&logoColor=white" alt="polars">
  &nbsp;
  <img src="https://img.shields.io/badge/PyArrow-FA7B17?style=for-the-badge&logo=apache&logoColor=white" alt="PyArrow">
</p>

## Purpose

This folder holds the **benchmark outputs and visualisation** for the cleaned BookXcess dataset. The benchmark itself is driven by [`../p1/optimize_pipeline.ipynb`](../p1/optimize_pipeline.ipynb), which executes the same six operations across Pandas, Polars, and PyArrow and writes the timing/CPU/memory measurements here. The notebook in this folder consumes those CSVs and produces side-by-side comparison charts.

## Files

| File | Description |
|------|-------------|
| [`performance_before.csv`](performance_before.csv) | **Baseline** — Pandas only, 3 runs × 6 operations + per-operation average row. |
| [`performance_after.csv`](performance_after.csv) | **Optimised** — Pandas + Polars + PyArrow, 3 runs × 6 operations + per-operation average row for each library. |
| [`evaluation_charts.ipynb`](evaluation_charts.ipynb) | Loads both CSVs and renders per-metric comparison charts (matplotlib). |

## Operations Benchmarked

1. Filter High Discount Books
2. GroupBy Publisher Aggregation
3. String Extract Price Tier
4. Calculate Savings
5. Sort by Discount and Price
6. Top Authors by Average Discount

## Metrics Captured

| Metric | Unit | Column in CSV |
|--------|------|---------------|
| Execution time | seconds | `execution_time_sec` |
| CPU utilisation (start) | % | `cpu_initial_percent` |
| CPU utilisation (end) | % | `cpu_final_percent` |
| Memory used | MB | `memory_used_mb` |
| Throughput | rows / second | `throughput_rows_per_sec` |

Each (library, operation) combination is repeated **3 runs** and an `average` row is appended.

## Summary of Findings

Polars achieved the lowest execution time on filter, sort, and groupby operations thanks to its multi-threaded query engine. PyArrow performed strongly on columnar aggregations and string extraction using its compute kernels. The optimised pipeline (Polars + PyArrow) showed a significant reduction in total execution time over the single-threaded Pandas baseline captured in `performance_before.csv`.
