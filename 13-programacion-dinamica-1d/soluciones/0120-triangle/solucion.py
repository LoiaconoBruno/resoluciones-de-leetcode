# 120. Triangle (Media)
# https://leetcode.com/problems/triangle/
#
# Idea: de abajo hacia arriba: el mejor camino desde una celda es su valor + el menor de los dos de
#       abajo. Reuso una sola fila.
# Tiempo: O(n²) · Espacio: O(n)

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        for fila in range(len(triangle) - 2, -1, -1):
            for i, valor in enumerate(triangle[fila]):
                dp[i] = valor + min(dp[i], dp[i + 1])
        return dp[0]


if __name__ == "__main__":
    s = Solution()
    assert s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert s.minimumTotal([[-10]]) == -10
    print("OK")
