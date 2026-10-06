# 212. Word Search II (Difícil)
# https://leetcode.com/problems/word-search-ii/
#
# Idea: meto todas las palabras en un trie y hago un DFS desde cada celda bajando por el trie a la
#       vez; si una letra no sigue ningún prefijo, corto. Las palabras encontradas las saco del trie
#       para no repetirlas y podar.
# Tiempo: O(f · c · 4 · 3^(L-1)), con L el largo de la palabra más larga · Espacio: O(total de letras de las palabras)

from typing import List


class NodoTrie:
    def __init__(self):
        self.hijos = {}
        self.palabra = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        raiz = NodoTrie()
        for w in words:
            nodo = raiz
            for c in w:
                nodo = nodo.hijos.setdefault(c, NodoTrie())
            nodo.palabra = w

        filas, cols = len(board), len(board[0])
        res = []

        def dfs(f, c, padre):
            letra = board[f][c]
            nodo = padre.hijos[letra]
            if nodo.palabra:
                res.append(nodo.palabra)
                nodo.palabra = None
            board[f][c] = "#"
            for df, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nf, nc = f + df, c + dc
                if 0 <= nf < filas and 0 <= nc < cols and board[nf][nc] in nodo.hijos:
                    dfs(nf, nc, nodo)
            board[f][c] = letra
            if not nodo.hijos and not nodo.palabra:
                del padre.hijos[letra]

        for f in range(filas):
            for c in range(cols):
                if board[f][c] in raiz.hijos:
                    dfs(f, c, raiz)
        return res


if __name__ == "__main__":
    s = Solution()
    tablero = [list("oaan"), list("etae"), list("ihkr"), list("iflv")]
    assert sorted(s.findWords(tablero, ["oath", "pea", "eat", "rain"])) == ["eat", "oath"]
    assert s.findWords([list("ab"), list("cd")], ["abcb"]) == []
    assert sorted(s.findWords([list("aa")], ["a", "aa", "aaa"])) == ["a", "aa"]
    print("OK")
