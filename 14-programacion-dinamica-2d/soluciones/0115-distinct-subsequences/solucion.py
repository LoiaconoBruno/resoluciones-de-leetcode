# 115. Distinct Subsequences (Difícil)
# https://leetcode.com/problems/distinct-subsequences/
#
# Idea: dp[j] = formas de formar los primeros j de t con lo recorrido de s. Con cada letra de s, si
#       coincide con t[j-1], suma las formas de dp[j-1]; recorro j de atrás para adelante para no
#       usar la letra dos veces.
# Tiempo: O(n · m) · Espacio: O(m)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [1] + [0] * len(t)
        for letra in s:
            for j in range(len(t), 0, -1):
                if t[j - 1] == letra:
                    dp[j] += dp[j - 1]
        return dp[len(t)]


if __name__ == "__main__":
    s = Solution()
    assert s.numDistinct("rabbbit", "rabbit") == 3
    assert s.numDistinct("babgbag", "bag") == 5
    print("OK")
