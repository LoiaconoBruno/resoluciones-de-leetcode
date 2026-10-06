# 36. Valid Sudoku (Media)
# https://leetcode.com/problems/valid-sudoku/
#
# Idea: uso un set por fila, otro por columna y otro por caja de 3x3 (la caja es (fila // 3, columna // 3)); si un número se repite en alguno, no es válido.
# Tiempo: O(1) (el tablero siempre es 9x9) · Espacio: O(1)

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        filas = defaultdict(set)
        columnas = defaultdict(set)
        cajas = defaultdict(set)
        for f in range(9):
            for c in range(9):
                v = board[f][c]
                if v == ".":
                    continue
                caja = (f // 3, c // 3)
                if v in filas[f] or v in columnas[c] or v in cajas[caja]:
                    return False
                filas[f].add(v)
                columnas[c].add(v)
                cajas[caja].add(v)
        return True


if __name__ == "__main__":
    s = Solution()
    tablero = [list(fila) for fila in [
        "53..7....",
        "6..195...",
        ".98....6.",
        "8...6...3",
        "4..8.3..1",
        "7...2...6",
        ".6....28.",
        "...419..5",
        "....8..79",
    ]]
    assert s.isValidSudoku(tablero) is True
    tablero[0][0] = "8"
    assert s.isValidSudoku(tablero) is False
    print("OK")
