# 238. Product of Array Except Self (Media)
# https://leetcode.com/problems/product-of-array-except-self/
#
# Idea: el resultado en i es (producto de todo lo que está a la izquierda) × (producto de todo lo que está a la derecha); hago una pasada para cada lado.
# Tiempo: O(n) · Espacio: O(1) extra (sin contar la respuesta)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        izquierda = 1
        for i in range(n):
            res[i] = izquierda
            izquierda *= nums[i]
        derecha = 1
        for i in range(n - 1, -1, -1):
            res[i] *= derecha
            derecha *= nums[i]
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("OK")
