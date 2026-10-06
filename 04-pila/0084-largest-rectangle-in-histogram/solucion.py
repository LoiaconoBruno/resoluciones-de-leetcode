# 84. Largest Rectangle In Histogram (Difícil)
# https://leetcode.com/problems/largest-rectangle-in-histogram/
#
# Idea: pila de barras con alturas crecientes; cuando llega una más baja, cada barra que sale ya
#       sabe hasta dónde se extiende su rectángulo (desde el índice donde empezó hasta acá).
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pila = []
        mejor = 0
        for i, h in enumerate(heights + [0]):
            inicio = i
            while pila and pila[-1][1] > h:
                j, alto = pila.pop()
                mejor = max(mejor, alto * (i - j))
                inicio = j
            pila.append((inicio, h))
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert s.largestRectangleArea([2, 4]) == 4
    print("OK")
