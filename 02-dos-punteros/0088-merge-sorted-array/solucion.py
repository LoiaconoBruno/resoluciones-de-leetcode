# 88. Merge Sorted Array (Fácil)
# https://leetcode.com/problems/merge-sorted-array/
#
# Idea: lleno nums1 desde el final poniendo siempre el mayor de los dos; así nunca piso un número que todavía no usé.
# Tiempo: O(m + n) · Espacio: O(1)

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        for k in range(m + n - 1, -1, -1):
            if j < 0:
                break
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1


if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 3, 0, 0, 0]
    s.merge(a, 3, [2, 5, 6], 3)
    assert a == [1, 2, 2, 3, 5, 6]
    a = [1]
    s.merge(a, 1, [], 0)
    assert a == [1]
    a = [0]
    s.merge(a, 0, [1], 1)
    assert a == [1]
    print("OK")
