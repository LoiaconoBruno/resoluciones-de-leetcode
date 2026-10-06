# 496. Next Greater Element I (Fácil)
# https://leetcode.com/problems/next-greater-element-i/
#
# Idea: recorro nums2 con una pila decreciente; cuando llega un número más grande, es el siguiente
#       mayor de todos los que saca de la pila. Guardo eso en un diccionario.
# Tiempo: O(n + m) · Espacio: O(m)

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        siguiente_mayor = {}
        pila = []
        for n in nums2:
            while pila and pila[-1] < n:
                siguiente_mayor[pila.pop()] = n
            pila.append(n)
        return [siguiente_mayor.get(n, -1) for n in nums1]


if __name__ == "__main__":
    s = Solution()
    assert s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert s.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
    print("OK")
