# 191. Number of 1 Bits (Fácil)
# https://leetcode.com/problems/number-of-1-bits/
#
# Idea: n & (n - 1) apaga el bit 1 más bajo; cuento cuántas veces puedo hacerlo hasta que n llegue a
#       0.
# Tiempo: O(cantidad de unos) · Espacio: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        unos = 0
        while n:
            n &= n - 1
            unos += 1
        return unos


if __name__ == "__main__":
    s = Solution()
    assert s.hammingWeight(11) == 3
    assert s.hammingWeight(128) == 1
    assert s.hammingWeight(2147483645) == 30
    print("OK")
