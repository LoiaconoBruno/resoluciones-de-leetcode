# 283. Move Zeroes (Fácil)
# https://leetcode.com/problems/move-zeroes/
#
# Idea: un puntero marca dónde va el próximo no-cero; cada no-cero que encuentro lo intercambio a
#       esa posición y los ceros quedan atrás solos.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1


if __name__ == "__main__":
    s = Solution()
    a = [0, 1, 0, 3, 12]
    s.moveZeroes(a)
    assert a == [1, 3, 12, 0, 0]
    a = [0]
    s.moveZeroes(a)
    assert a == [0]
    print("OK")
