# 🚗 Car Listings Data 

## 🔗 Data Files

- **[Raw Dataset](https://drive.google.com/file/d/1eK8V7xZXzvBDPVBAppC2TzItXCjdHnkr/view?usp=sharing)**  
  Original dataset containing **175,545 rows** and **17 columns**. Includes some missing values in `location`, `fuel type`, and `body type`.

- **[Cleaned Dataset](https://drive.google.com/file/d/1KVVZ2WM5iz2jZFF2iFwH8Gn16O9gvoxw/view?usp=sharing)**  
  Cleaned version of the dataset with missing values replaced and invalid URL entries removed. Final shape: **175,545 rows × 16 columns**.

---

## 📊 Dataset Overview

This dataset contains car listings from various regions in Malaysia. The dataset includes key attributes such as car name, price, location, brand, year of manufacture, and more. It provides valuable insights for car buyers, sellers, and analysts interested in the automotive market.

---

### 🧹 Data Cleaning Summary

- **Initial Data Shape**:  
  The dataset initially had **175,545 rows** and **17 columns**.

- **Initial Columns**:  
  The columns before cleaning were:  
  `['car name', 'price (myr)', 'currency', 'location', 'region', 'brand', 'model', 'year', 'mileage', 'fuel type', 'color', 'body type', 'seating capacity', 'condition', 'image', 'description', 'url']`

- **Duplicates**:  
  No duplicates were found in the dataset.

- **Missing Values**:  
  - `location`: 143 missing entries  
  - `fuel type`: 39 missing entries  
  - `body type`: 31 missing entries  
  - All other columns had no missing values.

- **Missing Values After Cleaning**:  
  All missing values in columns (`location`, `fuel type`, `body type`) were replaced with `'Unknown'`.  
  After replacing, there are **no missing values** left in the dataset.

- **Valid URL Rows**:  
  The dataset was filtered to only retain rows with valid URLs. After filtering, the dataset retained its original **175,545 rows** but had **16 columns** (the `currency` column was dropped, and URLs were validated).

- **Final Data Shape**:  
  After cleaning, the dataset has **175,545 rows** and **16 columns**.

- **Final Columns**:  
  After cleaning, the columns are:  
  `['car name', 'price (myr)', 'location', 'region', 'brand', 'model', 'year', 'mileage', 'fuel type', 'color', 'body type', 'seating capacity', 'condition', 'image', 'description', 'url']`

---

### 📝 Columns in Cleaned Dataset

| Column Name         | Description                              |
|---------------------|------------------------------------------|
| **car name**         | Name of the car listing                  |
| **price (myr)**      | Price in Malaysian Ringgit               |
| **location**         | City or area of the listing              |
| **region**           | Region or state in Malaysia              |
| **brand**            | Car brand                                |
| **model**            | Car model                                |
| **year**             | Year of manufacture                      |
| **mileage**          | Mileage of the car                       |
| **fuel type**        | Type of fuel (e.g., Petrol, Diesel)      |
| **color**            | Color of the car                         |
| **body type**        | Type of car body (e.g., SUV, Sedan)      |
| **seating capacity** | Number of seats                          |
| **condition**        | Car condition (e.g., New, Used)          |
| **image**            | Image file name or path                  |
| **description**      | Detailed description of the car          |

---

### 🧑‍🔬 Data Cleaning Process

The dataset underwent several cleaning steps to ensure its quality and usability for analysis:

1. **Handling Missing Values**:  
   - Replaced missing values in `location`, `fuel type`, and `body type` with `'Unknown'`.

2. **Duplicate Removal**:  
   - No duplicates were found in the dataset.

3. **Condition Standardization**:  
   - Standardized the `condition` column, converting entries like `usedcondition` to `used`.

4. **Valid URL Filtering**:  
   - Only valid rows with URLs starting with `http` were retained.

5. **Outlier Handling**:  
   - Removed unreasonable price and mileage values (e.g., negative values).

6. **Column Removal**:  
   - Dropped the `currency` column as it was redundant for analysis.

7. **Text Standardization**:  
   - Converted all string columns to lowercase and stripped any extra spaces.

---

## 💾 Dataset Usage

To use the cleaned dataset:

1. **Load the Raw Data**:
   ```python
   df_raw = pd.read_csv('raw_data.csv')
