# 846. Hand of Straights (Media)
# https://leetcode.com/problems/hand-of-straights/
#
# Idea: la carta más chica que queda tiene que empezar un grupo; armo el grupo desde ella (carta,
#       carta + 1, ...) descontando del contador. Si falta alguna, no se puede.
# Tiempo: O(n log n) · Espacio: O(n)

from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        cuenta = Counter(hand)
        for carta in sorted(cuenta):
            veces = cuenta[carta]
            if veces == 0:
                continue
            for siguiente in range(carta, carta + groupSize):
                if cuenta[siguiente] < veces:
                    return False
                cuenta[siguiente] -= veces
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True
    assert s.isNStraightHand([1, 2, 3, 4, 5], 4) is False
    print("OK")
