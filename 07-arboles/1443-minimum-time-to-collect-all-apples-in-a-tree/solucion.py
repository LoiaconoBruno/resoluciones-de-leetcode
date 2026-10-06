# 1443. Minimum Time to Collect All Apples in a Tree (Media)
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
#
# Idea: DFS desde la raíz: un hijo cuesta 2 segundos (ir y volver) más el tiempo de su subárbol,
#       pero solo si en ese subárbol hay alguna manzana.
# Tiempo: O(n) · Espacio: O(n)

from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        vecinos = defaultdict(list)
        for a, b in edges:
            vecinos[a].append(b)
            vecinos[b].append(a)

        def tiempo(nodo, padre):
            total = 0
            for hijo in vecinos[nodo]:
                if hijo == padre:
                    continue
                t = tiempo(hijo, nodo)
                if t or hasApple[hijo]:
                    total += t + 2
            return total

        return tiempo(0, -1)


if __name__ == "__main__":
    s = Solution()
    aristas = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    assert s.minTime(7, aristas, [False, False, True, False, True, True, False]) == 8
    assert s.minTime(7, aristas, [False, False, True, False, False, True, False]) == 6
    assert s.minTime(7, aristas, [False] * 7) == 0
    print("OK")
