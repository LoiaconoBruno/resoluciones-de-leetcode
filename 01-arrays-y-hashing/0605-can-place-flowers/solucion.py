# 605. Can Place Flowers (Fácil)
# https://leetcode.com/problems/can-place-flowers/
#
# Idea: agrego un 0 a cada punta y planto (greedy) en cada lugar vacío cuyos dos vecinos también
#       están vacíos.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cantero = [0] + flowerbed + [0]
        for i in range(1, len(cantero) - 1):
            if cantero[i - 1] == cantero[i] == cantero[i + 1] == 0:
                cantero[i] = 1
                n -= 1
        return n <= 0


if __name__ == "__main__":
    s = Solution()
    assert s.canPlaceFlowers([1, 0, 0, 0, 1], 1) is True
    assert s.canPlaceFlowers([1, 0, 0, 0, 1], 2) is False
    assert s.canPlaceFlowers([0, 0, 1, 0, 0], 2) is True
    print("OK")
