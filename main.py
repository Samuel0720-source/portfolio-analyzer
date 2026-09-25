import yfinance as yf 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


stocks = ["AAPL", "MSFT", "NVDA", "VFV.TO"]
weights = np.array([0.30, 0.20, 0.20, 0.30])

data = yf.download(stocks, start="2025-01-01", end="2026-01-01")
prices = data["Close"]

corr_matrix = returns.corr()
print("=== Correlation Matrix ===")
print(corr_matrix.round(2))

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
plt.show()

plt.figure(figsize=(12, 6))

for stock in stocks:
    plt.plot(prices[stock], label=stock)

plt.title("Stock Prices")
plt.xlabel("Date") 
plt.ylabel("Price(USD)")
plt.legend() 
plt.tight_layout() 
plt.savefig("stock_prices.png")
#plt.ioff()
#plt.show()

def download_prices(tickers, start="2024-01-01", end="2026-09-01"):
    data = yf.download(tickers, start=start, end=end)
    prices = data["Close"]
    prices = prices.dropna() # 결측치(빈 칸) 제거
    return prices

prices = download_prices(stocks)
returns = prices.pct_change().dropna()
portfolio_returns = returns @ weights

annual_return = portfolio_returns.mean() * 252

annual_volatility = portfolio_returns.std() * np.sqrt(252)
print(f"연간 변동성: {annual_volatility:.4f}")
print(f"퍼센트로: {annual_volatility * 100:.2f}%")

risk_free_rate = 0.05 # 5% (미국 국채 이자율)
sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility
print(f"Sharpe Ratio: {sharpe_ratio:.4f}")

if sharpe_ratio > 1:
    print("Good risk-adjusted return!")
elif sharpe_ratio > 0:
    print("Positive but could be better.")
else:
    print("Risk-free asset would be better.")

cumulative = (1 + portfolio_returns).cumprod()
running_max = cumulative.cummax()

drawdown = (cumulative - running_max) / running_max
max_drawdown = drawdown.min()
print(f"Maximum Drawdown: {max_drawdown:.4f}")
print(f"퍼센트로: {max_drawdown * 100:.2f}%")
print(f"최악의 날: {drawdown.idxmin().date()}")

print(f"연간 수익률: {annual_return:.4f}")
print(f"퍼센트로: {annual_return * 100:.2f}%")

print(prices.head(10))
print(f"\n데이터 기간: {prices.index[0].date()} ~ {prices.index[-1].date()}")
print(f"거래일 수: {len(prices)}")

print("=== Portfolio Daily Returns ===")
print(portfolio_returns[:10])
print(f"\n평균 일일 수익률: {portfolio_returns.mean():.6f}")
print(f"일일 수익률 표준편차: {portfolio_returns.std():.6f}")

data.to_csv("stock_data.csv")
print(prices.shape) 


