# Assignment 2: Big Data Handling and Optimization Using 2009 Airline On Time Data 
## 👥 Group Members

| Name               | Matric Number |
|--------------------|---------------|
| Muhammad Iman Firdaus Bin Baharuddin        | A22EC0216      |
| Muhammad Ariff Danish Bin Hashnan         | A22EC0204       |

---
## Summary 🚀
This project demonstrates effective strategies for handling and optimizing large-scale data processing using the Airline On-Time Performance dataset (2009) . The dataset, with over 7 million records posed significant challenges for traditional data handling methods. By applying various optimization techniques such as sampling, chunking, and selective column loading, we managed to process the dataset efficiently while minimizing memory usage.

We explored three powerful tools—**Pandas** 🐼 , **Polars** ❄️ , and **Dask** ⚡ —to compare their performance in terms of execution time and memory consumption. Each tool offers unique advantages depending on the specific requirements of the task.

Key techniques implemented include:

- 📥 Loading partial data and columns to reduce memory footprint
- 📚 Processed large files in smaller, manageable chunks to handle datasets that exceed available memory.
- 🧠 Converted columns to appropriate data types to minimize memory consumption without losing data integrity.
- 🎲 Sampling for quick data exploration
- ⚙️ Leveraged Dask for parallel computation, enabling efficient handling of large datasets by distributing tasks across multiple cores.

The comparative analysis shows Polars followed by Dask as the best performer in handling big data efficiently, while Pandas struggles with memory limitations. This underscores the importance of selecting appropriate tools and methods based on dataset size and processing needs.

Overall, this project reinforces best practices in big data handling and provides practical insights for optimizing data workflows in Python 🐍.
