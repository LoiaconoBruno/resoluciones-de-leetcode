# 1930. Unique Length 3 Palindromic Subsequences (Media)
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
#
# Idea: un palíndromo de largo 3 es "x ? x"; para cada letra x tomo su primera y su última aparición y cuento cuántas letras distintas hay en el medio.
# Tiempo: O(26 · n) · Espacio: O(1)

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for letra in set(s):
            primera, ultima = s.index(letra), s.rindex(letra)
            if ultima - primera > 1:
                res += len(set(s[primera + 1:ultima]))
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.countPalindromicSubsequence("aabca") == 3
    assert s.countPalindromicSubsequence("adc") == 0
    assert s.countPalindromicSubsequence("bbcbaba") == 4
    print("OK")
