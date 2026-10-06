# 877. Stone Game (Media)
# https://leetcode.com/problems/stone-game/
#
# Idea: dp[i][j] = la mejor diferencia (mis piedras - las del rival) que saca quien juega con las
#       pilas i..j: tomo la de la izquierda o la de la derecha y le resto lo mejor que hace el otro
#       con lo que queda.
# Tiempo: O(n²) · Espacio: O(n)

from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]
        for largo in range(2, n + 1):
            for i in range(n - largo + 1):
                j = i + largo - 1
                dp[i] = max(piles[i] - dp[i + 1], piles[j] - dp[i])
        return dp[0] > 0


if __name__ == "__main__":
    s = Solution()
    assert s.stoneGame([5, 3, 4, 5]) is True
    assert s.stoneGame([3, 7, 2, 3]) is True
    print("OK")
