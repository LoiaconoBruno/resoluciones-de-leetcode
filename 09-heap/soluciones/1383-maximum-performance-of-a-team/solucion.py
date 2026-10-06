# 1383. Maximum Performance of a Team (Difícil)
# https://leetcode.com/problems/maximum-performance-of-a-team/
#
# Idea: ordeno a los ingenieros por eficiencia de mayor a menor: el actual es el mínimo del equipo.
#       Llevo en un min-heap las k velocidades más altas (y su suma) y pruebo suma · eficiencia.
# Tiempo: O(n log n) · Espacio: O(n)

import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        ingenieros = sorted(zip(efficiency, speed), reverse=True)
        heap = []
        suma = mejor = 0
        for eficiencia, velocidad in ingenieros:
            heapq.heappush(heap, velocidad)
            suma += velocidad
            if len(heap) > k:
                suma -= heapq.heappop(heap)
            mejor = max(mejor, suma * eficiencia)
        return mejor % (10 ** 9 + 7)


if __name__ == "__main__":
    s = Solution()
    velocidad, eficiencia = [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2]
    assert s.maxPerformance(6, velocidad, eficiencia, 2) == 60
    assert s.maxPerformance(6, velocidad, eficiencia, 3) == 68
    assert s.maxPerformance(6, velocidad, eficiencia, 4) == 72
    print("OK")
