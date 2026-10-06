# 138. Copy List With Random Pointer (Media)
# https://leetcode.com/problems/copy-list-with-random-pointer/
#
# Idea: dos pasadas con un diccionario original -> copia: en la primera creo todas las copias y en
#       la segunda conecto next y random usando el diccionario.
# Tiempo: O(n) · Espacio: O(n)

from typing import Optional


# LeetCode ya define Node; está acá para poder probar localmente.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        copia = {None: None}
        actual = head
        while actual:
            copia[actual] = Node(actual.val)
            actual = actual.next
        actual = head
        while actual:
            copia[actual].next = copia[actual.next]
            copia[actual].random = copia[actual.random]
            actual = actual.next
        return copia[head]


if __name__ == "__main__":
    def crear(pares):
        nodos = [Node(v) for v, _ in pares]
        for i, (_, r) in enumerate(pares):
            if i + 1 < len(nodos):
                nodos[i].next = nodos[i + 1]
            nodos[i].random = nodos[r] if r is not None else None
        return nodos[0] if nodos else None

    def a_pares(cabeza):
        nodos = []
        n = cabeza
        while n:
            nodos.append(n)
            n = n.next
        posicion = {id(n): i for i, n in enumerate(nodos)}
        return [(n.val, posicion[id(n.random)] if n.random else None) for n in nodos], nodos

    s = Solution()
    for pares in ([(7, None), (13, 0), (11, 4), (10, 2), (1, 0)], [(1, 1), (2, 1)], [(3, None), (3, 0), (3, None)], []):
        original = crear(pares)
        copia = s.copyRandomList(original)
        resultado, nodos_copia = a_pares(copia)
        _, nodos_original = a_pares(original)
        assert resultado == pares
        assert not set(map(id, nodos_copia)) & set(map(id, nodos_original))
    print("OK")
