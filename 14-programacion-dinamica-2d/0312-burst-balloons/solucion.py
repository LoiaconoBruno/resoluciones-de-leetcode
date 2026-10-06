# 312. Burst Balloons (Difícil)
# https://leetcode.com/problems/burst-balloons/
#
# Idea: pienso al revés: en el intervalo (i, j) elijo qué globo k explota último; en ese momento sus
#       vecinos son los bordes i y j. dp[i][j] = max sobre k de nums[i]·nums[k]·nums[j] + dp[i][k] +
#       dp[k][j].
# Tiempo: O(n³) · Espacio: O(n²)

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        globos = [1] + nums + [1]
        n = len(globos)
        dp = [[0] * n for _ in range(n)]
        for largo in range(2, n):
            for i in range(n - largo):
                j = i + largo
                dp[i][j] = max(globos[i] * globos[k] * globos[j] + dp[i][k] + dp[k][j]
                               for k in range(i + 1, j))
        return dp[0][n - 1]


if __name__ == "__main__":
    s = Solution()
    assert s.maxCoins([3, 1, 5, 8]) == 167
    assert s.maxCoins([1, 5]) == 10
    print("OK")
