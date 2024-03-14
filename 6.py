import pandas as pd
import matplotlib.pyplot as plt
start_date = '2020-01-04'
end_date = '2020-04-30'
df = pd.read_csv('alphabet_stock_data.csv', index_col='Date', parse_dates=True)
df_filtered = df.loc[start_date:end_date]
plt.figure(figsize=(10, 6))
plt.scatter(df_filtered['Close'], df_filtered['Volume'])
plt.xlabel('Closing Price')
plt.ylabel('Volume')
plt.title('Scatter Plot of Alphabet Inc. Stock Price vs. Volume')
plt.grid(True)

# Show the plot
plt.show()
