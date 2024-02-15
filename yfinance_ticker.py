import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Ticker symbol for S&P 500
ticker = "AAPL"

# Get daily data for the past year for the ticker
historical_data = yf.download(ticker, period="6mo", interval="1d")["Close"]

# Transform data into a pandas DataFrame
df = pd.DataFrame(historical_data)

# Calculate percentage change for the ticker and store in a new DataFrame
percent_change_df = pd.DataFrame()
percent_change_df[ticker] = ((historical_data - historical_data.iloc[0]) / historical_data.iloc[0]) * 100

# Plot the percentage change for the ticker
percent_change_df.plot(figsize=(10, 6))
plt.title("Cumulative Percentage Change of S&P 500 over a Year")
plt.xlabel("Date")
plt.ylabel("Percentage Change")
plt.show()

