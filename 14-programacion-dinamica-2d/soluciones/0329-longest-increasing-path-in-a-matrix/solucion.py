# 329. Longest Increasing Path In a Matrix (Difícil)
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
#
# Idea: las flechas "de menor a mayor" forman un grafo sin ciclos. Pelo la matriz por capas como en
#       Kahn: primero las celdas que no tienen vecinos mayores, después las que quedan sin vecinos
#       mayores, etc. La cantidad de capas es el camino más largo.
# Tiempo: O(f · c) · Espacio: O(f · c)

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        filas, cols = len(matrix), len(matrix[0])
        direcciones = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def vecinos(f, c):
            for df, dc in direcciones:
                nf, nc = f + df, c + dc
                if 0 <= nf < filas and 0 <= nc < cols:
                    yield nf, nc

        mayores = [[sum(matrix[nf][nc] > matrix[f][c] for nf, nc in vecinos(f, c)) for c in range(cols)]
                   for f in range(filas)]
        capa = [(f, c) for f in range(filas) for c in range(cols) if mayores[f][c] == 0]
        capas = 0
        while capa:
            capas += 1
            siguiente = []
            for f, c in capa:
                for nf, nc in vecinos(f, c):
                    if matrix[nf][nc] < matrix[f][c]:
                        mayores[nf][nc] -= 1
                        if mayores[nf][nc] == 0:
                            siguiente.append((nf, nc))
            capa = siguiente
        return capas


if __name__ == "__main__":
    s = Solution()
    assert s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
    assert s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
    assert s.longestIncreasingPath([[1]]) == 1
    print("OK")
