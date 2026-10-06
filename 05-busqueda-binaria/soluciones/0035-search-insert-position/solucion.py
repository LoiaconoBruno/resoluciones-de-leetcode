# 35. Search Insert Position (Fácil)
# https://leetcode.com/problems/search-insert-position/
#
# Idea: búsqueda binaria normal; si no lo encuentro, izq termina justo en la posición donde habría
#       que insertarlo.
# Tiempo: O(log n) · Espacio: O(1)

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        izq, der = 0, len(nums) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if nums[medio] == target:
                return medio
            if nums[medio] < target:
                izq = medio + 1
            else:
                der = medio - 1
        return izq


if __name__ == "__main__":
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 7) == 4
    assert s.searchInsert([1, 3, 5, 6], 0) == 0
    print("OK")
