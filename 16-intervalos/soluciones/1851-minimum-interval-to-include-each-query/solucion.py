# 1851. Minimum Interval to Include Each Query (Difícil)
# https://leetcode.com/problems/minimum-interval-to-include-each-query/
#
# Idea: ordeno intervalos y consultas por inicio/valor. Para cada consulta meto en un min-heap (por
#       tamaño) los intervalos que ya empezaron y saco los que terminaron antes de la consulta; el
#       tope es la respuesta.
# Tiempo: O(n log n + q log q) · Espacio: O(n + q)

import heapq
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = []
        respuesta = {}
        i = 0
        for q in sorted(set(queries)):
            while i < len(intervals) and intervals[i][0] <= q:
                inicio, fin = intervals[i]
                heapq.heappush(heap, (fin - inicio + 1, fin))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            respuesta[q] = heap[0][0] if heap else -1
        return [respuesta[q] for q in queries]


if __name__ == "__main__":
    s = Solution()
    assert s.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]) == [3, 3, 1, 4]
    assert s.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]) == [2, -1, 4, 6]
    print("OK")
