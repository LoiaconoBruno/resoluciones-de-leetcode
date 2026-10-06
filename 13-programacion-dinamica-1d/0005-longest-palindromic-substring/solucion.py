# 5. Longest Palindromic Substring (Media)
# https://leetcode.com/problems/longest-palindromic-substring/
#
# Idea: todo palíndromo crece desde un centro; pruebo cada centro (una letra o el espacio entre dos
#       letras) y expando mientras los extremos coincidan.
# Tiempo: O(n²) · Espacio: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        inicio, largo = 0, 0
        for centro in range(len(s)):
            for izq, der in ((centro, centro), (centro, centro + 1)):
                while izq >= 0 and der < len(s) and s[izq] == s[der]:
                    izq -= 1
                    der += 1
                if der - izq - 1 > largo:
                    inicio, largo = izq + 1, der - izq - 1
        return s[inicio:inicio + largo]


if __name__ == "__main__":
    s = Solution()
    assert s.longestPalindrome("babad") in ("bab", "aba")
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("a") == "a"
    print("OK")
