# 2348. Number of Zero-Filled Subarrays (Media)
# https://leetcode.com/problems/number-of-zero-filled-subarrays/
#
# Idea: una racha de largo L de ceros aporta 1 + 2 + ... + L subarrays; sumo el largo de la racha
#       actual en cada cero.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = racha = 0
        for n in nums:
            racha = racha + 1 if n == 0 else 0
            res += racha
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6
    assert s.zeroFilledSubarray([0, 0, 0, 2, 0, 0]) == 9
    assert s.zeroFilledSubarray([2, 10, 2019]) == 0
    print("OK")
