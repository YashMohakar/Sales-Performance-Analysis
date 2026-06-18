import pandas as pd

df = pd.read_excel(r"C:\Users\hp\OneDrive\Documents\Desktop\project 2\sales_raw_500.xlsx")
# print(df.head())
# print(df.info())

###  we remove the duplicates in our data

df = df.drop_duplicates()
# print(df)


### fix the date column in our data ( remove the blank row in date column)

# df['order_Date'] = pd.to_datetime(df['Order_Date'],errors="coerce")

# output: [500 rows x 7 columns]


###dropna() is used to remove missing values (NaN, NaT, None) from a DataFrame
df = df.dropna(subset=['Order_Date'])
# print(df)

# output: [482 rows x 8 columns]


### Creating New Columns PROFIT,YEAR,MONTH

df['Profit'] = df['Sales'] - df['Cost']
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month

print(df)


###SAVING THE DF FILE:

df.to_csv('Sales_Cleaned2.csv',index = False)