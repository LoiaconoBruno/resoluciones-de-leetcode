# 516. Longest Palindromic Subsequence (Media)
# https://leetcode.com/problems/longest-palindromic-subsequence/
#
# Idea: dp[i][j] = la subsecuencia palíndroma más larga en s[i..j]. Si las puntas son iguales suman
#       2 a lo de adentro; si no, me quedo con lo mejor de sacar una de las dos puntas.
# Tiempo: O(n²) · Espacio: O(n)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            nuevo = [0] * n
            nuevo[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    nuevo[j] = dp[j - 1] + 2
                else:
                    nuevo[j] = max(dp[j], nuevo[j - 1])
            dp = nuevo
        return dp[n - 1]


if __name__ == "__main__":
    s = Solution()
    assert s.longestPalindromeSubseq("bbbab") == 4
    assert s.longestPalindromeSubseq("cbbd") == 2
    assert s.longestPalindromeSubseq("a") == 1
    print("OK")
