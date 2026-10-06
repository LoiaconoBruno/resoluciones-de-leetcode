# 51. N Queens (Difícil)
# https://leetcode.com/problems/n-queens/
#
# Idea: pongo una reina por fila; para saber en O(1) si una columna está atacada uso tres sets:
#       columnas, diagonales (fila - col) y antidiagonales (fila + col).
# Tiempo: O(n!) · Espacio: O(n²) (el tablero)

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        tablero = [["."] * n for _ in range(n)]
        columnas, diagonales, antidiagonales = set(), set(), set()

        def ubicar(f):
            if f == n:
                res.append(["".join(fila) for fila in tablero])
                return
            for c in range(n):
                if c in columnas or f - c in diagonales or f + c in antidiagonales:
                    continue
                columnas.add(c)
                diagonales.add(f - c)
                antidiagonales.add(f + c)
                tablero[f][c] = "Q"
                ubicar(f + 1)
                tablero[f][c] = "."
                columnas.remove(c)
                diagonales.remove(f - c)
                antidiagonales.remove(f + c)

        ubicar(0)
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.solveNQueens(4)) == sorted([[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
    assert s.solveNQueens(1) == [["Q"]]
    assert len(s.solveNQueens(8)) == 92
    print("OK")
