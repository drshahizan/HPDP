
<div align="center">

# Assignment 1: Data Analysis using Google Sheets
## Dataset 2 Report

</div>

### :octocat: Group Name: KhuChin
### Group Members

| Name                                     | Matrix Number |
| :---------------------------------------- | :-------------: |
| Muhammad Ashraaf Bin Saleh              |A21EC0068      |
| Nur Khuzairie Zakwan Bin Mohd Zamri              |A21EC0112      |
| Nur Shuhada Safiah Binti Ayob              |A21EC0114      |
| Ikmal Bin Khairulezuan              |A21EC0186      |

------
## 📑 KhuChin Dataset2 Dashboard
<a name = "KhuChin Dashboard"> </a>
<p align="center"><img align="center" alt="Table" width="500" src="dashboard.jpeg"></p>  

------

## 📕 Dataset Information

We were given a dataset called dataset2.txt. This dataset contain a total of nine columns from which customer, salesperson, sales and year are some of the column in the dataset. Our task is the design a functional dashboard using GoogleSheet.  

[Google Sheet Link](https://docs.google.com/spreadsheets/d/1FlDUjFDf7Puj6r3DAkL6wJ7Qjqy3FoYLm4cm6SP8fyc/edit?usp=sharing)

---

## 1. Import dataset into Google Sheet

- First we need to download the dataset from the file in GitHub. Then we will open a brand new google sheet. From there we can import the dataset into the sheets. 
- Click on the **File** at the top left corner and then click on the **Import**.
<p align="center">
<img src="ss1.png">
</p>

<div align="center">

_Figure 1.1: Opening the import pop-up screen_

</div>

- Then we will see a pop-up and we can click on **Upload**. From there you can just drag the database from your explorer file or browse through your files.
<p align="center">
<img src="ss2.png"  width="550" height="270">
</p>

<div align="center">

_Figure 1.2: Importing the data_

</div>

- After that, we have succesfully import the data into GoogleSheet.
<p align="center">
<img src="ss3.png"  width="550" height="270">
</p>

<div align="center">

_Figure 1.3: Data queries in spreadsheet_

</div>

------

## 2. Create new sheet for general purpose usage

- Now we will create a new sheet and transfer our data into that so that we can use it freely. This serve as a precaution so that if anything happen it does not affect the original database. We will use this new sheet to sort and add new column for later use. You can name the sheet however you like but we will go with "Sorting".
- In order to create new sheet in the same spreadsheet. We can just click on the **+** button at the bottom of the screen.
<p align="center">
<img src="ss4.png"  width="550" height="270">
</p>

<div align="center">

_Figure 2.1: Adding new sheet_

</div>

- Then we can transfer the data by using the copy and paste method. Just press **Ctrl** and **A** on your keyboard to select all. Then press **Ctrl** and **C** to copy the data. After that go to the new sheet we just created and paste the data by clicking on the box in the sheet and press **Ctrl** and **V** at the same time.
<p align="center">
<img src="ss5.png"  width="550" height="270">
</p>

<div align="center">

_Figure 2.2: Copy the data to new sheet_

</div>

## 3. Preprocessing

- For this part, we need to make sure our data is readable ny the computer to ensure smooth calculation and prevent any possible error. As for the database provided, there aren't any missing data or anything that need to be change. How ever for easier usage, we have assigned the month to number so that it is easier to sort. The result is stored in a new column name "Month". We use formula as below: 
<p align="center">
<img src="ss6.png"  width="550" height="270">
</p>

<div align="center">

_Figure 2.2: Formula for changing the month to number_

</div>

- Then we will combine the month and the year so that we can differentiate between same month but in different year. The result is stored in a new column name "YearMonth". For this we use this formula as below:
<p align="center">
<img src="ss7.png"  width="550" height="270">
</p>

<div align="center">

_Figure 2.2: Formula for combining the year and month_

</div>

- After that we will sort the data using the "YearMonth" column as our main in ascending order. The formula is as below:
<p align="center">
<img src="ss8.png"  width="550" height="270">
</p>

<div align="center">

_Figure 2.2: Formula for sorting the data_

</div>


