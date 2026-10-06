# 322. Coin Change (Media)
# https://leetcode.com/problems/coin-change/
#
# Idea: dp[m] = mínima cantidad de monedas para formar m; para cada monto pruebo cuál fue la última
#       moneda: dp[m] = 1 + min(dp[m - moneda]).
# Tiempo: O(amount · monedas) · Espacio: O(amount)

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        infinito = amount + 1
        dp = [0] + [infinito] * amount
        for m in range(1, amount + 1):
            for moneda in coins:
                if moneda <= m:
                    dp[m] = min(dp[m], dp[m - moneda] + 1)
        return dp[amount] if dp[amount] != infinito else -1


if __name__ == "__main__":
    s = Solution()
    assert s.coinChange([1, 2, 5], 11) == 3
    assert s.coinChange([2], 3) == -1
    assert s.coinChange([1], 0) == 0
    print("OK")
