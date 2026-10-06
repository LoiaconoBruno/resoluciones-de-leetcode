# 1466. Reorder Routes to Make All Paths Lead to The City Zero (Media)
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
#
# Idea: recorro el árbol desde la ciudad 0 como si fuera no dirigido, pero recuerdo el sentido real
#       de cada ruta; cada ruta que apunta "hacia afuera" (de 0 hacia las hojas) hay que darla
#       vuelta.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        vecinos = [[] for _ in range(n)]
        for a, b in connections:
            vecinos[a].append((b, 1))
            vecinos[b].append((a, 0))
        cambios = 0
        visitado = [False] * n
        visitado[0] = True
        pila = [0]
        while pila:
            ciudad = pila.pop()
            for vecina, hay_que_cambiar in vecinos[ciudad]:
                if not visitado[vecina]:
                    visitado[vecina] = True
                    cambios += hay_que_cambiar
                    pila.append(vecina)
        return cambios


if __name__ == "__main__":
    s = Solution()
    assert s.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
    assert s.minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
    assert s.minReorder(3, [[1, 0], [2, 0]]) == 0
    print("OK")
