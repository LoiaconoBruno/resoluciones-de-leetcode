# 215. Kth Largest Element In An Array (Media)
# https://leetcode.com/problems/kth-largest-element-in-an-array/
#
# Idea: min-heap con los k más grandes vistos; al terminar, la raíz es el k-ésimo más grande.
# Tiempo: O(n log k) · Espacio: O(k)

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


if __name__ == "__main__":
    s = Solution()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    print("OK")
