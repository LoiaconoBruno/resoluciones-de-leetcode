# 946. Validate Stack Sequences (Media)
# https://leetcode.com/problems/validate-stack-sequences/
#
# Idea: simulo: apilo en el orden de pushed y, cada vez que el tope coincide con el próximo de
#       popped, lo saco. Si al final la pila queda vacía, la secuencia era posible.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pila = []
        i = 0
        for x in pushed:
            pila.append(x)
            while pila and pila[-1] == popped[i]:
                pila.pop()
                i += 1
        return not pila


if __name__ == "__main__":
    s = Solution()
    assert s.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) is True
    assert s.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) is False
    print("OK")
