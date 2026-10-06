# 802. Find Eventual Safe States (Media)
# https://leetcode.com/problems/find-eventual-safe-states/
#
# Idea: un nodo es seguro si todos sus caminos terminan; invierto las aristas y hago Kahn desde los
#       terminales (sin salidas): un nodo queda seguro cuando todas sus salidas llevan a nodos
#       seguros.
# Tiempo: O(V + E) · Espacio: O(V + E)

from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        entrantes = [[] for _ in range(n)]
        salidas = [len(vecinos) for vecinos in graph]
        for nodo, vecinos in enumerate(graph):
            for v in vecinos:
                entrantes[v].append(nodo)
        cola = deque(i for i in range(n) if salidas[i] == 0)
        seguro = [False] * n
        while cola:
            nodo = cola.popleft()
            seguro[nodo] = True
            for anterior in entrantes[nodo]:
                salidas[anterior] -= 1
                if salidas[anterior] == 0:
                    cola.append(anterior)
        return [i for i in range(n) if seguro[i]]


if __name__ == "__main__":
    s = Solution()
    assert s.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]) == [2, 4, 5, 6]
    assert s.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]) == [4]
    print("OK")
