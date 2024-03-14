import pandas as pd
df = pd.read_csv(r"D:\0\ROHIT\QPDS\employee_data.csv")
grouped = df.groupby("EMPLOYEE_ID")
b=df.groupby("EMPLOYEE_ID").filter(lambda X:len(X)>1)
print(b["EMPLOYEE_ID"].unique())

