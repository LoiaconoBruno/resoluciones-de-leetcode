# 2001. Number of Pairs of Interchangeable Rectangles (Media)
# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
#
# Idea: dos rectángulos son intercambiables si tienen la misma proporción; la guardo como fracción reducida (con gcd, sin floats) y cada grupo de c rectángulos suma c·(c-1)/2 pares.
# Tiempo: O(n log M) · Espacio: O(n)

from collections import Counter
from math import gcd
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        proporciones = Counter()
        for ancho, alto in rectangles:
            g = gcd(ancho, alto)
            proporciones[(ancho // g, alto // g)] += 1
        return sum(c * (c - 1) // 2 for c in proporciones.values())


if __name__ == "__main__":
    s = Solution()
    assert s.interchangeableRectangles([[4, 8], [3, 6], [10, 20], [15, 30]]) == 6
    assert s.interchangeableRectangles([[4, 5], [7, 8]]) == 0
    print("OK")
