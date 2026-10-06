# 1639. Number of Ways to Form a Target String Given a Dictionary (Difícil)
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
#
# Idea: solo importa cuántas palabras tienen cada letra en cada columna. dp[j] = formas de armar
#       target[:j] con las columnas ya vistas; con cada columna, target[j-1] puede salir de ella
#       (dp[j-1] · cuántas veces aparece).
# Tiempo: O(columnas · largo de target + total de letras) · Espacio: O(columnas · 26 + largo de target)

from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        columnas = len(words[0])
        cuenta = [[0] * 26 for _ in range(columnas)]
        for w in words:
            for c, letra in enumerate(w):
                cuenta[c][ord(letra) - 97] += 1
        dp = [1] + [0] * len(target)
        for c in range(columnas):
            for j in range(len(target), 0, -1):
                dp[j] = (dp[j] + dp[j - 1] * cuenta[c][ord(target[j - 1]) - 97]) % MOD
        return dp[len(target)]


if __name__ == "__main__":
    s = Solution()
    assert s.numWays(["acca", "bbbb", "caca"], "aba") == 6
    assert s.numWays(["abba", "baab"], "bab") == 4
    print("OK")
