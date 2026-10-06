# 456. 132 Pattern (Media)
# https://leetcode.com/problems/132-pattern/
#
# Idea: recorro de derecha a izquierda con una pila decreciente; lo que saco de la pila es un candidato a "2" (tiene a su izquierda un "3" más grande). Si aparece un número menor que ese candidato, es el "1".
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        pila = []
        dos = float("-inf")
        for n in reversed(nums):
            if n < dos:
                return True
            while pila and pila[-1] < n:
                dos = pila.pop()
            pila.append(n)
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.find132pattern([1, 2, 3, 4]) is False
    assert s.find132pattern([3, 1, 4, 2]) is True
    assert s.find132pattern([-1, 3, 2, 0]) is True
    assert s.find132pattern([1, 0, 1, -4, -3]) is False
    print("OK")
