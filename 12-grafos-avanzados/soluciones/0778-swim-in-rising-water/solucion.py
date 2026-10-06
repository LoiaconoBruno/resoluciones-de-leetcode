# 778. Swim In Rising Water (Difícil)
# https://leetcode.com/problems/swim-in-rising-water/
#
# Idea: el costo de un camino es su celda más alta; uso Dijkstra pero guardando en el heap el máximo
#       del camino en vez de la suma. La primera vez que saco la esquina final, ese es el tiempo
#       mínimo.
# Tiempo: O(n² log n) · Espacio: O(n²)

import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visto = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        visto[0][0] = True
        while heap:
            tiempo, f, c = heapq.heappop(heap)
            if f == c == n - 1:
                return tiempo
            for nf, nc in ((f + 1, c), (f - 1, c), (f, c + 1), (f, c - 1)):
                if 0 <= nf < n and 0 <= nc < n and not visto[nf][nc]:
                    visto[nf][nc] = True
                    heapq.heappush(heap, (max(tiempo, grid[nf][nc]), nf, nc))
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.swimInWater([[0, 2], [1, 3]]) == 3
    grilla = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    assert s.swimInWater(grilla) == 16
    print("OK")
