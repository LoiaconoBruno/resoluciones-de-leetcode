# 1091. Shortest Path in Binary Matrix (Media)
# https://leetcode.com/problems/shortest-path-in-binary-matrix/
#
# Idea: BFS desde la esquina (0, 0) moviéndome en 8 direcciones por celdas con 0; el nivel en que
#       llego a la esquina opuesta es el largo del camino más corto.
# Tiempo: O(n²) · Espacio: O(n²)

from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        grid[0][0] = 1
        cola = deque([(0, 0, 1)])
        while cola:
            f, c, largo = cola.popleft()
            if f == c == n - 1:
                return largo
            for df in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nf, nc = f + df, c + dc
                    if 0 <= nf < n and 0 <= nc < n and grid[nf][nc] == 0:
                        grid[nf][nc] = 1
                        cola.append((nf, nc, largo + 1))
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2
    assert s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    assert s.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
    assert s.shortestPathBinaryMatrix([[0]]) == 1
    print("OK")
