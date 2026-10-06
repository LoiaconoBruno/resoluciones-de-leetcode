# 1866. Number of Ways to Rearrange Sticks With K Sticks Visible (Difícil)
# https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/
#
# Idea: pienso en dónde va el palito más corto: si va primero, se ve (queda un problema con n - 1
#       palitos y k - 1 visibles); si va en cualquiera de las otras n - 1 posiciones, queda tapado.
#       dp[n][k] = dp[n-1][k-1] + (n-1)·dp[n-1][k].
# Tiempo: O(n · k) · Espacio: O(k)

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] + [0] * k
        for palitos in range(1, n + 1):
            for visibles in range(min(palitos, k), 0, -1):
                dp[visibles] = (dp[visibles - 1] + (palitos - 1) * dp[visibles]) % MOD
            dp[0] = 0
        return dp[k]


if __name__ == "__main__":
    s = Solution()
    assert s.rearrangeSticks(3, 2) == 3
    assert s.rearrangeSticks(5, 5) == 1
    assert s.rearrangeSticks(20, 11) == 647427950
    print("OK")
