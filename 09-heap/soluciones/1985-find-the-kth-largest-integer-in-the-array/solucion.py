# 1985. Find The Kth Largest Integer In The Array (Media)
# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
#
# Idea: comparo los números como texto: primero por largo y, a igual largo, alfabéticamente (así no
#       convierto números de 100 dígitos). Min-heap de tamaño k con esa clave.
# Tiempo: O(n log k · m), con m la cantidad de dígitos · Espacio: O(k)

import heapq
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        for n in nums:
            heapq.heappush(heap, (len(n), n))
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0][1]


if __name__ == "__main__":
    s = Solution()
    assert s.kthLargestNumber(["3", "6", "7", "10"], 4) == "3"
    assert s.kthLargestNumber(["2", "21", "12", "1"], 3) == "2"
    assert s.kthLargestNumber(["0", "0"], 2) == "0"
    print("OK")
