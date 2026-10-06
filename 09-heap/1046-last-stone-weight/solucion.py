# 1046. Last Stone Weight (Fácil)
# https://leetcode.com/problems/last-stone-weight/
#
# Idea: max-heap (en Python, min-heap con los valores negados): saco las dos más pesadas y, si no
#       son iguales, vuelvo a meter la diferencia.
# Tiempo: O(n log n) · Espacio: O(n)

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-p for p in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            if a != b:
                heapq.heappush(heap, -(a - b))
        return -heap[0] if heap else 0


if __name__ == "__main__":
    s = Solution()
    assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeight([1]) == 1
    assert s.lastStoneWeight([3, 3]) == 0
    print("OK")
