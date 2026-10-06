# 875. Koko Eating Bananas (Media)
# https://leetcode.com/problems/koko-eating-bananas/
#
# Idea: búsqueda binaria sobre la respuesta: para una velocidad v, las horas son la suma de
#       ceil(pila / v). Busco la menor v que entra en h horas.
# Tiempo: O(n log M), con M la pila más grande · Espacio: O(1)

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        izq, der = 1, max(piles)
        while izq < der:
            v = (izq + der) // 2
            horas = sum((p + v - 1) // v for p in piles)
            if horas <= h:
                der = v
            else:
                izq = v + 1
        return izq


if __name__ == "__main__":
    s = Solution()
    assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    print("OK")
