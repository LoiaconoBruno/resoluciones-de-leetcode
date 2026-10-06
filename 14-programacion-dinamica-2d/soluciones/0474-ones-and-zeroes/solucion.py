# 474. Ones and Zeroes (Media)
# https://leetcode.com/problems/ones-and-zeroes/
#
# Idea: mochila con dos capacidades: dp[i][j] = más strings que entran usando como mucho i ceros y j
#       unos. Con cada string recorro las capacidades de mayor a menor para no usarlo dos veces.
# Tiempo: O(L · m · n), con L la cantidad de strings · Espacio: O(m · n)

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for texto in strs:
            ceros, unos = texto.count("0"), texto.count("1")
            for i in range(m, ceros - 1, -1):
                for j in range(n, unos - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - ceros][j - unos])
        return dp[m][n]


if __name__ == "__main__":
    s = Solution()
    assert s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4
    assert s.findMaxForm(["10", "0", "1"], 1, 1) == 2
    print("OK")
