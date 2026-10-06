# 417. Pacific Atlantic Water Flow (Media)
# https://leetcode.com/problems/pacific-atlantic-water-flow/
#
# Idea: al revés: en vez de ver desde cada celda si el agua llega al mar, arranco desde los bordes
#       de cada océano y subo (a celdas de igual o mayor altura). La respuesta son las celdas que
#       alcanzan los dos.
# Tiempo: O(f · c) · Espacio: O(f · c)

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        filas, cols = len(heights), len(heights[0])

        def alcanzables(inicios):
            vistos = set(inicios)
            pila = list(inicios)
            while pila:
                i, j = pila.pop()
                for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if (0 <= ni < filas and 0 <= nj < cols and (ni, nj) not in vistos
                            and heights[ni][nj] >= heights[i][j]):
                        vistos.add((ni, nj))
                        pila.append((ni, nj))
            return vistos

        pacifico = alcanzables([(0, c) for c in range(cols)] + [(f, 0) for f in range(filas)])
        atlantico = alcanzables([(filas - 1, c) for c in range(cols)] + [(f, cols - 1) for f in range(filas)])
        return [[f, c] for f, c in sorted(pacifico & atlantico)]


if __name__ == "__main__":
    s = Solution()
    alturas = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    assert s.pacificAtlantic(alturas) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert s.pacificAtlantic([[1]]) == [[0, 0]]
    print("OK")
