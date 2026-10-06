# 2218. Maximum Value of K Coins from Piles (Difícil)
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
#
# Idea: mochila por pilas: dp[c] = mejor valor con c monedas usando las pilas vistas. Para cada pila
#       pruebo tomar sus primeras x monedas (con suma prefija) y combino con dp[c - x].
# Tiempo: O(k · total de monedas) · Espacio: O(k)

from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k + 1)
        for pila in piles:
            prefijo = [0]
            for moneda in pila[:k]:
                prefijo.append(prefijo[-1] + moneda)
            for c in range(k, 0, -1):
                for x in range(1, min(c, len(prefijo) - 1) + 1):
                    dp[c] = max(dp[c], dp[c - x] + prefijo[x])
        return dp[k]


if __name__ == "__main__":
    s = Solution()
    assert s.maxValueOfCoins([[1, 100, 3], [7, 8, 9]], 2) == 101
    pilas = [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]]
    assert s.maxValueOfCoins(pilas, 7) == 706
    print("OK")
