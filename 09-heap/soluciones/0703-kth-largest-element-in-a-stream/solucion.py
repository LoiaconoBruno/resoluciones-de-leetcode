# 703. Kth Largest Element In a Stream (Fácil)
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
#
# Idea: mantengo un min-heap con los k más grandes; su raíz es justo el k-ésimo más grande. Si entra
#       uno nuevo y el heap se pasa de k, saco el menor.
# Tiempo: O(log k) por add · Espacio: O(k)

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    k = KthLargest(3, [4, 5, 8, 2])
    assert [k.add(v) for v in [3, 5, 10, 9, 4]] == [4, 5, 5, 8, 8]
    k = KthLargest(1, [])
    assert k.add(-3) == -3 and k.add(-2) == -2
    print("OK")
