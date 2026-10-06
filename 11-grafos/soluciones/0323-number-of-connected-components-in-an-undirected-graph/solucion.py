# 323. Number of Connected Components In An Undirected Graph (Media)
# https://www.lintcode.com/problem/3651/
#
# Idea: union-find: empiezo con n componentes y cada arista que une dos componentes distintas resta
#       una.
# Tiempo: O(E · α(n)), casi lineal · Espacio: O(n)

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        padre = list(range(n))

        def raiz(x):
            while padre[x] != x:
                padre[x] = padre[padre[x]]
                x = padre[x]
            return x

        componentes = n
        for a, b in edges:
            ra, rb = raiz(a), raiz(b)
            if ra != rb:
                padre[ra] = rb
                componentes -= 1
        return componentes


if __name__ == "__main__":
    s = Solution()
    assert s.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert s.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    assert s.countComponents(3, []) == 3
    print("OK")
