# 724. Find Pivot Index (Fácil)
# https://leetcode.com/problems/find-pivot-index/
#
# Idea: con la suma total, la suma de la derecha es total - izquierda - nums[i]; busco el primer i donde las dos sumas coinciden.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        izquierda = 0
        for i, n in enumerate(nums):
            if izquierda == total - izquierda - n:
                return i
            izquierda += n
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert s.pivotIndex([1, 2, 3]) == -1
    assert s.pivotIndex([2, 1, -1]) == 0
    print("OK")
