# 2215. Find the Difference of Two Arrays (Fácil)
# https://leetcode.com/problems/find-the-difference-of-two-arrays/
#
# Idea: paso los dos arrays a sets y me quedo con la diferencia en cada sentido.
# Tiempo: O(n + m) · Espacio: O(n + m)

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a, b = set(nums1), set(nums2)
        return [list(a - b), list(b - a)]


if __name__ == "__main__":
    s = Solution()
    r = s.findDifference([1, 2, 3], [2, 4, 6])
    assert sorted(r[0]) == [1, 3] and sorted(r[1]) == [4, 6]
    r = s.findDifference([1, 2, 3, 3], [1, 1, 2, 2])
    assert r[0] == [3] and r[1] == []
    print("OK")
