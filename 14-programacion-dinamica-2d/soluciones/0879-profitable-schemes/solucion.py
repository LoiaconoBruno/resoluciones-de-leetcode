# 879. Profitable Schemes (Difícil)
# https://leetcode.com/problems/profitable-schemes/
#
# Idea: mochila: dp[g][p] = cantidad de planes que usan g personas y logran ganancia p (topeada en
#       minProfit, porque pasarse no cambia nada). Con cada crimen recorro g de mayor a menor.
# Tiempo: O(crímenes · n · minProfit) · Espacio: O(n · minProfit)

from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for personas, ganancia in zip(group, profit):
            for g in range(n, personas - 1, -1):
                for p in range(minProfit, -1, -1):
                    nueva = min(minProfit, p + ganancia)
                    dp[g][nueva] = (dp[g][nueva] + dp[g - personas][p]) % MOD
        return sum(dp[g][minProfit] for g in range(n + 1)) % MOD


if __name__ == "__main__":
    s = Solution()
    assert s.profitableSchemes(5, 3, [2, 2], [2, 3]) == 2
    assert s.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]) == 7
    assert s.profitableSchemes(1, 0, [2], [1]) == 1
    print("OK")
