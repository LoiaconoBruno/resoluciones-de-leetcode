# 973. K Closest Points to Origin (Media)
# https://leetcode.com/problems/k-closest-points-to-origin/
#
# Idea: max-heap de tamaño k por distancia (negada): si entra un punto y el heap se pasa de k, sale
#       el más lejano. No hace falta la raíz cuadrada: comparo x² + y².
# Tiempo: O(n log k) · Espacio: O(k)

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (-(x * x + y * y), x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]


if __name__ == "__main__":
    s = Solution()
    assert s.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert sorted(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2)) == [[-2, 4], [3, 3]]
    print("OK")
