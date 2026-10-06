# 153. Find Minimum In Rotated Sorted Array (Media)
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Idea: comparo el medio con el último: si es mayor, el mínimo está a la derecha del medio; si no, el medio puede ser el mínimo y sigo por la izquierda (incluyéndolo).
# Tiempo: O(log n) · Espacio: O(1)

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        izq, der = 0, len(nums) - 1
        while izq < der:
            medio = (izq + der) // 2
            if nums[medio] > nums[der]:
                izq = medio + 1
            else:
                der = medio
        return nums[izq]


if __name__ == "__main__":
    s = Solution()
    assert s.findMin([3, 4, 5, 1, 2]) == 1
    assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert s.findMin([11, 13, 15, 17]) == 11
    print("OK")
