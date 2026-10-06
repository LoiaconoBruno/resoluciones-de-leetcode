# 34. Find First And Last Position of Element In Sorted Array (Media)
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#
# Idea: dos búsquedas binarias: una que, al encontrar el target, sigue buscando a la izquierda (primera aparición) y otra que sigue a la derecha (última).
# Tiempo: O(log n) · Espacio: O(1)

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def buscar(hacia_izquierda):
            izq, der = 0, len(nums) - 1
            res = -1
            while izq <= der:
                medio = (izq + der) // 2
                if nums[medio] < target:
                    izq = medio + 1
                elif nums[medio] > target:
                    der = medio - 1
                else:
                    res = medio
                    if hacia_izquierda:
                        der = medio - 1
                    else:
                        izq = medio + 1
            return res

        return [buscar(True), buscar(False)]


if __name__ == "__main__":
    s = Solution()
    assert s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert s.searchRange([], 0) == [-1, -1]
    print("OK")
