# 983. Minimum Cost For Tickets (Media)
# https://leetcode.com/problems/minimum-cost-for-tickets/
#
# Idea: dp[i] = costo mínimo para cubrir los viajes desde el día days[i] en adelante: compro un pase
#       de 1, 7 o 30 días y salto al primer viaje que el pase ya no cubre.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = float("inf")
            j = i
            for duracion, costo in zip((1, 7, 30), costs):
                while j < n and days[j] < days[i] + duracion:
                    j += 1
                dp[i] = min(dp[i], costo + dp[j])
        return dp[0]


if __name__ == "__main__":
    s = Solution()
    assert s.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11
    assert s.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]) == 17
    print("OK")
