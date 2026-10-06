# 1557. Minimum Number of Vertices to Reach all Nodes (Media)
# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
#
# Idea: un nodo al que no llega ninguna arista no lo alcanza nadie, así que tiene que estar en la
#       respuesta; y desde esos nodos se llega a todo el resto (el grafo no tiene ciclos).
# Tiempo: O(n + aristas) · Espacio: O(n)

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        tiene_entrada = [False] * n
        for _, destino in edges:
            tiene_entrada[destino] = True
        return [i for i in range(n) if not tiene_entrada[i]]


if __name__ == "__main__":
    s = Solution()
    assert s.findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]) == [0, 3]
    assert s.findSmallestSetOfVertices(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]) == [0, 2, 3]
    print("OK")
