<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1b: Sales performance

### Group Name: (3H) HAHAHA
1. Import the Dataset1.txt into Google Sheets, on the left upper menu bar, choose **"File" -> "Import"**.
<p align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/142320760/4e2ac1b6-db4b-49d4-8f50-1fd58ef1e8ea" alt="Image Description">
</p> 

2. Contain nine column
3. Monthly Sales
   - Click insert and choose pivot table
   ![image](https://github.com/drshahizan/HPDP/assets/101933666/7a31e6db-0e2d-41e2-acf0-822fd94994c3)

     + Select the data range from the dataset2 sheet
     + Insert the pivot table into new sheet name as Dashboard
     + Click create
   
      ![image](https://github.com/drshahizan/HPDP/assets/101933666/7b8f9d63-6469-4b63-a72d-a8978cc930df)
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

9. Slicer: Sales Year, Sales Region, Sales Products, Customer, Sales Person
    - Click Data
    - Click add a slicer
      
      ![image](https://github.com/drshahizan/HPDP/assets/101933666/7342938a-cba8-44b4-9842-65ed27c53b7f)
      
    - Select data range from dataset2 sheet
    - Column: click sales year

      ![image](https://github.com/drshahizan/HPDP/assets/101933666/bcfacdcb-9819-48b3-9315-5722731d9740)

      ![image](https://github.com/drshahizan/HPDP/assets/101933666/466fbcc4-195d-4b91-ac5d-95ed380d5cfe)




     Copy paste the slicer and change the column with sales region, sales products, customer and sales person
10. Dashboard

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




