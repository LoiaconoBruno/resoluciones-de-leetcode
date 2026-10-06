# 502. IPO (Difícil)
# https://leetcode.com/problems/ipo/
#
# Idea: ordeno los proyectos por capital; en cada ronda meto en un max-heap las ganancias de todos
#       los que ya puedo pagar y hago el más rentable.
# Tiempo: O(n log n + k log n) · Espacio: O(n)

import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        proyectos = sorted(zip(capital, profits))
        disponibles = []
        i = 0
        for _ in range(k):
            while i < len(proyectos) and proyectos[i][0] <= w:
                heapq.heappush(disponibles, -proyectos[i][1])
                i += 1
            if not disponibles:
                break
            w -= heapq.heappop(disponibles)
        return w


if __name__ == "__main__":
    s = Solution()
    assert s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) == 4
    assert s.findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) == 6
    assert s.findMaximizedCapital(1, 0, [1], [1]) == 0
    print("OK")
