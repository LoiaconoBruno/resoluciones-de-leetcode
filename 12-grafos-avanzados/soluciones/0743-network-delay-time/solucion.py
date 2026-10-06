# 743. Network Delay Time (Media)
# https://leetcode.com/problems/network-delay-time/
#
# Idea: Dijkstra desde k: saco del heap el nodo con menor tiempo conocido y relajo sus aristas. La
#       respuesta es el tiempo del nodo que tarda más; si alguno no se alcanza, -1.
# Tiempo: O(E log V) · Espacio: O(V + E)

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        vecinos = defaultdict(list)
        for u, v, w in times:
            vecinos[u].append((v, w))
        llegada = {}
        heap = [(0, k)]
        while heap:
            t, nodo = heapq.heappop(heap)
            if nodo in llegada:
                continue
            llegada[nodo] = t
            for v, w in vecinos[nodo]:
                if v not in llegada:
                    heapq.heappush(heap, (t + w, v))
        return max(llegada.values()) if len(llegada) == n else -1


if __name__ == "__main__":
    s = Solution()
    assert s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert s.networkDelayTime([[1, 2, 1]], 2, 1) == 1
    assert s.networkDelayTime([[1, 2, 1]], 2, 2) == -1
    print("OK")
