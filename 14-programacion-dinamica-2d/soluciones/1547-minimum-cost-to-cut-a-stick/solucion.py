# 1547. Minimum Cost to Cut a Stick (Difícil)
# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
#
# Idea: ordeno los cortes y agrego las puntas 0 y n. dp[i][j] = costo mínimo de hacer todos los
#       cortes entre la posición i y la j: elijo el primer corte k y pago el largo del pedazo más lo
#       de cada lado.
# Tiempo: O(c³), con c la cantidad de cortes · Espacio: O(c²)

from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        puntos = [0] + sorted(cuts) + [n]
        m = len(puntos)
        dp = [[0] * m for _ in range(m)]
        for largo in range(2, m):
            for i in range(m - largo):
                j = i + largo
                dp[i][j] = puntos[j] - puntos[i] + min(dp[i][k] + dp[k][j] for k in range(i + 1, j))
        return dp[0][m - 1]


if __name__ == "__main__":
    s = Solution()
    assert s.minCost(7, [1, 3, 4, 5]) == 16
    assert s.minCost(9, [5, 6, 1, 4, 2]) == 22
    print("OK")
