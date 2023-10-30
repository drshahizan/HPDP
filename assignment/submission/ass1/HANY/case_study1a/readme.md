<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1a: Examination results

### Group Name: HANY
### Group Members

| Name                                     | Matrix Number | Task |
| :---------------------------------------- | :-------------: | :-------------: |
| ALYA BALQISS BINTI AZAHAR             |A21EC0158      | DOCUMENTATION     |
| MUHAMMAD HARITH HAKIM BIN OTHMAN              | A21EC0205     | ANALYSIS     |
|NADIA SYAFIQAH BINTI ZULKIPLI|A21EC0098      | DOCUMENTATION     |
| LIEW YVONNE              |A21EC0045      | VISUALISATION     |

## Table of Contents
1. [Introduction](#1-introduction)
2. [Data Importation](#2-data-importation)
   - 2.1. [Importing a Dataset into Google Sheets](#21-importing-a-dataset-into-google-sheets)
3. [Data Processing](#3-data-preprocessing)
   - 3.1. [Decimal Places Adjustment](#31-decimal-places-adjustment)
   - 3.2. [Transformation of Value](#32-transformation-of-value)
   - 3.3. [Determine the Top Three Values](#33-determine-the-top-three-values)
   - 3.4. [Total Points Calculation](#34-total-points-calculation)
   - 3.5. [Percentage Value Calculation](#35-percentage-value-calculation)
   - 3.6. [Grade Assignment](#36-grade-assignment)
   - 3.7. [Differentiate Status Based on Color](#37-differentiate-status-based-on-color)
4. [Data Visualisation](#4-data-visualisation)
   - 4.1. [Min, Max and Average Values](#41-max-min-avg-value)
   - 4.2. [Grading Results](#42-grading-results)
   - 4.3. [Total Numbers of Records, Pass, and Fail](#43-records-pass-fail)
   - 4.4. [Pass and Fail View in Pie Chart](#44-pass-fail-chart)
5. [Contribution](#5-contribution)





## 1. Introduction 
**CASE STUDY 1: Examination Results** involves working with a dataset named [Dataset1.txt](https://docs.google.com/spreadsheets/d/1MN7NgsUQqE91JiYOJ1nSrjs41kqkYe8twM3xC_PYFrw/edit?usp=sharing), which contains valuable information about students' examination results. The objective of this case study is to use the dataset to carry out a series of data processing tasks. These steps are necessary to enhance the analysis and visualization of examination results using Google Sheets' features. This case study provides an opportunity to explore and analyze student examination results, from data processing to visualization, ultimately assisting in making informed decisions and improvements in academic performance evaluation.

## 2. Data Importation 
### 2.1. Importing a Dataset into Google Sheets 

Before you can create a dashboard or begin analyzing your data, you must first import your dataset into Google Sheets, as shown in Figure 1 and Figure 2. 
  1. Navigate to the **File** menu, and then choose for the **Import** option.
  2. Explore your directory to locate by clicking **Browse**.
  3. Choose for the file named **Dataset1.txt**.
  4. Click on **Open** to bring the data into Google Sheets.
<div align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/87573002/166e8597-288a-47e4-8ca9-54a2f43ab6a7" style="width: 500px; height: 200px;">  
    
**Figure 1: Importing dataset.**   
  <br><br>
  <img src="https://github.com/drshahizan/HPDP/assets/87573002/be3f5ddb-1eca-4457-9ac4-500c9608432c" style="width: 700px; height: 350px;">  
**Figure 2: Inserting file.**   
</div>

  5. Choose **Import Data** and ensure that the **Import location** is set to "Create a new spreadsheet".
<div align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/87573002/7bc4178d-c5ff-4ab0-9978-4432d0b85dd2" style="width: 400px; height: 250px;">
    
**Figure 3: Creating new spreadsheet by importing the data.**  
</div>

  6. The Dataset1 spreadsheet will be displayed as shown in Figure 4.
<div align="center">
  <img src="https://github.com/drshahizan/HPDP/assets/87573002/20ee4e61-358a-4252-b89b-a7a0e08545ed" style="width: 600px; height: 450px;">

**Figure 4: Imported Dataset1 spreadsheet into Google Sheet.**  
</div>

## 3. Data Processing
The following data processing processes must be completed:

### 3.1. Decimal Places Adjustment
   1. Choose the columns labeled **Academic**, **Sports**, **Co-Curriculum**, **Test_1**, and **Test_2** simultaneously as shown in Figure 5 below.
   2. Click the "Increase decimal places" option to convert the data values in the selected columns to two decimal places.
<div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/87573002/de86e86e-6b78-4ce8-9018-1b8efbf57924" style="width: 500px; height: 450px;">
   <br>
   
   **Figure 5: Shows the selected data columns that need to be converted.**  
</div>
      
### 3.2. Transformation of Value
   3. By using the formula shown in **Figure 6**, compute the new value for column B (**Academic**) through F (**Test2**) which the new maximum value is 3.33 for each column.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/48eda989-2b75-49cd-bd9b-cc7bcb50323d" style="width: 145px; height: 30px;"> 
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/f89b3483-e386-4e57-a103-8498065c9ce6" style="width: 145px; height: 30px;">
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/53bd2a16-914d-4bd6-9f9b-4f2ec16bf9aa" style="width: 145px; height: 30px;">

**Figure 6: Shows the formula used for column B to F.**
   <br>
   </div> 

   4. Enter the formula in the new columns, G to K, starting from the second row, following the format illustrated in **Figure 7**. 
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/87573002/f1d7ed26-86fe-42b2-976d-6883ed5fcd73" style="width: 500px; height: 350px;"> 
   <br>
      
   **Figure 7: Illustrates the correct placement for entering the formula.**
   <br>
   </div> 

   5. Double-click the corner dot, "🔵" of the row to ensure that the formula is applied to all rows in the column.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/87573002/83d7e971-1bc0-4e63-bf44-61b09e828898" style="width: 500px; height: 350px;"> 
      
   **Figure 8: Shows the value of row after inserting the formula.**
   <br>
   </div>

   6. Apply the C2 formula for E2 and F2 simultaneously. Then, named the column as **P1**, **P2**, **P3**, **P4** and **P5** simultaneously. The outcomes for these columns are displayed in **Figure 9** below.
<div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/965a0e15-634a-401e-b214-57e95d32bfbd" style="width: 400px; height: 400px;">
   
   **Figure 9: Display the values for column P1 to P5.**
   <br>
</div> 

### 3.3. Determine the Top Three Values
   7. Determine the maximum values from the data in columns G to K using the formula shown in **Figure 10**. Then, named the new columns, L to N as **B1**, **B2** and **B3**.
<div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/a04b939b-2e90-4f16-9122-46b637491ca5" style="width: 145px; height: 30px;">
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/d73e6421-d145-4e5b-840b-19a6574f92a6" style="width: 145px; height: 30px;">
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/91afc21c-d2e8-49a9-8f5a-507c1fff9493" style="width: 145px; height: 30px;">
   <br>
   
   **Figure 10: Shows the formula used to find the highest value of the columns.**
   </div>  
   
   8. The following outcomes of the data values is shown in **Figure 11**. Make sure that the values of column **B1** to **B3** is two decimal places.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/56527951-b23e-46a5-9bd6-60a7b6a2ddf7" style="width: 250px; height: 350px;">
      
   **Figure 11: Display the values for column B1 to B3.**
   </div>   

### 3.4. Total Points Calculation
   9. Calculate the total points by combining the data from columns L to N using the formula used in **Figure 12** below.
<div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/1b51f0f3-53cf-4683-b2a2-31a73d57ec13" style="width: 145px; height: 30px;">
   
   **Figure 12: Shows the formula to calculate total point of selected columns L to N.**
   <br>
   </div>
   
   10. The outcomes of the formula used must be inserted to a new column O, named **TM**. Then, make sure that the decimal places is set to two decimal places as shown in **Figure 13**.
   
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/4070a62b-459e-44ee-8f04-4b12b1a33946" style="width: 100px; height: 400px;">
      
   **Figure 13: Display the new column named TM.**
   <br>
   </div> 

### 3.5. Percentage Value Calculation
   11. Using the formula below, compute the percentage value for the data in column O. 
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/cf14d79d-0c70-459e-a7a5-7703c6b4f84a" style="width: 120px; height: 30px;">
   
   **Figure 14: Shows the formula to calculate the percentage for TM column.**
   <br>
   </div>
   
   12. As a result, a new column entitled **Percent** will be created.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/eb5cc4c1-9df5-4714-b815-d886fe83a3b4" style="width: 90px; height: 350px;">

   **Figure 15: Display the Percent column.**
   <br>
   </div>

### 3.6. Grade Assignment
   13. Assign the **Grade** and **Status** for the marks according to the given formula. 
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/4ac87301-d137-4eb6-bf62-7c35ffe7ab35" style="width: 1745px; height: 56px;">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/c45c123d-7bf6-4714-ac22-582bfbacad45" style="width: 1608px; height: 66px;">
   <br>
   
   **Figure 16: Display the formula used to assign Status and Grade respectively.**
   </div>

   14. As illustrated in **Figure 17**, the results of the assignment for **Grade** and **Status** will be placed in columns Q and R.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/340ed0cb-bb6c-4e4e-8efc-70457454c0bf" style="width: 100px; height: 400px;"><img src="https://github.com/drshahizan/HPDP/assets/106257072/dca3f4a6-3bde-465a-a56d-603062ab749c" style="width: 100px; height: 400px;">

   **Figure 17: Shows the Grade and Status column.**
   </div>
   
### 3.7. Differentiate Status Based on Color
   15. Click **Format** to differentiate the **Status**. Then, select **Conditional formatting**.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/87573002/2eaf0e9b-ef89-4b9c-aa02-f9d2016a5a41" style="width: 400px; height: 350px;">
      
  **Figure 18: Shows the format for conditional formatting.**
   <br>
   </div>
   
   16. Change the color of the formating style to green for "Status=Pass" and red for "Status=Fail" as illustrated in **Figure 19** below.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/87573002/7d456488-3016-42b8-8ec7-ad0b8f04edbb" style="width: 450px; height: 500px;"> <img src="https://github.com/drshahizan/HPDP/assets/87573002/b0b57aee-2441-4a12-b664-0ff3c6c4002a" style="width: 450px; height: 500px;">
   
   **Figure 19: Shows the setting for the colour formatting.**
   </div>

## 4. Data Visualisation
   1. To start visualizing the data, select the dataset which is **Dataset1**.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/86d0ed2b-a39e-41b0-b034-81cb872c63ed" style="width: 300px; height: 45px;">

   **Figure 20: Display the selected dataset.**
   <br>
   </div>
   
   2. At the top of Google Sheets, click **Insert** and then select **Chart**.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/87573002/14ec7605-cba6-45e2-b69a-0a414425865a" style="width: 450px; height: 300px;">
   <br>

   **Figure 21: Display the Insert chart option.**
   </div>

   3. Choose **Setup** to select the desired chart type.
   <div align="center">  
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/539423ab-4203-40e2-a24a-3e88ee7a02bf" style="width: 400px; height: 450px;">
   <br>
      
   **Figure 22: Displays the Setup option, which includes several chart.**
   </div>

### 4.1. Min, Max and Average Values
   4. Set the **Setup** as indicated in **Figure 23** below by clicking **Chart editor**. Check the **Aggregate** and **Use row 2 as headers** boxes. Then select the **Min** option.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/c0268e95-d7f4-4ba2-888c-03dd79bfa9fe" style="width: 300px; height: 450px;">
   <br>
      
   **Figure 23: Displays the setup of chart editor.**
   </div>
   
   5. Choose the **Chart & axis titles**. Select **Chart Title** option and customize the **Title Text** to **Min**. The value of Min will be display as shown in **Figure 25**.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/bf535eb6-1a4d-4098-ada8-3edbb12c57fd" style="width: 350px; height: 400px;"> 
   <br>

   **Figure 24: Customization of the chart editor.**
   <br>
  
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/8e93cba1-4676-4578-9e95-b32ba7bf82df" style="width: 200px; height: 100px;">

   **Figure 25: Shows the value of Min.**
    </div>
    
   6. Next, determine the maximum value by repeating step 4-5 with **Max** option as shown in **Figures 26 and 27** below. Then, it will be displayed as shown in **Figure 28**.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/acd7b8a3-590d-476a-9a2c-db28a9d2b1ea" style="width: 300px; height: 500px;"> 
   <br>
      
   **Figure 26: Displays the setup of chart editor.**
   <br>
   
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/2a0eee56-1129-431f-a2d8-4a84df58f827" style="width: 350px; height: 400px;">

   **Figure 27: Customization of the chart editor.**
   <br>
   
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/05b16016-153b-45ca-80cc-5db09dad5b16" style="width: 200px; height: 100px;">
   <br>

   **Figure 28: Shows the value of Max.**
   </div>

   7. To get an average result, repeat steps 4-5 with the **Average** option, as shown in **Figures 29 and 30**. **Figure 31** illustrates the outcome of the presented average value.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/9997c395-c404-4076-9fc8-5a00a38b7e02" style="width: 300px; height: 500px;">
   <br>

   **Figure 29: Displays the setup of chart editor.**
   <br>
   
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/31b0f553-47c0-4d27-9297-335c04a5394a" style="width: 350px; height: 400px;">
   <br>

   **Figure 30: Customization of the chart editor.**
   <br>
   
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/1e3d96f7-1ca1-4175-a2f0-37c01239f4ca" style="width: 200px; height: 100px;">
   <br>

   **Figure 31: Display the value of Average.**
   </div>
         
### 4.2. Grading Results
• Display grading results as tables.

   8. Create a table listed from **Grade A+** to **E** and total numbers of record as shown in **Figure 32**. 
   <div align="center">
         <img src="https://github.com/drshahizan/HPDP/assets/106257072/a31e3d4b-9c3c-42a8-904e-d820aeb6eee7" style="width: 100px; height: 300px;">
         <br>
      
   **Figure 32: Display the list of grade.**
         <br>
    </div>
    
   9. Formula in **Figure 33** is used to calculate the total numbers of each grade while formula in **Figure 34** is used to calculate the total numbers of record. **Figure 35** illustrates the outcome of the table.
   <br><br>
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/6216c889-c2a6-4eb2-bd3a-4a084b02d492" style="width: 350px; height: 30px;">
   <br>
      
   **Figure 33: Shows the formula used.**      
   <br>
   
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/d8bb7748-55c7-4142-9dc8-4992331956d1" style="width: 150px; height: 30px;">
         
   **Figure 34: Shows the total number of records formula.**     
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/5877d835-2678-49b1-aa7a-99574043f06c" style="width: 150px; height: 300px;">
   <br>
         
   **Figure 35: Display the outcomes in column Data.**     
   </div>

• Display grading results as charts.  

10. Click to the selcted column as shown in Figure 36 below and make sure that the **Aggregate** box is check. 
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/86b7b25d-1d1a-4489-9170-f88ff0daf434" style="width: 300px; height: 500px;">
   <br>
      
   **Figure 36: Displays the setup of chart editor.**
   <br>
   </div>
   
   11. Click the **Customize** option, to rename the **Vertical axis title** to **Num. of Students (10K)** and the **Chart Title** to **Grading**
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/3f1fdf2d-3007-4603-9610-cf93c184511a" style="width: 300px; height: 350px;"> <img src="https://github.com/drshahizan/HPDP/assets/106257072/c6ef4588-60b3-46b1-bb2a-7e16af11b9df" style="width: 300px; height: 350px;">
   <br>
      
   **Figure 37: Displays the customize of chart editor.**
   <br>
   </div> 

   12. Next, click the **Chart & axis titles** and select the **Horizontal axis title** option.
   13. **Title text** should be renamed as **Grade**.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/28d4fb18-91d7-4c43-8343-2199158b1229" style="width: 300px; height: 350px;"> <img src="https://github.com/drshahizan/HPDP/assets/106257072/02399022-a355-4121-92d8-acb3208a1548" style="width: 300px; height: 350px;">
   <br>

   **Figure 38: Displays the customize of chart editor for the axis.**
   <br>
   </div>

   14. The chart will be display as shown in Figure 39.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/2e044717-3cd1-4615-bba3-32ef75300cab" style="width: 500px; height: 350px;">
   <br>

   **Figure 39: Displays the grading chart.**
   <br>
   </div>
   
### 4.3. Total Numbers of Records, Pass, and Fail
• Total Records  

   15. As illustrated in **Figure 40**, click **Setup** for the selected column and check the **Aggregate** and **Use row 1 as headers** boxes. The whole record will then be displayed, as seen in **Figure 41**.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/77374422-462d-45f5-b56b-7bb039654608" style="width: 300px; height: 500px;">
   <br>

   **Figure 40: Displays the setup for chart editor.**
   <br>
   
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/dc6c336e-4670-4127-864a-4e0e92cddb73" style="width: 350px; height: 150px;">
   <br>

   **Figure 41: Shows the Total Record.**
   </div>

• Total Numbers of Pass 

   16. Create new sheet named **Statistic**.
   <div align="center">
      <img src="https://github.com/drshahizan/HPDP/assets/106257072/ae88cc45-d12f-407d-86c9-fb6824faa04f" style="width: 500px; height: 55px;">
      
   **Figure 42: Display the Statictic sheets.**
   <br>
   </div>
   
   17. Formula in **Figure 43** is used to calculate the percentage while formula in **Figure 44** is used to calculate the total numbers of fail and pass.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/2b84b43e-c619-4705-ac17-ff93f3ceedb1" style="width: 500px; height: 30px;">
   <br>
      
   **Figure 43: Shows the formula to calculate the percentage.**
   <br>
   
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/2f29cd10-b28f-4a44-835c-8153a1077a57" style="width: 600px; height: 30px;">

   **Figure 44: Shows the formula used to calculate to numbers of fail and pass.**
   <br>
   </div>
   
   18. **Figure 45** shows the result.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/920dce38-1307-4054-b7fb-806caf72ad1f" style="width: 400px; height: 85px;">
      
   **Figure 45: Result of the Percentage and Total Records.**
      <br>
</div>
      
   19. The percentage scorecard chart is a combination of two scorecard charts. One is to display the percentage of pass and fail, another is to display the total records of pass and fail. 
   20. To make a scorecard chart, choose **Scorecard chart** at chart type. Then choose the data range that is required for the chart, which is the data that is calculate in the Statistic sheet. At the Key Value, choose "Sum", as shown in **Figure 46**.
      <br>
   <div align="center">
      <img src="https://github.com/drshahizan/HPDP/assets/106257072/822904f4-bae0-404f-8de5-e9cafd6f5d8f" style="width: 300px; height: 450px;">
   
   **Figure 46: Shows the setup of the chart editor.**
   </div>
      <br>
      
   21. At **Customize**, expand **Key Value** and choose **Custom** for Number Format. Then, put **"%"** at suffix.
   <div align="center">
      <img src="https://github.com/drshahizan/HPDP/assets/106257072/5c923354-d001-43d1-b9c0-b41ed8b1fcf2" style="width: 300px; height: 500px;">

   **Figure 47: Shows the customize setting of the chart editor.**
   </div>
      <br>
      <br>

   22. For number of records, is the same as doing the scorecard chart for percentage value. A slight difference is the Number Format, put **"records"** instead of "%" as shown in **Figure 49**. **Figure 50** shows the result of combining two scorecard charts.
      <br>
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/7d4d6cff-7d3a-430d-b903-b1a81ad20649" style="width: 300px; height: 450px;">

   **Figure 48: Display the chart editor for scorecard chart.**
      <br>
      
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/30973090-a9f3-4636-8141-b18d72cc818c" style="width: 300px; height: 500px;">
   
   **Figure 49: Display the customize of chart editor.**
   <br>
   
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/c97af60a-303a-41d7-b358-5f9c9990d1da" style="width: 300px; height: 150px;">
      
   **Figure 50: Percentage for pass records.**
      <br>
   </div>

• Total Numbers of Fail

   23. Repeat steps from **23-25** to do another scorecard chart for total records of fail.
   <div align="center">
   
   <br>
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/f1ccb9da-9688-4f7c-aa84-158576a77a87" style="width: 300px; height: 500px;">
   
   **Figure 51: Display the setup of chart editor.**
   <br>
   
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/9fd9349a-54db-4af2-b2c3-2ffdc8d35b27" style="width: 300px; height: 500px;">

   **Figure 52: Display the customization of chart chosen.**
   <br>
   
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/4231b14c-e2d9-4dea-b5f7-4e814aee2b12" style="width: 300px; height: 500px;">

   **Figure 53: Display the chart editor's configuration.**
   <br>
   
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/bae1386b-4456-4022-aa62-06b19b9957c0" style="width: 300px; height: 500px;">

   **Figure 54: Display the chart's customization.**
   <br>
   
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/b204d576-67a8-44be-a5c0-574e4c94165e" style="width: 300px; height: 150px;">

   **Figure 55: Shows the Percentage for fail records.**
   <br>
</div>

### 4.4. Pass and Fail View in Pie Chart

   24. To make a pie chart, choose **"Doughnut chart"** at Chart Type, then choose the data range required. Tick **Aggregate**. **Figure 56** shows the final settings.
<div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/6583fa91-920e-4179-a221-a8a46b8d2078" style="width: 300px; height: 400px;">

   **Figure 56: Setup for the Doughnut chart.**
</div>
   <br>
   
   25.  The final result of the Doughnut chart is shown in **Figure 57**.
   <div align="center">
   <img src="https://github.com/drshahizan/HPDP/assets/106257072/e287404a-da5c-456c-a77a-fdcee890cd5c" style="width: 200px; height: 150px;">

   **Figure 57: Result of fail and pass doughnut chart.**
   <br>
</div>

   26. Overview of the Dashboard is shown in **Figure 58** below.
   <div align="center">
    <img src="https://github.com/drshahizan/HPDP/assets/87573002/31763f1d-b756-4e00-85eb-1f33c79d3776" style="width: 800px; height: 300px;">

   **Figure 58: The dashboard of case study.**
   <br>
</div>

## 5. Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)



