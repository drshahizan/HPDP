<h1 align="center"> 
  Web Scraping Jobstreet using Beautiful Soup
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>Najma Shakirah binti Shahrulzaman</td>
    <td>A23CS0140</td>
  </tr>
  <tr>
    <td width=80%>Asyikin</td>
    <td>A23CS</td>
  </tr>
  <tr>
    <td width=80%>Harini A/P Sangaran</td>
    <td>A23CS0081</td>
  </tr>
</table>
<br>
<div align='center'>
</div>
<br>

---
## 📂 Project Files

| File Name                     | Description                                | Link |
|------------------------------|--------------------------------------------|------|
| **Raw Dataset**              | Cleaned and raw data with URLs             | [![Download](https://img.shields.io/badge/Download-Drive-blue?logo=google-drive)](https://drive.google.com/file/d/1IsDhWyV1s5ZEcNX4ONSvjBH_eqpXPRZY/view?usp=sharing) |
| **Clean Dataset**            | Preprocessed data ready for use            | [![Download](https://img.shields.io/badge/Download-Drive-blue?logo=google-drive)](https://drive.google.com/file/d/11sVRLCCxbumTktiDYij8E4axO3FkLfOF/view?usp=sharing)|
| **Web Crawler Script**       | Python script to scrape jobstreet       | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](https://colab.research.google.com/drive/1PzGcCcfSxBqYafEWA6kZEVeAabeE_byP?usp=sharing) |
| **Data Cleaning Code**       | Script to clean and preprocess the data    | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](https://colab.research.google.com/drive/1hx2PhnfCMEx_uqwpPN5txIJrtMdq-P7l?usp=sharing) |
| **Optimization Code**        | Performance-optimized transformation code  | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](https://colab.research.google.com/drive/10s659IqvQ9ZlJiorg3izsnTkEVfCnfjS?usp=sharing) |



---

## 📚 Libraries Used

### 🕸️ Web Scraping Libraries


---
### ⚙️ Data Processing & Optimization Libraries


---
## 🛠️ System Architecture
This chapter discusses the overall system architecture and workflow developed for the JobStreet web scraping project. It explains the system layers, tools, and frameworks used for web crawling, data processing, optimisation, and data analysis. In addition, the chapter outlines the responsibilities of each team member throughout the project development process.

<img width="1065" height="1297" alt="ChatGPT Image May 24, 2026, 11_28_44 PM" src="https://github.com/user-attachments/assets/2feacf96-1dee-4d05-869c-988114da7eb6" />

1. Network Layer

The network layer provides secure and reliable communication between the web scraping system and external services. This layer uses cloud services and VPN technology to ensure secure data transmission during scraping operations. Since large-scale web scraping involves handling traffic and frequent HTTP requests, the network layer maintains high throughput and ensures uninterrupted communication with JobStreet.com. This enables the system to collect and process data efficiently in real time. 

2. Presentation Layer

The presentation layer displays the analysed and optimised job market data in a clear and user-friendly format. This layer uses data visualisation techniques such as charts and dashboards to present performance metrics and scraping results which allows users to compare processing time, memory usage, CPU usage and throughput generated from the analysis modules. 

3. Application Layer

a) Web Scraper Module
The web scraper module is responsible for sending HTTP requests to JobStreet.com using the Requests library and extracting relevant job-related information through BeautifulSoup parsing. The module collects data such as countries, job titles, company names, locations, salary, job industry, employment mode and when the jobs were posted in jobstreet. This process enables automated large-scale data collection from the website efficiently.

b) Data Processing Module
The data processing module is responsible for cleaning, validating and transforming the scraped data. Duplicate records, missing or null values are removed, data formats are standardised and data type consistency is ensured so that it is the same across the dataset. The processed data is then stored for optimisation and analytical tasks.

c) Performance Metrics Module
The performance metrics module evaluates the optimisation performance of the scraping workflow. This module calculates the processing time, CPU utilisation, memory consumption and throughput performance. These values are used to compare the efficiency of different optimisation techniques and measure the overall system performance during large-scale data scraping and processing activities.

4. Integration Layer

The integration layer acts as the bridge between system components to ensure interaction across modules. Within this layer, an API Gateway is implemented to manage incoming and outgoing requests between the application modules and the database layer. The API Gateway supports high-volume web scraping activities which improves the overall efficiency of the system architecture.

5. Database Layer

The database layer is responsible for storing and managing both raw and processed data collected from JobStreet.com. The Main Database stores cleaned and transformed datasets for further analysis and visualisation. Google Colab is utilised as a cloud-based environment to host datasets and support large-scale processing activities. The API Endpoint provides controlled access to stored data for external services or future system expansion. This layer ensures organised data management, efficient retrieval and reliable storage of large datasets generated through the web scraping process.


## 🔧 Architecture of Tools and Frameworks Used

<img width="1088" height="991" alt="Gemini_Generated_Image_z0b925z0b925z0b9" src="https://github.com/user-attachments/assets/ca0e3300-68fa-4927-821f-b477c7b59a1a" />

<br>
<br>

Figure 2 shows the overall workflow and system architecture of a web scraping and data analysis pipeline for JobStreet.com. The process begins with the Requests and BeautifulSoup libraries, which are used to scrape data from JobStreet.com. The scraped data is stored as Raw Data containing approximately 130,000 rows and is uploaded in GitHub. Then, the data is cleaned and processed using the pandas library to transform the dataset by removing duplicates, handling missing values, and standardising data types. The cleaned data is then processed in Google Colab, which provides a cloud runtime environment for handling large-scale datasets. Next, the data is optimised and analysed, where different libraries such as pandas, Polars, and DuckDB are tested and compared to evaluate optimisation performance. Finally, the processed data is stored in a database which is then used for data analysis. Data analysis is handled by analysing and comparing processing time, CPU usage, memory usage, and throughput. Data visualisation such as charts and graphical outputs are used to present the analysis.

<br>

| Member Name                        | Task                                                                               | 
|------------------------------------|------------------------------------------------------------------------------------|
| Najma Shakirah Binti Shahrulzaman  | Data cleaning, Documentation for Introduction, Data Processing and Conclusion      |
| Nurul Asyikin Binti Khairul Anuar  | Data Optimization using Pandas, Polars, DuckDB, Documentation for Optimization Techniques, Performance Evaluation and Challenges and Limitations  |
| Harini A/P Sangaran                | Web crawling, Documentation for System Design and Architecture and Data Collection |


## 🔗 Data Details


---

## 📊 Dataset Overview
---
## 📊 Data Description

---
## 🚀 Performance Benchmark

---

### 🕒 Total Processing Time (seconds)

---

### 🧠 CPU Usage (%)

---

### 💾 Memory Usage (MB)

---

### ⚡ Throughput (records/second)

