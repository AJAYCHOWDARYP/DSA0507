import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Set the start and end dates
start_date = '2023-01-01'
end_date = '2024-01-01'

# Fetch historical stock prices of Alphabet Inc. (Google) from Yahoo Finance
stock_data = yf.download('GOOG', start=start_date, end=end_date)

# Plot the trading volume
stock_data['Volume'].plot(kind='bar', figsize=(10, 6), color='green')
plt.title('Trading Volume of Alphabet Inc. (Google)')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid(True)
plt.show()
