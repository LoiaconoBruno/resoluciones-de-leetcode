# 53. Maximum Subarray (Media)
# https://leetcode.com/problems/maximum-subarray/
#
# Idea: Kadane: llevo la mejor suma de un subarray que termina acá; si lo que venía arrastrando es
#       negativo, conviene empezar de nuevo desde este número.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mejor = actual = nums[0]
        for n in nums[1:]:
            actual = max(n, actual + n)
            mejor = max(mejor, actual)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([1]) == 1
    assert s.maxSubArray([5, 4, -1, 7, 8]) == 23
    print("OK")
