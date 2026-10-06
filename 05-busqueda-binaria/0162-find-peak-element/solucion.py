# 162. Find Peak Element (Media)
# https://leetcode.com/problems/find-peak-element/
#
# Idea: si nums[medio] < nums[medio + 1] estoy subiendo, así que hay un pico a la derecha; si no,
#       hay uno a la izquierda (o es el medio).
# Tiempo: O(log n) · Espacio: O(1)

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        izq, der = 0, len(nums) - 1
        while izq < der:
            medio = (izq + der) // 2
            if nums[medio] < nums[medio + 1]:
                izq = medio + 1
            else:
                der = medio
        return izq


if __name__ == "__main__":
    s = Solution()

    def es_pico(a, i):
        return (i == 0 or a[i] > a[i - 1]) and (i == len(a) - 1 or a[i] > a[i + 1])

    assert s.findPeakElement([1, 2, 3, 1]) == 2
    a = [1, 2, 1, 3, 5, 6, 4]
    assert es_pico(a, s.findPeakElement(a))
    assert s.findPeakElement([1]) == 0
    print("OK")
