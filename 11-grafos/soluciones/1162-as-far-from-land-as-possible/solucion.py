# 1162. As Far from Land as Possible (Media)
# https://leetcode.com/problems/as-far-from-land-as-possible/
#
# Idea: BFS que arranca desde todas las celdas de tierra a la vez; la última celda de agua que
#       alcanzo es la más lejana, y su nivel es la respuesta.
# Tiempo: O(n²) · Espacio: O(n²)

from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cola = deque((f, c) for f in range(n) for c in range(n) if grid[f][c] == 1)
        if len(cola) in (0, n * n):
            return -1
        distancia = -1
        while cola:
            distancia += 1
            for _ in range(len(cola)):
                f, c = cola.popleft()
                for nf, nc in ((f + 1, c), (f - 1, c), (f, c + 1), (f, c - 1)):
                    if 0 <= nf < n and 0 <= nc < n and grid[nf][nc] == 0:
                        grid[nf][nc] = 1
                        cola.append((nf, nc))
        return distancia


if __name__ == "__main__":
    s = Solution()
    assert s.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2
    assert s.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4
    assert s.maxDistance([[0, 0], [0, 0]]) == -1
    assert s.maxDistance([[1, 1], [1, 1]]) == -1
    print("OK")
