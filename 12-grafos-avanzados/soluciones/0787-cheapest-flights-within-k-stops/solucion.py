# 787. Cheapest Flights Within K Stops (Media)
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
#
# Idea: Bellman-Ford limitado: hago k + 1 rondas y en cada una relajo todos los vuelos usando los
#       precios de la ronda anterior (una copia), así cada ronda agrega como mucho un vuelo más.
# Tiempo: O(k · vuelos) · Espacio: O(n)

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        precio = [float("inf")] * n
        precio[src] = 0
        for _ in range(k + 1):
            nuevo = precio[:]
            for desde, hasta, costo in flights:
                if precio[desde] + costo < nuevo[hasta]:
                    nuevo[hasta] = precio[desde] + costo
            precio = nuevo
        return -1 if precio[dst] == float("inf") else precio[dst]


if __name__ == "__main__":
    s = Solution()
    vuelos = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    assert s.findCheapestPrice(4, vuelos, 0, 3, 1) == 700
    vuelos = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert s.findCheapestPrice(3, vuelos, 0, 2, 1) == 200
    assert s.findCheapestPrice(3, vuelos, 0, 2, 0) == 500
    assert s.findCheapestPrice(3, [[0, 1, 100]], 0, 2, 1) == -1
    print("OK")
