# 1140. Stone Game II (Media)
# https://leetcode.com/problems/stone-game-ii/
#
# Idea: memoizo por (i, M): quien juega desde la pila i puede tomar x pilas (1 ≤ x ≤ 2M) y después
#       el rival se queda con lo mejor del resto. Con sumas de sufijo, lo mío es total restante - lo
#       mejor del rival.
# Tiempo: O(n³) · Espacio: O(n²)

from functools import lru_cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        sufijo = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            sufijo[i] = sufijo[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def mejor(i, m):
            if i + 2 * m >= n:
                return sufijo[i]
            return max(sufijo[i] - mejor(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        return mejor(0, 1)


if __name__ == "__main__":
    s = Solution()
    assert s.stoneGameII([2, 7, 9, 4, 4]) == 10
    assert s.stoneGameII([1, 2, 3, 4, 5, 100]) == 104
    print("OK")
