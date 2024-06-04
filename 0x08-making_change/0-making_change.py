#!/usr/bin/python3
"""
determine the fewest number
"""


def makeChange(coins, total):
    """
    Initialize an array to store the 
    minimum number of coins needed 
    for each amount
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total amount 0

    for coin in coins:
        for amount in range(coin, total + 1):
            # Update the minimum number of coins needed for each amount
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the final value in dp is still infinity, it means the total cannot be met
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]

# Example usage:
coins = [1, 2, 5]  # Example coin denominations
total_amount = 11
result = makeChange(coins, total_amount)
print(f"Fewest number of coins needed for {total_amount}: {result}")

