<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1b: Sales Performance

### Group Name: HANY
### Group Members

| Name                                     | Matrix Number | Task |
| :---------------------------------------- | :-------------: | :---------------------: |
| ALYA BALQISS BINTI AZAHAR             |A21EC0158      | VISUALISATION & DOCUMENTATION     |
| MUHAMMAD HARITH HAKIM BIN OTHMAN              | A21EC0205     | ANALYSIS     |
|NADIA SYAFIQAH BINTI ZULKIPLI|A21EC0098      | DOCUMENTATION     |
| LIEW YVONNE              |A21EC0045      | PREPROCESSING     |

## Table of Contents
1. [Introduction](#1-introduction)
2. [Data Importation](#2-data-importation)
   - 2.1. [Import Dataset](#21-import-dataset)
   - 2.2. [Enhance Dataset Appearance](#22-enhance-dataset-appearance)
3. [Data Processing](#3-data-preprocessing)
4. [Data Visualisation](#4-data-visualisation)
5. [Contribution](#5-contribution)

## 1. Introduction
**CASE STUDY 2: Sales Performance** presents an engaging challenge of creating a dynamic dashboard to analyze and visualize sales performance based on a provided dataset which is [Dataset2.txt](https://docs.google.com/spreadsheets/d/1rKwc9vmwvVDqHaBCEf31vlPtSSHoVWJi3Tsy18F0rDk/edit?usp=sharing).

## 2. Data Importation
### 2.1. Import Dataset
To get started with creating a dashboard or begin conducting data analysis, start by importing the dataset into Google Sheets, as illustrated in Figure 1. 
  1. Navigate to the **File** menu, and select the **Import** option.
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/a4d8fddf-5f74-495e-8548-70efcea68bd1" width="500"></div>
  2. Select **Upload** and browse through the directories by selecting **Browse** button.
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/c6d3f539-1a72-4759-b7a9-dd8cb8c850ae" width="500"></div>
  3. Locate the dataset file named **Dataset2.txt**.
  4. Initiate the import by clicking on **Open** to bring the data into Google Sheets.
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/eb53a195-5e31-4a40-a640-4ffcaa4a1284" width="500"></div>
  5. Click on the **Import Data** to proceed with the data import.
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/8a868c00-c4f0-4aff-9435-08960dd59ff3" width="500"></div>

### 2.2. Enhance Dataset Appearance
  1. Navigate to the **Format** menu and select **Alternating colors**.
      <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/da806f8e-d874-40d7-8bd2-4f7bfe377af7" width="500"></div>
  2. Choose the color theme according to preferred appearance.
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/5349797f-f3ac-4931-871e-aedf8c241bc8" width="500"></div>
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/fe250ee2-d5e5-4f63-9ace-c17bd9cb236e" width="500"></div>



## 3. Data Preprocessing
In order to facilitate accurate sorting of data in the pivot table in Google Sheets, it is necessary to create an additional column that aligns with column that contains month name to ensure that the data is sorted chronologically by month, as Google Sheets typically defaults to alphabetical sorting.
  1. Locate the column containing **"SALES MONTH"** (cell H).
  2. **Insert** a new column named **"NUMERICAL MONTH"**.
  3. In the first cell of the "NUMERICAL MONTH" (under the header), type in the formula **=MONTH(DATEVALUE(H2&1))**. Then auto fill in for the rest of the columns.
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/4c14b5a9-f856-4c50-a2ef-eb541f09cc5b" width="500"></div>
     
     - This formula is used to extract the month from the date provided in cell H2.
     - **'H2&1'**: Concatenates the value in cell **H2** with the number 1.
       - The number 1 in the formula acts as a placeholder and does not represent the actual day of the month. It is simply added to help convert the text in cell H2 into a date format that can be recognised by the **DATEVALUE()** function.
     - **'DATEVALUE()':** Converts a tect representation of a date into a date value.
     - **'MONTH()':** Extracts the month from the given date. It takes the date value and returns the month as a number.
  5. Notice that some values in the column could not be converted to numbers due to the non-standard format of the word **"Sept"**. To resolve this, the word needs to be replaced with **"Sep"**.
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/d7719e5d-337f-41c8-ad17-e17e4ee2c796" width="500"></div>
  6. Press **CTRL + F** and type in **"Sept"** in the search bar. Press the three-dotted menu.
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/699636d8-f8c6-4609-b74e-7e020ef4aecb" width="500"></div>
  7. Input **"Sep"** into the **Replace with** field and proceed to click on **Replace all**.
      <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/a9c3639b-5c18-4086-99f5-a0411f5f4989)" width="500"></div>
  8. Next, sort the dataset by ascending order according to the NUMERICAL MONTH column.
  9. Go to the **Format** menu, hover over **Sort range**, and then select **Advanced range sorting options**.
      <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/2c06cb45-eb23-4985-8443-2487561e4e7a" width="500"></div>
  10. Check the box labeled **Data has header row** and choose the **NUMERICAL MONTH** column in the dropdown menu. Opt for the **A-Z** sorting order.
      <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/323a127e-0469-442d-86d3-1b2dd8337829" width="500"></div>


## 4. Data Visualisation
  1. Navigate to the **Insert** menu and select **Pivot table**.
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/c1acb990-2d7c-4002-bb8d-8f7c646c3437" width="500"></div>
  2. Click on the header of the first column (CUSTOMER), and press **CTRL + SHIFT + RIGHT ARROW KEY** and **CTRL + SHIFT + DOWN ARROW KEY** to highlight all the columns and rows that contain data without including any blank cells.
  3. Proceed to create the pivot table by clicking on **Create**.
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/f867e3ce-ea55-4c79-96b0-ccafee7f962c" width="500"></div>
  4. Subsequently, add relevant headers into the **Row, Columns, Values,** and **Filters** field to generate the desired data analysis.
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/97207e71-40dd-49cd-a89f-64dcbb2cb4e2" width="500"></div>
     
     - Monthly Sales
       - Row: NUMERICAL MONTH, SALES MONTH
       - Values: Target, SALES
       <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/22e25c3a-89ee-417a-aa91-e1bf3bceb0a0" width="200"></div>
  5. Repeat the step of creating the pivot table for each data anaysis. The following are the inputs for respective data analysis.
     - Region
       - Row: Sales Region
       - Values: PRODUCTS
        <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/72d8ccad-aed5-40ee-8763-11679fa047df" width="200"></div>
     - Customer
       - Row: Customer
       - Values: PRODUCTS
       <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/7cd4ae1c-7899-4466-beb5-ae937f15c2ec" width="200"></div>
     - Sales Person
       - Row: SALES PERSON
       - Column: PRODUCTS
       - Values: SALES
       <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/15a54441-2d08-4ecc-93a0-1c9e8b52c8fc" width="200"></div>
     - Sales Trend
       - Row: SALES YEAR, NUMERICAL MONTH, SALES MONTH
       - Values: SALES
       <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/d7ff05c4-676c-4545-a2ef-bd906866ec1b" width="200"></div>
  6. Once all the pivot tables are created, duplicate and transfer them into a new new sheet named **"Dashboard"**.
     <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/a2d3339e-ed45-4851-9ab6-053172e671d6" width="500"></div>
  7. To generate the chart, select the related pivot table. Then, go to the **Insert** menu and select **Chart**.
      <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/80bb4dbd-9230-46c2-8b89-5f7898192b46" width="500">
 
      **Charts Created**
   
      - Monthly Sales
        <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/7a093daf-5f92-48b4-a58e-a505155fc3a5">

      - Sales Region
        <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/e7ab2edc-d427-4561-840e-f61523fcc5b0">

      - Customer
        <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/8fd5a737-dbae-4af6-93a5-40ca0e3509e4">

      - Sales Person
        <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/5f49c498-f7ca-4efb-85e8-4a4b6d9bbd80">

      - Sales Trend
        <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/5e088608-f376-4e56-8d1e-0e0581af390d">

        
  8. Repeat the process of generating the desired charts and customise the result according to preferred appearance.
  9. Next, to add a slicer, select the related pivot table, navigate to the **Data** menu and select **Add a slicer**.
      <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/c1de707f-5f76-4c0e-a2f2-d0ec04cf6b8e" width="500"></div>
  10. Click on the slicer. From the **Choose a column** dropdown menu, choose the appropriate header to act as the slicer.
      <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/b6eb97c9-8f65-42e5-8e8d-dcdb7ed13c50" width="500"></div>
  11. Repeat this process until all desired slicers are created. The slicers added include:
      - SALES YEAR
      - Sales Region
      - PRODUCTS
      - CUSTOMER
      - SALES PERSON
  12. After generating all the charts and slicers, it is time to enhance and organize the dashboard to improve its visual appearance.
      <div align="left"><img src="https://github.com/drshahizan/HPDP/assets/121602362/4b85bdf5-de8d-4dcc-abe5-39569490b88a" width="800"></div>

      
## 5. Contribution
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




