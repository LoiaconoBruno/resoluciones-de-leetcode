# 1376. Time Needed to Inform All Employees (Media)
# https://leetcode.com/problems/time-needed-to-inform-all-employees/
#
# Idea: armo el árbol jefe -> subordinados y bajo desde el jefe principal acumulando el tiempo de
#       aviso; la respuesta es el camino más largo hasta un empleado.
# Tiempo: O(n) · Espacio: O(n)

from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinados = defaultdict(list)
        for empleado, jefe in enumerate(manager):
            if jefe != -1:
                subordinados[jefe].append(empleado)
        mejor = 0
        pila = [(headID, 0)]
        while pila:
            empleado, tiempo = pila.pop()
            mejor = max(mejor, tiempo)
            for sub in subordinados[empleado]:
                pila.append((sub, tiempo + informTime[empleado]))
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.numOfMinutes(1, 0, [-1], [0]) == 0
    assert s.numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]) == 1
    assert s.numOfMinutes(7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]) == 21
    print("OK")
