import yfinance as yf
import matplotlib.pyplot as plt
start_date = '2023-01-01'
end_date = '2024-01-01'
stock_data = yf.download('GOOG', start=start_date, end=end_date)
stock_data['Close'].plot(figsize=(10, 6), color='blue')
plt.title('Historical Stock Prices of Alphabet Inc. (Google)')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.grid(True)
plt.show()
