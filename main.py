# === main.py ===
# Portfolio Analyzer: download stock prices and calculate key portfolio metrics

import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from metrics import calculate_returns, portfolio_performance, print_metrics

# 1) Settings
stocks = ["AAPL", "MSFT", "NVDA", "VFV.TO"]
weights = np.array([0.30, 0.20, 0.20, 0.30])

# 2) Download data
data = yf.download(stocks, start="2024-01-01", end="2026-09-01")
prices = data["Close"][stocks].dropna()  # keep columns in the same order as stocks
prices.to_csv("stock_data.csv")

print(f"Period: {prices.index[0].date()} ~ {prices.index[-1].date()}")
print(f"Trading days: {len(prices)}")

# 3) Returns and metrics
returns = calculate_returns(prices)
metrics = portfolio_performance(returns, weights)
print_metrics(metrics)

# 4) Correlation
corr_matrix = returns.corr()
print("\n=== Correlation Matrix ===")
print(corr_matrix.round(2))

# 5) Chart: stock prices
plt.figure(figsize=(12, 6))
for stock in stocks:
    plt.plot(prices[stock], label=stock)
plt.title("Stock Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.savefig("stock_prices.png")
plt.close()

# 6) Chart: correlation heatmap
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(corr_matrix, cmap="RdYlGn", vmin=-1, vmax=1)
ax.set_xticks(range(len(stocks)))
ax.set_xticklabels(stocks)
ax.set_yticks(range(len(stocks)))
ax.set_yticklabels(stocks)
for i in range(len(stocks)):
    for j in range(len(stocks)):
        ax.text(j, i, f"{corr_matrix.iloc[i, j]:.2f}",
                ha="center", va="center", fontsize=12)
plt.colorbar(im)
plt.title("Stock Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_matrix.png")
plt.close()

# 7) Chart: portfolio cumulative return
cumulative = (1 + metrics["daily_returns"]).cumprod()
plt.figure(figsize=(12, 6))
plt.plot(cumulative)
plt.title("Portfolio Cumulative Return")
plt.xlabel("Date")
plt.ylabel("Growth of $1")
plt.axhline(y=1, color="gray", linestyle="--")
plt.tight_layout()
plt.savefig("cumulative_return.png")
plt.close()

print("\nAll done! Check the saved charts.")