<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1a: Examination results

### Group Name: BYTE NAVIGATORS
### Group Members

| Name                                     | Matrix Number | Task |
| :---------------------------------------- | :-------------: | ------------- |
| LOO ZHI YUAN            |A21EC0197      |Data Preprocessing|
| SOO WAN YING              |A21EC0227      |Documentation      |
| LAU YEE CHI              |A21EC0042      |Visualization     |

### Table of Contents
+ [Import Dataset](#dataset_import)
+ [Data Preprocessing](#dataset_preprocessing)
+ [Data Processing](#dataset_processing)
+ [Create Dashboard](#create_dashboard)
  + [Pass and Fail Views](#passfail_dashboard)
  + [Total Number of Records](#total_dashboard)
  + [Pass Percentage](#pass_dashboard)
  + [Fail Percentage](#fail_dashboard)
  + [Maximum Value](#max_dashboard)
  + [Minimum Value](#min_dashboard)
  + [Average Value](#avg_dashboard)
  + [Number of Students and Grades](#numstu_grades_dashboard)
  + [Total Number of Grades](#grade_dashboard)
+ [Dashboard](#dashboard)
+ [Contributions](#contribution)

## Import Dataset <a name = "dataset_import"></a>
1. Click on the **"File"** menu and select **"Import"**.
<p align="center"><img align="center" alt="Coding" width="400" src="import.jpeg"></p>
<p align="center"> <em> Figure 1: Import data </em> </p> 

2. Click on the **"Upload"** and select the file to import from computer.
<p align="center"><img align="center" alt="Coding" width="400" src="importselectfile.jpeg"></p>  
<p align="center"> <em> Figure 2: Upload data </em> </p> 

3. Click **"Import data"** button after configuring the setting.
<p align="center"><img align="center" alt="Coding" width="400" src="importfile.jpeg"></p>
<p align="center"> <em> Figure 3: Import data </em> </p> 

4. The data was imported sucessfully.
<p align="center"><img align="center" alt="Coding" width="400" src="afterimport.png"></p>
<p align="center"> <em> Figure 4: Dataset1 imported successfully </em> </p> 

## Data Preprocessing <a name = "dataset_preprocessing"></a>
1. Select the range of cells that contain data need to be convert to 2 decimal places and click on the **"Format"**, and select **"Number"**.
<p align="center"><img align="center" alt="Coding" width="400" src="numberformat.png"></p> 
<p align="center"> <em> Figure 5: Convert the data to 2 decimal places </em> </p> 

2. The data values was displayed in two decimal places.
<p align="center"><img align="center" alt="Table" width="400" src="numberformatdone.png"></p>
<p align="center"> <em> Figure 6: The data converted to 2 decimal places </em> </p> 

## Data Processing <a name = "dataset_processing"> </a>
1. Use function **"=(B2/61*3.33)"** to update the new maximum value of 3.33, same procedure apply to column H **"(=C2/10*3.33)"**, I **"(=D2/15*3.33)"**, J **"(=E2/10*3.33)"**, and K **"(=F2/10*3.33)"** with different function.
<p align="center"><img align="center" alt="Equation" width="200" src="newvalue.png"></p>
<p align="center"> <em> Figure 7: Function used to update the new maximum value </em> </p> 
<p align="center"><img align="center" alt="Equation" width="200" src="newvaluedone.png"></p>
<p align="center"> <em> Figure 8: The updated data with new maximum value </em> </p> 

2. Use function **"=LARGE(data,n)"** to find the highest, second highest and third highest value for column G to K.
<p align="center"><img align="center" alt="Equation" width="200" src="largest.png"></p>
<p align="center"> <em> Figure 9: Function used to find the highest value </em> </p> 
<p align="center"><img align="center" alt="Table" width="200" src="largestdone.png"></p>  
<p align="center"> <em> Figure 10: The updated data with  B1 is the highest, B2 is the second highest and B3 is the third highest</em> </p> 

3. Use function **"=SUM(value1)"** to calculate the total point for column L to N.
<p align="center"><img align="center" alt="Equation" width="200" src="sum.png"></p> 
<p align="center"> <em> Figure 11: Function used to calculate the sum </em> </p> 
<p align="center"><img align="center" alt="Table" width="200" src="totalpoint.png"></p>  
<p align="center"> <em> Figure 12: The total point was calculated for each row </em> </p> 

4. Multiply the value in column O with 10 to calculate the percentage in column P.
<p align="center"><img align="center" alt="Equation" width="200" src="percentage.png"></p>
<p align="center"> <em> Figure 13: Function used to calculate percentafe </em> </p> 
<p align="center"><img align="center" alt="Table" width="200" src="percentagedone.png"></p>
<p align="center"> <em> Figure 14: The caulcuated percentage </em> </p> 

5. Use function **"=IF(P2>=90,"A+",IF(P2>=80,"A",IF(P2>=75,"A-",IF(P2>=70,"B+",IF(P2>=65,"B",IF(P2>=60,"B-",IF(P2>=55,"C+",IF(P2>=50,"C",IF(P2>=45,"C-",IF(P2>=40,"D+",IF(P2>=35,"D",IF(P2>=30,"D-","E"))))))))))))"** to assign the grade of each record.
<p align="center"><img align="center" alt="Equation" width="200" src="grade_formula.png"></p> 
<p align="center"> <em> Figure 15: Function used to assign the grade </em> </p> 
<p align="center"><img align="center" alt="Table" width="200" src="gradedone.png"></p>
<p align="center"> <em> Figure 16: The grade was updated for each record </em> </p> 

6. Use function **"=IF(P2>=65,"Pass","Fail")"** to categorize the grades as PASS or FAIL.
<p align="center"><img align="center" alt="Equation" width="200" src="passorfail.png"></p> 
<p align="center"> <em> Figure 17: Function used to assign the grade </em> </p> 
<p align="center"><img align="center" alt="Table" width="200" src="passorfaildone.png"></p> 
<p align="center"> <em> Figure 18: The status for each grade was updated </em> </p> 

7. Use **"Conditional Formatting"** to colour column P with green and colour the Pass line with a light red.
<p align="center">
  <img src="columnformat.png" width="200" />
  <img src="rowformat.png" width="200" />
</p>
<p align="center"> <em> Figure 19 & 20: Conditional formatting to colour the column </em> </p> 
<p align="center"><img align="center" alt="Table" width="400" src="conditionalformat.png"></p> 
<p align="center"> <em> Figure 21: Data after conditional formatting </em> </p> 

8. Use **"Text color"** to colour the column L, M and N (B1, B2, B3) into red colour.
   
   Use "CTRL + Shift + ↓(Downward Arrow)" to select the whole column, repeat this step on column L, M and L. Then, change the text colour into red colour.

<p align="center">
  <img src="textcolor.png" width="200" />
</p>
<p align="center"> <em> Figure 22: Text color to colour the columns </em> </p> 
<p align="center"><img align="center" alt="Table" width="400" src="redcolor_column.png"></p> 
<p align="center"> <em> Figure 23: The columns colour in red </em> </p> 
   
## Create Dashboard <a name = "create_dashboard"> </a>
1. Create and rename **"Dashboard"** at new spreadsheet.
<p align="center"><img align="center" alt="Table" width="200" src="createnewsheet.png"></p> 
<p align="center"> <em> Figure 24: Create new speardsheet through "+" button </em> </p> 

<p align="center"><img align="center" alt="Table" width="200" src="rename_dashboard.png"></p> 
<p align="center"> <em> Figure 25: Rename the spreadsheet to "Dashboard" </em> </p> 

2. Insert new chart into the "Dashboard" spreadsheet
   
   Insert the new chart by clicking the "Insert" at the menu on top. Then, choose "Chart" to insert it.
<p align="center"><img align="center" alt="Table" width="200" src="insert_chart.png"></p> 
<p align="center"> <em> Figure 26: Insert new chart</em> </p> 

### Pass and Fail views by using Doughnut chart <a name = "passfail_dashboard"> </a>

3. Customize and setup the chart
   Setup the chart through the following settings:
   + Chart type: Doughnut chart
   + Data range: R3:R111521 (Dataset1!R3:R111521)

<p align="center"><img align="center" alt="Table" width="200" src="editchart_passfail.png"></p> 
<p align="center"> <em> Figure 27: Setup the Pass and Fail views chart</em> </p> 

4. Tick the "Aggregate" section
<p align="center"><img align="center" alt="Table" width="200" src="aggregate.png"></p> 
<p align="center"> <em> Figure 28: Tick the "Aggregate" section</em> </p> 

5. Result of **"Pass and Fail views Doughnut chart"** dashboard
<p align="center"><img align="center" alt="Table" width="200" src="passfailviews.png"></p> 
<p align="center"> <em> Figure 29: Final result for Pass and Fail views Doughnut chart</em> </p> 

### Total Number of Records by using Scorecard chart <a name = "total_dashboard"> </a>
6. Customize and setup the chart
   Setup the chart through the following settings:
   + Chart type: Scorecard chart
   + Data range: R2:R111521 (Dataset1!R2:R111521)
  
<p align="center"><img align="center" alt="Table" width="200" src="editchart_total.png"></p> 
<p align="center"> <em> Figure 30: Setup the Total Number of Records chart</em> </p> 

7. Tick the "Aggregate" section and choose "Count"
<p align="center"><img align="center" alt="Table" width="200" src="aggregate_total.png"></p> 
<p align="center"> <em> Figure 31: Tick the "Aggregate" section and choose "Count"</em> </p> 

8. Result of **"Total Number of Records Scorecard chart"** dashboard
<p align="center"><img align="center" alt="Table" width="200" src="total.png"></p> 
<p align="center"> <em> Figure 32: Final result for Total Number of Records Scorecard chart</em> </p> 

### Pass Percentage by using Scorecard chart <a name = "pass_dashboard"> </a>
9. Customize and setup the chart
   Setup the chart through the following settings:
   + Chart type: Scorecard chart
   + Data range: E26
  
<p align="center"><img align="center" alt="Table" width="200" src="editchart_pass.png"></p> 
<p align="center"> <em> Figure 33: Setup the Pass Percentage chart</em> </p> 

10. Result of **"Pass Percentage Scorecard chart"** dashboard
<p align="center"><img align="center" alt="Table" width="200" src="pass.png"></p> 
<p align="center"> <em> Figure 34: Final result for Pass Percentage Scorecard chart</em> </p> 

### Fail Percentage by using Scorecard chart <a name = "fail_dashboard"> </a>
11. Customize and setup the chart
   Setup the chart through the following settings:
   + Chart type: Scorecard chart
   + Data range: E33
  
<p align="center"><img align="center" alt="Table" width="200" src="editchart_fail.png"></p> 
<p align="center"> <em> Figure 33: Setup the Fail Percentage chart</em> </p> 

12. Result of **"Fail Percentage Scorecard chart"** dashboard
<p align="center"><img align="center" alt="Table" width="200" src="fail.png"></p> 
<p align="center"> <em> Figure 34: Final result for Fail Percentage Scorecard chart</em> </p> 

### Maximum Value by using Scorecard chart <a name = "max_dashboard"> </a>
13. Customize and setup the chart
   Setup the chart through the following settings:
   + Chart type: Scorecard chart
   + Data range: U6:U8, P2:P111725 (Dataset1!U6:U8,Dataset1!P2:P111725)
   + Combine ranges: Horizontally
  
<p align="center"><img align="center" alt="Table" width="200" src="editchart_max.png"></p> 
<p align="center"> <em> Figure 35: Setup the Maximum Value chart</em> </p> 

14. Result of **"Maximum Value Scorecard chart"** dashboard
<p align="center"><img align="center" alt="Table" width="200" src="max.png"></p> 
<p align="center"> <em> Figure 36: Final result for Maximum Value Scorecard chart</em> </p> 

### Minimum Value by using Scorecard chart <a name = "min_dashboard"> </a>
15. Customize and setup the chart
   Setup the chart through the following settings:
   + Chart type: Scorecard chart
   + Data range: R4
  
<p align="center"><img align="center" alt="Table" width="200" src="editchart_max.png"></p> 
<p align="center"> <em> Figure 37: Setup the Minimum Value chart</em> </p> 

16. Result of **"Minimum Value Scorecard chart"** dashboard
<p align="center"><img align="center" alt="Table" width="200" src="min.png"></p> 
<p align="center"> <em> Figure 38: Final result for Minimum Value Scorecard chart</em> </p> 

### Average Value by using Scorecard chart <a name = "avg_dashboard"> </a>
17. Customize and setup the chart
   Setup the chart through the following settings:
   + Chart type: Scorecard chart
   + Data range: R6
  
<p align="center"><img align="center" alt="Table" width="200" src="editchart_avg.png"></p> 
<p align="center"> <em> Figure 37: Setup the Average Value chart</em> </p> 

18. Result of **"Average Value Scorecard chart"** dashboard
<p align="center"><img align="center" alt="Table" width="200" src="avg.png"></p> 
<p align="center"> <em> Figure 38: Final result for Average Value Scorecard chart</em> </p> 

### Number of Students and Grades by using Column chart <a name = "numstu_grades_dashboard"> </a>
19. Customize and setup the chart
   Setup the chart through the following settings:
   + Chart type: Column chart
   + Data range: K10:L23
   + Stacking: None
   + X-axis: Grade
   + Series: Total
  
<p align="center"><img align="center" alt="Table" width="200" src="editchart_numstu_grades.png"></p> 
<p align="center"> <em> Figure 39: Setup the Number of Students and Grades chart</em> </p> 

20. Result of **"Number of Students and Grades Column chart"** dashboard
<p align="center"><img align="center" alt="Table" width="200" src="numstu_grades.png"></p> 
<p align="center"> <em> Figure 40: Final result for Number of Students and Grades Column chart</em> </p> 

### Total Number of Grades table <a name = "grade_dashboard"> </a>
21. Use formula in Figure 41 and Figure 42 to link to total number of grades to the table on dashboard.
<p align="center"><img align="center" alt="Table" width="200" src="dashboard_table_formula1.png"></p> 
<p align="center"> <em> Figure 41: Formula to retrieve the grades</em> </p> 
<p align="center"><img align="center" alt="Table" width="200" src="dashboard_table_formula2.png"></p> 
<p align="center"> <em> Figure 42: Formula to retrieve the total number of grades</em> </p> 

   Repeat the step in Figure 42 for every grades such as. A+, A, A-, B+, B and more.

22. Result of **"Total Number of Grades table"** dashboard
<p align="center"><img align="center" alt="Table" width="200" src="dashboard_table.png"></p> 
<p align="center"> <em> Figure 43: Final result for Total Number of Grades table</em> </p> 

## Dashboard <a name = "dashboard"> </a>
<p align="center"><img align="center" alt="Table" width="400" src="dashboard.png"></p> 
<p align="center"> <em> Figure 44: Dashboard </em> </p> 

## Contribution 🛠️  <a name = "contribution"> </a>
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


