# 1129. Shortest Path with Alternating Colors (Media)
# https://leetcode.com/problems/shortest-path-with-alternating-colors/
#
# Idea: BFS donde el estado es (nodo, color de la última arista); desde un estado solo puedo seguir
#       por aristas del otro color. La primera vez que llego a cada nodo (con cualquier color) es su
#       distancia.
# Tiempo: O(n + aristas) · Espacio: O(n + aristas)

from collections import deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]],
                                 blueEdges: List[List[int]]) -> List[int]:
        vecinos = [[[] for _ in range(n)] for _ in range(2)]
        for a, b in redEdges:
            vecinos[0][a].append(b)
        for a, b in blueEdges:
            vecinos[1][a].append(b)
        res = [-1] * n
        vistos = {(0, 0), (0, 1)}
        cola = deque([(0, 0, 0), (0, 1, 0)])
        while cola:
            nodo, color, dist = cola.popleft()
            if res[nodo] == -1:
                res[nodo] = dist
            otro = 1 - color
            for v in vecinos[otro][nodo]:
                if (v, otro) not in vistos:
                    vistos.add((v, otro))
                    cola.append((v, otro, dist + 1))
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.shortestAlternatingPaths(3, [[0, 1], [1, 2]], []) == [0, 1, -1]
    assert s.shortestAlternatingPaths(3, [[0, 1]], [[2, 1]]) == [0, 1, -1]
    assert s.shortestAlternatingPaths(3, [[0, 1]], [[1, 2]]) == [0, 1, 2]
    assert s.shortestAlternatingPaths(3, [[0, 1], [0, 2]], [[1, 0]]) == [0, 1, 1]
    print("OK")
