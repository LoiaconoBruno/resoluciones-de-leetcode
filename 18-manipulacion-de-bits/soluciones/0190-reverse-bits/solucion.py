# 190. Reverse Bits (Fácil)
# https://leetcode.com/problems/reverse-bits/
#
# Idea: 32 veces: saco el último bit de n y lo meto por la derecha en el resultado (que se va
#       corriendo a la izquierda).
# Tiempo: O(32) = O(1) · Espacio: O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.reverseBits(43261596) == 964176192
    assert s.reverseBits(4294967293) == 3221225471
    print("OK")
