# 73. Set Matrix Zeroes (Media)
# https://leetcode.com/problems/set-matrix-zeroes/
#
# Idea: uso la primera fila y la primera columna como marcadores de "esta columna/fila va en cero";
#       como la primera columna se pisa, guardo aparte si ella misma tenía un cero.
# Tiempo: O(f · c) · Espacio: O(1)

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        filas, cols = len(matrix), len(matrix[0])
        primera_col_cero = any(matrix[f][0] == 0 for f in range(filas))
        for f in range(filas):
            for c in range(1, cols):
                if matrix[f][c] == 0:
                    matrix[f][0] = 0
                    matrix[0][c] = 0
        for f in range(filas - 1, -1, -1):
            for c in range(cols - 1, 0, -1):
                if matrix[f][0] == 0 or matrix[0][c] == 0:
                    matrix[f][c] = 0
            if primera_col_cero:
                matrix[f][0] = 0


if __name__ == "__main__":
    s = Solution()
    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes(m)
    assert m == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(m)
    assert m == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    print("OK")
