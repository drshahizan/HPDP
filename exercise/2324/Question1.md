# QUESTION 1 \[20 MARKS\]

In this case study, **Nurul**, a skilled Data Scientist in Malaysia, is
working to improve crop yield predictions for **Evergreen Farms** in
2023. She is using **Google Colab** and **Google Drive** to process a
large dataset named `crop_data.csv`, which is larger than **1 GB** and
stored at:

``` text
/content/drive/My Drive/agri_datasets/crop_data.csv
```

To improve processing efficiency, Nurul optimizes memory usage by
reducing the size of numerical data types and assigning appropriate data
types to each column. She first performs exploratory data analysis using
statistical summaries, distribution plots, and correlation matrices.

Since the dataset is very large, she uses **chunked loading**,
processing the dataset in smaller chunks before merging them into a
single DataFrame. Finally, she performs **random sampling** by selecting
**15%** of the dataset to ensure efficient yet representative analysis.

Based on the case study, answer the following questions.

> **Answers must be written in Python code.**

## a) Import the necessary Python libraries. Then, read the dataset from Google Drive and display the first few rows.

**(4 marks)**

## b) Write the Python code to perform the following data type conversions.

**(6 marks)**

   No.  Existing Data Type   New Data Type
  ----- -------------------- ---------------
    i   float64              float16
   ii   int64                int16
   iii  datetime64           datetime16

## c) Write the Python code to load the large dataset in **chunks** and merge all chunks into a single DataFrame.

**(5 marks)**

## d) Write the Python code to perform **random sampling** by selecting **15%** of the dataset. Display the first few rows of the sampled dataset.

**(5 marks)**
