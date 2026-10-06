# 746. Min Cost Climbing Stairs (Fácil)
# https://leetcode.com/problems/min-cost-climbing-stairs/
#
# Idea: costo mínimo para llegar al escalón i = cost[i] + el menor costo entre los dos escalones
#       anteriores; la cima se alcanza desde cualquiera de los dos últimos.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = 0, 0
        for c in cost:
            a, b = b, c + min(a, b)
        return min(a, b)


if __name__ == "__main__":
    s = Solution()
    assert s.minCostClimbingStairs([10, 15, 20]) == 15
    assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    print("OK")
