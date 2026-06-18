# 📊 Sales Performance Analysis using Python, SQL & Power BI

## 📌 Project Overview

This project demonstrates an end-to-end Data Analytics workflow using Python, SQL (SQLite), and Power BI. The objective is to analyze sales transaction data and generate actionable business insights related to revenue, profitability, regional performance, customer behavior, and product performance.

The project includes data cleaning and transformation using Pandas, SQL-based business analysis using SQLite, and an interactive Power BI dashboard for visualization and decision-making.

---

## 🎯 Business Objectives

The project aims to answer the following business questions:

* Which region generates the highest profit?
* Which products contribute the most revenue?
* Who are the top customers by sales?
* What is the overall profit margin?
* How do sales trends vary over time?
* Which areas require business improvement?

---

## 🛠️ Technologies Used

* Python
* Pandas
* SQLite
* SQL
* Power BI
* Microsoft Excel
* VS Code
* GitHub

---

## 📂 Dataset Information

| Metric           | Value |
| ---------------- | ----- |
| Original Records | 500   |
| Cleaned Records  | 482   |
| Total Columns    | 10    |

### Dataset Columns

* Order_ID
* Order_Date
* Customer
* Region
* Product
* Sales
* Cost
* Profit
* Year
* Month

---

## 🧹 Data Cleaning & Transformation

Data preprocessing was performed using the Pandas library.

### Steps Performed

✅ Removed duplicate records

```python
df = df.drop_duplicates()
```

✅ Removed rows with missing Order_Date values

```python
df = df.dropna(subset=['Order_Date'])
```

✅ Created Profit column

```python
df['Profit'] = df['Sales'] - df['Cost']
```

✅ Extracted Year and Month

```python
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month
```

✅ Exported cleaned dataset

```python
df.to_csv('Sales_Cleaned2.csv', index=False)
```

---

## 🗄️ SQL Analysis

The cleaned dataset was loaded into a SQLite database for business analysis.

### SQL Queries Performed

### 1. Total Sales, Cost & Profit

```sql
SELECT
SUM(Sales) AS Total_Sales,
SUM(Cost) AS Total_Cost,
SUM(Profit) AS Total_Profit
FROM sales;
```

### 2. Total Sales by Region

```sql
SELECT Region,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;
```

### 3. Total Profit by Region

```sql
SELECT Region,
SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Region
ORDER BY Total_Profit DESC;
```

### 4. Top 10 Customers by Sales

```sql
SELECT Customer,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Customer
ORDER BY Total_Sales DESC
LIMIT 10;
```

### 5. Top 5 Products by Profit

```sql
SELECT Product,
SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Product
ORDER BY Total_Profit DESC
LIMIT 5;
```

### 6. Average Profit per Order

```sql
SELECT AVG(Profit) AS Avg_Profit
FROM sales;
```

### 7. Most Profitable Region

```sql
SELECT Region,
SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Region
ORDER BY Total_Profit DESC
LIMIT 1;
```

---

## 📈 Power BI Dashboard

The interactive Power BI dashboard provides a visual representation of business performance.

### Dashboard Features

* KPI Cards

  * Total Sales
  * Total Profit
  * Profit Margin

* Monthly Sales Trend

* Profit by Region

* Sales by Product

* Interactive Filters

  * Region
  * Year

---

## 📊 Key Insights

### Overall Performance

* Total Sales: 20M+
* Total Profit: 5M+
* Profit Margin: 25.09%

### Regional Insights

* North region generated the highest profit.
* West region generated the lowest profit.
* Regional performance remains balanced across markets.

### Product Insights

* Printer is the best-performing product.
* Mobile generated the lowest sales.
* Product sales are diversified.

### Sales Trends

* Sales peaked during the early period.
* Temporary decline followed by stabilization.
* Trend analysis supports demand forecasting.

---

## 💡 Business Recommendations

* Increase investment in high-profit regions.
* Improve performance in lower-performing regions.
* Promote high-performing products.
* Develop customer loyalty programs.
* Use sales trends for inventory planning.
* Monitor KPIs regularly using Power BI dashboards.

---

## 🚀 Project Workflow

```text
Raw Excel Dataset
        │
        ▼
Data Cleaning (Python)
        │
        ▼
Feature Engineering
        │
        ▼
SQLite Database
        │
        ▼
SQL Business Analysis
        │
        ▼
Power BI Dashboard
        │
        ▼
Business Insights
```

---

## 📁 Project Structure

```text
Sales-Performance-Analysis/
│
├── data/
│   ├── sales_raw_500.xlsx
│   └── Sales_Cleaned2.csv
│
├── scripts/
│   ├── python_project2.py
│   └── project2_sql.py
│
├── dashboard/
│   └── project_2_bi.pbix
│
├── images/
│   └── dashboard.png
│
├── reports/
│   └── Sales_Performance_Analysis_Report.pdf
│
├── README.md
│
└── requirements.txt
```

---

## 📌 Conclusion

This project demonstrates a complete Data Analytics workflow from raw data processing to business intelligence reporting. By combining Python, SQL, and Power BI, meaningful business insights were generated to support data-driven decision-making and improve organizational performance.
