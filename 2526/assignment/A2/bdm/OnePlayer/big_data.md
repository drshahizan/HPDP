# 📘 Assignment 2: Mastering Big Data Handling

**Group Information**
- Group Name: OnePlayer

| Name | Matric Number |
|---|---|
| Muhammad Afiq Danish bin Mohd Hazni | A23CS0118 |

---

## 📝 1. Dataset Description

### 📌 Dataset Overview

* **Dataset Name**: _Cell Towers Worldwide: Location Data by Continent (Asia)_ 
* **Source**: [Kaggle - zakariaeyoussefi](https://www.kaggle.com/datasets/zakariaeyoussefi/cell-towers-worldwide-location-data-by-continent) |
* **File**: _Asia towers.csv _
* **File Size**: _~1.46 GB _
* **Domain**: _Telecommunications / Network Infrastructure _
* **Number of Records**: _13.38 million rows × 18 columns_ 

This dataset contains geographical and technical information of cell towers located across Asia.
It is sourced from OpenCelliD, the world's largest open database of cell towers, and is 
well-suited for large-scale data processing analysis due to its size and diversity of column 
types including integers, floats, strings, and categorical values.

### 🔍 Key Features
- Over 13 million cell tower records across Asia
- Covers multiple radio technologies including GSM, LTE, UMTS and NR
- Contains both geographical coordinates and network metadata
- Includes categorical columns suitable for data type optimisation
- Rich enough for exploratory analysis including groupby, aggregation and filtering operations

### 📊 Column Descriptions

| Column | Data Type | Description |
|---|---|---|
| **Radio** | object | The generation of broadband cellular network technology (e.g., LTE, GSM) |
| **MCC** | int64 | Mobile Country Code, a unique identifier for each country in the mobile network |
| **MNC** | int64 | Mobile Network Code, identifying the mobile network within a country |
| **TAC** | int64 | Location Area Code, Tracking Area Code, or Network Identifier |
| **CID** | int64 | Unique identifier for each Base Transceiver Station (BTS) or sector |
| **LON** | float64 | Geographic coordinate specifying the east-west position |
| **LAT** | float64 | Geographic coordinate specifying the north-south position |
| **RANGE** | int64 | Approximate area within which the cell coverage extends (in meters) |
| **SAM** | int64 | Number of measures processed to derive the data point |
| **changeable** | int64 | Indicates if the cell location was determined through sample processing (1) or directly obtained from the telecom firm (0) |
| **created** | int64 | Timestamp indicating when the cell was first added to the database (UNIX format) |
| **updated** | int64 | Timestamp indicating when the cell was last seen or updated in the database (UNIX format) |
| **averageSignal** | int64 | Represents the averaged signal strength of the cell location |
| **Country** | object | The country of the cell tower |
| **Network** | object | The company that owns the cell tower |
| **Continent** | object | The continent of the cell tower |
