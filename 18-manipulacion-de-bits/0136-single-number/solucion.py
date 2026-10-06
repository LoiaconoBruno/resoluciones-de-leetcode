# 136. Single Number (Fácil)
# https://leetcode.com/problems/single-number/
#
# Idea: XOR de todo: x ^ x = 0 y x ^ 0 = x, así que los pares se cancelan y queda solo el que
#       aparece una vez.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.singleNumber([2, 2, 1]) == 1
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
    assert s.singleNumber([1]) == 1
    print("OK")
