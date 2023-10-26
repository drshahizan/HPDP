<div align="center">

# Assignment 1: Data Analysis using Google Sheets
## Dataset 1 Report

</div>


---

### 🍀Group Name: sheemart
### 🌼Group Members

| Name                                     | Matrix Number | 
| :---------------------------------------- |--------------|
| MUHAMMAD AMIR JAMIL BIN JAMLUS | A21EC0202 |              
| MUHAMMAD NAQUIB BIN ZAKARIA | A20BE0161 |              
| MUHAMMAD HAZIM BIN SALMAN | A21EC0078 |              
| NURUNNAJWA BINTI ZULKIFLI | A21EC0121 |                  

------

## Dataset Information

We work with a dataset called dataset1.txt. This dataset has five column that contain information about Id_no, Academic, Sports, Co-curiculum, Test_1 and Test_2.

---

## 1. Import dataset into Google Sheet


<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/96f95fff-a9e4-4864-a031-bf3dc30c80ad"  width = "400">
</p>

<div align="center">
  
_Figure 1: Import the data_

</div>


- After opening Google Sheet, click on **File** and choose **Import**.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/ab5caf43-26f0-4553-a10e-e53e97b2f043" width = "400">
</p>

<div align="center">
  
_Figure 2: Choose your data_

</div>

- Choose **Browse** and choose 'Dataset1.txt' as our dataset.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/d98a6b2b-0750-4eff-bc2b-75d20c3ccd3d"  width = "400">
</p>
  
<div align="center">
  
_Figure 3: Import data_

</div>

- Choose '**Replace in current sheet**' as Import location and '**Detect automatically**' as separator type. Check on the checkboard. Then, click Import Data.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/8cc5a7e5-f0f7-44e6-8911-d34385360f96"  width = "400">
</p>

<div align="center">
  
_Figure 4: Database imported successfully_

</div>

- The database has imported successfully.
  
----

## 2. Perform data processing
#### i. Convert the Academic, Sports, Co-Curriculum, Test 1 and Test 2 data values to two decimal places.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/2ae18c09-70d7-4de1-975e-141a90cbd05f" width = "400">
</p>

<div align="center">
  
_Figure 5 : Convert the value to two decimal places_

</div>

- Click **Ctrl+ Shift** and click on Academics table, Sports, Co-Curriculum, Test 1 and Test 2. Then, click on **increase decimal place** button on the ribbon one time.

-----

#### ii.	Please provide a new value for columns B (Academic) through F (Test 2), with the new maximum value of 3.33 for each column. Please update the values in columns G (P1) to K (PS) (refer to Table 2 and Figure 2). Values are displayed to two decimal places.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/6de5b0fb-cd84-40e8-a426-26ef9bb014e1" width = "400">
</p>

<div align="center">
  
_Figure 6 : Add column P1 in on the sheet_

</div>

- **Add** column P1, P2, P3, P4 and P5
- For **column P1**, use formula =(B2/61)*3.33. This formula calculates the normalized value for the first academic column (P1) based on the value in B2 (which represents the row number) and considering 61 as the full mark for the Academic column. The maximum value is set to 3.33.
- **Continue** to calculate the value of P2 until P5 by using
  -  P2 = (C2/61)*3.33
  -  P3 = (D2/10)*3.33
  -  P4 = (E2/15)**3.33
  -  P5 = (F2/15)*3.33
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

- These instructions guide the user to calculate normalized values for academic columns P1 to P5 based on specific formulas.
- Each formula divides the corresponding academic score by the full mark for that column and then scales the result to a maximum value of 3.33, ensuring consistent representation of academic performance across different columns.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/b37b0731-9fc3-402c-816f-8ab3adb82158" width = "400">
</p>

<div align="center">
  
_Figure 7: The output of the data_

</div>

----

#### iii. Determine the top three values based on the values in columns G to K. Fill in the highest value in column L (B1), the second highest value in column M (B2), and the third highest value in column N (B3)

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/69a28f08-53d2-4773-812a-66d4b58ea695" width = "400">
</p>

<div align="center">
  
_Figure 8: Output of B1,B2,B3_

</div>

- **Add** column B1, B2 AND B3.
- For **column B1**, use formula

-   *=LARGE(UNIQUE(G2:K2),1)*
  
- The reason behind this formula is to find the first highest mark of P1 until P5 in column L (B1).
- **Continue** to calculate the value of B2 until B3 by using
  - B2 = *LARGE(UNIQUE(G2:K2),2)*
  - B3 = *LARGE(UNIQUE(G2:K2),3)*
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

- These instructions guide the user to add columns B1, B2, and B3 and use specific formulas to calculate the top three highest marks from the range G2 to K2.
-  B1 calculates the highest mark, B2 calculates the second-highest mark, and B3 calculates the third-highest mark.
- The LARGE function combined with UNIQUE helps identify these top marks, aiding in the analysis of the dataset.

------

#### iv. Compute total points by combining the data from column L to N. The total mark value is entered in column O (TM).

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/190c0f40-3524-4b60-8e9a-ca9841b97f5d" width = "400">
</p>

<div align="center">
  
_Figure 9 : Output of TM_

</div>


- **Add** column **TM**.
- For **column TM**, use formula
  
   *=SUM(L2,M2,N2)1)*
  
- The reason behind this formula is to find the total of COLUMN  L2, M2 and N2.
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

- This instruction directs the user to add a new column titled TM and populate it with a formula that calculates the sum of values in columns L, M, and N for each row. The SUM function is used to perform this calculation, providing the total marks for each corresponding entry in the dataset.
------

#### V. Please calculate the percentage value for data in the column O. In column P, enter percentage value (Percent). Check that the percentage value is within two decimal places.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/c6152175-33ab-4475-806d-6115dd9a4a20" height= "400">
</p>

<div align="center">
  
_Figure 10 : Output of Percentage_

</div>

- **Add** column **Percentage**.
- For **column Percentage**, use formula
  
  *=ROUND(O2*10, 2)*
  
- The reason behind this formula is to find the percentage of of column TM within two decimal places.
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

- These instructions guide the user to create a new column called Percentage and calculate percentages based on the values in column O. The formula multiplies the value in cell O2 by 10 and rounds the result to two decimal places, effectively providing the percentage representation.
  
  -------

 #### vi. Based on Table 3, assist a grade, Column Q is for grade, and column R is for status.

<p align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/89633522/f08923f8-c81f-40e4-bfc6-2a8d49176fc1"  height = "400">
</p>

 <div align="center">
  
_Table 3_

</div>

 <p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/76216ecc-40f8-4757-b831-ccd0d9387ff1" height= 400">
</p>

<div align="center">
  
_Figure 10: Output of Grade_

</div>

- **Add** column **Grade**.
- For **column Grade**, use formula
  
- *=IF(P2 >= 90, "A+", IF(P2 >= 80, "A", IF(P2 >= 75, "A-", IF(P2 >= 70, "B+", IF(P2 >= 65, "B", IF(P2 >= 60, "B-", IF(P2 >= 55, "C+", IF(P2 >= 50, "C", IF(P2 >= 45, "C-", IF(P2 >= 40, "D+", IF(P2 >= 35, "D", IF(P2 >= 30, "D-", "E"))))))))))))*
  
- The reason behind this formula is to find the grade based on the mark given.
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.

- These instructions guide the user to add a new column called Grade and populate it with grades based on a specific grading formula. The provided formula assesses the mark in cell P2 and assigns the corresponding grade. 

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/e0a94d7c-0144-4102-8620-662178ba21ff"  height = "400">
</p>

<div align="center">
  
_Figure 11: Output of status_

</div>

- **Add** column **Status**.
- For **column Status**, use formula *=IF(OR(Q2="B", Q2="B+", Q2="A", Q2="A-", Q2="A+"), "Pass", "Fail")*
- The reason behind this formula is to find the statsu based on the mark and grades given.
- Press **Ctrl + D** to fills and overwrites a cell(s) with the contents of the cell above it in a column.


------

 #### vii. If the status is Pass, please colour column P with Green, You should colour the Pass line with light red.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/4e6d702f-5d90-4bff-ba16-bed7bb3ee6b2" height ="400" >
</p>

<div align="center">
  
_Figure 12: Green colour with Pass status and Light Red for pass line_

</div>

- **Choose** *Fill color* on the ribon.
- **Select** respective line to fill in the colour.
-  Fill in *green colour* for *column P with status Pass*.
-  Fill in *light red* for *Pass line*

----

## Output of the data

<p align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/89633522/33d3ef01-ccd6-4dca-9d19-3ca09cf7366e" width ="700">
</p>

<div align="center">
  
_Figure 13 : Final ouput of the sheet_

</div>

<p align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/89633522/536afc26-de8a-4fdb-9f42-36733e62b7b8" width ="700">
</p>

<div align="center">

_Figure 14 : Final ouput of the sheet_

</div>

-------

# 3. Create Dashboard in Google Sheet.

#### i. Create minimum, maximum and average.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/3c455373-496c-458e-8e50-2756f5eaa05c"  width="300">
</p>


<div align="center">
  
_Figure 15 : Choose pivot table_

</div>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/ef3f09fe-5da6-424c-91f5-2d91272a362a"   width = "300" >
</p>

<div align="center">
  
_Figure 16 : Create pivot table_

</div>

- Access the pivot table function from the Insert ribbon. Specify the appropriate dataset as the data range and select a new sheet as the destination under the Insert to section. Finally, click the **Create** button to generate the pivot table.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/d564a9d3-b851-4871-8da6-b48cc6f942fa"  height="300" >
</p>

<div align="center">
  
_Figure 17 : Output of pivot table_

</div>

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/ffe72b0a-85b6-4e7d-ad82-c011c516dc9d" width="500">
</p>


<div align="center">
  
_Figure 18 : Setup of chart_

</div>

- **Customize** the setup by using the information below
    - **Chart type** : Scorecard chart
    - **Data range** : A1:A6905.A2:A6903
    - **Combine ranges** : Horizontally
    - **Key Value** : Percent and choose either **'min', 'average' and 'max'**
    - **Tick** on 'Aggregate' and choose Min at the dropdown.

- **Drag and drop Percent** into the Rows section. Set the order to  **Ascending** and sort by **Percent.** Tick on the **Show totals**.

- These instructions outline the steps to customize a data visualization, specifically a scorecard chart. The user is advised to set the chart type, define the data range, and aggregate the data based on the chosen key value ('min', 'average,' or 'max').
  
- Dragging and arranging the 'Percent' field in ascending order and displaying the totals allow for a clear and organized presentation of the data, aiding in better analysis and understanding.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/61d5a63e-8dd3-4543-8cc6-0ed83c4b48e5" width="600">
</p>

<div align="center">
  
_Figure 19 : Change of scoreboard title_

</div>

- By click on **Customize**, please choose **Chart & axis titles**. Enter either **Min , Average or Max** for the title text

  <p align="center">
      
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/65d190e2-025c-4b2f-9d8e-65015c0480c5"  height="400">
    
  </p>

<div align="center">
  
_Figure 20 : Output of Min, Average and Max_

</div>

-----------------

#### ii. Display grading results as charts and table.


<p align="center"> 
    
<img width="155" alt="Screenshot 2023-10-25 201251" src="https://github.com/drshahizan/HPDP/assets/89633522/076ae197-a861-49b7-936b-af6e9001f672" height="400">

</p>

<div align="center">
  
_Figure 21 : Create pivot table of grading results_

</div>

- In the Pivot Table Fields, place the Grade field in the Rows section. 
  Arrange it in ascending order and sort the data by grades. Enable the 
  option to display totals for comprehensive insights.

- In the Values section, include the "Id_No (numerical) data to further 
  enrich the analysis, providing a numerical perspective alongside the 
  graded information.

 <p align="center"> 
<img  alt="Screenshot 2023-10-25 201353" src="https://github.com/drshahizan/HPDP/assets/89633522/4f8e6659-da3a-408e-9948-155b3871207b" height="400">
 </p>
 
<div align="center">
  
_Figure 22 : Output of table of grade and num_

</div>

- The table above show the result of table of grade and num.


<p align="center"> 
<img  alt="Screenshot 2023-10-25 201353" src="https://github.com/drshahizan/HPDP/assets/89633522/8d6c9b7c-e5af-44ca-847b-0b01a7318ca6" width = "600">
 </p>
    

</p>

<div align="center">
  
_Figure 23 : Choose column chart for grading_

</div>

<p align="center"> 
    
<img  alt="Screenshot 2023-10-25 201353" src="https://github.com/drshahizan/HPDP/assets/89633522/4c3402fa-1b27-475d-9b53-c921047695a4" width = "600">

</p>

<p align="center">
    
</p>

<div align="center"> 
    
_Figure 24 : Fill in different colour for each grade_

</div>

-  Selecting the right chart type is important. Column charts are excellent for comparing values across different categories, making them suitable for various analytical purposes.
  
-  To choose chart type, In the Chart Editor on the right, click on **'Setup'**. Under **'Chart type'**, select **'Column chart'**.
  
-  It ensures the data is visualized in a way that emphasizes comparisons between different categories, enhancing the viewer's understanding.

-  To colour the columns, Click on a column to select them all. Right-click and choose **'Format data series'**. Under **'Fill color'**, pick the color that desire.
  
-  This differentiation aids in emphasizing specific data points, patterns, or trends, making it easier for viewers to identify and interpret critical information within the chart.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/5b81e60a-fbd5-4520-85b9-21e4ef7a8c2a.jpg" width = "600">    
</p>

<div align="center">
  
_Figure 25 :Output for grading chart_

</div>

---

#### iii. Show the total number of records. Please display Pass and Fail in the form of a percentage and the number of records.

<p align="center">
<img width="176" alt="Screenshot 2023-10-25 204900" src="https://github.com/drshahizan/HPDP/assets/89633522/37b9efcd-f280-4286-9e5d-70f5b588f697">
</p>

<div align="center">
    
_Figure 26_

</div>

<p align="center">
<img width="147" alt="Screenshot 2023-10-25 205008" src="https://github.com/drshahizan/HPDP/assets/89633522/310f1788-cced-4cf0-a7fc-00252d129bdb">
</p>

<div align="center">
    
_Figure 27_

</div>


- In the pivot table, place **'Status'** in the rows section. In the columns section, add **'id_no' (number of students)**, and summarize it by count, which is the default setting. Additionally, include **'Id_no (percent)'** and display it as a **percentage of grades**.

-  Therefore, the pivot table effectively communicates the distribution of student statuses, provides numerical insights into the number of students in each category, and offers a percentage-based view for a comprehensive understanding of the grade distribution among students.
  
<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/901dafcc-9485-4b88-ba51-b0275e727013" width = "400">    
</p>

<div align="center">
    
_Figure 28 : Result of pivot table of total record, fail percentage and pass percentage_
</div>

------------------

#### iv. Create Pass and Fail views in the form of pie chart as well.

<p align="center">
<img width="233" alt="Screenshot 2023-10-25 210737" src="https://github.com/drshahizan/HPDP/assets/89633522/49999457-6518-45e2-b130-d0fdee4753e0">
</p>

<div align="center">
    
_Figure 29 : Doughnut chart setup_

</div>

- Place the **'Status'** field in the **Label** section and select the option to use row 6 as headers, providing clear labels for each column of data.

- Also, check the box for using column **K** as labels. This configuration ensures that the values from column K will provide specific identifiers or descriptors for the rows, enhancing the clarity and context of the information presented in the pivot table.

<p align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/89633522/7e105f35-6b3a-49dd-a5ea-b2a2719601be" width = "600">    
</p>

<div align="center">
    
_Figure 30 : Doughnut chart output_

</div>

------------

# 4. Final Result


<p align="center">
    <img width="808" alt="Screenshot 2023-10-25 210849" src="https://github.com/drshahizan/HPDP/assets/89633522/8c059463-bd43-4daa-bdd7-55afedad5025">
</p>

<div align="center">
    
_Figure 31 : Final Result_

</div>



  




 
