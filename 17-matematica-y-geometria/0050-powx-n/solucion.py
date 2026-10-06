# 50. Pow(x, n) (Media)
# https://leetcode.com/problems/powx-n/
#
# Idea: exponenciación rápida: x^n = (x²)^(n/2), y si n es impar multiplico una x más. Si n es
#       negativo, calculo 1 / x^(-n).
# Tiempo: O(log n) · Espacio: O(1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1 / x, -n
        res = 1.0
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert abs(s.myPow(2.0, 10) - 1024.0) < 1e-9
    assert abs(s.myPow(2.1, 3) - 9.261) < 1e-9
    assert abs(s.myPow(2.0, -2) - 0.25) < 1e-9
    assert s.myPow(1.0, -2147483648) == 1.0
    print("OK")
