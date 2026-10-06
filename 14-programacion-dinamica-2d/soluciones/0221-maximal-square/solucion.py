# 221. Maximal Square (Media)
# https://leetcode.com/problems/maximal-square/
#
# Idea: lado[f][c] = lado del cuadrado de unos más grande con esquina inferior derecha en (f, c): 1
#       + el mínimo entre el de arriba, el de la izquierda y el de la diagonal.
# Tiempo: O(f · c) · Espacio: O(c)

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cols = len(matrix[0])
        anterior = [0] * (cols + 1)
        mejor = 0
        for fila in matrix:
            actual = [0] * (cols + 1)
            for c in range(cols):
                if fila[c] == "1":
                    actual[c + 1] = 1 + min(anterior[c], anterior[c + 1], actual[c])
                    mejor = max(mejor, actual[c + 1])
            anterior = actual
        return mejor * mejor


if __name__ == "__main__":
    s = Solution()
    m = [list("10100"), list("10111"), list("11111"), list("10010")]
    assert s.maximalSquare(m) == 4
    assert s.maximalSquare([list("01"), list("10")]) == 1
    assert s.maximalSquare([["0"]]) == 0
    print("OK")
