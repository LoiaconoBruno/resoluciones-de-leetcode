# 121. Best Time to Buy And Sell Stock (Fácil)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# Idea: recorro los días llevando el precio más barato visto hasta ahora; vender hoy deja precio -
#       mínimo, y me quedo con el mejor.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimo = prices[0]
        mejor = 0
        for p in prices:
            minimo = min(minimo, p)
            mejor = max(mejor, p - minimo)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    print("OK")
