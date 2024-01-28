<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/issues"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/Python_Tutorial?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Case Study 5: How Walmart Uses Big Data to Optimize Its Pricing Strategy

## Introduction

Walmart is the world's largest retailer, operating more than 11,000 stores in 27 countries, serving over 260 million customers every week. Walmart's mission is to save people money so they can live better, and one of the key factors that enables Walmart to offer low prices is its pricing strategy. Walmart's pricing strategy is based on the principle of everyday low prices (EDLP), which means that Walmart offers consistent and competitive prices across its products and categories, rather than relying on frequent promotions and discounts. Walmart's pricing strategy is also dynamic and responsive, which means that Walmart adjusts its prices according to various factors, such as market conditions, customer demand, competitor actions, and product availability.

However, Walmart's pricing strategy poses many challenges, such as:

- The data is large and complex, involving millions of products and categories, as well as multiple channels, such as online, in-store, and mobile.
- The data is dynamic and evolving, requiring real-time updates and revisions, as well as historical and predictive analysis.
- The data is noisy and incomplete, containing errors, outliers, and missing values, due to various factors, such as human errors, system failures, etc.
- The data is heterogeneous and diverse, reflecting different geographic, demographic, and behavioral factors, as well as different data sources and formats.

To address these challenges, Walmart uses big data to optimize its pricing strategy, using advanced techniques and tools. Big data refers to the vast amount of data that is generated from various sources, both structured and unstructured. It encompasses the volume, velocity, and variety of data and includes information from sales transactions, customer interactions, competitor actions, product attributes, etc. The term “big data” is derived from the immense size of datasets that cannot be easily managed or processed using traditional data processing methods. However, with advancements in technology and data analytics, businesses can now harness the power of big data to derive actionable insights and make data-driven decisions.

In this case study, we will explore how Walmart uses big data to optimize its pricing strategy, using a 10GB data set from Walmart's online channel, which contains information on product prices, sales, ratings, reviews, etc. We will also discuss the benefits and challenges of using big data for pricing optimization, as well as the ethical and social implications of big data in retail.

## Data Sources and Cloud Platform

The data set that we will use for this case study comes from Walmart's online channel, which provides customers with the option to shop online and get their products delivered or pick them up at the store. The data set contains 10GB of data, with 50 million records and 20 variables, such as:

- ITEM_ID: Unique identifier for each product
- ITEM_NAME: Name of the product
- ITEM_CATEGORY: Category of the product
- ITEM_PRICE: Price of the product
- ITEM_SALES: Number of units sold
- ITEM_RATING: Average rating of the product
- ITEM_REVIEWS: Number of reviews of the product
- ITEM_DATE: Date of the data record
- COMPETITOR_NAME: Name of the competitor
- COMPETITOR_PRICE: Price of the competitor's product

The data set is in CSV format, which can be easily downloaded and processed. However, the data is also large and complex, involving millions of products and categories, as well as multiple factors that affect the pricing strategy, such as customer demand, competitor actions, product availability, etc. Therefore, we need a high performance data processing platform that can handle the data efficiently and scalably.

For this case study, we will use Microsoft Azure  as our cloud-based platform for data processing and EDA. Azure is a suite of cloud services that provides various solutions for data storage, processing, analysis, and visualization. Azure offers many benefits for data processing and EDA, such as:

- Scalability: Azure can scale up or down the resources (such as CPU, memory, disk, etc.) according to the data size and complexity, ensuring optimal performance and cost-effectiveness.
- Flexibility: Azure can support various data formats, sources, and destinations, allowing seamless integration and transformation of the data.
- Reliability: Azure can ensure high availability and durability of the data, as well as backup and recovery options in case of failures or disasters.
- Security: Azure can protect the data from unauthorized access and malicious attacks, using encryption, authentication, and authorization mechanisms.
- Collaboration: Azure can enable collaboration and sharing of the data and results among multiple users and teams, using cloud-based tools and frameworks.

However, Azure also poses some challenges for data processing and EDA, such as:

- Complexity: Azure can be complex and overwhelming for beginners, requiring familiarity with the concepts, terminologies, and architectures of cloud computing, as well as the specific features and functionalities of Azure services and tools.
- Compatibility: Azure can have compatibility issues with some existing tools and frameworks, requiring adaptation or migration of the code and data.
- Privacy: Azure can raise privacy concerns, as the data is stored and processed in remote servers that may be subject to different laws and regulations, as well as potential breaches or leaks.

## Data Processing and EDA Tools and Frameworks

To perform data processing and EDA on Azure, we will use various tools and frameworks that are compatible and integrated with Azure services. The main tools and frameworks that we will use are:

- Azure Blob Storage (ABS) : ABS is a service that provides scalable and durable object storage for any type of data. We will use ABS to store the raw and processed data set in CSV format, as well as the intermediate and final results of the data processing and EDA.
- Azure Databricks (ADB) : ADB is a service that provides a unified platform for data engineering, data science, and machine learning. ADB allows users to write and execute code, as well as interact with the data and results using notebooks, scripts, or APIs. ADB is integrated with Azure and can access ABS and other Azure services and tools. We will use ADB to write and run code for data processing and EDA on the data set, using various libraries and packages, such as PySpark , pandas , numpy , matplotlib , seaborn , etc. PySpark is a Python API for Spark, which is an open-source framework that enables distributed and parallel processing of large-scale data, using various libraries and modules for data ingestion, transformation, analysis, and output. Pandas is a library that provides high-performance data structures and operations for manipulating and analyzing tabular data. Numpy is a library that provides efficient numerical computation and linear algebra operations for multidimensional arrays. Matplotlib and seaborn are libraries that provide various data visualization techniques, such as charts, graphs, maps, etc.
- Azure Machine Learning (AML) : AML is a service that provides a comprehensive platform for machine learning and data science. AML allows users to build, train, deploy, and manage machine learning models, as well as perform data analysis and experimentation. AML is integrated with Azure and can access ABS, ADB, and other Azure services and tools. We will use AML to build and train machine learning models for pricing optimization, using various algorithms and frameworks, such as linear regression , random forest , TensorFlow , etc. Linear regression is a supervised learning algorithm that models the relationship between a dependent variable and one or more independent variables. Random forest is a supervised learning algorithm that builds a collection of decision trees and aggregates their predictions. TensorFlow is an open-source framework that provides a platform for building and deploying machine learning models, using various tools and libraries.
- Azure Power BI (PBI) : PBI is a service that provides interactive and customizable dashboards and reports for data visualization and exploration. PBI can connect to various data sources, such as ABS, ADB, AML, and other Azure services and tools, as well as external sources, such as CSV files, databases, etc. We will use PBI to create and share dashboards and reports for data analysis and pricing optimization, using various widgets and features, such as charts, tables, filters, etc.

## Data Processing and EDA Workflow

The workflow for data processing and EDA on the data set using Azure and the tools and frameworks mentioned above is as follows:

- Data Ingestion: We will download the data set from Walmart's online channel in CSV format, and upload it to ABS, using the ABS web console or the az command-line tool . We will also create an ADB cluster, using the ADB web console or the az command-line tool , and configure it to access the ABS and run code.
- Data Transformation: We will write and run code on the ADB cluster, using ADB notebooks and the PySpark API , to transform the data set from CSV format to Spark DataFrames , which are distributed and resilient data structures that can be manipulated and analyzed using various operations and functions. We will also perform data cleaning, preprocessing, and transformation tasks, such as:

    - Filtering and selecting the relevant variables and records for the data analysis and pricing optimization, such as item price, item sales, item rating, item reviews, competitor price, etc.
    - Handling missing values, outliers, and errors in the data, using various strategies, such as imputation, interpolation, deletion, etc.
    - Creating new variables and features from the existing ones, such as calculating the price elasticity, the price index, the price gap, etc.
    - Aggregating and summarizing the data at different levels of granularity, such as item, category, channel, etc.

**Source:** 
- (1) [Big Data Case Study on Walmart | PPT - SlideShare.](https://www.slideshare.net/JainamParikh3/big-data-case-study-on-walmart)
- (2) [How Walmart Uses Big Data | Robots.net](https://robots.net/fintech/how-walmart-uses-big-data/)
- (3) [Big Data and Decision Making Techniques: A Case Study of Walmart - Desklib](https://desklib.com/document/walmart-big-data-case-study/)
- (4) [Walmart Data Analysis Using Machine Learning](https://ijcrt.org/papers/IJCRT2307693.pdf)
- (5) [Walmart's Sales Data Analysis - A Big Data Analytics Perspective | IEEE ...](https://ieeexplore.ieee.org/document/8487274)

### Questions
- What are the benefits and challenges of using Walmart's online channel as a data source for pricing optimization?
- How does Azure Blob Storage (ABS) provide scalable and durable object storage for the data set in CSV format?
- How does Azure Databricks (ADB) provide a unified platform for data engineering, data science, and machine learning?
- How does PySpark enable distributed and parallel processing of large-scale data, using various libraries and modules for data ingestion, transformation, analysis, and output?
- How does pandas provide high-performance data structures and operations for manipulating and analyzing tabular data?
- How does machine learning and artificial intelligence enhance data processing and EDA, such as feature engineering, dimensionality reduction, anomaly detection, etc.?
- How does big data in retail raise ethical and social implications, such as privacy, security, bias, fairness, etc.?

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
