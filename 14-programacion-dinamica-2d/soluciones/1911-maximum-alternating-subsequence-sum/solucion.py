# 1911. Maximum Alternating Subsequence Sum (Media)
# https://leetcode.com/problems/maximum-alternating-subsequence-sum/
#
# Idea: dos estados: la mejor suma si el último elegido quedó en posición par (suma) o impar
#       (resta). Cada número puede extender cualquiera de los dos.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        par, impar = 0, 0
        for n in nums:
            par, impar = max(par, impar + n), max(impar, par - n)
        return par


if __name__ == "__main__":
    s = Solution()
    assert s.maxAlternatingSum([4, 2, 5, 3]) == 7
    assert s.maxAlternatingSum([5, 6, 7, 8]) == 8
    assert s.maxAlternatingSum([6, 2, 1, 2, 4, 5]) == 10
    print("OK")
