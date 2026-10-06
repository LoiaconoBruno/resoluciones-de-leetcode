# 2477. Minimum Fuel Cost to Report to the Capital (Media)
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
#
# Idea: por cada ruta hacia la capital pasan todos los representantes del subárbol de abajo, y
#       necesitan ceil(personas / asientos) autos. Cuento personas por subárbol (de las hojas hacia
#       la raíz) y sumo eso por cada ruta.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        vecinos = [[] for _ in range(n)]
        for a, b in roads:
            vecinos[a].append(b)
            vecinos[b].append(a)
        padre = [-1] * n
        orden = [0]
        for nodo in orden:
            for v in vecinos[nodo]:
                if v != padre[nodo]:
                    padre[v] = nodo
                    orden.append(v)
        personas = [1] * n
        litros = 0
        for nodo in reversed(orden[1:]):
            litros += (personas[nodo] + seats - 1) // seats
            personas[padre[nodo]] += personas[nodo]
        return litros


if __name__ == "__main__":
    s = Solution()
    assert s.minimumFuelCost([[0, 1], [0, 2], [0, 3]], 5) == 3
    assert s.minimumFuelCost([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2) == 7
    assert s.minimumFuelCost([], 1) == 0
    print("OK")
