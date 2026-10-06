# 10. Regular Expression Matching (Difícil)
# https://leetcode.com/problems/regular-expression-matching/
#
# Idea: dp[i][j] dice si s[i:] matchea p[j:]. Si p[j + 1] es '*', o salteo "x*" entero o, si la
#       letra matchea, consumo una letra de s y me quedo en el mismo patrón. Si no, matcheo una
#       letra y avanzo los dos.
# Tiempo: O(n · m) · Espacio: O(n · m)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = True
        for i in range(n, -1, -1):
            for j in range(m - 1, -1, -1):
                coincide = i < n and p[j] in (s[i], ".")
                if j + 1 < m and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (coincide and dp[i + 1][j])
                else:
                    dp[i][j] = coincide and dp[i + 1][j + 1]
        return dp[0][0]


if __name__ == "__main__":
    s = Solution()
    assert s.isMatch("aa", "a") is False
    assert s.isMatch("aa", "a*") is True
    assert s.isMatch("ab", ".*") is True
    assert s.isMatch("aab", "c*a*b") is True
    assert s.isMatch("mississippi", "mis*is*p*.") is False
    print("OK")
