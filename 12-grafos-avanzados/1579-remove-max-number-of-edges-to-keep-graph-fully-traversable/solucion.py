# 1579. Remove Max Number of Edges to Keep Graph Fully Traversable (Difícil)
# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
#
# Idea: dos union-find, uno para Alice y otro para Bob. Primero meto las aristas de tipo 3 (sirven a
#       los dos) y después las propias de cada uno; toda arista que no une nada nuevo se puede
#       borrar. Al final los dos tienen que quedar con una sola componente.
# Tiempo: O(E · α(n)) · Espacio: O(n)

from typing import List


class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n + 1))
        self.componentes = n

    def raiz(self, x):
        while self.padre[x] != x:
            self.padre[x] = self.padre[self.padre[x]]
            x = self.padre[x]
        return x

    def unir(self, a, b):
        ra, rb = self.raiz(a), self.raiz(b)
        if ra == rb:
            return False
        self.padre[ra] = rb
        self.componentes -= 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UnionFind(n), UnionFind(n)
        usadas = 0
        for tipo, a, b in sorted(edges, key=lambda e: -e[0]):
            if tipo == 3:
                unio_alice = alice.unir(a, b)
                unio_bob = bob.unir(a, b)
                usadas += unio_alice or unio_bob
            elif tipo == 1:
                usadas += alice.unir(a, b)
            else:
                usadas += bob.unir(a, b)
        if alice.componentes > 1 or bob.componentes > 1:
            return -1
        return len(edges) - usadas


if __name__ == "__main__":
    s = Solution()
    assert s.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]) == 2
    assert s.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]) == 0
    assert s.maxNumEdgesToRemove(4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]]) == -1
    print("OK")
