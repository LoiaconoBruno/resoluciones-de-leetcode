# 2101. Detonate the Maximum Bombs (Media)
# https://leetcode.com/problems/detonate-the-maximum-bombs/
#
# Idea: una bomba i detona a j si j está dentro de su radio (comparo distancias al cuadrado para no
#       usar raíces). Es un grafo dirigido: hago un DFS desde cada bomba y me quedo con el que
#       alcanza más.
# Tiempo: O(n³) · Espacio: O(n²)

from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        alcanza = [[] for _ in range(n)]
        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if i != j and (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 * r1:
                    alcanza[i].append(j)
        mejor = 0
        for inicio in range(n):
            vistos = {inicio}
            pila = [inicio]
            while pila:
                for j in alcanza[pila.pop()]:
                    if j not in vistos:
                        vistos.add(j)
                        pila.append(j)
            mejor = max(mejor, len(vistos))
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.maximumDetonation([[2, 1, 3], [6, 1, 4]]) == 2
    assert s.maximumDetonation([[1, 1, 5], [10, 10, 5]]) == 1
    assert s.maximumDetonation([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]) == 5
    print("OK")
