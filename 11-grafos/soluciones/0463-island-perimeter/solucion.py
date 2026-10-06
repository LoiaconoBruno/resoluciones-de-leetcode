# 463. Island Perimeter (Fácil)
# https://leetcode.com/problems/island-perimeter/
#
# Idea: cada celda de tierra aporta 4 lados, y cada par de celdas de tierra pegadas tapa 2 (uno de
#       cada una). Cuento mirando solo arriba y a la izquierda para no contar dos veces.
# Tiempo: O(f · c) · Espacio: O(1)

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimetro = 0
        for f in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[f][c] == 1:
                    perimetro += 4
                    if f > 0 and grid[f - 1][c] == 1:
                        perimetro -= 2
                    if c > 0 and grid[f][c - 1] == 1:
                        perimetro -= 2
        return perimetro


if __name__ == "__main__":
    s = Solution()
    assert s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
    assert s.islandPerimeter([[1]]) == 4
    assert s.islandPerimeter([[1, 0]]) == 4
    print("OK")
