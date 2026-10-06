# 338. Counting Bits (Fácil)
# https://leetcode.com/problems/counting-bits/
#
# Idea: i tiene los mismos unos que i >> 1 (lo mismo sin el último bit) más ese último bit: bits[i]
#       = bits[i >> 1] + (i & 1).
# Tiempo: O(n) · Espacio: O(n) (la respuesta)

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)
        for i in range(1, n + 1):
            bits[i] = bits[i >> 1] + (i & 1)
        return bits


if __name__ == "__main__":
    s = Solution()
    assert s.countBits(2) == [0, 1, 1]
    assert s.countBits(5) == [0, 1, 1, 2, 1, 2]
    assert s.countBits(1000) == [bin(i).count("1") for i in range(1001)]
    print("OK")
