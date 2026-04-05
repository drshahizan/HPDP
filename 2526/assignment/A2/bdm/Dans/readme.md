# 📊 Assignment 2: Mastering Big Data Handling 🚀

**Course:** *HPDP SECP3133-01*

---

### 🧑‍🤝‍🧑 Group Members

| Name                               | Matric Number |
|------------------------------------|---------------|
| MUHAMMAD DANIAL BIN AHMAD SYAHIR  | A22EC0206 |
| MUHAMMAD ANAS BIN MOHD PIKRI      | A21SC0464 |



---

### 🌟 Introduction

Handling large-scale datasets presents real-world challenges, especially when the data exceeds system memory.  
This project explores efficient techniques for working with such datasets using information derived from the anime and entertainment domain.

We start by applying foundational strategies using **Pandas**, including:

- 🚪 Loading only the necessary columns to reduce memory overhead  
- 📦 Processing data in chunks for better memory management  
- 🧠 Converting data types to more memory-efficient formats  
- 🎯 Using samples of the dataset for quicker testing and exploration

We then shift to more scalable solutions like **Dask** and **Polars**, assessing their ability to handle big data operations with better performance and parallel processing support.


---

### 🎌 Dataset Overview

**📂 Dataset:** MyAnimeList Dataset 2023  
**🔗 Source:** [📦 Kaggle Dataset](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset)

| Feature     | Description                                                      |
|-------------|------------------------------------------------------------------|
| 💾 Size     | ~4GB (CSV)                                                       |
| 📈 Records  | Thousands of anime titles + user interaction logs                |
| 🎭 Domain   | Anime, Entertainment, Streaming                                  |
| 📊 Use Case | Recommendation, Popularity, Ratings, Demographic Analysis       |
| ✅ Reason    | Real-world size and diversity make it ideal for scalability tests|

---

### 🛠️ Libraries Used (Phase 1)

| Library     | Purpose                                      |
|-------------|----------------------------------------------|
| `pandas`    | Traditional DataFrame operations             |
| `time`      | Performance benchmarking                     |
| `gc`        | Garbage collection to manage memory          |
| `dask`      | Parallel, out-of-core computation            |
| `polars`    | High-speed DataFrame operations (Rust-backed)|
| `psutil`    | Memory tracking                              |
| `matplotlib`, `seaborn` | Data visualization and analysis  |

---

### 🔍 Project Navigation

| Resource             | Description                             | Link                                                              |
|----------------------|-----------------------------------------|-------------------------------------------------------------------|
| 📄 **Main Report**    | Full analysis, comparison, and summary  | [big_data.md](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/Dans/big_data.md)|
| 📓 **Notebook Code**  | Full implementation in Colab            | [Open in Colab ▶️](https://colab.research.google.com/drive/1ztlLQDrfvT1gRwekZ3E_5p93nWnl6QrO?usp=sharing)|
| 📦 **Dataset Source** | Original dataset on Kaggle              | [Go to Dataset](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset) |

---

### 🔧 Project Outcomes

- Identified limitations of Pandas on large-scale data
- Applied chunking, sampling, and optimization for efficient processing
- Successfully benchmarked Dask and Polars for time and memory
- Delivered clean, scalable workflows for big data analysis

---

### 🎓 Instructor Info

**Lecturer**: Dr. Mohd Shahizan Othman  
**Course**: High Performance Data Processing *(SECP3133)*  
**Institution**: Universiti Teknologi Malaysia

---

> ✨ *Built with 💻 Python, 🔍 curiosity, and ⚙️ performance-driven mindset.*

