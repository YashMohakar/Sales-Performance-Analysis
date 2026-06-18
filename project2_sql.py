# Import required libraries
import pandas as pd
import sqlite3

# Read the CSV file and store it in a Pandas DataFrame
df = pd.read_csv(r"C:\Users\hp\OneDrive\Documents\Desktop\project 2\Sales_Cleaned2.csv")

# Create a connection to the SQLite database
# If 'sales.db' does not exist, it will be created automatically
conn = sqlite3.connect("sales.db")

# Convert the DataFrame into a SQL table named 'sales'
# index=False: Do not add the DataFrame index as a column
# if_exists="replace": Replace the table if it already exists


df.to_sql("sales", conn, index=False, if_exists="replace")

# print(df)


#### Run SQL query
# query = """
# SELECT count(*) from sales
# """

# result = pd.read_sql_query(query, conn)

# print(result)


###. Total Sales, Cost, and Profit:

# query = """
# select sum(sales) as Total_sales,
# sum(cost) as Total_cost,
# sum(profit) as Total_profit
# from sales"""

# result = pd.read_sql_query(query,conn)
# print(result)


###Total Sales by Region
# query = """
# select region,sum(sales) as total_sales
# from sales
# group by region
# order by total_sales desc;
# """
# result = pd.read_sql_query(query,conn)
# print(result)


###Total Profit by Region:

# query = """
# select region,sum(profit) as total_profit
# from sales
# group by region
# order by total_profit desc;"""

# result= pd.read_sql_query(query,conn)
# print(result)


###Top 10 Customers by Sales:

# query = """
# select customer,sum(sales) as total_sales
# from sales
# group by customer
# order by total_sales desc
# limit 10;"""

# result = pd.read_sql_query(query,conn)

# print(result)


###Top 5 Products by Profit:
# query = """
# select product,sum(profit) as total_profit
# from sales
# group by product
# order by total_profit desc
# limit 5;
# """

# result = pd.read_sql_query(query,conn)

# print(result)


####Average Profit per Order

# query = """
# select avg(profit) as avg_profit
# from sales;"""

# result = pd.read_sql_query(query,conn)

# print(result)


###Most Profitable Region:

query = """
select region,sum(profit) as total_profit
from sales
group by region
order by total_profit desc
limit 1;
"""
result = pd.read_sql_query(query,conn)
print(result)