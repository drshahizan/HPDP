<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

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
<p align="center">
  <img src="textcolor.png" width="200" />
</p>
<p align="center"> <em> Figure 22: Text color to colour the columns </em> </p> 
<p align="center"><img align="center" alt="Table" width="400" src="redcolor_column.png"></p> 
<p align="center"> <em> Figure 23: The columns colour in red </em> </p> 

## Dashboard <a name = "dashboard"> </a>
<p align="center"><img align="center" alt="Table" width="400" src="dashboard.png"></p> 
<p align="center"> <em> Figure x: Dashboard </em> </p> 

## Contribution 🛠️  <a name = "contribution"> </a>
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


