# 79. Word Search (Media)
# https://leetcode.com/problems/word-search/
#
# Idea: DFS desde cada celda siguiendo la palabra letra por letra; marco la celda como usada
#       mientras estoy en ese camino y la desmarco al volver.
# Tiempo: O(f · c · 4^L), con L el largo de la palabra · Espacio: O(L) de recursión

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        filas, cols = len(board), len(board[0])

        def dfs(f, c, i):
            if i == len(word):
                return True
            if not (0 <= f < filas and 0 <= c < cols) or board[f][c] != word[i]:
                return False
            letra, board[f][c] = board[f][c], "#"
            encontrado = (dfs(f + 1, c, i + 1) or dfs(f - 1, c, i + 1) or
                          dfs(f, c + 1, i + 1) or dfs(f, c - 1, i + 1))
            board[f][c] = letra
            return encontrado

        return any(dfs(f, c, 0) for f in range(filas) for c in range(cols))


if __name__ == "__main__":
    s = Solution()
    tablero = [list("ABCE"), list("SFCS"), list("ADEE")]
    assert s.exist(tablero, "ABCCED") is True
    assert s.exist(tablero, "SEE") is True
    assert s.exist(tablero, "ABCB") is False
    print("OK")
