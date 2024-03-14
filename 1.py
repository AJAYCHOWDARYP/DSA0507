import pandas as pd
data=pd.read_csv(r"D:\0\ROHIT\QPDS\departments.csv")
print(data["DEPARTMENT_ID"].unique())