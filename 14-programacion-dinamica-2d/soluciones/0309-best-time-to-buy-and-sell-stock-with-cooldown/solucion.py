# 309. Best Time to Buy And Sell Stock With Cooldown (Media)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
#
# Idea: tres estados por día: tengo una acción, la acabo de vender (mañana es cooldown) o estoy
#       libre sin acción. Cada día calculo el mejor resultado de cada estado a partir del día
#       anterior.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tengo, vendi, libre = float("-inf"), 0, 0
        for p in prices:
            tengo, vendi, libre = max(tengo, libre - p), tengo + p, max(libre, vendi)
        return max(vendi, libre)


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([1, 2, 3, 0, 2]) == 3
    assert s.maxProfit([1]) == 0
    print("OK")
