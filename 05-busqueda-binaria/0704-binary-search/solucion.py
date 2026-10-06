# 704. Binary Search (Fácil)
# https://leetcode.com/problems/binary-search/
#
# Idea: miro el del medio: si es el target, listo; si es más chico, el target solo puede estar a la
#       derecha; si es más grande, a la izquierda.
# Tiempo: O(log n) · Espacio: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        izq, der = 0, len(nums) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if nums[medio] == target:
                return medio
            if nums[medio] < target:
                izq = medio + 1
            else:
                der = medio - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1
    print("OK")
