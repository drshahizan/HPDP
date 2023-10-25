<a href="https://github.com/drshahizan/BDM/stargazers"><img src="https://img.shields.io/github/stars/drshahizan/BDM" alt="Stars Badge"/></a>
<a href="https://github.com/drshahizan/BDM/network/members"><img src="https://img.shields.io/github/forks/drshahizan/BDM" alt="Forks Badge"/></a>
<a href="https://github.com/drshahizan/BDM/pulls"><img src="https://img.shields.io/github/issues-pr/drshahizan/BDM" alt="Pull Requests Badge"/></a>
<a href="https://github.com/drshahizan/BDM"><img src="https://img.shields.io/github/issues/drshahizan/BDM" alt="Issues Badge"/></a>
<a href="https://github.com/drshahizan/BDM/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/drshahizan/BDM?color=2b9348"></a>
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan%2BDM&labelColor=%23d9e3f0&countColor=%23697689&style=flat)

# Assignment 1b: Sales Performance

### Group Name: HANY

## Importing a Dataset into Google Sheets
To get started with creating a dashboard or begin conducting data analysis, start by importing the dataset into Google Sheets, as illustrated in Figure 1. 
  1. Navigate to the **File** menu, and select the **Import** option.
  2. Browse through the directories by selecting **Browse** button.
  3. Locate the dataset file named **Dataset2.txt**.
  4. Initiate the import by clicking on **Open** to bring the data into Google Sheets.
  5. Click on the **Import Data** to proceed with the data import.

## Enhance the dataset appearance
  1. Navigate to the **Format** menu and select **Alternating colors**.
  2. Choose the color theme according to preferred appearance.

## Data preparation
In order to facilitate accurate sorting of data in the pivot table in Google Sheets, it is necessary to create an additional column that aligns with column that contains month name to ensure that the data is sorted chronologically by month, as Google Sheets typically defaults to alphabetical sorting.
  1. Locate the column containing **"SALES MONTH"** (cell H).
  2. **Insert** a new column named **"NUMERICAL MONTH"**.
  3. In the first cell of the "NUMERICAL MONTH" (under the header), type in the formula **=MONTH(DATEVALUE(H2&1))**
     - This formula is used to extract the month from the date provided in cell H2.
     - **'H2&1'**: Concatenates the value in cell **H2** with the number 1.
       - The number 1 in the formula acts as a placeholder and does not represent the actual day of the month. It is simply added to help convert the text in cell H2 into a date format that can be recognised by the **DATEVALUE()** function.
     - **'DATEVALUE()':** Converts a tect representation of a date into a date value.
     - **'MONTH()':** Extracts the month from the given date. It takes the date value and returns the month as a number.
  4. Notice that some values in the column could not be converted to numbers due to the non-standard format of the word **"Sept"**. To resolve this, the word needs to be replaced with **"Sep"**.
  5. Press **CTRL + F** and type in **"Sept"** in the search bar. Press the three-dotted menu.
  6. Input **"Sep"** into the **Replace with** field and proceed to click on **Replace all**.
  7. Next, sort the dataset by ascending order according to the NUMERICAL MONTH column.
  8. Go to the **Format** menu, hover over **Sort range**, and then select **Advanced range sorting options**.
  9. Check the box labeled **Data has header row** and choose the **NUMERICAL MONTH** column in the dropdown menu. Opt for the **A-Z** sorting order.

## Data Analysis
  1. Navigate to the **Insert** menu and select **Pivot table**.
  2. Click on the header of the first column (CUSTOMER), and press **CTRL + SHIFT + RIGHT ARROW KEY** and **CTRL + SHIFT + DOWN ARROW KEY** to highlight all the columns and rows that contain data without including any blank cells.
  3. Proceed to create the pivot table by clicking on **Create**.
  4. Subsequently, add relevant headers into the **Row, Columns, Values,** and **Filters** field to generate the desired data analysis.
  5. Repeat the step of creating the pivot table for each data anaysis. The following are the inputs for respective data analysis.
     - Monthly Sales
       - Row: NUMERICAL MONTH, SALES MONTH
       - Values: Target, SALES
     - Region
       - Row: Sales Region
       - Values: PRODUCTS
     - Customer
       - Row: Customer
       - Values: PRODUCTS
     - Sales Person
       - Row: SALES PERSON
       - Column: PRODUCTS
       - Values: SALES
     - Sales Trend
       - Row: SALES YEAR, NUMERICAL MONTH, SALES MONTH
       - Values: SALES
  7. Once all the pivot tables are created, duplicate and transfer them into a new new sheet named **"Dashboard"**.
  8. To generate the chart, select the related pivot table. Then, go to the **Insert** menu and select **Chart**.
  9. Repeat the process of generating the desired charts and customise the result according to preferred appearance.
  10. Next, to add a slicer, select the related pivot table, navigate to the **Data** menu and select **Add a slicer**.
  11. Click on the slicer. From the **Choose a column** dropdown menu, choose the appropriate header to act as the slicer.
  12. Repeat this process until all desired slicers are created.
  13. After generating all the charts and slicers, it is time to enhance and organize the dashboard to improve its visual appearance.
## Contribution 🛠️
Please create an [Issue](https://github.com/drshahizan/BDM/issues) for any improvements, suggestions or errors in the content.

You can also contact me using [Linkedin](https://www.linkedin.com/in/drshahizan/) for any other queries or feedback.

[![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fdrshahizan&labelColor=%23697689&countColor=%23555555&style=plastic)](https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fdrshahizan)
![](https://hit.yhype.me/github/profile?user_id=81284918)




