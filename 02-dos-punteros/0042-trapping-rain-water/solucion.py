# 42. Trapping Rain Water (Difícil)
# https://leetcode.com/problems/trapping-rain-water/
#
# Idea: el agua sobre una barra es min(máximo a la izquierda, máximo a la derecha) - altura; con dos
#       punteros avanzo siempre por el lado de máximo más bajo, porque ese es el que limita.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        izq, der = 0, len(height) - 1
        max_izq = max_der = 0
        agua = 0
        while izq < der:
            if height[izq] < height[der]:
                max_izq = max(max_izq, height[izq])
                agua += max_izq - height[izq]
                izq += 1
            else:
                max_der = max(max_der, height[der])
                agua += max_der - height[der]
                der -= 1
        return agua


if __name__ == "__main__":
    s = Solution()
    assert s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert s.trap([4, 2, 0, 3, 2, 5]) == 9
    print("OK")
