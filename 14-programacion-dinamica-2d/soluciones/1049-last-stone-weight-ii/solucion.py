# 1049. Last Stone Weight II (Media)
# https://leetcode.com/problems/last-stone-weight-ii/
#
# Idea: al final las piedras quedan divididas en dos grupos que se restan; quiero el grupo cuya suma
#       esté lo más cerca posible de la mitad. Busco todas las sumas alcanzables hasta total / 2.
# Tiempo: O(n · suma) · Espacio: O(suma)

from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        mitad = total // 2
        alcanzables = {0}
        for piedra in stones:
            alcanzables |= {a + piedra for a in alcanzables if a + piedra <= mitad}
        return total - 2 * max(alcanzables)


if __name__ == "__main__":
    s = Solution()
    assert s.lastStoneWeightII([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeightII([31, 26, 33, 21, 40]) == 5
    print("OK")
