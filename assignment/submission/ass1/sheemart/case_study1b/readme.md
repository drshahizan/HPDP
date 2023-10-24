
<div align="center">

# Assignment 1: Data Analysis using Google Sheets
## Dataset 2 Report

</div>
---

### 🍀Group Name: sheemart
### 🌼Group Members

| Name                                     | Matrix Number | Photo |
| :---------------------------------------- | :-------------: | ------------|
| MUHAMMAD AMIR JAMIL BIN JAMLUS | A21EC0202 |              |
| MUHAMMAD NAQUIB BIN ZAKARIA | A20BE0161 |              |
| MUHAMMAD HAZIM BIN SALMAN | A21EC0078 |              |
| NURUNNAJWA BINTI ZULKIFLI | A21EC0121 |                  |

------
## 🌟Table of content

- [Table of content](#Table-of-content)
- [1. Import dataset into Google Sheet](#1-Import-dataset-into-Google-Sheet)
- [2. Create "TempData"](#2-Create-"TempData")
- [3. Create Pivot Table](#3-Create-Pivot-Table)
- [4. Create Chart](#4-Create-Chart)
- [5. Create Slicer](#5-Create-Slicer)

------

## Dataset Information

We work with a dataset called dataset2.txt. This dataset contain nine columns. Customer, product, and salespeson are some of the column use

Google Sheet : https://docs.google.com/spreadsheets/d/1NeqlqmzfCoZzOjti6SplwZSnEMmr9rE3DAy8bdw6gSY/edit#gid=1654905438

---

## 1. Import dataset into Google Sheet


<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/96f95fff-a9e4-4864-a031-bf3dc30c80ad">
</p>

<div align="center">
  
_Figure 1: Import the data_

</div>


- After opening Google Sheet, click on **File** and choose **Import**.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/73b7f84c-2493-4f09-a9bd-63f06f0d1b3a">
</p>

<div align="center">
  
_Figure 2: Choose your data_

</div>

- Choose** Browse **and choose 'Dataset2.txt' as our dataset.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/225bac12-557e-4e84-802c-01aa98711cf7">
</p>

<div align="center">
  
_Figure 3: Import data_

</div>

- Choose '**Replace in current sheet**' as Import location and '**Detect automatically**' as separator type. Check on the checkboard. Then, click Import Data.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/969f848b-a9a4-4910-aea6-ec1981f67d99">
</p>

<div align="center">

_Figure 4: Database imported successfully_

</div>

- The database has been imported successfully.
  
----
## 2. Create "TempData"

We then created a temporary dataset called "TempData". The purpose of this temporary data is to allow us to work with the exact copy of the Dataset2.txt without applying permanent changes to the original dataset. This allows us to preprocess, transform and also add columns to the copy of the dataset without affecting the original dataset.

------
<p align="center">
<img width="789" alt="image" src="https://github.com/drshahizan/HPDP/assets/146797903/e8d96153-193c-4b3f-bc2f-2e0b903f9084">
</p>

<div align="center">
    
_Figure 5: Creation of TempData_

</div>
- We then began preprocessing the data, because the decimal place wasnt consistent. We then fixed the issue using Google Sheet provided tool "Increase decimal place" to make sure the decimal place becomes cosistent.

<p align="center">
<img width="196" alt="image" src="https://github.com/drshahizan/HPDP/assets/146797903/0b6581db-f385-4b28-b37a-82ea26ed3b0d">
</p>

_Figure 6: Google Sheet provided tool_

-Then we observed the provided data set 

## 3. Create Pivot Table

Creating a pivot table in Google Sheets is a powerful way to analyze and summarize data. It allows you to group and aggregate data to gain insights and create customized reports.

#### Steps on creating pivot table

1. **Insert Pivot Table**: Go to the "Insert" menu at the top and select "Pivot table." This will open a new sheet or insert a pivot table in your current sheet.

<div align="center">
    
![image](https://github.com/drshahizan/HPDP/assets/92329710/12b022bc-3e33-4964-83d9-fca9ffa7633f)

</div>



2. **Select the Data Range**: Select the range of data you want to use for the pivot table. This should include column headers and the data you want to analyze.

<div align="center">

![image](https://github.com/drshahizan/HPDP/assets/92329710/ef5818a9-fc6c-47e8-aa9e-df67980a4549)

</div>



3. **Pivot Table Editor**: On the right side of the screen, you will see the Pivot Table Editor.

<div align="center">
    
![image](https://github.com/drshahizan/HPDP/assets/92329710/1ad92419-a22e-4a3a-9976-6c291026e16c)

</div>



- Rows: Drag the column that you want to group by into the "Rows" section. This will be the primary category for your pivot table.

<div align="center">
    
![image](https://github.com/drshahizan/HPDP/assets/92329710/f86b4d66-26a9-47dc-ae30-b1e0fe090224)

</div>


- Columns: Drag another column into the "Columns" section to create a subcategory.

- Values: Drag the column you want to analyze or summarize into the "Values" section. You can choose the type of aggregation you want (e.g., sum, average, count) by clicking on the "Summarize by" dropdown.

<div align="center">
    
![image](https://github.com/drshahizan/HPDP/assets/92329710/fd2d13b1-2b77-4b50-92bd-8660dc27537e)

</div>



## 4. Create Chart

Creating a chart from a pivot table in Google Sheets is a straightforward process. Pivot tables help summarize and organize data, and you can easily visualize the summarized data by creating a chart.

#### Steps on creating chart from pivot table

1. **Select the Pivot Table**: Click on your pivot table to select it.
2. **Insert a Chart**:

    - Go to the "Insert" menu at the top.
    - Choose "Chart."
  
3. **Chart Editor**:

    - A sidebar called "Chart editor" will appear on the right.
    - In the Chart Editor, you can choose the type of chart you want to create, such as a bar chart, column chart, pie chart, etc., based on your data and the type of analysis you want to perform.

4. **Customize the Chart**:

    - You can customize the chart further by adjusting the Chart Editor settings. These settings include options like chart title, axis labels, legend, colors, and more.
    - The data range should automatically be populated with your pivot table's data. However, double-check to ensure it's using the correct range.


## 5. Create Slicer

Creating a slicer in Google Sheets is a great way to provide an interactive way for users to filter data in a pivot table or data range. Slicers are especially useful for dashboard-style sheets.

#### Steps on creating chart from pivot table

1. **Insert Slicer**:

    - Go to the "Data" menu at the top.
    - Select "Add a slicer."
2. **Select the Data Range or Pivot Table**:

    - Click on the data range or pivot table that you want to associate with the slicer.

3. **Configure Slicer Options**:

    - A "Slicer" pane will appear on the right side of the screen. In this pane, you can:
        - Choose which column from your data or pivot table you want to use for filtering.
        - Adjust the slicer's appearance, such as its style, size, and alignment.
        - Customize the slicer name and title, which will be displayed above the slicer.
        - Select the "Data range" if it's not automatically detected.
