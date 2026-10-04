import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Prepare data
stocks = ["AAPL", "MSFT", "NVDA", "VFV.TO"]
weights = np.array([0.30, 0.20, 0.20, 0.30])
data = yf.download(stocks, start="2024-01-01", end="2026-09-01")
prices = data["Close"].dropna()  # keep columns in the same order as stocks
returns = prices.pct_change().dropna()
portfolio_returns = returns @ weights

plt.figure(figsize=(10, 6))
plt.hist(portfolio_returns, bins=50, density=True, alpha=0.7, color='steelblue', edgecolor = "white")
# bins=50: 50개 구간으로 나눔
# density=True: y축을 확률 밀도로 (% 대신)
# alpha=0.7: 투명도 (0=투명, 1=불투명)

plt.title("Portfolio Return Distribution")
plt.xlabel("Daily Return")
plt.ylabel("Density")
plt.axvline(x=0, color="red", linestyle="--") # 0% 기준선
plt.tight_layout()
plt.savefig("return_distribution.png")
plt.show()

# 음수 skewness = 하락 위험이 더 크다는 의미
skewness = stats.skew(portfolio_returns)
print(f"Skewness : {skewness:.4f}")

if skewness < -0.5:
    print("Negatively skewed: might drop alot")
elif skewness > 0.5:
    print("Positively skewed: might rise alot")
else: 
    print("Approximately symmetric: normal distribution")

kurtosis = stats.kurtosis(portfolio_returns)
print(f"Kurtosis : {kurtosis:.4f}")
# 정규분포의 kurtosis = 3 (excess kurtosis = 0)

if kurtosis > 1:
    print("Fat tails: more extreme events than normal distribution")
else:
    print("Normal-like tails: similar to normal distribution")
