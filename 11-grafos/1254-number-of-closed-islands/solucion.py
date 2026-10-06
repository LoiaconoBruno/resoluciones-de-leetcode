# 1254. Number of Closed Islands (Media)
# https://leetcode.com/problems/number-of-closed-islands/
#
# Idea: primero hundo (con DFS) toda la tierra conectada al borde, porque esas islas no están
#       cerradas; después cuento las islas que quedan como en Number of Islands.
# Tiempo: O(f · c) · Espacio: O(f · c)

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        filas, cols = len(grid), len(grid[0])

        def hundir(f, c):
            pila = [(f, c)]
            while pila:
                i, j = pila.pop()
                if 0 <= i < filas and 0 <= j < cols and grid[i][j] == 0:
                    grid[i][j] = 1
                    pila.extend(((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)))

        for f in range(filas):
            for c in range(cols):
                if f in (0, filas - 1) or c in (0, cols - 1):
                    hundir(f, c)
        islas = 0
        for f in range(filas):
            for c in range(cols):
                if grid[f][c] == 0:
                    islas += 1
                    hundir(f, c)
        return islas


if __name__ == "__main__":
    s = Solution()
    assert s.closedIsland([[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0],
                           [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]) == 2
    assert s.closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]) == 1
    assert s.closedIsland([[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1],
                           [1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]) == 2
    print("OK")
