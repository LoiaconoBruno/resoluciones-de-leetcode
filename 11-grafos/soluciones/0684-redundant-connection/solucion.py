# 684. Redundant Connection (Media)
# https://leetcode.com/problems/redundant-connection/
#
# Idea: union-find: agrego las aristas una por una uniendo componentes; la primera arista cuyos dos
#       extremos ya estaban en la misma componente cierra el ciclo y es la que sobra.
# Tiempo: O(n · α(n)), casi lineal · Espacio: O(n)

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        padre = list(range(len(edges) + 1))

        def raiz(x):
            while padre[x] != x:
                padre[x] = padre[padre[x]]
                x = padre[x]
            return x

        for a, b in edges:
            ra, rb = raiz(a), raiz(b)
            if ra == rb:
                return [a, b]
            padre[ra] = rb
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    print("OK")
