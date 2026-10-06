# 1626. Best Team with no Conflicts (Media)
# https://leetcode.com/problems/best-team-with-no-conflicts/
#
# Idea: ordeno por (edad, puntaje); así un equipo sin conflictos es una subsecuencia con puntajes no
#       decrecientes. dp[i] = mejor suma de un equipo que termina en el jugador i (como LIS, pero
#       sumando).
# Tiempo: O(n²) · Espacio: O(n)

from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        jugadores = sorted(zip(ages, scores))
        dp = [0] * len(jugadores)
        for i, (_, puntaje) in enumerate(jugadores):
            dp[i] = puntaje
            for j in range(i):
                if jugadores[j][1] <= puntaje:
                    dp[i] = max(dp[i], dp[j] + puntaje)
        return max(dp)


if __name__ == "__main__":
    s = Solution()
    assert s.bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]) == 34
    assert s.bestTeamScore([4, 5, 6, 5], [2, 1, 2, 1]) == 16
    assert s.bestTeamScore([1, 2, 3, 5], [8, 9, 10, 1]) == 6
    print("OK")
