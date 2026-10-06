# 1553. Minimum Number of Days to Eat N Oranges (Difícil)
# https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/
#
# Idea: comer de a una naranja solo sirve para llegar a un múltiplo de 2 o de 3; así que desde n
#       pruebo ir a n // 2 (gastando n % 2 días sueltos + 1) o a n // 3 (n % 3 + 1), con
#       memoización.
# Tiempo: O(log² n) · Espacio: O(log² n)

from functools import lru_cache


class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def dias(m):
            if m <= 1:
                return m
            return 1 + min(m % 2 + dias(m // 2), m % 3 + dias(m // 3))

        return dias(n)


if __name__ == "__main__":
    s = Solution()
    assert s.minDays(10) == 4
    assert s.minDays(6) == 3
    assert s.minDays(1) == 1
    assert s.minDays(2 * 10 ** 9) == 32
    print("OK")
