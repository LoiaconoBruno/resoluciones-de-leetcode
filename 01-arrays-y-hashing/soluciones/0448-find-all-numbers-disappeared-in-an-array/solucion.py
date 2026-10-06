# 448. Find All Numbers Disappeared in An Array (Fácil)
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
#
# Idea: uso el propio array como marca: por cada número n pongo en negativo la posición n - 1; las
#       posiciones que quedan positivas son los que faltan.
# Tiempo: O(n) · Espacio: O(1) extra

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) - 1
            nums[i] = -abs(nums[i])
        return [i + 1 for i, n in enumerate(nums) if n > 0]


if __name__ == "__main__":
    s = Solution()
    assert s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert s.findDisappearedNumbers([1, 1]) == [2]
    print("OK")
