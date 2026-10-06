# 261. Graph Valid Tree (Media)
# https://www.lintcode.com/problem/178/
#
# Idea: un árbol de n nodos tiene exactamente n - 1 aristas y ningún ciclo; con union-find chequeo
#       que ninguna arista una dos nodos que ya estaban conectados.
# Tiempo: O(n · α(n)), casi lineal · Espacio: O(n)

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        padre = list(range(n))

        def raiz(x):
            while padre[x] != x:
                padre[x] = padre[padre[x]]
                x = padre[x]
            return x

        for a, b in edges:
            ra, rb = raiz(a), raiz(b)
            if ra == rb:
                return False
            padre[ra] = rb
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
    assert s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
    assert s.validTree(1, []) is True
    assert s.validTree(4, [[0, 1], [2, 3], [0, 1]]) is False
    print("OK")
