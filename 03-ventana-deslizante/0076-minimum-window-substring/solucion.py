# 76. Minimum Window Substring (Difícil)
# https://leetcode.com/problems/minimum-window-substring/
#
# Idea: agrando la ventana hasta cubrir todas las letras de t y, mientras siga cubriendo, la achico desde la izquierda guardando la más corta. "faltan" cuenta cuántas letras me faltan todavía.
# Tiempo: O(n + m) · Espacio: O(alfabeto)

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        necesito = Counter(t)
        faltan = len(t)
        izq = 0
        mejor = (float("inf"), 0, 0)
        for der, c in enumerate(s):
            if necesito[c] > 0:
                faltan -= 1
            necesito[c] -= 1
            while faltan == 0:
                if der - izq + 1 < mejor[0]:
                    mejor = (der - izq + 1, izq, der + 1)
                necesito[s[izq]] += 1
                if necesito[s[izq]] > 0:
                    faltan += 1
                izq += 1
        return "" if mejor[0] == float("inf") else s[mejor[1]:mejor[2]]


if __name__ == "__main__":
    s = Solution()
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("a", "a") == "a"
    assert s.minWindow("a", "aa") == ""
    print("OK")
