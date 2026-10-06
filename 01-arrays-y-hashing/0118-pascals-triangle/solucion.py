# 118. Pascals Triangle (Fácil)
# https://leetcode.com/problems/pascals-triangle/
#
# Idea: cada fila empieza y termina en 1, y cada número del medio es la suma de los dos que tiene arriba.
# Tiempo: O(n²) · Espacio: O(n²) (la respuesta)

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        filas = [[1]]
        for _ in range(numRows - 1):
            anterior = filas[-1]
            fila = [1]
            for j in range(1, len(anterior)):
                fila.append(anterior[j - 1] + anterior[j])
            fila.append(1)
            filas.append(fila)
        return filas


if __name__ == "__main__":
    s = Solution()
    assert s.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert s.generate(1) == [[1]]
    print("OK")
