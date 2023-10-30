<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1b: Sales performance

### Group Name: (3H) HAHAHA

### Group Members

| Name                                     | Matrix Number | 
| :---------------------------------------- | :-------------: |
| IZZAT HAQEEMI BIN HAIRUDIN | A21EC0033	   |    
| MOHAMAD AZRI HADIF BIN MOHAMMAD RIZAL	              | A21EC0054   |     
| NG SUANG JOO     | A21EC0102   |   
| NG ZI XING | A21EC0213   |      

## Table of Contents <a name = "table-of-contents"></a>
- [Assignment 1b: Sales performance](#assignment-1b-sales-performance)
   * [Table of Contents](#table-of-contents)
   * [Dataset Information](#datasetinfo)
   * [Pivot Table](#pivottable)
   * [Dashboard](#dashboard)
   * [Contribution 🛠️](#contribution-)
  
## Dataset Information <a name = "datasetinfo"></a>
This dataset is called dataset1.txt. This dataset has five columns that contain information about Id_No, Academic, Sports, Co-Curriculum, Test_1 and Test_2. Table 1 shows the full marks for the data

**Source**: 

  
1. Import the Dataset1.txt into Google Sheets, on the left upper menu bar, choose **"File" -> "Import"**.
<p align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/142320760/4e2ac1b6-db4b-49d4-8f50-1fd58ef1e8ea" alt="Image Description">
</p> 

<p align="center">
  For the dataset , we add a new column which is "Month Index" to sort out the month.
  For example, Jan = 1 / Feb = 2 and etc. <br>
  This is made to sort out the month easier for out visualization later on. </p>
<p align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/142320760/9ff9976e-f62e-456c-945e-0fd47b205a63" alt="Image Description">
</p>




<p align="center"> The formula that we inserted into the column is:</p> 

<p align="center">=IF(H2="Jan", 1, IF(H2="Feb", 2, IF(H2="Mar", 3, IF(H2="Apr", 4, IF(H2="May", 5, IF(H2="Jun", 6, IF(H2="Jul", 7, IF(H2="Aug", 8, IF(H2="Sept", 9, IF(H2="Oct", 10, IF(H2="Nov", 11, IF(H2="Dec", 12, 0))))))))))))</p> 

<br>

## Pivot Table <a name = "pivottable"></a>

2. Inserting Pivot Table
   - Click insert and choose pivot table
   ![image](https://github.com/drshahizan/HPDP/assets/101933666/7a31e6db-0e2d-41e2-acf0-822fd94994c3)

     + Select the data range from the dataset2 sheet
     + Insert the pivot table into new sheet name as Dashboard
     + Click create
   
      ![image](https://github.com/drshahizan/HPDP/assets/101933666/7b8f9d63-6469-4b63-a72d-a8978cc930df)

     + Pivot tables are used for creating charts and integrating slicers. They enable data organization and summarization, making it easy to create accurate charts and dynamically filter data using slicers. They save time, ensure consistency, and adapt well to changing data and analysis requirements.
       
4. Monthly Sales
   - Click insert and choose pivot table
     * In Pivot table editor;
       + Rows: click/drag Month Index and Sales Month
       + Values: click/drag Sales and Target
       + Close Pivot table editor

      ![image](https://github.com/drshahizan/HPDP/assets/101933666/780d5648-e3af-485e-9dc7-531fe73c82e7)
      ![image](https://github.com/drshahizan/HPDP/assets/101933666/c95d3400-ff8b-40c9-868f-a6d855cc4d99)

   - Click insert and choose chart
  
        ![image](https://github.com/drshahizan/HPDP/assets/101933666/30d5175c-540c-4305-bfe3-35c33bf1831f)

     * In Chart editor;
       + Chart type: Stacked area chart
       + Stacking: Standard
       + Data range: select the pivot table of Monthly Sales
       + X-axis: Sales Month
       + Series: Sum of Target and Sum of Month
       + Close Chart editor
      
     ![image](https://github.com/drshahizan/HPDP/assets/101933666/5442a30c-0f1e-4c04-a7e2-481fc10b5c25)
         
     ![image](https://github.com/drshahizan/HPDP/assets/101933666/025716d2-40fe-48ee-85ba-359430ab594d)

5. Region
   - Click insert and choose pivot table
     + Select the data range from the dataset2 sheet
     + Insert the pivot table into exisitng sheet name as Dashboard
     + Click create
     * In Pivot table editor;
       + Rows: click/drag Sales Region
       + Values: click/drag Sales
       + Close Pivot table editor
      
      ![image](https://github.com/drshahizan/HPDP/assets/101933666/3ae79d02-b246-4dee-9532-1d6099ef70c6)
         ![image](https://github.com/drshahizan/HPDP/assets/101933666/b20fb4f7-51f6-4e29-a8d1-673e97a416ab)


   - Click insert and choose chart
     * In Chart editor;
       + Chart type: 3D pie chart
       + Data range: select the pivot table of region
       + Label: Sales Region
       + Values: Sum of Sales
       + Close Chart editor
      
      ![image](https://github.com/drshahizan/HPDP/assets/101933666/4664f187-7fa6-4296-a159-263818d42252)
         
      ![image](https://github.com/drshahizan/HPDP/assets/101933666/ec5611a9-542b-4369-8d29-ba8f925271b5)


6. Salesperson
   - Click insert and choose pivot table
     + Select the data range from the dataset2 sheet
     + Insert the pivot table into existing sheet name as Dashboard
     + Click create
     * In Pivot table editor;
       + Rows: click/drag Sales Person
       + Columns: click/drag Product
       + Values: click/drag Sales
       + Close Pivot table editor

      ![image](https://github.com/drshahizan/HPDP/assets/101933666/075c4167-f485-40fa-9507-35c9c6f7c2d1)
         
     ![image](https://github.com/drshahizan/HPDP/assets/101933666/1d425ce5-5223-43d6-b10c-4a47c22e68ff)


   - Click insert and choose chart
     * In Chart editor;
       + Chart type: Stacked column chart
       + Stacking: Standard
       + Data range: select the pivot table of salesperson
       + X-axis: Sales Person
       + Series: Cooking Oil, Flour, Milk, Sugar
       + Close Chart editor
      
      ![image](https://github.com/drshahizan/HPDP/assets/101933666/ad40f920-aeff-4b28-a039-bfcb69c9f1ea)
         
       ![image](https://github.com/drshahizan/HPDP/assets/101933666/56f3826a-dd2d-4540-b394-2248151f2a79)


7.Customer
- Click insert and choose pivot table
     + Select the data range from the dataset2 sheet
     + Insert the pivot table into exisitng sheet name as Dashboard
     + Click create
     * In Pivot table editor;
       + Rows: click/drag Customer
       + Values: click/drag Products
       + Close Pivot table editor
      
         
       ![Customer (1)](https://github.com/drshahizan/HPDP/assets/142320760/ee4eafa7-60fd-4a42-a057-fc12fbaa60b0)
         
       ![Customer (2)](https://github.com/drshahizan/HPDP/assets/142320760/99674fae-0133-4e89-8c49-2e9decf4afcd)

   - Click insert and choose chart
     * In Chart editor;
       + Chart type: 3D pie chart
       + Data range: select the pivot table of region
       + Label: Customer
       + Values: Count Of Products
       + Close Chart editor
      
      ![Customer (4)](https://github.com/drshahizan/HPDP/assets/142320760/74f7b94d-b738-4980-837a-d322fa5a5d99)
      
       ![Customer (5)](https://github.com/drshahizan/HPDP/assets/142320760/89ec8abd-d14e-4f50-93ad-aa51c34a333b)

8.Sales Trend
- Click insert and choose pivot table
     + Select the data range from the dataset2 sheet
     + Insert the pivot table into exisitng sheet name as Dashboard
     + Click create
     * In Pivot table editor;
       + Rows: click/drag Sales Year , Month Index , Sales Month
       + Values: click/drag Sales
       + Close Pivot table editor
      
       ![Sales Trend (1)](https://github.com/drshahizan/HPDP/assets/142320760/39c54aba-83f2-4019-a3b3-725ccba81594)

       ![Sales Trend (2)](https://github.com/drshahizan/HPDP/assets/142320760/e3ef06d9-8a56-4582-bf53-b4b806787bd3)


   - Click insert and choose chart
     * In Chart editor;
       + Chart type: 3D pie chart
       + Data range: select the pivot table of region
       + Label: Sales Month`
       + Values: Sum of Sales
       + Close Chart editor
      
      ![Sales Trend (4)](https://github.com/drshahizan/HPDP/assets/142320760/22aa9055-8cc8-4e7b-a79a-d0b48c6ac959)
         
     ![Sales Trend (3)](https://github.com/drshahizan/HPDP/assets/142320760/fac09837-93aa-4e18-a094-58db968c61db)

9. Total Sales By Year (2020 & 2021)
- Click insert and choose pivot table
     + Select the data range from the dataset2 sheet
     + Insert the pivot table into exisitng sheet name as Dashboard
     + Click create
     * In Pivot table editor;
       + Rows: click/drag Sales Year 
       + Values: click/drag Sales
       + Close Pivot table editor
      
        ![Screenshot 2023-10-25 024705](https://github.com/drshahizan/HPDP/assets/142320760/98a4b91f-0970-4416-820b-0aeba2751920)
        ![Screenshot 2023-10-25 024635](https://github.com/drshahizan/HPDP/assets/142320760/cfaf6be8-be3b-43c5-8c11-58e8e220125f)


   - Click insert and choose chart
     * In Chart editor;
       + Chart type: Scorecard chart
       + Data range: select the pivot table of region
       + Key Values: Sum of Sales (2020) & (2021) cell
       + Close Chart editor
      
      ![Screenshot 2023-10-25 024850](https://github.com/drshahizan/HPDP/assets/142320760/96295019-80c9-4e94-922a-ad74089555d8)
     ![Screenshot 2023-10-25 024758](https://github.com/drshahizan/HPDP/assets/142320760/3716c314-8303-4598-ba46-e2e7062aaf24)

11. Slicer: Sales Year, Sales Region, Sales Products, Customer, Sales Person
    - Click Data
    - Click add a slicer
      
      ![image](https://github.com/drshahizan/HPDP/assets/101933666/7342938a-cba8-44b4-9842-65ed27c53b7f)
      
    - Select data range from dataset2 sheet
    - Column: click sales year

      ![image](https://github.com/drshahizan/HPDP/assets/101933666/bcfacdcb-9819-48b3-9315-5722731d9740)

      ![image](https://github.com/drshahizan/HPDP/assets/101933666/466fbcc4-195d-4b91-ac5d-95ed380d5cfe)




     Copy paste the slicer and change the column with sales region, sales products, customer and sales person

<br>

## Dashboard <a name = "dashboard"></a>

12. Dashboard
    
<br>

<p align="center"><strong><em><u>UNFILTERED</u></em></strong></p>
    <p align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/142320760/f5d0e74d-3cc6-4638-886b-fd725cc4408c" alt="Image Description">


 - **Slicer** : We can filter the charts based on specific criteria, providing a flexible view of the data.
 - **Monthly Sales** : Depicts the monthly target sales and achieved monthly sales
 - **Regional graph** : Offers insights into total sales figures, providing an overview of regional performance.
 - **Customer chart** : Highlights the number of products sold in each store, with data displayed to the left of the pie chart for easy reference.
 - **Salesperson chart** : showcases the quantity of products sold by each salesperson and offers a detailed breakdown of individual product sales for each salesperson.
 - **Sales trend chart** : tracks monthly sales in both 2020 and 2021, facilitating the observation of sales trends over the two-year period.

<br>
<br>
<br>

<p align="center"><strong><em><u>FILTERED</u></em></strong></p>
  <img src="https://github.com/drshahizan/HPDP/assets/142320760/092d288a-6e01-4707-8c84-7d63117235ec" alt="Image Description">
</p>

  - **Salesperson Performance** : We can filter the charts based on specific criteria, providing a flexible view of the data.
  - **Target vs. Actual Sales** : By comparing target sales to actual sales, we can evaluate how well the salesperson is meeting their sales goals.
  - **Sales Trend Analysis:** : The sales trend data enables us to analyze trends in monthly sales, helping us identify peak customer activity and the most sold products.
  - **Customer Analysis** : By deducing where the salesperson's primary customer base is located, we gain insights into regional preferences and demands.
  - **Top-Selling Products** : Identifying the products sold in the highest quantity offers valuable information on product popularity and market demand.
  - **Salesperson Productivity** : By examining target and actual sales, we can assess the salesperson's productivity, identifying areas for improvement and optimization.

<br>
<br>
<br>


## Contribution 🛠️ <a name = "contribution-"></a>
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




