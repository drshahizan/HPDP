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

# Assignment Tasks
## Task1: Dataset Selection <br>
We had select a dataset larger than 700MB from Kaggle which is the Transaction data.<br>
### **Data Details** 
-**Dataset**: Transaction Data <br>
-**Data source**: [Kaggle - Transaction Data](https://www.kaggle.com/datasets/ismetsemedov/transactions) <br>
-**File size**: 2.93GB <br>
-**Data Shape**: (7483766, 24) <br>
-**Domain**: Explore Realistic Patterns in Financial Transactions for Fraud Detection <br>

### Column
-Transaction_id: Unique identifier for each transaction.

-customer_id: Unique identifier for each customer in the dataset.

-card_number: Masked card number associated with the transaction.

-timestamp: Date and time of the transaction.

-merchant_category: General category of the merchant (e.g., Retail, Grocery, Travel).

-merchant_type: Specific type within the merchant category (e.g., "online" for Retail).

-merchant: Name of the merchant where the transaction took place.

-amount: Transaction amount (currency based on the country).

-currency: Currency used for the transaction (e.g., USD, EUR, JPY).

-country: Country where the transaction occurred.

-city: City where the transaction took place.

-city_size: Size of the city (e.g., medium, large).

-card_type: Type of card used (e.g., Basic Credit, Gold Credit).

-card_present: Indicates if the card was physically present during the transaction (used in POS transactions).

-device: Device used for the transaction (e.g., Chrome, iOS App, NFC Payment).

-channel: Type of channel used for the transaction (web, mobile, POS).

-device_fingerprint: Unique fingerprint for the device used in the transaction.

-ip_address: IP address associated with the transaction.

-distance_from_home: Binary indicator showing if the transaction occurred outside the customer's home country.

-high_risk_merchant: Indicates if the merchant category is known for higher fraud risk (e.g., Travel, Entertainment).

-transaction_hour: Hour of the day when the transaction was made.

-weekend_transaction: Boolean indicating if the transaction took place on a weekend.

-velocity_last_hour:
Dictionary containing metrics on the transaction velocity, including:
num_transactions: Number of transactions in the last hour for this customer.
total_amount: Total amount spent in the last hour.
unique_merchants: Count of unique merchants in the last hour.
unique_countries: Count of unique countries in the last hour.
max_single_amount: Maximum single transaction amount in the last hour.

-is_fraud: Binary indicator showing if the transaction is fraudulent (True for fraudulent transactions, False for legitimate ones).
## Task 2: Load and Inspect Data <br>
To start working with our dataset, we used Pandas, a popular Python library for data analysis. We loaded the full CSV file using pandas.read_csv() and understand what kind of data it has. We looked at the number of rows and columns (called the shape), the names of the columns, and the data types for each column.
