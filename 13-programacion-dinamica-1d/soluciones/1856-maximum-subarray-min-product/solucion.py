# 1856. Maximum Subarray Min Product (Media)
# https://leetcode.com/problems/maximum-subarray-min-product/
#
# Idea: para cada número, lo tomo como el mínimo del subarray y lo estiro lo más posible hacia los
#       dos lados mientras los vecinos sean mayores o iguales; los límites salen con una pila
#       monótona y la suma con sumas prefijas.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefijo = [0]
        for n in nums:
            prefijo.append(prefijo[-1] + n)
        mejor = 0
        pila = []
        for i, n in enumerate(nums + [0]):
            inicio = i
            while pila and pila[-1][1] > n:
                j, minimo = pila.pop()
                mejor = max(mejor, minimo * (prefijo[i] - prefijo[j]))
                inicio = j
            pila.append((inicio, n))
        return mejor % (10 ** 9 + 7)


if __name__ == "__main__":
    s = Solution()
    assert s.maxSumMinProduct([1, 2, 3, 2]) == 14
    assert s.maxSumMinProduct([2, 3, 3, 1, 2]) == 18
    assert s.maxSumMinProduct([3, 1, 5, 6, 4, 2]) == 60
    print("OK")
