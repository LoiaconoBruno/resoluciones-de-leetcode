# 268. Missing Number (Fácil)
# https://leetcode.com/problems/missing-number/
#
# Idea: hago XOR de todos los índices 0..n con todos los números: cada número presente se cancela
#       con su índice y sobrevive solo el que falta.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, n in enumerate(nums):
            res ^= i ^ n
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.missingNumber([3, 0, 1]) == 2
    assert s.missingNumber([0, 1]) == 2
    assert s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    print("OK")
