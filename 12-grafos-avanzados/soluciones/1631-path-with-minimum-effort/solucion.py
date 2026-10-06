# 1631. Path with Minimum Effort (Media)
# https://leetcode.com/problems/path-with-minimum-effort/
#
# Idea: el esfuerzo de un camino es el mayor salto entre celdas vecinas; Dijkstra guardando en el
#       heap ese máximo en lugar de una suma.
# Tiempo: O(f · c · log(f · c)) · Espacio: O(f · c)

import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        filas, cols = len(heights), len(heights[0])
        esfuerzo = [[float("inf")] * cols for _ in range(filas)]
        esfuerzo[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            e, f, c = heapq.heappop(heap)
            if (f, c) == (filas - 1, cols - 1):
                return e
            if e > esfuerzo[f][c]:
                continue
            for nf, nc in ((f + 1, c), (f - 1, c), (f, c + 1), (f, c - 1)):
                if 0 <= nf < filas and 0 <= nc < cols:
                    nuevo = max(e, abs(heights[nf][nc] - heights[f][c]))
                    if nuevo < esfuerzo[nf][nc]:
                        esfuerzo[nf][nc] = nuevo
                        heapq.heappush(heap, (nuevo, nf, nc))
        return 0


if __name__ == "__main__":
    s = Solution()
    assert s.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert s.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    assert s.minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]) == 0
    print("OK")
