# 2421. Number of Good Paths (Difícil)
# https://leetcode.com/problems/number-of-good-paths/
#
# Idea: proceso los nodos de menor a mayor valor y los voy uniendo (union-find) con los vecinos de
#       valor menor o igual. Después de procesar un valor v, cada componente con c nodos de valor v
#       suma c · (c + 1) / 2 caminos buenos (incluye los de un solo nodo).
# Tiempo: O(n log n) · Espacio: O(n)

from collections import Counter, defaultdict
from typing import List


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        vecinos = [[] for _ in range(n)]
        for a, b in edges:
            vecinos[a].append(b)
            vecinos[b].append(a)
        padre = list(range(n))

        def raiz(x):
            while padre[x] != x:
                padre[x] = padre[padre[x]]
                x = padre[x]
            return x

        por_valor = defaultdict(list)
        for i, v in enumerate(vals):
            por_valor[v].append(i)
        res = 0
        for v in sorted(por_valor):
            for nodo in por_valor[v]:
                for vecino in vecinos[nodo]:
                    if vals[vecino] <= v:
                        padre[raiz(nodo)] = raiz(vecino)
            grupos = Counter(raiz(nodo) for nodo in por_valor[v])
            res += sum(c * (c + 1) // 2 for c in grupos.values())
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.numberOfGoodPaths([1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]]) == 6
    assert s.numberOfGoodPaths([1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]]) == 7
    assert s.numberOfGoodPaths([1], []) == 1
    print("OK")
