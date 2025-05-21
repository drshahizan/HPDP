# 🧼 Folder Data

This repository includes the raw data and cleaned data before and after as well as raw data for mapping process 

---

## 📁 Folder Structure & File Descriptions



### 🧪 Dataset

#### 🔹 Raw Scraped Data
- [`Item_list.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/data/Item_list.csv)  
  ➤ Raw product dataset collected from PG Mall before cleaning. Contains product name, price, location, and link with some duplicates, null values, and uncleaned fields.

#### 🔹 Raw Scraped Data by Subcategory in Folder `Item_By_Category`
  ➤ Raw product datasets collected from PG Mall before cleaning. Contains product name and link.

#### 🔹 Raw Scraped Data by Subcategory (merged)
- [`merged_product_list.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/data/merged_product_list.csv)  
  ➤ Merged raw product dataset of all the raw data in folder `Item_By_Category`.

#### 🔹 Updated Raw Scraped Data
- [`updated_item_list.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/data/updated_item_list.csv)  
  ➤ Raw product dataset collected from PG Mall before cleaning. Contains product name, price, location, link, and type.

#### 🔹 Cleaned Data (Without Optimization)
- [`Item_list_cleaned.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/data/Item_list_cleaned.csv)  
  ➤ Dataset after cleaning using Pandas.

#### 🔹 Cleaned Data (With Polars)
- [`Item_list_cleaned_optimized.csv`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/data/Item_list_cleaned_optimized.csv)  
  ➤ Cleaned dataset processed using Polars.

#### 🔹 Cleaned Data (With Dask)
- [`Item_list_cleaned_dask.csv.ipynb`](https://github.com/drshahizan/HPDP/blob/main/2425/project/p1/GroupD/data/Item_list_cleaned_dask.csv)  
  ➤ Cleaned dataset processed using Dask.



---




