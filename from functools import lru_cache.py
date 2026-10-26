
from functools import lru_cache


def coin_change_dp(coins, amount):
    """Return the fewest coins needed to make 'amount' , or -1 if impossible."""
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == INF else dp[amount]


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(coin_change_dp([1, 2, 5], 11))
    print(coin_change_dp([2], 3))
    print(coin_change_dp([1], 0))
    print(coin_change_dp([1, 2, 5], 10000))
    print(f"Elapsed time: {time.perf_counter() - start:.6f} seconds")