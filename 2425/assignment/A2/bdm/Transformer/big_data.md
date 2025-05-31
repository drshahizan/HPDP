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
  ![image](https://github.com/user-attachments/assets/2ed1415b-87a4-436c-93f9-6a01a4facafb)

- the names of the columns
  ![image](https://github.com/user-attachments/assets/06b4356e-0007-4262-89f7-2f207b30d7d1)

- the data types for each column.<br>
  ![image](https://github.com/user-attachments/assets/d965020f-0e0e-4de7-9cb1-c8e88cb880db) <br>


This step helped us understand what kind of data we are working with and prepared for further data handling tasks.

## 🛠️Task 3: Apply Big Data Handling Strategies
In this part, we used five strategies to work with our large dataset to observe the result of the performance of using different strategies applying to handle big dataset. These methods help save time, memory, and make processing faster. <br><br>
We apply the following five strategies to our dataset: <br>

### 📉 1. Load Less Data

Load only required columns or filter relevant rows during read operation.
### 📦 2. Use Chunking

Process the data in small chunks using pandas.read_csv(chunksize=...).
### 🧮 3. Optimize Data Types

Convert columns to appropriate types (e.g., category, float32) to reduce memory usage.
### 🔍 4. Sampling

Apply random or stratified sampling to reduce the dataset size for fast prototyping.

### ⚡ 5. Parallel Processing with Dask

Use Dask DataFrame to read and process large files in parallel.


