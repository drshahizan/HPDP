<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

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
     * [Pivot Table](#pivot-table)
       * [How to create Pivot table](#how-to-create-pivot-table)
       * [Monthly sales](#monthly-sales)
       * [Region](#region)
       * [Customer](#customer)
       * [Salesperson](#salesperson)
       * [Sales trend](#sales-trend)
     * [Dashboard](#dashboard)
     * [Contribution 🛠️](#contribution)

<br>

## Dataset Information 
This dataset is named Dataset2.txt. This dataset contains a few columns of data which are Customer, Products, Sales Person, Sales Region, Target, Sales, Sales Year, Sales Month and Sales QTR.

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

## Pivot Table

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
4. Then customize your chart as you see fit at the customize tab. For example, change the chart title to Monthly Sales.

#### Region

1. Create a new pivot table.
2. In the pivot table editor, select:
   * for rows, add **SALES REGION**column. ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/region%20rows.png)
   * for values, add **SALES** column. Make sure **SALES** column is summarised by **SUM**. ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/monthly%20values.png)
3. To create the chart, go to **Insert >> Chart**. In the chart editor, setup the chart as below:
   * Chart type = Pie chart
   * Data range = A1 : B5
   * Label = SALES REGION
   * Series = Sum of sales
   ![image](https://github.com/drshahizan/HPDP/blob/main/assignment/submission/ass1/DEADPOOL/case_study1b/images/setup%20chart%20monthly.png)
4. Then customize your chart as you see fit at the customize tab. For example, change the chart title to Monthly Sales.

   
#### Customer
#### Salesperson
#### Sales Trend


<br>



## Dashboard



<br>



## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



