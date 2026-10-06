# 263. Ugly Number (Fácil)
# https://leetcode.com/problems/ugly-number/
#
# Idea: divido por 2, 3 y 5 todas las veces que pueda; si lo que queda es 1, no tenía otros factores
#       primos.
# Tiempo: O(log n) · Espacio: O(1)

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for primo in (2, 3, 5):
            while n % primo == 0:
                n //= primo
        return n == 1


if __name__ == "__main__":
    s = Solution()
    assert s.isUgly(6) is True
    assert s.isUgly(1) is True
    assert s.isUgly(14) is False
    assert s.isUgly(0) is False
    print("OK")
