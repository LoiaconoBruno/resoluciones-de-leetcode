# 785. Is Graph Bipartite? (Media)
# https://leetcode.com/problems/is-graph-bipartite/
#
# Idea: pinto con dos colores haciendo BFS desde cada componente: cada vecino tiene que tener el
#       color contrario. Si encuentro dos vecinos del mismo color, no es bipartito.
# Tiempo: O(V + E) · Espacio: O(V)

from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        for inicio in range(len(graph)):
            if color[inicio] != -1:
                continue
            color[inicio] = 0
            cola = deque([inicio])
            while cola:
                nodo = cola.popleft()
                for v in graph[nodo]:
                    if color[v] == -1:
                        color[v] = 1 - color[nodo]
                        cola.append(v)
                    elif color[v] == color[nodo]:
                        return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False
    assert s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True
    print("OK")
