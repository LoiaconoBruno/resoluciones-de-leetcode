# 2466. Count Ways to Build Good Strings (Media)
# https://leetcode.com/problems/count-ways-to-build-good-strings/
#
# Idea: dp[largo] = cantidad de strings de ese largo; el último bloque agregado fue de zero ceros o
#       de one unos, así que dp[largo] = dp[largo - zero] + dp[largo - one]. Sumo entre low y high.
# Tiempo: O(high) · Espacio: O(high)

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] + [0] * high
        for largo in range(1, high + 1):
            if largo >= zero:
                dp[largo] += dp[largo - zero]
            if largo >= one:
                dp[largo] += dp[largo - one]
            dp[largo] %= MOD
        return sum(dp[low:high + 1]) % MOD


if __name__ == "__main__":
    s = Solution()
    assert s.countGoodStrings(3, 3, 1, 1) == 8
    assert s.countGoodStrings(2, 3, 1, 2) == 5
    print("OK")
