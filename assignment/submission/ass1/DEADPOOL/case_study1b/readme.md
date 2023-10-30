<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1b: Sales performance

### Group Name: DEADPOOL
### Group Members

| Name                                     | Matrix Number | Task |
| :---------------------------------------- | :-------------: | ------------- |
| UMAR HAZIQ BIN MUHAMAD NORHISHAM            | A21EC0235     |  DATA PREPROCESSING DASHBOARD ASM1  |
| SAM CHIA YUN              | A21EC0127     | DATA TRANSFORMATION     |
| MUHAMMAD IZZUDDIN BIN SHABRIN             | A21EC0083     |   VISUALIZATION   |
| KEE SHIN PEARL             | A21EC0190     | DOCUMENTATION     |

<br>

## **Table of Content**
- [Assignment 1b: Sales performance](#assignment-1b-sales-performance)
   * [Table of Contents](#table-of-contents)
     * [Dataset Information](#dataset-information)
     * [Pivot Table & Visualisation](#pivot-table-n-visualisation)
       * [How to create Pivot table](#how-to-create-pivot-table)
       * [Monthly sales](#monthly-sales)
       * [Region](#region)
       * [Customer](#customer)
       * [Salesperson](#salesperson)
       * [Sales trend](#sales-trend)
     * [Dashboard & Slicer](#dashboard-n-slicer)
     * [Contribution 🛠️](#contribution)

<br>

## Dataset Information 
This dataset is named Dataset2.txt. This dataset contains a few columns of data which are Customer, Products, Sales Person, Sales Region, Target, Sales, Sales Year, Sales Month and Sales QTR.
<br>
**Deadpool Google Sheet** : [Google Sheets 1b](https://docs.google.com/spreadsheets/d/1ErXkBNCsOU6VQPeIP2vVHM2jvqTJuzJYaDOvqtMf_LY/edit?usp=sharing)

**Importing Data**

1. In Google Sheet, go to the upper left menu and choose **File >> Import**
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/import%20data.png)
2. Then, go to **Upload >> Browse** and select Dataset.txt file then import the dataset in a new spreadsheet
    ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/browse%20data.png)
3. In this dataset, we created one new column named **MONTH INDEX** which we use to sort the month as we assign values from 1 to 12 to the month.For example, Jan = 1, Feb = 2, and so on.<br>
    ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/month%20index.png)
   <p align = "center">The formula that we use for MONTH INDEX column is as below:</p>
   <p align ="center">=IF(H2="Jan", 1, IF(H2="Feb", 2, IF(H2="Mar", 3, IF(H2="Apr", 4, IF(H2="May", 5, IF(H2="Jun", 6, IF(H2="Jul", 7, IF(H2="Aug", 8, IF(H2="Sept", 9, IF(H2="Oct", 10, IF(H2="Nov", 11, IF(H2="Dec", 12, 0)))))))))))) </p>
  
   

<br>

## Pivot Table & Visualisation

#### How to create Pivot table

1. In the spreadsheet, select all the values in the dataset by using the command **CTRL A**. Then go to **Insert >> Pivot table**.![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/create%20pivot%20table.png)
2. In the data range option, make sure the value is the one that has been selected before. Make the pivot table in a new sheet.![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/data%20range%20pivot%20table.png)
3. A new sheet will be created which has the pivot table.![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/pivot%20table.png)
   
#### Monthly Sales

1. Create a new pivot table just like the previous step.
2. In the pivot table editor, select:
   * for rows, add **MONTH INDEX** and **SALES MONTH** column. ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/monthly%20rows.png)
   * for values, add **SALES** and **TARGET** column. For both columns, summarize by **SUM**. ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/monthly%20values.png)
3. To create the chart, go to **Insert >> Chart**. In the chart editor, setup the chart as below:
   * Chart type = Stacked area chart
   * Stacking = Standard
   * Data range = B1 : D13
   * X-axis = SALES MONTH
   * Series = Sum of sales and Sum of target
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/setup%20chart%20monthly.png)
4. Then customize your chart as you see fit at the customize tab. For example, change the chart title to Region, make a legend for the pie chart, make the pie chart 3d or change the color of slices in the pie chart

#### Region

1. Create a new pivot table.
2. In the pivot table editor, select:
   * for rows, add **SALES REGION**column. ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/region%20rows.png)
   * for values, add **SALES** column. Make sure **SALES** column is summarised by **SUM**. ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/region%20values.png)
3. To create the chart, go to **Insert >> Chart**. In the chart editor, setup the chart as below:
   * Chart type = Pie chart
   * Data range = A1 : B5
   * Label = SALES REGION
   * Series = Sum of sales
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/region%20chart%20setup.png)
4. Then customize your chart as you see fit at the customize tab. For example, change the chart title to Monthly Sales.

   
#### Customer
1. Create a new pivot table
2. In the pivot table editor, select:
   *for rows add **CUSTOMER** column.
   *for values, add **SALES** column. The **SALES** value is summarised using **SUM**.
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Customer%20Pivot%20Table.png).
4. To create the chart, go to **Insert >> Chart**. In the chart editor setup the chart as below:
   * Chart type = Pie chart
   * Data range = A1 : B8
   * Label = CUSTOMER
   * Series = SUM of SALES
    ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Customer%20Chart.png)
5. Customize the chart at the chart tab. For this Customer chart, the slice is labeled using the percentage calculated and each of the pie slice is 5% away from the center.
   
#### Salesperson
1. Create a new pivot table
2. In the pivot table editor, select:
   *for rows add **SALES PERSON**. The data from the **SALES PERSON** is arranged in alphabetical ascending order.
   *for column add **PRODUCT**.
   *for values, select **SALES**. The **SALES** value is summarised using **SUM**.
    ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Salesperson%20Pivot%20Table.png)
4. To create the chart, go to **Insert >> Chart**. In the chart editor setup the chart as below:
   * Chart type = Stacked Column Chart
   * Data range = A1 : E10
   * X-axis = SALES PERSON
   * Series = PRODUCT
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Salesperson%20Chart.png)
5. Select on the chart tab to customize the chart. The series of Product in this chart is given distinctive colour to differentiate the amount of product sold by the sales person clearly.
   
#### Sales Trend
1. Create a new pivot table
2. In the pivot table editor, select:
   *for rows select **SALES YEAR**, **MONTH INDEX** and **SALES MONTH** column.
   *for values, select **SALES**. The **SALES** value is summarised using **SUM**.
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Sales%20Trend%20Pivot%20Table.png)
4. To create the chart, go to **Insert >> Chart**. In the chart editor setup the chart as below:
   * Chart type = Smooth Line Chart
   * Data range = C1 : D25
   * X-axis = SALES MONTH
   * Series = SUM of SALES
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Sales%20Trend%20Chart.png)
5. Customize the the smooth line chart. The title is changed to Sales Trend and the data points are listed out for the series.

<br>



## Dashboard & Slicer
1. Prepare dashboard by selecting all cells in spreadsheet named **Dashboard2** using the command **CTRL A** and sellect **FILL** to set dashboard background colour.
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Dashboard%20Background.png)
3. All of the charts created are copied and arranged organizedly **Dashboard2** spreadsheet.
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Dashboard%20Chart.png)
5. Merge the first 3 rows of the spreadsheet, then go to **Insert >> Drawing** to create a headline for the dashboard.
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Dashboard%20headline.png)
7. Select **Insert >> Drawing**, using rectangle shape tool to create border for slicer. Repeat this step 4 more times and adjust to the suitable size on the dashboard.
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Dashboard%20Border.png)
9. Insert text using **Insert >> Drawing**. **SALES YEAR**, **SALES REGION** and **PRODUCT** is on the left side while **CUSTOMER** and **SALES PERSON** is on the right side
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Dashboard%20Text.png)

#### How to create Slicer
1. From the spreadsheet named **Dataset2** go to **Data >> Add Slicer** to create slicer that contain the data range from the main dataset.
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Slicer%20Dataset.png)
3. Copy the created slicer from **Dataset2** and paste it to the **Dashboard2** spreadsheet.
5. Select the column to filter from the slicer editor.
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Slicer%20Filter.png)
7. Google sheet slicer only will work on the pivot tables that are from the same sheet. Hence, insert some column to the right and copy all of the pivot table to **Dashboard2** spreadsheet.
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Slicer%20Pivot%20Table.png)
9. Select the Monthly Sales chart to readjust the data range of the chart to the corresponding pivot table on the same sheet. Repeat the same step to all of the remaining visualization in the dashboard.
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Slicer%20Range1.png)
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Slicer%20Range2.png)
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Slicer%20Range3.png)
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Slicer%20Range4.png)
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Slicer%20Range5.png)
11. Customize the slicer to match the palette of the dashboard. Make a total of slicers and change the each of filter columns to **SALES YEAR**, **SALES REGION**, **CUSTOMER**, **SALES PERSON** and **PRODUCT**.
![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Slicer.png)

After all of the slicer is created the interactive dashboard for Deadpool Sales Performance is done.
![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Dashboard.png)

<br>

The display of dashboard when :
* **SALES PERSON** is **Loh Yew Chong**
  ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Dashboard%20Case1.png)
* **PRODUCT** is **cooking oil** and the **SALES YEAR** is **2021**
  ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/Dashboard%20Case2.png)

<br>



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



