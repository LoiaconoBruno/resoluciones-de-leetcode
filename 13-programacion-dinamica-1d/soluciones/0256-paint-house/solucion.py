# 256. Paint House (Media)
# https://leetcode.com/problems/paint-house/
#
# Idea: el costo mínimo de pintar hasta la casa i con el color c es su costo + el mínimo de la casa
#       anterior pintada con cualquiera de los otros dos colores.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        rojo = azul = verde = 0
        for r, a, v in costs:
            rojo, azul, verde = r + min(azul, verde), a + min(rojo, verde), v + min(rojo, azul)
        return min(rojo, azul, verde)


if __name__ == "__main__":
    s = Solution()
    assert s.minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10
    assert s.minCost([[7, 6, 2]]) == 2
    assert s.minCost([]) == 0
    print("OK")
