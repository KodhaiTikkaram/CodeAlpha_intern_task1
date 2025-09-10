stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 130,
    "MSFT": 320
}

portfolio = {}

# Get user input for portfolio
print("Enter stock symbol and quantity (type 'done' to finish):")
while True:
    stock = input("Stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    try:
        qty = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")
