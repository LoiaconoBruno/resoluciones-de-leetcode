# 69. Sqrt(x) (Fácil)
# https://leetcode.com/problems/sqrtx/
#
# Idea: busco el r más grande con r · r ≤ x usando búsqueda binaria.
# Tiempo: O(log x) · Espacio: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        izq, der = 0, x
        while izq < der:
            r = (izq + der + 1) // 2
            if r * r <= x:
                izq = r
            else:
                der = r - 1
        return izq


if __name__ == "__main__":
    s = Solution()
    assert s.mySqrt(4) == 2
    assert s.mySqrt(8) == 2
    assert s.mySqrt(0) == 0
    assert s.mySqrt(1) == 1
    assert all(s.mySqrt(x) == int(x ** 0.5) for x in range(2000))
    print("OK")
