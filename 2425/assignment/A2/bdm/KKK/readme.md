# 📚Assignment 2:  Mastering Big Data Handling🚀

## Group Name: KKK
👨‍💻 Group Members
- KOH LI HUI (A22EC0059)
- KOH SU XUAN (A22EC0060)

### Project Description
This project focuses on Mastering Big Data Handling using Python. We explore various strategies and libraries to efficiently process and analyze large datasets that exceed typical memory capacities.

### 📊 Data Details
- **Source:** https://www.kaggle.com/datasets/perkymaster/school-donations?select=Projects.csv
- **Dataset Name:** School Donation Dataset
- **Size:** 2.57 GB _(The Projects.csv file is 2452.40 MB)_
- **Domain:** Education/Non-profit Funding, specifically teacher project proposals on the DonorsChoose.org platform.
- **Number of Records:** The _Projects.csv_ file contains 1,110,017 records (rows).
- **Description:** This dataset comprises teacher project proposals submitted to DonorsChoose.org, including various attributes about teachers, schools, and the project requests themselves. Its large size makes it suitable for automating the screening process for these proposals.

### ✨ Key Highlights 
- **Strategies for Efficiency:** We implemented and benchmarked techniques like **loading less data** (selecting essential columns), **chunking** (processing data in smaller parts), **optimizing data types** (converting to more memory-efficient formats), **sampling** (using representative subsets), and **parallel processing with Dask** for out-of-core computations.
- **Library Performance:** We conducted a comparative analysis of **Pandas** (as a baseline), **Polars** (a high-performance Rust-based DataFrame library), and **Dask** (for scalable, parallel computing) to evaluate their speed, memory usage, and suitability for large datasets.

### What's Inside?
| File Name                     | Description                                | Link |
|------------------------------|--------------------------------------------|------|
| **big_data.md**  |A detailed overview of the project, including the strategies explored, performance comparisons, and key takeaways.| [![Markdown](https://img.shields.io/badge/Read-MD-lightgrey?logo=markdown&logoColor=black)](2425/assignment/A2/bdm/KKK/big_data.md)|
|**big_data.ipynb**| The annotated Google Colab notebook containing all the working code implementations, step-by-step analysis, and outputs for each strategy and library comparison.|[![Jupyter](https://img.shields.io/badge/Open-Jupyter-orange?logo=jupyter&logoColor=white)](https://github.com/username/repo/blob/main/notebook.ipynb)|
|**HPDP Assignment 2 Report.pdf**|The comprehensive academic report detailing the introduction, dataset selection, detailed implementation code and results, performance comparison, discussion, conclusion, and reflections.|[![Report](https://img.shields.io/badge/View-Report-blue?logo=readthedocs&logoColor=white)](https://github.com/username/repo/blob/main/report.pdf)
|
**Dive in and explore how we tackled the challenges of big data!**
