# 424. Longest Repeating Character Replacement (Media)
# https://leetcode.com/problems/longest-repeating-character-replacement/
#
# Idea: una ventana sirve si (largo - frecuencia de la letra más común) ≤ k, porque esas son las
#       letras a cambiar; si no sirve, achico desde la izquierda.
# Tiempo: O(n) · Espacio: O(1) (26 letras)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cuenta = {}
        izq = max_frec = mejor = 0
        for der, c in enumerate(s):
            cuenta[c] = cuenta.get(c, 0) + 1
            max_frec = max(max_frec, cuenta[c])
            while (der - izq + 1) - max_frec > k:
                cuenta[s[izq]] -= 1
                izq += 1
            mejor = max(mejor, der - izq + 1)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.characterReplacement("ABAB", 2) == 4
    assert s.characterReplacement("AABABBA", 1) == 4
    print("OK")
