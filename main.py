import matplotlib.pyplot as plt
from scipy import stats

from data_loader import STOCKS, WEIGHTS, load_prices
from metrics import calculate_returns, portfolio_performance, print_metrics


# 1) Load data
prices = load_prices()

# 종목 순서를 비중 순서와 맞춤
prices = prices[STOCKS].dropna()

prices.to_csv("stock_data.csv")

print(f"Period: {prices.index[0].date()} ~ {prices.index[-1].date()}")
print(f"Trading days: {len(prices)}")


# 2) Returns and metrics
returns = calculate_returns(prices)
metrics = portfolio_performance(returns, WEIGHTS)
print_metrics(metrics)

port_returns = metrics["daily_returns"]


# 3) Correlation
corr_matrix = returns.corr()

print("\n=== Correlation Matrix ===")
print(corr_matrix.round(2))


# 4) Chart: stock prices
plt.figure(figsize=(12, 6))

for stock in STOCKS:
    plt.plot(prices[stock], label=stock)

plt.title("Stock Prices")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.tight_layout()
plt.savefig("stock_prices.png")
plt.close()


# 5) Chart: correlation heatmap
fig, ax = plt.subplots(figsize=(8, 6))

im = ax.imshow(corr_matrix, cmap="RdYlGn", vmin=-1, vmax=1)

ax.set_xticks(range(len(STOCKS)))
ax.set_xticklabels(STOCKS)
ax.set_yticks(range(len(STOCKS)))
ax.set_yticklabels(STOCKS)

for i in range(len(STOCKS)):
    for j in range(len(STOCKS)):
        ax.text(
            j,
            i,
            f"{corr_matrix.iloc[i, j]:.2f}",
            ha="center",
            va="center",
            fontsize=12,
        )

plt.colorbar(im)
plt.title("Stock Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_matrix.png")
plt.close()


# 6) Chart: portfolio cumulative return
cumulative = (1 + port_returns).cumprod()

plt.figure(figsize=(12, 6))
plt.plot(cumulative)
plt.title("Portfolio Cumulative Return")
plt.xlabel("Date")
plt.ylabel("Growth of $1")
plt.axhline(y=1, color="gray", linestyle="--")
plt.tight_layout()
plt.savefig("cumulative_return.png")
plt.close()


# 7) Shapiro-Wilk normality test
sample = port_returns.dropna()

if len(sample) > 5000:
    sample = sample.sample(5000, random_state=42)

shapiro_stat, p_value = stats.shapiro(sample)

print("\n=== Shapiro-Wilk Normality Test ===")
print(f"Shapiro-Wilk Statistic: {shapiro_stat:.6f}")
print(f"P-Value: {p_value:.6f}")

if p_value < 0.05:
    print("Result: Reject the null hypothesis of normality.")
else:
    print("Result: Insufficient evidence to reject normality.")

plt.close("all")

print("\nAll done! Check the saved charts.")