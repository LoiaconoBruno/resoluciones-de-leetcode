# 2542. Maximum Subsequence Score (Media)
# https://leetcode.com/problems/maximum-subsequence-score/
#
# Idea: ordeno los pares por nums2 de mayor a menor: al recorrerlos, el nums2 actual es el mínimo de
#       lo elegido. Llevo en un min-heap los k nums1 más grandes y su suma.
# Tiempo: O(n log n) · Espacio: O(n)

import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pares = sorted(zip(nums1, nums2), key=lambda p: -p[1])
        heap = []
        suma = mejor = 0
        for a, b in pares:
            heapq.heappush(heap, a)
            suma += a
            if len(heap) > k:
                suma -= heapq.heappop(heap)
            if len(heap) == k:
                mejor = max(mejor, suma * b)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3) == 12
    assert s.maxScore([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1) == 30
    print("OK")
