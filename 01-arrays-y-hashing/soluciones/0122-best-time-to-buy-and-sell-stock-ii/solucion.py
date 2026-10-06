# 122. Best Time to Buy And Sell Stock II (Media)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#
# Idea: como puedo comprar y vender cuantas veces quiera, me quedo con cada subida de un día al
#       siguiente.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ganancia = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ganancia += prices[i] - prices[i - 1]
        return ganancia


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    print("OK")
