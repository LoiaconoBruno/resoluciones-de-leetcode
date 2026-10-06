# 300. Longest Increasing Subsequence (Media)
# https://leetcode.com/problems/longest-increasing-subsequence/
#
# Idea: colas[i] guarda el menor final posible de una subsecuencia creciente de largo i + 1. Cada
#       número reemplaza (con búsqueda binaria) el primer final que sea ≥ a él, o alarga la lista.
# Tiempo: O(n log n) · Espacio: O(n)

from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        colas = []
        for n in nums:
            i = bisect_left(colas, n)
            if i == len(colas):
                colas.append(n)
            else:
                colas[i] = n
        return len(colas)


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert s.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    print("OK")
