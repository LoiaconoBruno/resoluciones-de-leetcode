# 279. Perfect Squares (Media)
# https://leetcode.com/problems/perfect-squares/
#
# Idea: dp[i] = menor cantidad de cuadrados que suman i; para cada i pruebo cuál fue el último
#       cuadrado: dp[i] = 1 + min(dp[i - k²]).
# Tiempo: O(n · √n) · Espacio: O(n)

class Solution:
    def numSquares(self, n: int) -> int:
        cuadrados = [k * k for k in range(1, int(n ** 0.5) + 1)]
        dp = [0] + [n] * n
        for i in range(1, n + 1):
            for c in cuadrados:
                if c > i:
                    break
                dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    assert s.numSquares(12) == 3
    assert s.numSquares(13) == 2
    assert s.numSquares(1) == 1
    print("OK")
