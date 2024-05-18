def max_profit(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# Example usage:
prices = [7, 1, 5, 3, 6, 4]
print(f"The maximum profit is: {max_profit(prices)}")
