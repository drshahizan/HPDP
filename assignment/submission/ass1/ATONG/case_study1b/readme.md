<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

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
   * [Table of Contents](#table-of-contents)
   * [Pivot Table <a name = "pivot_table"></a>](#pivot-table)
      - [Pivot Table for Monthly Sales](#pivot-table-for-monthly-sales)
      - [Pivot Table for Region](#pivot-table-for-region)
      - [Pivot Table for Salesperson](#pivot-table-for-salesperson)
      - [Pivot Table for Trend](#pivot-table-for-trend)
   * [Chart <a name = "chart"></a>](#chart)
      - [Chart for Monthly Sales](#chart-for-monthly-sales)
      - [Chart for Region](#chart-for-region)
      - [Chart for Salesperson](#chart-for-salesperson)
      - [Chart for Trend](#chart-for-trend)
   * [Adding Slicer](#adding-slicer)
   * [Dashboard <a name = "dashboard"></a>](#dashboard)
   * [Contribution 🛠️](#contribution-)
 
     <br><br>


## Importing Datasets
1. Import Dataset2.txt into Google Sheets. **[File » Import]**
  ![image](https://github.com/drshahizan/HPDP/assets/108865725/f2a5ec37-8b11-4075-90f2-4e068924440c)

2. Click **Upload >> Browse >> Dataset2.txt**.
   ![image](https://github.com/drshahizan/HPDP/assets/108865725/b151e81e-782d-4341-87f1-28bf85690ed3)

  

3. Click “Replace current sheet”, and then import data.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/777f009c-e01d-4ed4-9b8c-443f5d83cdbc)



4. Use format *"=MONTH(DATEVALUE(H2:H324&1))"* to give value of month based on sales month.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/92522e8f-e41b-432d-887b-8ae1a74e2b68)



5. For those **"#VALUE!"**, we need to correct it by clicking **Ctrl+F**, then type Sept. Then click the three button.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/917370da-89a3-4e41-98de-e7d76904b14a)



6. Type the replace with *Sep*, and click *"replace all"* first, then the *"done"* button.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/99d00787-c3f6-45e9-a60b-d714722adc8a)




   Result Displayed:
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/f998bec5-ad76-4235-9d22-c4753a79b640)


<br><br>

## Pivot Table
### Pivot Table for Monthly Sales

7. Select all columns ( BY CLICK ON CTRL + SHIFT + RIGHT CLICK + DOWN CLICK) and click on **insert » pivot table » new sheet**.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/7563d1e6-a626-4d6b-93e9-46bc780dd511)




8. Choose the Rows variables and value column.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/81335fcf-de6a-4cfd-98ff-08258eb610f1)


    ![image](https://github.com/drshahizan/HPDP/assets/108865725/39e758b5-dbf8-447b-a0e0-63fb8ae2a041)




    
### Pivot Table for Region 

10. Repeat [**Step 7**](#pivot-table-for-monthly-sales) 

11. Select Row and Value.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/3727fb48-82fa-405b-a942-00b9ab88aafb)



### Pivot Table for Salesperson
12. Repeat [**Step 7**](#pivot-table-for-monthly-sales) 
  
13. Edit the pivot table by choosing **row** and **value**.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/4b407df7-ed87-4981-af77-7ddfe0fadb11)
    
14. **NOTE THIS IS FOR PIVOT BY SALESPERSON:** <br>
    Copy the dataset and select the pivot table. Then choose the row and column.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/e7b24520-4b5f-4780-8720-fc003c022969)

15. Select the value to sum the sales by each salesperson.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/e391ac8d-5727-43ac-b99b-f641f08653ac)


### Pivot Table for Trend
16. Repeat [**Step 7**](#pivot-table-for-monthly-sales) 
17. Select **Rows** and **Values**.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/b0fd7968-272a-46fd-b502-a16b355b6ad6)

    ![image](https://github.com/drshahizan/HPDP/assets/108865725/0365f03a-ab07-4f05-b918-65a7ba08d7b3)

18. Copy all the pivot tables [CLICK CTRL+SHIFT+ RIGHT BUTTON +DOWN BUTTON].
    **PASTE** it into a sheet named **"dashboard"**.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/2fb3ee54-fe00-4402-8a83-852f349936f9)

    Result Displayed:
      ![image](https://github.com/drshahizan/HPDP/assets/108865725/bfb51c7e-2924-4e25-9832-befc3a8bd882)

<br><br>

## Chart
### Chart for Monthly Sales
19. Click **Insert » Chart**.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/0b52a7b8-529c-4120-af1f-de9e9104bd67)

20. Choose the **stacked area chart**, then customize it before arranging it into **Dashboard** sheet.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/37a18e02-18d4-4231-b0df-d6815f0204d6)

### Chart for Region
21. Select the **Region** pivot table.
    Then repeat [Step 19](#chart-for-monthly-sales).
22. Customize it before arranging it into the **Dashboard** sheet.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/b202c13a-8971-418a-a838-7902f767d853)

### Chart for Customer
23. Select the **Customer** pivot table.
    Then repeat [Step 19](#chart-for-monthly-sales).
24. Choose **Pie Chart**, then customize it before arranging it into the **Dashboard** sheet.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/522ec5b3-5e37-4c72-b5f2-045f15885c85)

### Chart for Salesperson
25. Select the **Customer** pivot table.
    Then repeat [Step 19](#chart-for-monthly-sales).
26. Choose ** Stacked Column Chart**, then customize it to look more organized and presentable in the **Dashboard** sheet.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/2e659da8-329a-4436-a1a8-c10d4adcce05)


### Chart for Trend
27. Select the **Customer** pivot table.
    Then repeat [Step 19](#chart-for-monthly-sales).
28. Choose **Smooth Line Chart**, then customize it before arranging it into the **Dashboard** sheet.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/a70a694e-37e2-4e57-98cf-e5ed8d3389a5)




<br><br>

## Adding Slicer
29. Click on **Insert** » **Add Slicer**.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/d8a7ccd8-9122-473d-89c7-0774e950178e)

31. Select the appropriate range as below.
    Therefore, all datasets will be selected and linked to the chart.
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/13a216b7-329c-4c38-9623-4555fe535071)

    Otherwise, click one of the pivot tables then choose your column.
      ![image](https://github.com/drshahizan/HPDP/assets/108865725/37aa9a49-7f70-4973-97f2-134964097e85)
      For example, if a customer slicer is about to be created, click on **Customer Pivot Table**, then choose the column of **Customer**.

32. Repeat the [steps](#adding-slicer) for other pivot tables.


<br><br>

## Dashboard
   **Dashboard** successfully created.    
   <br>
    ![image](https://github.com/drshahizan/HPDP/assets/108865725/5b5f1532-708b-467e-a0a3-652a55dba72e)





<br><br>
## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



