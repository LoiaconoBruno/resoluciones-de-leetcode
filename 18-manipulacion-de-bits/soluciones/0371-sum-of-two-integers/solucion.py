# 371. Sum of Two Integers (Media)
# https://leetcode.com/problems/sum-of-two-integers/
#
# Idea: a ^ b suma sin acarreo y (a & b) << 1 es el acarreo; repito hasta que no quede acarreo. En
#       Python los enteros no tienen 32 bits, así que uso una máscara y al final interpreto el
#       signo.
# Tiempo: O(32) = O(1) · Espacio: O(1)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASCARA = 0xFFFFFFFF
        MAXIMO = 0x7FFFFFFF
        while b:
            a, b = (a ^ b) & MASCARA, ((a & b) << 1) & MASCARA
        return a if a <= MAXIMO else ~(a ^ MASCARA)


if __name__ == "__main__":
    s = Solution()
    assert s.getSum(1, 2) == 3
    assert s.getSum(2, 3) == 5
    assert s.getSum(-1, 1) == 0
    assert s.getSum(-2, -3) == -5
    assert all(s.getSum(a, b) == a + b for a in range(-30, 31) for b in range(-30, 31))
    print("OK")
