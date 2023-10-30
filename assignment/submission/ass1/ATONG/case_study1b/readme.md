<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1b: Sales performance

### Group Name: ATONG (ATG)
### Group Members

| Name                                     | Matrix Number |
| :---------------------------------------- | :-------------: |
| ALIYA ZARENA BINTI ZAINULANUAR            |A21EC0013        |
| MUHAMMAD FIKRI BIN SHARUNAZIM             |A21EC0075        |
| MUHAMMAD IQMAL BIN SIS                    |A21EC0080        |
| ANG YI QIN                                |A21EC0163        |


<br><br>
## Table of Contents
- [Assignment 1b: Sales performance](#assignment-1b-sales-performance)
   * [Importing Datasets](#importing-datasets)
   * [Pivot Table <a name = "pivot_table"></a>](#pivot-table)
      - [Pivot Table for Monthly Sales](#pivot-table-for-monthly-sales)
      - [Pivot Table for Region](#pivot-table-for-region)
      - [Pivot Table for Customer](#pivot-table-for-customer)
      - [Pivot Table for Salesperson](#pivot-table-for-salesperson)
      - [Pivot Table for Trend](#pivot-table-for-trend)
   * [Create Chart <a name = "chart"></a>](#Create-Chart)
      - [Chart for Monthly Sales](#chart-for-monthly-sales)
      - [Chart for Region](#chart-for-region)
      - [Chart for Customer](#chart-for-customer)
      - [Chart for Salesperson](#chart-for-salesperson)
      - [Chart for Trend](#chart-for-trend)
   * [Adding Slicer](#adding-slicer)
   * [Dashboard <a name = "dashboard"></a>](#dashboard)
   * [Contribution 🛠️](#contribution-)
 
     <br><br>


## Importing Datasets
1. We need to import our Dataset2.txt into [Google Sheets](https://docs.google.com/spreadsheets/) by clicking on the **File** then choose the **Import** button.
  <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/f2a5ec37-8b11-4075-90f2-4e068924440c" width="700"></div>

2. Since the Dataset2.txt in our own device, then we need to click  on **Upload >> Browse >> Dataset2.txt** in order to insert the dataset into sheets.
   <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/b151e81e-782d-4341-87f1-28bf85690ed3" width="700"></div>

  > [!IMPORTANT]
> Please make sure you selecting the correct dataset and click on *Done* button in order to successfully importing the dataset.

<br>
3. Click “Replace current sheet” for the *Import location* option, and then import data.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/777f009c-e01d-4ed4-9b8c-443f5d83cdbc" width="700"></div>



4. Use format *"=MONTH(DATEVALUE(H2:H324&1))"* to give value of each rows of months based on *SALES MONTH* column.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/92522e8f-e41b-432d-887b-8ae1a74e2b68" width="700"></div>



5. For those rows that consists the result of *"#VALUE!"*, we need to fix and correct it by clicking **Ctrl+F**. Then type "Sept" as the null value is month of September.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/917370da-89a3-4e41-98de-e7d76904b14a" width="700"></div>



6. Next, we need to replace with the correct format which is *"Sep"*. Following with clicking the **"Replace All"** first, then the **"Done"** button.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/99d00787-c3f6-45e9-a60b-d714722adc8a" width="700"></div>




   Result of Monthly Sales Pivot Table:
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/f998bec5-ad76-4235-9d22-c4753a79b640" width="700"></div>


<br><br>

## Pivot Table
### Pivot Table for Monthly Sales

7. In order to create a pivot table, we need to enter **Ctrl + Shift + Right Arrow Key + Down Arrow Key** in order to select exact rows and columns that consists dataset value only. Next, proceed with click on the **Insert >> Pivot Table >> New Sheet**. 
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/7563d1e6-a626-4d6b-93e9-46bc780dd511" width="700"></div>


8. As for the Monthly Sales pivot table, we will be choosing the *"MONTH* and *SALES MONTH"* as the **Rows** variables.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/81335fcf-de6a-4cfd-98ff-08258eb610f1" width="700"></div>

9. Choose *"SALES* and *TARGET"* as the **Value** columns. The pivot table should be displayed as shown below.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/39e758b5-dbf8-447b-a0e0-63fb8ae2a041" width="700"></div>




    <br>
### Pivot Table for Region 

10. Repeat [**Step 7**](#pivot-table-for-monthly-sales) where we copy the dataset and create a new pivot table.

11. Select *"Sales Region"* as the **Row**  variable and *"Products"* as the **Value** one. Make sure you follow the setting of variables as shown in the figure below such as unclick the **Show Totals** option.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/3727fb48-82fa-405b-a942-00b9ab88aafb" width="700"></div>


<br></br>
### Pivot Table for Customer
12. Repeat [**Step 7**](#pivot-table-for-monthly-sales) where converting from datasets into pivot table.
  
13. Edit the pivot table by choosing **Rows** and **Values**. As shown in the figure below, *"CUSTOMER"* is selected as the row value and *"PRODUCTS"* as the **Value** item. <br>
Result of Customer Pivot Table:
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/4b407df7-ed87-4981-af77-7ddfe0fadb11" width="700"></div>


<br></br>
### Pivot Table for SalesPerson
    
14. Copy the dataset from the *TempData* sheet and select the pivot table. We need to customize the pivot table by choosing the *"SALESPERSON"* as the row and *"PRODUCTS"* as the column.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/e7b24520-4b5f-4780-8720-fc003c022969" width="700"></div>

15. We select the value to sum the sales by each salesperson.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/e391ac8d-5727-43ac-b99b-f641f08653ac" width="700"></div>



<br></br>
### Pivot Table for Trend
16. Repeat [**Step 7**](#pivot-table-for-monthly-sales) where converting from datasets into pivot table.
17. In creating Trend Pivot Table, we will select the "*SALES YEAR*, *SALES MONTH*, and *MONTH*" as the **Rows** items. 
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/b0fd7968-272a-46fd-b502-a16b355b6ad6" width="700"></div>

     Here, we can see that selecting *"SALES"* as the **Values** item is needed in order to create and analyze the trend chart in next step later.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/0365f03a-ab07-4f05-b918-65a7ba08d7b3" width="700"></div>



<br></br>

## Create Chart

18.   Before proceeding to create charts, we need to copy all the pivot tables by using **Ctrl + C** from each sheets. Next, proceed to **PASTE** it into a new sheet named **"Dashboard"**.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/2fb3ee54-fe00-4402-8a83-852f349936f9" width="700"></div>

Result of arranging all pivot table in **DASHBOARD** sheet:
      <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/bfb51c7e-2924-4e25-9832-befc3a8bd882" width="700"></div>
    <br></br>
    
### Chart for Monthly Sales
19. Click **Insert >> Chart** option from the menu above in order to produce a chart based on the pivot tables.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/0b52a7b8-529c-4120-af1f-de9e9104bd67" width="700"></div>
<br><br>
20. As for the chart type, we need to choose the **Stacked Area Chart** , then customize it before arranging it.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/37a18e02-18d4-4231-b0df-d6815f0204d6" width="700"></div>
<br></br>

### Chart for Region
21. Select any rows from the **Region** pivot table before proceeding to repeat the [Step 19: Create Chart](#chart-for-monthly-sales).<br> Choose **Pie Chart** since these datas are suitable being presented in this type of chart.
    
23. We continue to customize the chart such as by changing the position of legend and change the color of pie chart in order to make the chart more outstanding and attractive.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/b202c13a-8971-418a-a838-7902f767d853" width="700"></div>
<br></br>

### Chart for Customer
23. Select the **Customer** pivot table before proceeding to repeat the [Step 19: Create Chart](#chart-for-monthly-sales).
    
24. Choose **Pie Chart** under **Chart Editor >> Setup** option, then customize it where the highlight of key points from the chart can be emphasized later.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/522ec5b3-5e37-4c72-b5f2-045f15885c85" width="700"></div>
<br></br>

### Chart for Salesperson
25. Select the **Customer** pivot table before proceeding to repeat the [Step 19: Create Chart](#chart-for-monthly-sales).
    
27. In **Chart Editor >> Setup** option, we need to choose **Stacked Column Chart**, then customize it to look more organized and presentable in the **Dashboard** sheet.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/2e659da8-329a-4436-a1a8-c10d4adcce05" width="700"></div>
<br></br>

### Chart for Trend
27. Select the **Customer** pivot table before proceeding to repeat the [Step 19: Create Chart](#chart-for-monthly-sales).
    
29. Choose **Smooth Line Chart** to create a line chart. Then, we add on the data labels into the line by clicking **Chart Editor >> Customize** menu under **Series**. 
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/a70a694e-37e2-4e57-98cf-e5ed8d3389a5" width="700"></div>

 > [!IMPORTANT]
> Make sure the data and labelling in each your chart are clear and oustanding in order to ease the analyst to preview the charts including able to absorb the data being presented.

<br></br>

## Adding Slicer
29. Select any rows from the pivot table. For instance, if a region slicer is about to created, we click on the value from **"Region pivot table"** then continue click on **Insert** >> **Add a Slicer**.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/d8a7ccd8-9122-473d-89c7-0774e950178e" width="700"></div>

30. Select the appropriate range: *TempData!A1:J324*. Therefore, all datasets will be selected and linked to the slicer.
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/13a216b7-329c-4c38-9623-4555fe535071" width="700"></div>

    Otherwise, we can click **Insert** >> **Add a Slicer** directly to create a slicer. Make sure to select the right variable as the **Column** variable.<br></br>
      <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/37aa9a49-7f70-4973-97f2-134964097e85" width="700"></div>
      
31. Repeat the [Step 29: Add Slicer](#adding-slicer) to add another slicers for each pivot tables that will linked to all charts in the dashboard.


<br><br>

## Dashboard
   **Dashboard** successfully created!    
   <br>
    <div align="center"><img src="https://github.com/drshahizan/HPDP/assets/108865725/5b5f1532-708b-467e-a0a3-652a55dba72e" width="800"></div>
    <br>
    For example, we select *Loh Yew Chong* from the **SALESPERSON** slicer, and analyze all the charts in order to know the information related with *Loh Yew Chong* only. Make sure to click *Done* button to apply the changes.
<br>
<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/121778984/2a933bf7-c5ef-46cd-b121-061c23541947" width="800"></div>

<br><br>
Here is the result after selecting the option.
<div align="center"><img src="https://github.com/drshahizan/HPDP/assets/121778984/72a4bd27-6695-4ff5-b40f-4c195aa80d55" width="800"></div>




<br><br>
## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



