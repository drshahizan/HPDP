# 🏥 Healthcare Patient Monitoring Dashboard

## Introduction

The **Healthcare Patient Monitoring Dashboard** 
---

### Purpose
In today's healthcare environments, the ability to monitor patients' vital signs in real-time and maintain accurate health records is essential for improving patient outcomes, ensuring timely medical interventions, and reducing hospital workloads. This project proposes the development of a Healthcare Patient Monitoring System, a web-based application that leverages MySQL, MongoDB, and PHP to manage both structured and semi-structured patient data efficiently.

The core objective of the system is to facilitate seamless CRUD (Create, Read, Update, Delete) operations for patient records and their corresponding health vitals. By dividing the data storage between MySQL (for patient demographic and medical history data) and MongoDB (for storing frequently updated vitals such as heart rate, temperature, and blood pressure), the system ensures optimized performance, flexibility, and scalability.

This system is designed to:

- Streamline the registration and management of patient information such as name, age, gender, contact details, and medical history.

- Enable real-time entry and tracking of patient vitals including heart rate, temperature, blood oxygen levels (SpO₂), blood pressure, and respiratory rate.

- Allow healthcare staff to add, edit, and delete patient records and vitals from an intuitive web interface.

- Store historical vitals data for future analysis and healthcare insights.

Ultimately, the system provides a reliable foundation for monitoring patient health and supports the future integration of analytics and alert mechanisms to detect abnormal patterns and support clinical decision-making.

## System Design

### System Architecture

### Data Requirements

The data requirements for the systems are as follows:
  <table>
  <tr>
    <th>Field</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Patient ID</td>
    <td>A unique identifier for each patient</td>
  </tr>
  <tr>
    <td>Full Name</td>
    <td>The patient's name</td>
  </tr>
  <tr>
    <td>Age</td>
    <td>The patient's age</td>
  </tr>
  <tr>
    <td>Gender</td>
    <td>The patient's gender (e.g., Male, Female)</td>
  </tr>
  <tr>
    <td>Date of Birth</td>
    <td>The patient's birth date</td>
  </tr>
  <tr>
    <td>Contact Number</td>
    <td>Phone number for emergency or personal contact</td>
  </tr>
  <tr>
    <td>Address</td>
    <td>The patient's residential address</td>
  </tr>
  <tr>
    <td>Medical History</td>
    <td>Summary of previous illnesses or conditions</td>
  </tr>
  <tr>
    <td>Heart Rate (bpm)</td>
    <td>Beats per minute measured by monitoring device</td>
  </tr>
  <tr>
    <td>Temperature (°C)</td>
    <td>Body temperature in degrees Celsius</td>
  </tr>
  <tr>
    <td>SpO2 (%)</td>
    <td>Oxygen saturation level in blood</td>
  </tr>
  <tr>
    <td>Blood Pressure</td>
    <td>Systolic/diastolic pressure reading</td>
  </tr>
  <tr>
    <td>Respiratory Rate</td>
    <td>Number of breaths per minute</td>
  </tr>
</table>


### Functionalities

## Web Interface

## Testing and Validation

## Conclusion

## References

