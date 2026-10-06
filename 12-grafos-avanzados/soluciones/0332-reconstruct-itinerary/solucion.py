# 332. Reconstruct Itinerary (Difícil)
# https://leetcode.com/problems/reconstruct-itinerary/
#
# Idea: es un camino que usa cada pasaje una vez (camino euleriano); con el algoritmo de Hierholzer:
#       avanzo siempre por el destino alfabéticamente menor y, cuando un aeropuerto se queda sin
#       salidas, lo agrego al itinerario. Al final lo doy vuelta.
# Tiempo: O(E log E) · Espacio: O(E)

from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        destinos = defaultdict(list)
        for desde, hasta in sorted(tickets, reverse=True):
            destinos[desde].append(hasta)
        itinerario = []
        pila = ["JFK"]
        while pila:
            aeropuerto = pila[-1]
            if destinos[aeropuerto]:
                pila.append(destinos[aeropuerto].pop())
            else:
                itinerario.append(pila.pop())
        return itinerario[::-1]


if __name__ == "__main__":
    s = Solution()
    assert s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == \
        ["JFK", "MUC", "LHR", "SFO", "SJC"]
    assert s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]) == \
        ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    assert s.findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]) == ["JFK", "NRT", "JFK", "KUL"]
    print("OK")
