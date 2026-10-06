# 1905. Count Sub Islands (Media)
# https://leetcode.com/problems/count-sub-islands/
#
# Idea: recorro cada isla de grid2 con un DFS; es sub-isla solo si todas sus celdas también son
#       tierra en grid1. Igual termino de recorrerla entera para no volver a visitarla.
# Tiempo: O(f · c) · Espacio: O(f · c)

from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        filas, cols = len(grid2), len(grid2[0])
        res = 0
        for f in range(filas):
            for c in range(cols):
                if grid2[f][c] != 1:
                    continue
                grid2[f][c] = 0
                pila = [(f, c)]
                es_sub = True
                while pila:
                    i, j = pila.pop()
                    if grid1[i][j] == 0:
                        es_sub = False
                    for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= ni < filas and 0 <= nj < cols and grid2[ni][nj] == 1:
                            grid2[ni][nj] = 0
                            pila.append((ni, nj))
                res += es_sub
        return res


if __name__ == "__main__":
    s = Solution()
    g1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
    g2 = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    assert s.countSubIslands(g1, g2) == 3
    g1 = [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]]
    g2 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]
    assert s.countSubIslands(g1, g2) == 2
    print("OK")
