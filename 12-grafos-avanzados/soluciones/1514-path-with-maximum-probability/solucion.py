# 1514. Path with Maximum Probability (Media)
# https://leetcode.com/problems/path-with-maximum-probability/
#
# Idea: Dijkstra al revés: en vez de minimizar una suma, maximizo un producto de probabilidades
#       (todas ≤ 1, así que nunca mejoran al alargar el camino). Uso un max-heap con las
#       probabilidades negadas.
# Tiempo: O(E log V) · Espacio: O(V + E)

import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float],
                       start_node: int, end_node: int) -> float:
        vecinos = [[] for _ in range(n)]
        for (a, b), p in zip(edges, succProb):
            vecinos[a].append((b, p))
            vecinos[b].append((a, p))
        mejor = [0.0] * n
        mejor[start_node] = 1.0
        heap = [(-1.0, start_node)]
        while heap:
            p, nodo = heapq.heappop(heap)
            p = -p
            if nodo == end_node:
                return p
            if p < mejor[nodo]:
                continue
            for v, q in vecinos[nodo]:
                if p * q > mejor[v]:
                    mejor[v] = p * q
                    heapq.heappush(heap, (-p * q, v))
        return 0.0


if __name__ == "__main__":
    s = Solution()
    assert abs(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2) - 0.25) < 1e-9
    assert abs(s.maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2) - 0.3) < 1e-9
    assert s.maxProbability(3, [[0, 1]], [0.5], 0, 2) == 0.0
    print("OK")
