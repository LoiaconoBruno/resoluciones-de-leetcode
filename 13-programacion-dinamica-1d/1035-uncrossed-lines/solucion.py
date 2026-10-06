# 1035. Uncrossed Lines (Media)
# https://leetcode.com/problems/uncrossed-lines/
#
# Idea: líneas que no se cruzan = subsecuencia común más larga (LCS) entre los dos arrays. Hago la
#       tabla de LCS guardando solo la fila anterior.
# Tiempo: O(n · m) · Espacio: O(m)

from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        anterior = [0] * (len(nums2) + 1)
        for a in nums1:
            actual = [0] * (len(nums2) + 1)
            for j, b in enumerate(nums2):
                actual[j + 1] = anterior[j] + 1 if a == b else max(anterior[j + 1], actual[j])
            anterior = actual
        return anterior[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.maxUncrossedLines([1, 4, 2], [1, 2, 4]) == 2
    assert s.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]) == 3
    assert s.maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]) == 2
    print("OK")
