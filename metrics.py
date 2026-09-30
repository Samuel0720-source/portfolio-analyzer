import numpy as np
import pandas as pd

def calculate_returns(prices):
    return prices.pct_change().dropna()

def portfolio_performance(returns, weights, risk_free_rate = 0.05):
    port_returns = returns @ weights
    annual_return = port_returns.mean() * 252
    annual_vol = port_returns.std() * np.sqrt(252)
    sharpe = (annual_return - risk_free_rate) / annual_vol

    cumulative = (1 + port_returns).cumprod()
    running_max = cumulative.cummax()
    drawdown = (cumulative - running_max) / running_max
    max_dd = drawdown.min()

    return {
        "annual_return": annual_return, 
        "annual_volatility": annual_vol, 
        "sharpe_ratio": sharpe, 
        "max_drawdown": max_dd,
        "daily_returns": port_returns,
        }

def print_metrics(metrics):
    print("=" * 40)
    print("Portfolio Performance Metrics")
    print("=" * 40)
    print(f"Annual Return: {metrics['annual_return']*100:>8.2f}%")
    print(f"Annual Volatility: {metrics['annual_volatility']*100:>8.2f}%")
    print(f"Sharpe Ratio: {metrics['sharpe_ratio']:>8.4f}")
    print(f"Max Drawdown: {metrics['max_drawdown']*100:>8.2f}%")
    print("=" * 40)