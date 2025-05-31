# <div align='center'>📘 Assignment 2: Mastering Big Data Handling</div>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>TIEW CHUAN RONG</td>
    <td>A22EC0112</td>
  </tr>
  <tr>
    <td width=80%>DANIAL HARRIZ BIN MOHD ASINEH @MOHD ASNEH</td>
    <td>A22EC0152</td>
  </tr>
</table>
<br>

# 📝 Assignment Tasks

## 📂 Task 1: Dataset Selection  
We selected a dataset larger than 700MB from Kaggle which is the Transaction data. Below show the details of the data and description of the column of the dataset:  

### 📊 Data Details
- **Dataset**: Transaction Data  
- **Data source**: [Kaggle - Transaction Data](https://www.kaggle.com/datasets/ismetsemedov/transactions)  
- **File size**: 2.93GB  
- **Data Shape**: (7,483,766 rows, 24 columns)  
- **Domain**: Explore Realistic Patterns in Financial Transactions for Fraud Detection  

### 🧾 Dataset Column Descriptions
Below is a detailed breakdown of the columns in the file:

| Column Name           | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| transaction_id        | Unique identifier for each transaction.                                     |
| customer_id           | Unique identifier for each customer in the dataset.                         |
| card_number           | Masked card number associated with the transaction.                         |
| timestamp             | Date and time of the transaction.                                           |
| merchant_category     | General category of the merchant (e.g., Retail, Grocery, Travel).           |
| merchant_type         | Specific type within the merchant category (e.g., "online" for Retail).     |
| merchant              | Name of the merchant where the transaction took place.                      |
| amount                | Transaction amount (currency based on the country).                         |
| currency              | Currency used for the transaction (e.g., USD, EUR, JPY).                    |
| country               | Country where the transaction occurred.                                     |
| city                  | City where the transaction took place.                                      |
| city_size             | Size of the city (e.g., medium, large).                                     |
| card_type             | Type of card used (e.g., Basic Credit, Gold Credit).                        |
| card_present          | Whether the card was physically present during the transaction.             |
| device                | Device used for the transaction (e.g., Chrome, iOS App, NFC Payment).       |
| channel               | Type of channel used (web, mobile, POS).                                    |
| device_fingerprint    | Unique fingerprint for the device used in the transaction.                  |
| ip_address            | IP address associated with the transaction.                                 |
| distance_from_home    | Whether the transaction occurred outside the customer's home country.       |
| high_risk_merchant    | Indicates if the merchant is in a high-fraud-risk category.                 |
| transaction_hour      | Hour of the day when the transaction occurred.                              |
| weekend_transaction   | Indicates if the transaction took place on a weekend.                       |
| velocity_last_hour    | Dictionary with metrics on recent transactions:                             |
| └─ num_transactions   | └─ Number of transactions in the last hour.                                 |
| └─ total_amount       | └─ Total amount spent in the last hour.                                     |
| └─ unique_merchants   | └─ Number of unique merchants in the last hour.                             |
| └─ unique_countries   | └─ Number of unique countries in the last hour.                             |
| └─ max_single_amount  | └─ Maximum single transaction amount in the last hour.                      |
| is_fraud              | Whether the transaction was fraudulent (True or False).                     |

---

## 🔍 Task 2: Load and Inspect Data  
To start working with our dataset, we used **Pandas**, a popular Python library for data analysis.  
We loaded the full CSV file using `pandas.read_csv()` and looked at:
- the number of rows and columns (shape) <br>
  (74383766, 24) : (rows, columns)

- the names of the columns
![image](https://github.com/user-attachments/assets/c2113dfd-04d9-4b33-98fc-c5b6cb8a5c51)


- the data types for each column.<br>
  ![image](https://github.com/user-attachments/assets/5cfbde8f-be11-4fb2-9a8c-0b294439ce13)<br>

This step helped us understand what kind of data we are working with and prepared for further data handling tasks.

## 🛠️Task 3: Apply Big Data Handling Strategies
In this part, we used five strategies to work with our large dataset to observe the result of the performance of using different strategies applying to handle big dataset. These methods help save time, memory, and make processing faster. <br><br>
We apply the following five strategies to our dataset: <br>

### 📉 1. Load Less Data
Instead of loading the entire dataset, we only picked the columns or rows we needed. This is helpful when we don’t need all the data detail. <br><br>
**Example**: We used the usecols argument in read_csv() to load only a few important columns. <br><br>
**Code Snippets**-
![image](https://github.com/user-attachments/assets/f477cb31-7313-45b5-9296-adc1e726b9ec)

<br><br>**Outputs**-<br>
![image](https://github.com/user-attachments/assets/9c63f2f7-df67-4ab5-b0ae-15138b510185)



### 📦 2. Use Chunking
Since the dataset is very large, we didn’t load all at once. Instead, we read it in smaller parts with chunks. This prevents the system from crashing or running out of memory. <br><br>
**Example**: We used chunksize=100000 to read 100,000 rows into chunk at a time using pandas.read_csv(chunksize=...). 

<br><br>**Code Snippets**-
![image](https://github.com/user-attachments/assets/ee2b9f74-16f5-40da-bc97-7d43cce5825b)

<br><br>**Outputs**-<br>
![image](https://github.com/user-attachments/assets/61bd6233-12ac-4cb4-9ea9-f605acfae0cb)



### 🧮 3. Optimize Data Types
Some columns take up more space than they need. So, We changed their data types to smaller or more efficient ones. This can helped reduce the memory used by the dataset. <br><br>
**Example**: We converted strings with repeated values into category type, and used float32 instead of float64.
Convert columns to appropriate types (e.g., category, float32) to reduce memory usage.<br><br>

**Code Snippets**-<br>
![image](https://github.com/user-attachments/assets/9b070d6e-3ae0-4af5-867c-a32a2f4dd12d)

<br><br>**Outputs**-<br>
![image](https://github.com/user-attachments/assets/da97ef81-c567-4b38-aa3d-9eb4edadd410)


### 🔍 4. Sampling
We are using random sampling to reduce the dataset size. So, We took a smaller random portion of the dataset to test our code quickly without waiting too long. This is great for trying things out before working with the full dataset.<br><br>
**Example**: We used .sample(frac=0.1) to get 10% of the data, we used skip that help randomly select only a portion of the dataset and skip the rest when loading.<br><br>

**Code Snippets**-<br>
![image](https://github.com/user-attachments/assets/928bee48-6005-4d16-913b-badc833a6989)

<br><br>**Outputs**-<br>
![image](https://github.com/user-attachments/assets/5a4e091d-35e0-4a13-98e4-1bd4d687c500)



## 📊 Task4 : Comparative Analysis
### Part1: Camparing the performance of different optimized strategies in handling large dataset
In this part, we compare the performance of different optimized strategies we used earlier in handling large dataset. These optimized methods include:

1. Load less data (Loading only selected columns)

2. Use chunk (Reading the data in small chunks)

3. Optimize data types (Changing data types to save memory)

4. Sampling (Using a smaller sample of the data)

We focus on comparing:

**Memory usage**: How much RAM is used when reading the data

**Processing time**: How long it takes to load or process the data <br>

|**Optimized Strategies**|**Processing Time (S)**|**Memory Usage (MB)**|
|------------------------|-------------------|----------------|
| Load less data|62.19|4347.03|
| Use chunk|162.15|48.51|
| Optimize data types |229.73|3981.57|
| Sampling |27.03|906.22|

<br> **Visualization of comparative analysis** <br>
![Untitled](https://github.com/user-attachments/assets/f99c73fc-6753-4437-b902-4480eb49ffc5)


### Part 2: Comparing the performance of using different library or tools to handle large dataset.

To test the the limits and performance across 3 different libraries which are Pandas, Dask, and Polars, we decided on the simplest task which is loading the data. The performance metrics used remain the same which are **Execution Time**, and **Memory Usage**.

Pandas: 
- 

Polars:
-

Dask: 
- 

## 📌 Task 5: Conclusion & Reflection

### Summary of Findings

-   **Polars** is the best in terms of execution time and memory due to its optimized nature.
    
-   **Dask** is useful for distributed or larger-than-memory datasets.
    
-   **Pandas** is easiest to use but is slow and not suitable for large scale data.
    

### Benefits
- In terms of Processing/Execution Time, the **Load Less Data** and **Sampling** technique performed the best.
- In terms of Memory Usage, the **Chunking** and **Sampling** technique consumed the least memory.
- These techniques are applied using the **Pandas** library only.

    

### Limitations



### Learning Reflection

This assignment showed how memory and performance differs between different libraries. This helps us understand which tools to use based on dataset size and task type.


