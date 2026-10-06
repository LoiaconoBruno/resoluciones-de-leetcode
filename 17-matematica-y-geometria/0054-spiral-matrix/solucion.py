# 54. Spiral Matrix (Media)
# https://leetcode.com/problems/spiral-matrix/
#
# Idea: cuatro bordes (arriba, abajo, izquierda, derecha); recorro el borde de arriba, el de la
#       derecha, el de abajo y el de la izquierda, y después cierro los bordes hacia adentro.
# Tiempo: O(f · c) · Espacio: O(1) extra

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        arriba, abajo = 0, len(matrix) - 1
        izq, der = 0, len(matrix[0]) - 1
        while arriba <= abajo and izq <= der:
            for c in range(izq, der + 1):
                res.append(matrix[arriba][c])
            for f in range(arriba + 1, abajo + 1):
                res.append(matrix[f][der])
            if arriba < abajo and izq < der:
                for c in range(der - 1, izq - 1, -1):
                    res.append(matrix[abajo][c])
                for f in range(abajo - 1, arriba, -1):
                    res.append(matrix[f][izq])
            arriba, abajo, izq, der = arriba + 1, abajo - 1, izq + 1, der - 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert s.spiralOrder([[1], [2], [3]]) == [1, 2, 3]
    print("OK")
