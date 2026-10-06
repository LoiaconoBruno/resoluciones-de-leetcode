# 2359. Find Closest Node to Given Two Nodes (Media)
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
#
# Idea: como cada nodo tiene a lo sumo una salida, desde cada inicio hay un único camino: lo recorro
#       y anoto la distancia a cada nodo. Elijo el nodo que minimiza el máximo de las dos
#       distancias.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def distancias(inicio):
            dist = [-1] * len(edges)
            nodo, d = inicio, 0
            while nodo != -1 and dist[nodo] == -1:
                dist[nodo] = d
                nodo = edges[nodo]
                d += 1
            return dist

        d1, d2 = distancias(node1), distancias(node2)
        mejor, res = float("inf"), -1
        for i in range(len(edges)):
            if d1[i] >= 0 and d2[i] >= 0 and max(d1[i], d2[i]) < mejor:
                mejor, res = max(d1[i], d2[i]), i
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.closestMeetingNode([2, 2, 3, -1], 0, 1) == 2
    assert s.closestMeetingNode([1, 2, -1], 0, 2) == 2
    assert s.closestMeetingNode([1, 0], 0, 1) == 0
    print("OK")
