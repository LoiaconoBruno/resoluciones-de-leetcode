# 977. Squares of a Sorted Array (Fácil)
# https://leetcode.com/problems/squares-of-a-sorted-array/
#
# Idea: los cuadrados más grandes están en las puntas (negativos grandes o positivos grandes); con
#       dos punteros lleno la respuesta desde el final.
# Tiempo: O(n) · Espacio: O(n) (la respuesta)

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        izq, der = 0, len(nums) - 1
        for k in range(len(nums) - 1, -1, -1):
            if abs(nums[izq]) > abs(nums[der]):
                res[k] = nums[izq] ** 2
                izq += 1
            else:
                res[k] = nums[der] ** 2
                der -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert s.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    print("OK")
