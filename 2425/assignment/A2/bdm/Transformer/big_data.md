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
Instead of loading the entire dataset, we only picked the columns or rows we needed. This is helpful when we don’t need all the data detail. <br><br>
**Example**: We used the usecols argument in read_csv() to load only a few important columns. <br><br>
**Code Snippets**-
![image](https://github.com/user-attachments/assets/9f22722a-0452-4f58-a72e-0a3d0e36dc29)

### 📦 2. Use Chunking
Since the dataset is very large, we didn’t load all at once. Instead, we read it in smaller parts with chunks. This prevents the system from crashing or running out of memory. <br><br>
**Example**: We used chunksize=100000 to read 100,000 rows into chunk at a time using pandas.read_csv(chunksize=...). <br><br>
**Code Snippets**-
![image](https://github.com/user-attachments/assets/8ec7d86e-5939-416b-baa1-04272642ba81)

### 🧮 3. Optimize Data Types
Some columns take up more space than they need. So, We changed their data types to smaller or more efficient ones. This can helped reduce the memory used by the dataset. <br><br>
**Example**: We converted strings with repeated values into category type, and used float32 instead of float64.
Convert columns to appropriate types (e.g., category, float32) to reduce memory usage.<br><br>
**Code Snippets**-<br>
![image](https://github.com/user-attachments/assets/a12e48ac-519d-40c0-a735-514e076421df)

### 🔍 4. Sampling
We are using random sampling to reduce the dataset size. So, We took a smaller random portion of the dataset to test our code quickly without waiting too long. This is great for trying things out before working with the full dataset.<br><br>
**Example**: We used .sample(frac=0.1) to get 10% of the data, we used skip that help randomly select only a portion of the dataset and skip the rest when loading.<br><br>
**Code Snippets**-<br>
![image](https://github.com/user-attachments/assets/edcaa089-243e-45ba-bd63-6fdccb3f8e23)

## 📊 Task4 : Comparative Analysis
### Part1
In this part, we compare the performance of optimized strategies we used earlier in handling large dataset. These optimized methods include:

1. Load less dsata (Loading only selected columns)

2. Use chunk (Reading the data in small chunks)

3. Optimize data types (Changing data types to save memory)

4. Sampling (Using a smaller sample of the data)

We focus on comparing:

**Memory usage**: How much RAM is used when reading the data

**Execution time**: How long it takes to load or process the data

