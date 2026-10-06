# 48. Rotate Image (Media)
# https://leetcode.com/problems/rotate-image/
#
# Idea: rotar 90° a la derecha es transponer (cambiar filas por columnas) y después dar vuelta cada
#       fila.
# Tiempo: O(n²) · Espacio: O(1)

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for f in range(n):
            for c in range(f + 1, n):
                matrix[f][c], matrix[c][f] = matrix[c][f], matrix[f][c]
        for fila in matrix:
            fila.reverse()


if __name__ == "__main__":
    s = Solution()
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(m)
    assert m == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    print("OK")
