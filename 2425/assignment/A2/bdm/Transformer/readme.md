# 📘 Assignment 2: Mastering Big Data Handling

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>Tiew Chuan Rong</td>
    <td>A22EC0112</td>
  </tr>
  <tr>
    <td width=80%>DANIAL HARRIZ BIN MOHD ASINEH @MOHD ASNEH</td>
    <td>A22EC0152</td>
  </tr>
</table>
<br>

## Introduction
   In today’s digital world, companies collect a huge amount of data every day. So, it is important to select a efficient technique to handle this huge data. It is because with a correct tool we can load and process data faster and efficiently. This project is about learning how to deal with big data using real tools used by data engineer.
  
   For our project, we chose a large Transaction dataset that’s about 2.93MB in size. This dataset is selecting from kaggle with name 'ismetsemedov/transactions'. It contains records of financial transactions, including things like 'transaction_id', 'customer_id', 'card_number', 'timestamp','merchant_category', 'merchant_type', 'merchant', 'amount', 'currency','country', 'city', 'city_size', 'card_type', 'card_present', 'device','channel', 'device_fingerprint','ip_address', 'distance_from_home', 'high_risk_merchant', 'transaction_hour', 'weekend_transaction','velocity_last_hour', 'is_fraud'.

   Handling such a big dataset can be tricky because it can slow down the computer or even crash the program. So, we used several smart techniques to make it easier and faster to load, process, and analyze the data. These include breaking the data into chunks, loading only what we need, using lighter data types, sampling small parts, and using parallel processing tools like Dask and Polars.

   Through this project, we gained hands-on experience in working with big data and learned how professional data engineers manage huge datasets efficiently.
  
## Library used
- Pandas
- Polars
- Dask
