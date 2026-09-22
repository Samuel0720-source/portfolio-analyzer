stocks = ["AAPL", "MSFT", "NVDA", "VFV.TO"]
weights = [0.30, 0.20, 0.10, 0.30]

total = sum(weights)

print("Stocks:", stocks)
print("Weights:", weights)
print("Total:", total * 100, "%")

if total == 1.0:
    print("Portfolio is valid!")
else:
    print("Error: weights must add up to 100%")