import pandas as pd
data=pd.read_csv(r"D:\0\ROHIT\QPDS\departments.csv")
b=data.sort_values("DEPARTMENT_NAME",ascending=False)
print(b["DEPARTMENT_NAME"])