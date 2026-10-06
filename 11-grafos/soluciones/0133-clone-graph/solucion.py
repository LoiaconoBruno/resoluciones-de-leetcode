# 133. Clone Graph (Media)
# https://leetcode.com/problems/clone-graph/
#
# Idea: DFS con un diccionario original -> copia: la primera vez que llego a un nodo creo su copia y
#       después clono sus vecinos; si ya existe, la reutilizo (así no me pierdo en los ciclos).
# Tiempo: O(V + E) · Espacio: O(V)

from typing import Optional


# LeetCode ya define Node; está acá para poder probar localmente.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        copias = {}

        def clonar(original):
            if original in copias:
                return copias[original]
            copia = Node(original.val)
            copias[original] = copia
            for vecino in original.neighbors:
                copia.neighbors.append(clonar(vecino))
            return copia

        return clonar(node) if node else None


if __name__ == "__main__":
    def crear(adyacencia):
        nodos = [Node(i + 1) for i in range(len(adyacencia))]
        for i, vecinos in enumerate(adyacencia):
            nodos[i].neighbors = [nodos[v - 1] for v in vecinos]
        return nodos[0] if nodos else None

    def a_lista(nodo):
        vistos, pila = {}, [nodo]
        while pila:
            n = pila.pop()
            if n.val not in vistos:
                vistos[n.val] = n
                pila.extend(n.neighbors)
        return [[v.val for v in vistos[i].neighbors] for i in sorted(vistos)], set(map(id, vistos.values()))

    s = Solution()
    for ady in ([[2, 4], [1, 3], [2, 4], [1, 3]], [[]]):
        original = crear(ady)
        copia = s.cloneGraph(original)
        (lista_copia, ids_copia), (_, ids_original) = a_lista(copia), a_lista(original)
        assert lista_copia == ady and not ids_copia & ids_original
    assert s.cloneGraph(None) is None
    print("OK")
