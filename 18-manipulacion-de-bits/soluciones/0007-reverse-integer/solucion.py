# 7. Reverse Integer (Media)
# https://leetcode.com/problems/reverse-integer/
#
# Idea: armo el número dado vuelta dígito por dígito (trabajando con el valor absoluto) y, si se
#       sale del rango de 32 bits con signo, devuelvo 0.
# Tiempo: O(log x) · Espacio: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        signo = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        res *= signo
        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0


if __name__ == "__main__":
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(1534236469) == 0
    print("OK")
