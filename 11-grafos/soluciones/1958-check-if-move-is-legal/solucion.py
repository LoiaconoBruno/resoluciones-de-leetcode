# 1958. Check if Move Is Legal (Media)
# https://leetcode.com/problems/check-if-move-is-legal/
#
# Idea: pruebo las 8 direcciones desde la jugada: es legal si en alguna hay una o más fichas del
#       rival seguidas y justo después una de mi color.
# Tiempo: O(8 · 8) = O(1) · Espacio: O(1)

from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        rival = "W" if color == "B" else "B"
        for df in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if df == dc == 0:
                    continue
                f, c = rMove + df, cMove + dc
                largo = 1
                while 0 <= f < 8 and 0 <= c < 8 and board[f][c] == rival:
                    f += df
                    c += dc
                    largo += 1
                if largo >= 2 and 0 <= f < 8 and 0 <= c < 8 and board[f][c] == color:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    tablero = [list(fila) for fila in ["...B....", "...W....", "...W....", "...W....",
                                       "WBB.WWWB", "...B....", "...B....", "...W...."]]
    assert s.checkMove(tablero, 4, 3, "B") is True
    tablero = [list(fila) for fila in ["........", ".B..W...", "..W.....", "...WB...",
                                       "........", "....BW..", "......W.", ".......B"]]
    assert s.checkMove(tablero, 4, 4, "W") is False
    print("OK")
