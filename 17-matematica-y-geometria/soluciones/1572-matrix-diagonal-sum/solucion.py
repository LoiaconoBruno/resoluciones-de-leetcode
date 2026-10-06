# 1572. Matrix Diagonal Sum (Fácil)
# https://leetcode.com/problems/matrix-diagonal-sum/
#
# Idea: sumo matriz[i][i] y matriz[i][n-1-i] para cada fila; si n es impar, el centro se contó dos
#       veces y lo resto.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = sum(mat[i][i] + mat[i][n - 1 - i] for i in range(n))
        if n % 2:
            total -= mat[n // 2][n // 2]
        return total


if __name__ == "__main__":
    s = Solution()
    assert s.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25
    assert s.diagonalSum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 8
    assert s.diagonalSum([[5]]) == 5
    print("OK")
