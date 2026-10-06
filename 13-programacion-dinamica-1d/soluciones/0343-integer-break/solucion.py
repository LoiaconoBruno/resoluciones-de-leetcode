# 343. Integer Break (Media)
# https://leetcode.com/problems/integer-break/
#
# Idea: dp[i] = mejor producto partiendo i (o dejándolo entero si no es n). Para cada i pruebo el
#       primer pedazo j: max(j, dp[j]) · max(i - j, dp[i - j]).
# Tiempo: O(n²) · Espacio: O(n)

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    assert s.integerBreak(2) == 1
    assert s.integerBreak(10) == 36
    assert s.integerBreak(3) == 2
    print("OK")
