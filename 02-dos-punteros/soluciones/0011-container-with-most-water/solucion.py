# 11. Container With Most Water (Media)
# https://leetcode.com/problems/container-with-most-water/
#
# Idea: arranco con el recipiente más ancho y siempre muevo la pared más baja: es la que limita el
#       agua, moverla es la única chance de mejorar.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        izq, der = 0, len(height) - 1
        mejor = 0
        while izq < der:
            mejor = max(mejor, (der - izq) * min(height[izq], height[der]))
            if height[izq] < height[der]:
                izq += 1
            else:
                der -= 1
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert s.maxArea([1, 1]) == 1
    print("OK")
