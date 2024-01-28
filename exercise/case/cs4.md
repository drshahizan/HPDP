<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/issues"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/Python_Tutorial?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

Don't forget to hit the :star: if you like this repo.

# Case Study 4: Airline Flight Data Analysis

## Introduction

Airline flight data is a valuable source of information for various stakeholders, such as airlines, airports, regulators, travelers, etc. The analysis of airline flight data can provide insights into the performance, efficiency, safety, and customer satisfaction of the aviation industry. However, airline flight data analysis poses many challenges, such as:

- The data is large and complex, involving millions of flights and hundreds of variables, such as departure and arrival times, delays, cancellations, routes, distances, carriers, etc.
- The data is dynamic and evolving, requiring frequent updates and revisions, as well as historical and predictive analysis.
- The data is noisy and incomplete, containing errors, outliers, and missing values, due to various factors, such as weather, mechanical issues, human errors, etc.
- The data is heterogeneous and diverse, reflecting different geographic, temporal, and operational factors, as well as different data sources and formats.

To address these challenges, high performance data processing and exploratory data analysis (EDA) are essential. High performance data processing is the process of analyzing large and complex data sets using advanced techniques and tools. EDA is a subfield of data processing that focuses on discovering patterns, trends, and outliers in the data, often using visual methods. EDA can help to generate hypotheses, identify data quality issues, and guide further analysis.

In this case study, we will demonstrate how high performance data processing and EDA can be applied to airline flight data analysis, using a 10GB data set from the U.S. Bureau of Transportation Statistics (BTS) , which contains domestic flight information for the year 2019. We will also discuss the benefits and challenges of using cloud computing for data processing and EDA, as well as the ethical and social implications of airline flight data analysis.

## Data Sources and Cloud Platform

The airline flight data that we will use for this case study comes from the BTS website , which provides monthly data files in CSV format, containing information on domestic flights operated by U.S. air carriers. The data files include variables such as:

- FL_DATE: Flight date
- OP_CARRIER: Operating carrier code
- OP_CARRIER_FL_NUM: Flight number
- ORIGIN: Origin airport code
- DEST: Destination airport code
- CRS_DEP_TIME: Scheduled departure time
- DEP_TIME: Actual departure time
- DEP_DELAY: Departure delay in minutes
- TAXI_OUT: Taxi out time in minutes
- WHEELS_OFF: Wheels off time
- WHEELS_ON: Wheels on time
- TAXI_IN: Taxi in time in minutes
- CRS_ARR_TIME: Scheduled arrival time
- ARR_TIME: Actual arrival time
- ARR_DELAY: Arrival delay in minutes
- CANCELLED: Cancellation indicator
- CANCELLATION_CODE: Cancellation code
- DIVERTED: Diversion indicator
- CRS_ELAPSED_TIME: Scheduled elapsed time in minutes
- ACTUAL_ELAPSED_TIME: Actual elapsed time in minutes
- AIR_TIME: Flight time in minutes
- DISTANCE: Distance in miles
- CARRIER_DELAY: Carrier delay in minutes
- WEATHER_DELAY: Weather delay in minutes
- NAS_DELAY: National Air System delay in minutes
- SECURITY_DELAY: Security delay in minutes
- LATE_AIRCRAFT_DELAY: Late aircraft delay in minutes

The data set contains 7,665,648 records and 109 variables, with a total size of 10GB. Therefore, we need a high performance data processing platform that can handle the data efficiently and scalably.

For this case study, we will use the Amazon Web Services (AWS)  as our cloud-based platform for data processing and EDA. AWS is a suite of cloud services that provides various solutions for data storage, processing, analysis, and visualization. AWS offers many benefits for data processing and EDA, such as:

- Scalability: AWS can scale up or down the resources (such as CPU, memory, disk, etc.) according to the data size and complexity, ensuring optimal performance and cost-effectiveness.
- Flexibility: AWS can support various data formats, sources, and destinations, allowing seamless integration and transformation of the data.
- Reliability: AWS can ensure high availability and durability of the data, as well as backup and recovery options in case of failures or disasters.
- Security: AWS can protect the data from unauthorized access and malicious attacks, using encryption, authentication, and authorization mechanisms.
- Collaboration: AWS can enable collaboration and sharing of the data and results among multiple users and teams, using cloud-based tools and frameworks.

However, AWS also poses some challenges for data processing and EDA, such as:

- Complexity: AWS can be complex and overwhelming for beginners, requiring familiarity with the concepts, terminologies, and architectures of cloud computing, as well as the specific features and functionalities of AWS services and tools.
- Compatibility: AWS can have compatibility issues with some existing tools and frameworks, requiring adaptation or migration of the code and data.
- Privacy: AWS can raise privacy concerns, as the data is stored and processed in remote servers that may be subject to different laws and regulations, as well as potential breaches or leaks.

## Data Processing and EDA Tools and Frameworks

To perform data processing and EDA on AWS, we will use various tools and frameworks that are compatible and integrated with AWS services. The main tools and frameworks that we will use are:

- Amazon Simple Storage Service (S3) : S3 is a service that provides scalable and durable object storage for any type of data. We will use S3 to store the raw and processed airline flight data in CSV format, as well as the intermediate and final results of the data processing and EDA.
- Amazon Elastic MapReduce (EMR) : EMR is a service that provides managed clusters of virtual machines (VMs) that can run Apache Spark  and Apache Hadoop  applications. Spark and Hadoop are open-source frameworks that enable distributed and parallel processing of large-scale data, using various libraries and modules for data ingestion, transformation, analysis, and output. We will use EMR to create and manage Spark and Hadoop clusters, and run Spark applications for data processing and EDA on the airline flight data.
- Amazon SageMaker (SM) : SM is a service that provides a fully managed platform for machine learning and data science. SM allows users to write and execute Python code, as well as interact with the data and results using notebooks, scripts, or APIs. SM is integrated with AWS and can access S3 and EMR resources, as well as other AWS services and tools. We will use SM to write and run Python code for data processing and EDA on the airline flight data, using various libraries and packages, such as pandas , numpy , matplotlib , seaborn , etc. Pandas is a library that provides high-performance data structures and operations for manipulating and analyzing tabular data. Numpy is a library that provides efficient numerical computation and linear algebra operations for multidimensional arrays. Matplotlib and seaborn are libraries that provide various data visualization techniques, such as charts, graphs, maps, etc.
- Amazon QuickSight (QS) : QS is a service that provides interactive and customizable dashboards and reports for data visualization and exploration. QS can connect to various data sources, such as S3, EMR, SM, and other AWS services and tools, as well as external sources, such as CSV files, databases, etc. We will use QS to create and share dashboards and reports for airline flight data analysis, using various widgets and features, such as charts, tables, filters, etc.

## Data Processing and EDA Workflow

The workflow for data processing and EDA on the airline flight data using AWS and the tools and frameworks mentioned above is as follows:

- Data Ingestion: We will download the airline flight data from the BTS website in CSV format, and upload them to S3 buckets, using the S3 web console or the aws command-line tool . We will also create an EMR cluster, using the EMR web console or the aws command-line tool , and configure it to access the S3 buckets and run Spark applications.
- Data Transformation: We will write and run Spark applications on the EMR cluster, using SM notebooks and the PySpark API , to transform the airline flight data from CSV format to Spark DataFrames , which are distributed and resilient data structures that can be manipulated and analyzed using various operations and functions. We will also perform data cleaning, preprocessing, and transformation tasks, such as:

    - Filtering and selecting the relevant variables and records for the data analysis, such as departure and arrival times, delays, cancellations, routes, distances, carriers, etc.
    - Handling missing values, outliers, and errors in the data, using various strategies, such as imputation, interpolation, deletion, etc.
    - Creating new variables and features from the existing ones, such as calculating the average speed, the on-time performance, the delay causes, etc.
    - Aggregating and summarizing the data at different levels of granularity, such as month, day, hour, airport, carrier, etc.

- Data Analysis: We will write and run Python code on SM notebooks, using various libraries and packages, such as pandas, numpy, matplotlib, seaborn, etc., to perform data analysis on the airline flight data, such as:

    - Exploring the descriptive statistics and distributions of the variables and features, such as mean, median, standard deviation, skewness, kurtosis, etc.
    - Visualizing the trends and patterns of the variables and features over time and space, using various charts, graphs, maps, etc.
    - Comparing and contrasting the variables and features across different groups and categories, such as months, days, hours,

### Question:
- What are the main advantages of using Amazon Web Services (AWS) for high performance data processing and EDA?
- What are the main challenges of using Amazon Web Services (AWS) for high performance data processing and EDA?
- How does Amazon Simple Storage Service (S3) provide scalable and durable object storage for the airline flight data?
- How does Amazon Elastic MapReduce (EMR) provide managed clusters of virtual machines (VMs) that can run Apache Spark and Apache Hadoop applications?
- How does Amazon SageMaker (SM) provide a fully managed platform for machine learning and data science?
- How does Spark enable distributed and parallel processing of large-scale data, using various libraries and modules for data ingestion, transformation, analysis, and output?
- How does pandas provide high-performance data structures and operations for manipulating and analyzing tabular data?

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)
