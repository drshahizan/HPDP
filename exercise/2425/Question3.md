<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/issues"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/Python_Tutorial?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# QUESTION 3 \[20 MARKS\]

In 2024, **Kuala Lumpur City Hall (DBKL)** launched an initiative to
analyze traffic congestion and urban mobility using data collected from
**Global Positioning System (GPS)** devices installed in more than
**3,000 buses and ride-hailing vehicles**.

The dataset is stored in **Google Drive**, exceeds **2 GB**, and
contains:

-   Timestamps
-   Coordinates
-   Speed
-   Route IDs
-   Traffic condition flags

Dataset location:

``` text
/content/drive/MyDrive/kl_traffic/gps_data.csv
```

## Questions

### a) Import the required Python libraries. Load the dataset from Google Drive and display the first **five (5)** rows.

**(4 marks)**

### b) Perform data type conversion according to the table below.

**(6 marks)**

   No.  Original Data Type   New Data Type
  ----- -------------------- ---------------
    i   float64              float32
   ii   int64                int16
   iii  object (timestamp)   datetime64


### c) Load the GPS dataset in **chunks of 5,000,000 rows** and combine them into a single DataFrame.

**(5 marks)**


### d) Extract a **10% stratified random sample** based on `route_id` and display the first few rows.

**(5 marks)**
