# 130. Surrounded Regions (Media)
# https://leetcode.com/problems/surrounded-regions/
#
# Idea: las 'O' que se salvan son las conectadas al borde; las marco con un DFS desde el borde y
#       después todo 'O' sin marcar pasa a 'X' y las marcadas vuelven a 'O'.
# Tiempo: O(f · c) · Espacio: O(f · c)

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        filas, cols = len(board), len(board[0])
        pila = [(f, c) for f in range(filas) for c in range(cols)
                if (f in (0, filas - 1) or c in (0, cols - 1)) and board[f][c] == "O"]
        while pila:
            f, c = pila.pop()
            if 0 <= f < filas and 0 <= c < cols and board[f][c] == "O":
                board[f][c] = "S"
                pila.extend(((f + 1, c), (f - 1, c), (f, c + 1), (f, c - 1)))
        for f in range(filas):
            for c in range(cols):
                board[f][c] = "O" if board[f][c] == "S" else "X"


if __name__ == "__main__":
    s = Solution()
    tablero = [list("XXXX"), list("XOOX"), list("XXOX"), list("XOXX")]
    s.solve(tablero)
    assert tablero == [list("XXXX"), list("XXXX"), list("XXXX"), list("XOXX")]
    tablero = [["X"]]
    s.solve(tablero)
    assert tablero == [["X"]]
    print("OK")
