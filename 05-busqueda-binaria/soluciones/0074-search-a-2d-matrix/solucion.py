# 74. Search a 2D Matrix (Media)
# https://leetcode.com/problems/search-a-2d-matrix/
#
# Idea: la matriz leída fila por fila es un array ordenado; hago búsqueda binaria sobre índices
#       0..f·c-1 y convierto cada índice en (i // c, i % c).
# Tiempo: O(log(f · c)) · Espacio: O(1)

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        filas, cols = len(matrix), len(matrix[0])
        izq, der = 0, filas * cols - 1
        while izq <= der:
            medio = (izq + der) // 2
            valor = matrix[medio // cols][medio % cols]
            if valor == target:
                return True
            if valor < target:
                izq = medio + 1
            else:
                der = medio - 1
        return False


if __name__ == "__main__":
    s = Solution()
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert s.searchMatrix(m, 3) is True
    assert s.searchMatrix(m, 13) is False
    assert s.searchMatrix(m, 60) is True
    print("OK")
