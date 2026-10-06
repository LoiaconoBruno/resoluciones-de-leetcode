# 1406. Stone Game III (Difícil)
# https://leetcode.com/problems/stone-game-iii/
#
# Idea: dp[i] = la mejor diferencia (mis puntos - los del rival) que puede sacar quien juega desde
#       la piedra i. Pruebo tomar 1, 2 o 3: lo que tomo menos dp de donde arranca el otro.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = float("-inf")
            tomo = 0
            for j in range(i, min(i + 3, n)):
                tomo += stoneValue[j]
                dp[i] = max(dp[i], tomo - dp[j + 1])
        if dp[0] > 0:
            return "Alice"
        return "Bob" if dp[0] < 0 else "Tie"


if __name__ == "__main__":
    s = Solution()
    assert s.stoneGameIII([1, 2, 3, 7]) == "Bob"
    assert s.stoneGameIII([1, 2, 3, -9]) == "Alice"
    assert s.stoneGameIII([1, 2, 3, 6]) == "Tie"
    print("OK")
