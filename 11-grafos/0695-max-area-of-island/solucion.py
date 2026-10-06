# 695. Max Area of Island (Media)
# https://leetcode.com/problems/max-area-of-island/
#
# Idea: igual que contar islas, pero el DFS de cada isla cuenta cuántas celdas hunde; me quedo con
#       el máximo.
# Tiempo: O(f · c) · Espacio: O(f · c)

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        filas, cols = len(grid), len(grid[0])
        mejor = 0
        for f in range(filas):
            for c in range(cols):
                if grid[f][c] != 1:
                    continue
                grid[f][c] = 0
                pila = [(f, c)]
                area = 0
                while pila:
                    i, j = pila.pop()
                    area += 1
                    for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= ni < filas and 0 <= nj < cols and grid[ni][nj] == 1:
                            grid[ni][nj] = 0
                            pila.append((ni, nj))
                mejor = max(mejor, area)
        return mejor


if __name__ == "__main__":
    s = Solution()
    grilla = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    assert s.maxAreaOfIsland(grilla) == 6
    assert s.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
    print("OK")
