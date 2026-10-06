# 1857. Largest Color Value in a Directed Graph (Difícil)
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
#
# Idea: orden topológico (Kahn) llevando, para cada nodo y cada color, la mayor cantidad de ese
#       color en un camino que termina ahí; al pasar a un vecino propago esos conteos. Si no proceso
#       todos los nodos, hay un ciclo.
# Tiempo: O(26 · (V + E)) · Espacio: O(26 · V)

from collections import deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        vecinos = [[] for _ in range(n)]
        entrantes = [0] * n
        for a, b in edges:
            vecinos[a].append(b)
            entrantes[b] += 1
        cuenta = [[0] * 26 for _ in range(n)]
        cola = deque(i for i in range(n) if entrantes[i] == 0)
        procesados = mejor = 0
        while cola:
            nodo = cola.popleft()
            procesados += 1
            cuenta[nodo][ord(colors[nodo]) - 97] += 1
            mejor = max(mejor, cuenta[nodo][ord(colors[nodo]) - 97])
            for v in vecinos[nodo]:
                for k in range(26):
                    if cuenta[nodo][k] > cuenta[v][k]:
                        cuenta[v][k] = cuenta[nodo][k]
                entrantes[v] -= 1
                if entrantes[v] == 0:
                    cola.append(v)
        return mejor if procesados == n else -1


if __name__ == "__main__":
    s = Solution()
    assert s.largestPathValue("abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]) == 3
    assert s.largestPathValue("a", [[0, 0]]) == -1
    print("OK")
