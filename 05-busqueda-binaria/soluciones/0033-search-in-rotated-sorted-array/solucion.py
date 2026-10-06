# 33. Search In Rotated Sorted Array (Media)
# https://leetcode.com/problems/search-in-rotated-sorted-array/
#
# Idea: en un array rotado, al menos una de las dos mitades (izq..medio o medio..der) está ordenada;
#       me fijo si el target cae en esa mitad ordenada y descarto la otra.
# Tiempo: O(log n) · Espacio: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        izq, der = 0, len(nums) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if nums[medio] == target:
                return medio
            if nums[izq] <= nums[medio]:
                if nums[izq] <= target < nums[medio]:
                    der = medio - 1
                else:
                    izq = medio + 1
            else:
                if nums[medio] < target <= nums[der]:
                    izq = medio + 1
                else:
                    der = medio - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([1], 0) == -1
    assert s.search([3, 1], 1) == 1
    print("OK")
