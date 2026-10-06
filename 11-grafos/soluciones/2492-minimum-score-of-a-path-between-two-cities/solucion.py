# 2492. Minimum Score of a Path Between Two Cities (Media)
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
#
# Idea: el camino puede repetir rutas, así que puedo usar cualquier ruta de la componente que
#       contiene a 1 (y a n). La respuesta es la ruta más corta de esa componente; la recorro con
#       BFS.
# Tiempo: O(n + rutas) · Espacio: O(n + rutas)

from collections import deque
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        vecinos = [[] for _ in range(n + 1)]
        for a, b, d in roads:
            vecinos[a].append((b, d))
            vecinos[b].append((a, d))
        minimo = float("inf")
        visitado = [False] * (n + 1)
        visitado[1] = True
        cola = deque([1])
        while cola:
            ciudad = cola.popleft()
            for vecina, d in vecinos[ciudad]:
                minimo = min(minimo, d)
                if not visitado[vecina]:
                    visitado[vecina] = True
                    cola.append(vecina)
        return minimo


if __name__ == "__main__":
    s = Solution()
    assert s.minScore(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]) == 5
    assert s.minScore(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]) == 2
    print("OK")
