# 152. Maximum Product Subarray (Media)
# https://leetcode.com/problems/maximum-product-subarray/
#
# Idea: llevo el producto máximo y el mínimo que terminan en la posición actual, porque un negativo
#       puede convertir el mínimo en el nuevo máximo.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mejor = maximo = minimo = nums[0]
        for n in nums[1:]:
            candidatos = (n, maximo * n, minimo * n)
            maximo, minimo = max(candidatos), min(candidatos)
            mejor = max(mejor, maximo)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.maxProduct([2, 3, -2, 4]) == 6
    assert s.maxProduct([-2, 0, -1]) == 0
    assert s.maxProduct([-2, 3, -4]) == 24
    print("OK")
