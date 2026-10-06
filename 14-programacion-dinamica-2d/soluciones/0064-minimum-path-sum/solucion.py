# 64. Minimum Path Sum (Media)
# https://leetcode.com/problems/minimum-path-sum/
#
# Idea: a cada celda llego desde arriba o desde la izquierda; el costo mínimo es su valor + el menor
#       de esos dos. Reuso una sola fila.
# Tiempo: O(m · n) · Espacio: O(n)

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        fila = [float("inf")] * cols
        fila[0] = 0
        for valores in grid:
            fila[0] += valores[0]
            for c in range(1, cols):
                fila[c] = valores[c] + min(fila[c], fila[c - 1])
        return fila[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert s.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
    print("OK")
