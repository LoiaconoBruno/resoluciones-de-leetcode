# 1584. Min Cost to Connect All Points (Media)
# https://leetcode.com/problems/min-cost-to-connect-all-points/
#
# Idea: árbol de expansión mínima con Prim: arranco desde un punto y en cada paso sumo el punto no
#       conectado más barato de enganchar. Como todos los pares son aristas (grafo denso), uso un
#       array de costos en vez de heap.
# Tiempo: O(n²) · Espacio: O(n)

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        costo = [float("inf")] * n
        en_arbol = [False] * n
        costo[0] = 0
        total = 0
        for _ in range(n):
            i = min((j for j in range(n) if not en_arbol[j]), key=lambda j: costo[j])
            en_arbol[i] = True
            total += costo[i]
            xi, yi = points[i]
            for j in range(n):
                if not en_arbol[j]:
                    costo[j] = min(costo[j], abs(xi - points[j][0]) + abs(yi - points[j][1]))
        return total


if __name__ == "__main__":
    s = Solution()
    assert s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert s.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18
    assert s.minCostConnectPoints([[0, 0]]) == 0
    print("OK")
