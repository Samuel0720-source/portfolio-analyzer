import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


stocks = ["AAPL", "MSFT", "NVDA", "VFV.TO"]
weights = np.array([0.30, 0.20, 0.20, 0.30])

data = yf.download(stocks, start="2025-01-01", end="2026-01-01")
prices = data["Close"]

plt.figure(figsize=(12, 6))

for stock in stocks:
    plt.plot(prices[stock], label=stock)

plt.title("Stock Prices")
plt.xlabel("Date") 
plt.ylabel("Price(USD)")
plt.legend() 
plt.tight_layout() 
plt.savefig("stock_prices.png")
plt.ioff()
plt.show()

def download_prices(tickers, start="2024-01-01", end="2026-09-01"):
    data = yf.download(tickers, start=start, end=end)
    prices = data["Close"]
    prices = prices.dropna() # 결측치(빈 칸) 제거
    return prices

prices = download_prices(stocks)
returns = prices.pct_change().dropna()

print(prices.head(10))
print(f"\n데이터 기간: {prices.index[0].date()} ~ {prices.index[-1].date()}")
print(f"거래일 수: {len(prices)}")

print("=== Daily Returns ===")
print(returns.head())
print(f"\n행 수: {len(returns)}")

data.to_csv("stock_data.csv")
print(prices.shape) 

