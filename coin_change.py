def min_coins(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], dp[value - coin] + 1)

    return -1 if dp[amount] == amount + 1 else dp[amount]


print(min_coins([1, 2, 5], 11))  # 3
print(min_coins([2], 3))        # -1: impossible
