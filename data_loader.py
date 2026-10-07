import numpy as np
import yfinance as yf


STOCKS = ["AAPL", "MSFT", "NVDA", "VFV.TO"]
WEIGHTS = np.array([0.30, 0.20, 0.20, 0.30])
START_DATE = "2024-01-01"
END_DATE = "2026-09-01"


def load_prices(stocks=STOCKS, start=START_DATE, end=END_DATE):
    """Download closing prices, keeping columns in the same order as stocks."""
    data = yf.download(stocks, start=start, end=end, progress=False)
    prices = data["Close"][stocks].dropna()
    return prices