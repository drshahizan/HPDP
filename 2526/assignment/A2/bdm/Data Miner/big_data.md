# 📘 Assignment 2: Mastering Big Data Handling

**Group Members**:  
- Student 1: *Muhammad Syahmi Faris bin Rusli, A23CS0138*  
- Student 2: *Ng Yu Hin, A23CS0148*

---

## 📝 Task 1: Dataset Selection

### 📌 Dataset Overview

* **Name**: *🚕 NYC Yellow Taxi Trip Data 🗽*
* **Source**: [Kaggle – Elemento](https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data)
* **Domain**: *Transportation / Urban Analytics*
* **File Size**: *~1.99 GB (January 2015 subset)*
* **Shape**: *~12.7 Million rows × 19 columns*


### 📖 Description

🔍 Key Features

- **Temporal**: Pickup and drop-off timestamps.
- **Geospatial**: Longitude and latitude coordinates for trip start and end.
- **Financial**: Fare amount, mta_tax, tip_amount, and total_amount.
- **Trip Metadata**: Passenger count, trip distance, and payment type.

This dataset contains records of yellow medallion taxicab trips in New York City. The data was collected and provided to the NYC Taxi and Limousine Commission (TLC). Each record includes fields capturing pick-up and drop-off dates/times, locations, distances, itemized fares, rate types, and payment types.

### 📊 Data Column Description

| Column Name              | Data Type | Description                                                                     |
| -------------------------| --------- | ------------------------------------------------------------------------------- |
| `VendorID`               | int64     | A code indicating the TPEP provider that provided the record                    |
| `tpep_pickup_datetime`   | object    | The date and time when the meter was engaged                                    |
| `tpep_dropoff_datetime`  | object    | The date and time when the meter was disengaged                                 |
| `passenger_count`        | int64     | The number of passengers in the vehicle. This is a driver-entered value         |
| `trip_distance`          | float64   | The elapsed trip distance in miles reported by the taximeter                    |
| `pickup_longitude`       | float64   | Longitude where the meter was engaged                                           |
| `pickup_latitude`        | float64   | Latitude where the meter was engaged                                            |
| `RatecodeID`             | int64     | The final rate code in effect at the end of the trip                            |
| `store_and_fwd_flag`     | object    | This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka "store and forward"                                                                           |
| `dropoff_longitude`      | float64   | Longitude where the meter was disengaged                                        |
| `dropoff_latitude`       | float64   | Latitude where the meter was disengaged                                         |
| `payment_type`           | int64     | A numeric code signifying how the passenger paid for the trip                   |
| `fare_amount`            | float64   | The time-and-distance fare calculated by the meter                              |
| `extra`                  | float64   | Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges                                                                                       |
| `mta_tax`                | float64   | $0.50 MTA tax that is automatically triggered based on the metered rate in use  |
| `tip_amount`             | float64   | This field is automatically populated for credit card tips. Cash tips are not included                                                                                                                 |
| `tolls_amount`           | float64   | Total amount of all tolls paid in trip                                          |
| `improvement_surcharge`  | float64   | $0.30 improvement surcharge assessed on trips at the flag drop                  |
| `total_amount`           | float64   | The total amount charged to passengers. Does not include cash tips              |


---
