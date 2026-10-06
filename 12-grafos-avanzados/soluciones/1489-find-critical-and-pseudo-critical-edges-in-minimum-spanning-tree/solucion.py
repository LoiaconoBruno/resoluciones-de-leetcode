# 1489. Find Critical and Pseudo Critical Edges in Minimum Spanning Tree (Difícil)
# https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
#
# Idea: calculo el peso del MST con Kruskal. Una arista es crítica si, sacándola, el MST cuesta más
#       (o el grafo se desconecta); es pseudo-crítica si no es crítica y, forzándola primero, el MST
#       sigue costando lo mismo.
# Tiempo: O(E² · α(n)) · Espacio: O(n + E)

from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        orden = sorted(range(len(edges)), key=lambda i: edges[i][2])

        def kruskal(saltear=-1, forzar=-1):
            padre = list(range(n))

            def raiz(x):
                while padre[x] != x:
                    padre[x] = padre[padre[x]]
                    x = padre[x]
                return x

            peso, aristas = 0, 0
            if forzar != -1:
                a, b, w = edges[forzar]
                padre[raiz(a)] = raiz(b)
                peso, aristas = w, 1
            for i in orden:
                if i == saltear:
                    continue
                a, b, w = edges[i]
                ra, rb = raiz(a), raiz(b)
                if ra != rb:
                    padre[ra] = rb
                    peso += w
                    aristas += 1
            return peso if aristas == n - 1 else float("inf")

        minimo = kruskal()
        criticas, pseudo = [], []
        for i in range(len(edges)):
            if kruskal(saltear=i) > minimo:
                criticas.append(i)
            elif kruskal(forzar=i) == minimo:
                pseudo.append(i)
        return [criticas, pseudo]


if __name__ == "__main__":
    s = Solution()
    aristas = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
    assert s.findCriticalAndPseudoCriticalEdges(5, aristas) == [[0, 1], [2, 3, 4, 5]]
    assert s.findCriticalAndPseudoCriticalEdges(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]) == [[], [0, 1, 2, 3]]
    print("OK")
