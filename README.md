# 📊 Exploratory Data Analysis (EDA) – Project 2

## 📌 Project Overview

This project focuses on **Exploratory Data Analysis (EDA)** using Python. The objective is to analyze an e-commerce dataset, discover patterns, identify trends and outliers, calculate descriptive statistics, and visualize the data to gain meaningful business insights. The project aligns with the requirements of **Project 2 – Exploratory Data Analysis (EDA)**. :contentReference[oaicite:0]{index=0}

---

## 🎯 Objectives

- Understand the dataset structure
- Perform descriptive statistical analysis
- Identify trends and patterns
- Detect outliers using the IQR method
- Analyze relationships between numerical variables
- Create meaningful visualizations
- Summarize key insights from the data

---

## 📂 Project Files

| File | Description |
|------|-------------|
| `Dataset for Data Analytics (Project-2).xlsx` | E-commerce dataset used for analysis |
| `project2.py` | Complete Python program for Exploratory Data Analysis |
| `README.md` | Project documentation |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- OpenPyXL
- Visual Studio Code

---

## 📚 Python Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

## 🔍 Exploratory Data Analysis Performed

### ✅ Data Loading
- Loaded the Excel dataset using Pandas.

### ✅ Data Inspection
- Displayed first five rows
- Displayed dataset dimensions
- Displayed column names
- Checked data types

### ✅ Data Quality Checks
- Checked missing values
- Checked duplicate records

### ✅ Descriptive Statistics
- Mean
- Median
- Count
- Minimum
- Maximum
- Five-number summary

### ✅ Product Analysis
- Product-wise order count
- Product-wise total sales
- Product-wise average sales

### ✅ Order Analysis
- Order status count
- Payment method analysis
- Referral source analysis
- Coupon code analysis

### ✅ Trend Analysis
- Monthly sales trend
- Highest and lowest sales months

### ✅ Outlier Detection
- IQR (Interquartile Range) Method
- Lower and Upper limits
- Outlier records

### ✅ Correlation Analysis
- Relationship between:
  - Quantity
  - Unit Price
  - Items in Cart
  - Total Price

### ✅ Data Validation
- Verified Total Price using:
  ```
  Quantity × Unit Price
  ```

---

## 📈 Visualizations Created

- Histogram
- Boxplot
- Bar Chart
- Scatter Plot
- Monthly Sales Line Chart

---

## 📊 Key Features

- Dataset exploration
- Statistical analysis
- Trend analysis
- Outlier detection
- Correlation analysis
- Data visualization
- Business insights

---

## ▶️ How to Run

### 1. Install Required Libraries

```bash
pip install pandas numpy matplotlib openpyxl
```

### 2. Keep Both Files in the Same Folder

```
project2.py
Dataset for Data Analytics (Project-2).xlsx
```

### 3. Run the Program

```bash
python project2.py
```

---

## 📌 Learning Outcomes

Through this project, I learned how to:

- Perform Exploratory Data Analysis (EDA)
- Work with Excel datasets using Python
- Calculate descriptive statistics
- Detect outliers using the IQR method
- Analyze trends and correlations
- Create professional data visualizations
- Extract meaningful insights from real-world data

---

## 📷 Sample Output

The program generates:

- Dataset Summary
- Statistical Analysis
- Product Analysis
- Order Analysis
- Correlation Matrix
- Outlier Detection
- Histogram
- Boxplot
- Bar Charts
- Scatter Plot
- Monthly Sales Trend
- Final EDA Summary

---

## 🚀 Project Outcome

This project demonstrates the practical application of **Exploratory Data Analysis (EDA)** using Python. By analyzing an e-commerce dataset, it provides meaningful insights through descriptive statistics, trend analysis, outlier detection, correlation analysis, and data visualization, helping transform raw data into actionable information. :contentReference[oaicite:1]{index=1}
