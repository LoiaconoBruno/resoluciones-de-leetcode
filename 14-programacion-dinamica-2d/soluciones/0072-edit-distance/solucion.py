# 72. Edit Distance (Media)
# https://leetcode.com/problems/edit-distance/
#
# Idea: dp[i][j] = operaciones para convertir los primeros i de word1 en los primeros j de word2. Si
#       las letras coinciden no cuesta nada; si no, 1 + el mínimo entre insertar, borrar o
#       reemplazar.
# Tiempo: O(n · m) · Espacio: O(m)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        anterior = list(range(len(word2) + 1))
        for i, a in enumerate(word1, 1):
            actual = [i] + [0] * len(word2)
            for j, b in enumerate(word2, 1):
                if a == b:
                    actual[j] = anterior[j - 1]
                else:
                    actual[j] = 1 + min(anterior[j], actual[j - 1], anterior[j - 1])
            anterior = actual
        return anterior[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.minDistance("horse", "ros") == 3
    assert s.minDistance("intention", "execution") == 5
    assert s.minDistance("", "abc") == 3
    print("OK")
