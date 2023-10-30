<a href="https://github.com/drshahizan/HPDP/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/HPDP" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/network/members"><img src="https://img.shields.io/github/forks/drshahizan/HPDP" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/HPDP" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/HPDP"><img src="https://img.shields.io/github/issues/drshahizan/HPDP" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/HPDP/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/HPDP?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2FHPDP&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1a: Examination results

### Group Name: ohSheet
### Group Members

| Name                                     | Matrix Number | Task |
| :---------------------------------------- | :-------------: | ------------- |
| MIKHAIL BIN YASSIN                       |  A21EC0053   |    Pre-processing |
| FAUZAN AQIL BIN AZMAN                    |  A21EC0174   |    Data Transformation |
| YASMEEN NATASHA BINTI HAFIZ SHAHREL      |  A21EC0147   |    Documentation |   
| MUHAMMAD ADAM FAHMI BIN MOHD TAUFIQ      |  A21EC0061   |    Visualization |     

## Table of Contents
+ [About](#about)
+ [Importing and Preprocessing Data](#preprocess)
+ [Obtaining Grade and Status](#grade_status)
+ [Creating a Dashboard](#dashboard)
+ [Contributing](../CONTRIBUTING.md)


## About <a name="about"></a>

The main goal of this project is to utilize Google Sheets to process and present data, with a specific focus on a case study related to examination results. The project involves tasks such as calculating statistics, creating charts, and generating meaningful insights from the examination results.

We were given **Dataset1** where information about **Id_No**, **Academic**, **Sports**, **Co-Curriculum**, **Test_1**, and **Test_2** are contained.

Firstly, we need to **Import the Data** followed by **Preprocessing the Data**. Next, **Grade** and **Status** are obtained. Last but not least, we are tasked to **Create a Dashboard** to visualize the overall result.

In a nutshell, the project emphasizes practical data manipulation and visualization skills within the context of educational assessment.

## Importing and Preprocessing Data <a name="preprocess"></a>

1. Download the Dataset1.txt file.

2. To import the Dataset1.txt file on Google Sheets, choose **File** and click **Import**.
   
   <div align="center">
   <img src="import.png" alt="import"  width="250" >
   </div><br>
   
3. Choose the file and click **Import data**.

4. Figure shows the data that has been entered into Google Sheets. This dataset contains five columns: **Id_No**, **Academic**, **Sports**, **Co-Curriculum**, **Test_1**, and **Test_2**.
   <div align="center">
      <img src="dataset.png" alt="dataset" width="250">
      </div><br>
5. To convert the **Academic**, **Sports**, **Co-Curriculum**, **Test_1**, and **Test_2** data values to two decimal places, select column B through column F.
   <div align="center">
      <img src="format1.png" alt="format1" width="250" >
      </div><br>
6. Choose **Format** and click **Number**.
   <div align="center">
      <img src="format2.png" alt="format2" width="250">
      </div><br>
7. Select **Custom number format** and apply the two decimal values.
   <div align="center">
      <img src="format3.png" alt="format3" width="250">
      </div><br>
8. Create new columns to create new values of column B (Academic) to column F (Test_2) to standardize the maximum value to 3.33 for each column. The new columns should be named as below:
   
   - Academic: P1 (Column G)
   - Sports: P2 (Column H)
   - Co-Curriculum: P3 (Column I)
   - Test_1: P4 (Column J)
   - Test_2: P5 (Column K)
     
   <div align="center">
      <img src="newmax.png" alt="newmax" width="250">
      </div><br>
      
   To calculate the new values, divide the score of each category by its full mark. The formula for each column is:
   
   - Column P1: `=(B2/61)*3.33`
   - Column P2: `=(C2/10)*3.33`
   - Column P3: `=(D2/15)*3.33`
   - Column P4: `=(E2/10)*3.33`
   - Column P5: `=(F2/10)*3.33`

   For each column, click enter after filling out the formula to autofill the entire column.

9. Create three new columns named B1 (Column L), B2 (Column M), and B3 (Column N) to determine the top three values based on the values on columns G to K. The new columns represent information as below:

   - Column L (B1): The highest value
   - Column M (B2): The second highest value
   - Column N (B3): The third highest value
     
   <div align="center">
      <img src="top3.png" alt="top3" width="250">
      </div><br>
      
   The formula to get the values for each column is:
   
   - Column B1: `=LARGE($G2:$K2,1)`
   - Column B2: `=LARGE($G2:$K2,2)`
   - Column B3: `=LARGE($G2:$K2,3)`

   For each column, click enter after filling out the formula to autofill the entire column.

10. Create a new column named TM (Column O) to calculate the total points by combining the data from columns L to N. The formula to calculate the total mark value is:
    
   - `=SUM(L2:N2)`

   Click enter after filling out the formula to autofill the entire column.
   
   <div align="center">
      <img src="TM.png" alt="TM" width="250" >
      </div><br>
      
11. Create a new column named Percent (Column P) to calculate the percentage value for the data in Column O (TM). The formula to calculate the percentage is:
    
   - `=(O2/9.99)*100`

   Click enter after filling out the formula to autofill the entire column.
   The percentage value must be in two decimal places.
   
   <div align="center">
      <img src="percent.png" alt="percent" width="250">
      </div><br>
      
## Obtaining Grade and Status <a name="grade_status"></a>

1. Create two new columns, Column Q for Grade and Column R for Status.
   The grade and status must be obtained based on the following table.
   
<div align="center">
   <img src="tablegradestatus.png" alt="tablegradestatus" width="250">
   </div><br>
   
2. The formula to determine the grade is:
   
   - `=VLOOKUP(P2,$U3:$W16,2)`

   Click enter after filling out the formula to autofill the entire column.

3. The formula to determine the status is:
   
   - `=VLOOKUP(P2,$Y$4:$Z$16,2)`

   Click enter after filling out the formula to autofill the entire column.

   Colour column P with green for Pass and light red for the Pass line.

4. Figure shows the final result of Dataset1 sheet before creating a dashboard.
   
   <div align="center">
   <img src="finaldataset.png" alt="finaldataset" width="700">
   </div><br>
   
## Creating a Dashboard <a name = "dashboard"></a>

1. On the Dataset1 sheet, select **Insert** > **Pivot Table**.
   <div align="center">
   <img src="pivottable.png" alt="pivottable" width="250">
   </div><br>
   
2. Select **New sheet** and click **Create**. A new sheet should be created.
   <div align="center">
   <img src="createpivottable.png" alt="createpivottable" width="250">
   </div><br>
   
3. Rename the sheet to **Dashboard** by right-clicking the sheet name and select **Rename**.

4. Under the **Pivot table editor** > **Values**, click **Add** and select **Percent**. Set the summarization to **MIN** and leave the show as **Default**.
<div align="center">
   <img src="pivotmin.png" alt="pivotmin" width="250">
   </div><br>
   
5. Select **Insert** > **Pivot Table**. Click on **Existing sheet**, which in this case is Dashboard. Enter the appropriate data range and click **Create**.
<div align="center">
   <img src="existsheet.png" alt="existsheet" width="250">
   </div><br>
   
6. Under the **Pivot table editor** > **Values**, click **Add** and select **Percent**. Set the summarization to **MAX** and leave the show as **Default**.
<div align="center">
   <img src="pivotmax.png" alt="pivotmax" width="250">
   </div><br>
   
7. Repeat step 5. Under the **Pivot table editor** > **Values**, click **Add** and select **Percent**. Set the summarization to **AVERAGE** and leave the show as **Default**.
<div align="center">
   <img src="pivotavg.png" alt="pivotavg" width="250">
   </div><br>
   
8. Repeat step 5. Under the **Pivot table editor** > **Rows** and **Values**, click **Add** and select **Grade**.
<div align="center">
   <img src="pivotgrade.png" alt="pivotgrade" width="250">
   </div><br>
   
9. Repeat step 5. Under the **Pivot table editor** > **Rows** and **Values**, click **Add** and select **Status**.
<div align="center">
   <img src="pivotstatus.png" alt="pivotstatus" width="250">
   </div><br>
   
10. Figure shows the created pivoted tables. These tables show a summarization of each category.
<div align="center">
   <img src="finalpivot.png" alt="finalpivot" width="250">
   </div><br>
   
11. Select **Insert** > **Chart**. Click on the **Scorecard chart** under **Chart editor** > **Setup**.

    - Enter the appropriate data range and click **OK**.
    
12. Figure below shows the **Setup** for **Min**, **Max**, and **Average** scorecards.
<div align="center">
   <img src="setupmin.png" alt="setupmin" width="250">
   </div><br>
   <div align="center">
   <img src="setupmax.png" alt="setupmax" width="250">
   </div><br>
   <div align="center">
   <img src="setupavg.png" alt="setupavg" width="250">
   </div><br>
   
13. Select **Insert** > **Chart**. Click on the **Column chart** under **Chart editor** > **Setup**.

    - Enter the appropriate data range and click **OK**.

    Figure below shows the **Setup** for the **Grading** chart.
<div align="center">
   <img src="setupgrading.png" alt="setupgrading" width="250">
   </div><br>
   
14. Select **Insert** > **Chart**. Click on the **Table chart** under **Chart editor** > **Setup**.

    - Enter the appropriate data range and click **OK**.

    Figure below shows the **Setup** for the **Grading** table.
<div align="center">
   <img src="setuptablegrading.png" alt="setuptablegrading" width="250">
   </div><br>
   
15. Select **Insert** > **Chart**. Click on the **Doughnut chart** under **Chart editor** > **Setup**.

    - Enter the appropriate data range and click **OK**.

    Figure below shows the **Setup** for the **Pass** and **Fail** doughnut chart.
<div align="center">
   <img src="setuppiechart.png" alt="setuppiechart" width="250">
   </div><br>
   
16. To create **Total Record**, **Pass**, and **Fail** scorecards, select **Insert** > **Chart**. Click on the **Scorecard chart** under **Chart editor** > **Setup**.

    Figure below shows the **Setup** for **Total Record**, **Pass**, and **Fail** scorecards.
<div align="center">
   <img src="totalscorecard.png" alt="totalscorecard" width="250">
   </div><br>
   <div align="center">
   <img src="maxscorecard.png" alt="maxscorecard" width="250">
   </div><br>
   <div align="center">
   <img src="minscorecard.png" alt="minscorecard" width="250">
   </div><br>
   
17. Create another two scorecards to display the total record of **Pass** and **Fail**.

    Figure below shows the **Setup** for the total record of **Pass** and **Fail** scorecards.
<div align="center">
   <img src="setuptotalpass.png" alt="setuptotalpass" width="250">
   </div><br>
   <div align="center">
   <img src="setuptotalfail.png" alt="setuptotalfail" width="250">
   </div><br>
   
18. Figure shows the created dashboard.
    <div align="center">
   <img src="dashboard.png" alt="dashboard">
   </div><br>

## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/HPDP/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)


