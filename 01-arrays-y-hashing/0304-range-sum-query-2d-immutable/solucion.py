# 304. Range Sum Query 2D Immutable (Media)
# https://leetcode.com/problems/range-sum-query-2d-immutable/
#
# Idea: sumas prefijas en 2D: pre[f][c] es la suma del rectángulo desde (0,0); cualquier región sale con inclusión-exclusión de cuatro valores.
# Tiempo: O(filas · columnas) para construir, O(1) por consulta · Espacio: O(filas · columnas)

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        filas, cols = len(matrix), len(matrix[0])
        self.pre = [[0] * (cols + 1) for _ in range(filas + 1)]
        for f in range(filas):
            for c in range(cols):
                self.pre[f + 1][c + 1] = (matrix[f][c] + self.pre[f][c + 1]
                                          + self.pre[f + 1][c] - self.pre[f][c])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p = self.pre
        return p[row2 + 1][col2 + 1] - p[row1][col2 + 1] - p[row2 + 1][col1] + p[row1][col1]


if __name__ == "__main__":
    m = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    assert m.sumRegion(2, 1, 4, 3) == 8
    assert m.sumRegion(1, 1, 2, 2) == 11
    assert m.sumRegion(1, 2, 2, 4) == 12
    print("OK")
