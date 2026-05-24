# 🏠 Malaysia Property Listings Dataset

## 📁 1. Data Files

| File | Description | Rows | Columns | Download |
|------|-------------|------|---------|----------|
| `raw_data.csv` | Original scraped property listings  | 111,620 | 16 | [Raw data](https://drive.google.com/file/d/1ChZQvgmhdtkBeFkbFYOfcypWMZR9Rn7X/view?usp=drive_link) |
| `cleaned_data.csv` | Cleaned and processed version of the raw data | 100,442 | 16 | [Cleaned data](https://drive.google.com/file/d/1zyY6UdG1mjZ_joEZJAkjhC06SJzkmqWq/view?usp=drive_link) |

---

## 📊 2. Dataset Overview

This dataset contains Malaysia property listings scraped from an online property platform which is Mudah.my. It covers both **sale** and **rental** property listings across various states. Each record represents a single property listing and includes details such as pricing, size, location, property type, and seller information.

- **Total raw records:** 111,620  
- **Total cleaned records:** 100,442  
- **Number of features:** 16  
- **Listing types:** Sale, Rent  
- **Geographic coverage:** Multiple states in Malaysia  

---

### 2.1 🧹 Data Cleaning Summary

| Metric | Value |
|--------|-------|
| Raw rows | 111,620 |
| Cleaned rows | 100,442 |
| Rows removed (duplicates) | 11,178|
| Columns before cleaning | 16 |
| Columns after cleaning | 16 |

**Key cleaning actions performed:**
- Removed 11,178 duplicate rows
- Standardized column names (lowercase, underscores)
- Stripped HTML tags from text fields (scraped data)
- Validated and nullified broken/invalid URLs
- Filled missing numeric values with column median
- Filled missing text values with `'N/A'`
- Enforced correct data types across all columns
- Capped unrealistic values (bedrooms/bathrooms > 20 → null)

---

### 2.2 📋 Columns in Cleaned Dataset

| # | Column | Type | Description |
|---|--------|------|-------------|
| 1 | `listing_id` | String | Unique identifier for each listing |
| 2 | `property_type` | String | Type of property (e.g., Condo, Terrace, Apartment) |
| 3 | `description` | String | Full text description of the listing |
| 4 | `location` | String | Specific area/neighbourhood of the property |
| 5 | `state` | String | Malaysian state where the property is located |
| 6 | `price_rm` | Float | Listing price in Malaysian Ringgit (RM) |
| 7 | `mortgage_est_rm` | Float | Estimated monthly mortgage in RM (nulls filled with median) |
| 8 | `land_title` | String | Land title type (e.g., Freehold, Leasehold) |
| 9 | `size_sqft` | Float | Property size in square feet (nulls filled with median) |
| 10 | `bedrooms` | Float | Number of bedrooms (values > 20 set to null, then median-filled) |
| 11 | `bathrooms` | Float | Number of bathrooms (values > 20 set to null, then median-filled) |
| 12 | `tenure` | String | Tenure type (Freehold / Leasehold) |
| 13 | `seller_type` | String | Type of seller (e.g., Agent, Owner) |
| 14 | `seller_name` | String | Name of the seller/agent |
| 15 | `url` | String | URL link to the original listing page |
| 16 | `img_url` | String | URL link to the listing's image |

---

### 2.3 🔧 Data Cleaning Process

The cleaning pipeline was implemented in Python (Google Colab) and followed these steps:

**Step 1 — Merge Sale & Rent Data**  
Two separate CSV files (`data_sale.csv` and `data_rent.csv`) were loaded and combined into a single dataframe. A `listing_type` column was added to distinguish between sale and rent records.

**Step 2 — Enforce Data Types**  
- `listing_id` → converted to string, `.0` suffixes removed  
- `price_rm`, `mortgage_est_rm`, `size_sqft` → converted to numeric  
- `bedrooms`, `bathrooms` → converted to numeric, values above 20 set to `null`  
- All text columns → stripped and normalized  

**Step 3 — Standardize Column Names**  
All column names converted to lowercase with underscores, and special characters removed.

**Step 4 — Remove Duplicate Rows**  
Exact duplicate rows were identified and removed (11,178 rows dropped).

**Step 5 — Strip Whitespace & Normalize Text**  
All string columns were stripped of leading/trailing whitespace and multiple internal spaces were collapsed to a single space.

**Step 6 — Remove HTML Tags**  
HTML tags (common in scraped data) were removed from all non-URL text columns using regex.

**Step 7 — Validate URLs**  
URL columns were checked — entries that did not start with `http://` or `https://` were set to `null`.

**Step 8 — Handle Missing Values**  
- Rows where **all** values were null → dropped  
- Numeric columns (`size_sqft`, `bedrooms`, `bathrooms`, `mortgage_est_rm`) → filled with **column median**  
- Text columns → filled with `'N/A'`  

**Step 9 — Reset Index**  
The dataframe index was reset after all cleaning operations.

---

### 2.4 💡 Dataset Usage

This dataset can be used for a variety of data science and analytics tasks, including:

- **Market Trend Analysis** — Identify which property types, locations, or tenures are most common or expensive.
- **Property Price Prediction** — Train regression models to predict `price_rm` based on features like location, size, bedrooms, and property type.
- **Geospatial Analysis** — Explore property distribution and price heatmaps across Malaysian states.



---
