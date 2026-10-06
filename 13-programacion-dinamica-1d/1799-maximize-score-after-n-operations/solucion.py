# 1799. Maximize Score after N Operations (Difícil)
# https://leetcode.com/problems/maximize-score-after-n-operations/
#
# Idea: con 2n ≤ 14 números, el estado es la máscara de los ya usados; el número de operación sale
#       de cuántos bits hay prendidos. dp[máscara] = mejor puntaje usando esos; pruebo agregar cada
#       par libre.
# Tiempo: O(2^(2n) · n²) · Espacio: O(2^(2n))

from math import gcd
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = len(nums)
        g = [[gcd(a, b) for b in nums] for a in nums]
        dp = [-1] * (1 << m)
        dp[0] = 0
        for mascara in range(1 << m):
            if dp[mascara] < 0:
                continue
            operacion = bin(mascara).count("1") // 2 + 1
            libres = [i for i in range(m) if not mascara >> i & 1]
            for a in range(len(libres)):
                for b in range(a + 1, len(libres)):
                    i, j = libres[a], libres[b]
                    nueva = mascara | (1 << i) | (1 << j)
                    dp[nueva] = max(dp[nueva], dp[mascara] + operacion * g[i][j])
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.maxScore([1, 2]) == 1
    assert s.maxScore([3, 4, 6, 8]) == 11
    assert s.maxScore([1, 2, 3, 4, 5, 6]) == 14
    print("OK")
