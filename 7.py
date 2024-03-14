import pandas as pd
sales_data=pd.read_csv(r"D:\0\ROHIT\QPDS\sales_data.csv")
pivot_table = pd.pivot_table(sales_data, values='Sale_amt', index='Item', aggfunc=['max', 'min'])
print(pivot_table)
pivot_table.columns = ['Max_Sale', 'Min_Sale']
print(pivot_table)