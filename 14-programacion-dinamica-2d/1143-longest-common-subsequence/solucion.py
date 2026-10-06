# 1143. Longest Common Subsequence (Media)
# https://leetcode.com/problems/longest-common-subsequence/
#
# Idea: dp[i][j] = LCS entre los primeros i caracteres de text1 y los primeros j de text2. Si las
#       letras coinciden, es 1 + dp[i-1][j-1]; si no, el mejor de descartar una de las dos.
# Tiempo: O(n · m) · Espacio: O(m)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        anterior = [0] * (len(text2) + 1)
        for a in text1:
            actual = [0] * (len(text2) + 1)
            for j, b in enumerate(text2):
                actual[j + 1] = anterior[j] + 1 if a == b else max(anterior[j + 1], actual[j])
            anterior = actual
        return anterior[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonSubsequence("abcde", "ace") == 3
    assert s.longestCommonSubsequence("abc", "abc") == 3
    assert s.longestCommonSubsequence("abc", "def") == 0
    print("OK")
