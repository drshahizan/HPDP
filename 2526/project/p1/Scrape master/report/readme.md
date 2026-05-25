# Final Report and Presentation Slides

This folder holds the project's written deliverables: the final report (PDF) and the presentation slides (PPTX). Both summarise the full pipeline — from web crawling Carousell.com.my through cleaning the dataset to benchmarking four data-processing libraries — and explain how the four assessment metrics (time, CPU, memory, throughput) were measured.

## Course details

| Field | Value |
|---|---|
| **Course**         | SECP3133-01 Pemprosesan Data Berprestasi Tinggi (High Performance Data Processing) |
| **Project**        | Project 1 — Optimizing High Performance Data Processing for Large Scale Web Crawlers |
| **Lecturer**       | Mohd Shahizan bin Othman |

## Group members

| # | Name | Matric No. |
|---|---|---|
| 1 | Muhammad Adam bin Razali  | A23CS0116 |
| 2 | Afif Shaqir Irfan bin Arqam | A23CS0204 |
| 3 | Pravinraj a/l Sivabathi    | A23CS0171 |

## Report structure

The final report follows the structure recommended in 7.3 of the assignment brief.

| # | Section | What it covers |
|---|---|---|
| 1  | **Introduction**                       | Background, motivation, target website (Carousell.com.my), and a one-paragraph summary of what the project produced |
| 2  | **Project Objectives**                 | Four numbered objectives covering crawling, cleaning, HPC techniques, and quantitative evaluation |
| 3  | **System Design and Architecture**     | Five-layer system architecture diagram, tools and frameworks diagram, tools summary |
| 4  | **Data Collection**                    | Target website, crawling strategy (infinite scroll, "Show more" button, stale-page detection), multi-threaded architecture, data fields collected, ethical considerations |
| 5  | **Data Cleaning and Processing**       | Observed quality issues, the 10-step cleaning pipeline, output data structure |
| 6  | **Optimization Techniques**            | Benchmarking design, code implementation, per-operation breakdown of the four library implementations |
| 7  | **Performance Evaluation**             | Per-operation results (Time, CPU, Peak Memory, Throughput) and per-metric cross-operation results |
| 8  | **Challenges and Limitations**         | Bot detection, dynamic page structure, thread safety, browser overhead, PySpark startup cost, relative-timestamp imprecision |
| 9  | **Conclusion**                         | Project-wide summary and recommendation (Polars as the best library for this dataset size) |
| 10 | **Future Work**                        | Scaling the dataset, real-time crawling, smarter anti-bot handling, analytical dashboards |
