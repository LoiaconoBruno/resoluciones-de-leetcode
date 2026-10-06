# 540. Single Element in a Sorted Array (Media)
# https://leetcode.com/problems/single-element-in-a-sorted-array/
#
# Idea: antes del número solo, cada par empieza en índice par; después, en índice impar. Miro un índice par en el medio: si es igual a su siguiente, el solo está más a la derecha.
# Tiempo: O(log n) · Espacio: O(1)

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        izq, der = 0, len(nums) - 1
        while izq < der:
            medio = (izq + der) // 2
            if medio % 2:
                medio -= 1
            if nums[medio] == nums[medio + 1]:
                izq = medio + 2
            else:
                der = medio
        return nums[izq]


if __name__ == "__main__":
    s = Solution()
    assert s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
    assert s.singleNonDuplicate([1]) == 1
    print("OK")
