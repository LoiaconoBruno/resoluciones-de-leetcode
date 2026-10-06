# 518. Coin Change II (Media)
# https://leetcode.com/problems/coin-change-ii/
#
# Idea: dp[m] = formas de armar m. Recorro las monedas por afuera y los montos por adentro: así cada
#       combinación se cuenta una sola vez, en el orden de las monedas (no como permutación).
# Tiempo: O(amount · monedas) · Espacio: O(amount)

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for moneda in coins:
            for m in range(moneda, amount + 1):
                dp[m] += dp[m - moneda]
        return dp[amount]


if __name__ == "__main__":
    s = Solution()
    assert s.change(5, [1, 2, 5]) == 4
    assert s.change(3, [2]) == 0
    assert s.change(10, [10]) == 1
    print("OK")
