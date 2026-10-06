# 59. Spiral Matrix II (Media)
# https://leetcode.com/problems/spiral-matrix-ii/
#
# Idea: igual que recorrer en espiral, pero escribiendo 1, 2, 3, ... en vez de leer: lleno el borde
#       de arriba, la derecha, abajo y la izquierda, y achico los bordes.
# Tiempo: O(n²) · Espacio: O(n²) (la respuesta)

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0] * n for _ in range(n)]
        arriba, abajo, izq, der = 0, n - 1, 0, n - 1
        valor = 1
        while arriba <= abajo and izq <= der:
            for c in range(izq, der + 1):
                m[arriba][c] = valor
                valor += 1
            for f in range(arriba + 1, abajo + 1):
                m[f][der] = valor
                valor += 1
            if arriba < abajo and izq < der:
                for c in range(der - 1, izq - 1, -1):
                    m[abajo][c] = valor
                    valor += 1
                for f in range(abajo - 1, arriba, -1):
                    m[f][izq] = valor
                    valor += 1
            arriba, abajo, izq, der = arriba + 1, abajo - 1, izq + 1, der - 1
        return m


if __name__ == "__main__":
    s = Solution()
    assert s.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert s.generateMatrix(1) == [[1]]
    assert s.generateMatrix(4) == [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    print("OK")
