<h1 align="center"> 
  Mastering Big Data Handling
  <br>
</h1>

<table border="solid" align="center">
  <tr>
    <th>Name</th>
    <th>Matric Number</th>
  </tr>
  <tr>
    <td width=80%>MULYANI BINTI SARIPUDDIN</td>
    <td>A22EC0223</td>
  </tr>
  <tr>
    <td width=80%>ALIATUL IZZAH BINTI JASMAN</td>
    <td>A22EC0136</td>
  </tr>
</table>

# 📊 Mastering Big Data Handling

This project focuses on efficiently managing large datasets using Python and scalable libraries. We applied various strategies to handle datasets exceeding 700MB, specifically the NYC Parking Tickets dataset from Kaggle.

---

## 📂 Project Files

| File Name                     | Description                                | Link |
|------------------------------|--------------------------------------------|------|
| **Raw Dataset**              | Original dataset with parking tickets data | [![Download](https://img.shields.io/badge/Download-Kaggle-blue?logo=kaggle)](https://www.kaggle.com/datasets/new-york-city/nyc-parking-tickets?select=Parking_Violations_Issued_-_Fiscal_Year_2014__August_2013___June_2014_.csv)|
| **Google Collab**      | Code to load and inspect data              | [![Open](https://img.shields.io/badge/View-Code-green?logo=jupyter)](https://github.com/drshahizan/HPDP/blob/main/2425/assignment/A2/bdm/Mainecoon/big_data.ipynb) |


---

## 📚 Libraries Used

| Library | Description |
|--------|-------------|
| `Pandas` | A popular library for data manipulation and analysis, ideal for smaller datasets. |
| `Dask`   | A parallel computing library that scales Pandas operations for larger datasets. |
| `Polars` | A high-performance DataFrame library optimised for speed and memory efficiency. |

---

## 🔗 Data Details

- **Original Dataset**: Contains over **10,803,028 rows** of data and **43 columns** related to parking violations in NYC.

### Columns

This dataset contains detailed information about parking violations in New York City. Below is a description of each column:

| Column Name                                         | Description                                                                            |
|-----------------------------------------------------|----------------------------------------------------------------------------------------|
| `Summons Number`                                   | Unique identifier for each parking violation                                          |
| `Plate ID`                                         | Vehicle license plate identifier                                                        |
| `Registration State`                               | State in which the vehicle is registered                                              |
| `Plate Type`                                       | Type of license plate (e.g., passenger, commercial)                                   |
| `Issue Date`                                       | Date when the parking violation was issued                                             |
| `Violation Code`                                   | Code representing the specific type of violation                                       |
| `Vehicle Body Type`                                | Description of the vehicle's body style (e.g., sedan, SUV)                           |
| `Vehicle Make`                                     | Manufacturer of the vehicle                                                            |
| `Issuing Agency`                                   | Government agency issuing the parking ticket                                           |
| `Street Code1`, `Street Code2`, `Street Code3`    | Codes representing the streets where the violation occurred                            |
| `Vehicle Expiration Date`                           | Expiration date of the vehicle registration                                            |
| `Violation Location`                               | Location of the violation (latitude and longitude)                                    |
| `Violation Precinct`                               | Police precinct where the violation was issued                                         |
| `Issuer Precinct`                                  | Precinct of the officer who issued the ticket                                          |
| `Issuer Code`                                      | Code identifying the issuing officer                                                   |
| `Issuer Command`                                   | Command of the issuing officer's unit                                                 |
| `Issuer Squad`                                     | Specific squad or team of the issuing officer                                          |
| `Violation Time`                                   | Time when the violation occurred                                                       |
| `Time First Observed`                              | Time when the violation was first observed                                             |
| `Violation County`                                 | County where the violation took place                                                  |
| `Violation In Front Of Or Opposite`                | Description of the location relative to a specific address                             |
| `House Number`                                     | House number associated with the violation location                                    |
| `Street Name`                                      | Name of the street where the violation occurred                                        |
| `Intersecting Street`                              | Name of the street that intersects with the violation location                         |
| `Date First Observed`                              | Date when the violation was first observed                                             |
| `Law Section`                                      | Legal section that pertains to the violation                                           |
| `Sub Division`                                     | Subdivision related to the law section                                                |
| `Violation Legal Code`                             | Legal code associated with the specific violation                                      |
| `Days Parking In Effect`                           | Number of days the parking rule was in effect                                         |
| `From Hours In Effect`                             | Starting hour when the parking rule is enforced                                        |
| `To Hours In Effect`                               | Ending hour when the parking rule is enforced                                          |
| `Vehicle Color`                                    | Color of the vehicle                                                                    |
| `Unregistered Vehicle?`                            | Indicates whether the vehicle was unregistered (1 = Yes, 0 = No)                      |
| `Vehicle Year`                                     | Year of manufacture for the vehicle                                                    |
| `Meter Number`                                     | Identifier for the parking meter (if applicable)                                      |
| `Feet From Curb`                                   | Distance from the curb where the vehicle was parked                                    |
| `Violation Post Code`                              | Postal code associated with the violation location                                      |
| `Violation Description`                            | Detailed description of the violation                                                  |
| `No Standing or Stopping Violation`                | Indicates if the violation is for no standing or stopping (1 = Yes, 0 = No)          |
| `Hydrant Violation`                                | Indicates if the violation is for parking in front of a hydrant (1 = Yes, 0 = No)    |
| `Double Parking Violation`                          | Indicates if the violation is for double parking (1 = Yes, 0 = No)                    |
---

## 📊 Key Observations

1. **Efficiency Gains**: Using Dask and Polars significantly reduced memory usage and execution time compared to traditional Pandas methods.
2. **Scalability**: Dask’s ability to handle large datasets in parallel allowed for smoother processing.
3. **Data Integrity**: Data cleaning improved data quality, ensuring reliable analysis.

---

## 🔗 Part 1 - Technique Comparison
---

## 🔗 Part 2 - Library Comparison
---

## 📈 Benefits and Limitations of Each Method

### Pandas
- **Benefits**: 
  - Easy to use and well-documented.
  - Great for exploratory data analysis on smaller datasets.
- **Limitations**: 
  - Struggles with memory management for very large datasets.
  - Slower execution times compared to optimized libraries.

### Dask
- **Benefits**:
  - Handles larger-than-memory datasets effectively.
  - Parallel processing capabilities enhance performance.
- **Limitations**:
  - Slightly steeper learning curve than Pandas.
  - Overhead can be significant for smaller datasets.

### Polars
- **Benefits**:
  - Extremely fast and memory-efficient.
  - Excellent performance for large-scale data manipulation.
- **Limitations**:
  - Less mature ecosystem compared to Pandas and Dask.
  - May require adjustments for compatibility with existing Pandas-based workflows.

---

## ✅ Reflection

This assignment enhanced our understanding of big data handling techniques. We learned the importance of choosing the right tools for specific tasks, especially when dealing with large datasets. The experience reinforced the need for efficient data processing strategies to extract meaningful insights without compromising performance. Overall, mastering these techniques equips us with essential skills for navigating the data-driven landscape more effectively.
