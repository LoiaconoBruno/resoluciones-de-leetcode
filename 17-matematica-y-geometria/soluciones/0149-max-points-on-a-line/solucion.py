# 149. Maximum Points on a Line (Difícil)
# https://leetcode.com/problems/max-points-on-a-line/
#
# Idea: fijo un punto y agrupo a los demás por la pendiente que forman con él, guardada como
#       fracción reducida (dy, dx) con signo normalizado para no usar floats. El grupo más grande +
#       1 son los puntos en una recta que pasa por él.
# Tiempo: O(n² log M) · Espacio: O(n)

from collections import Counter
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        mejor = 1
        for i, (x1, y1) in enumerate(points):
            pendientes = Counter()
            for x2, y2 in points[i + 1:]:
                dx, dy = x2 - x1, y2 - y1
                g = gcd(dx, dy)
                dx, dy = dx // g, dy // g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                pendientes[(dx, dy)] += 1
            if pendientes:
                mejor = max(mejor, max(pendientes.values()) + 1)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.maxPoints([[1, 1], [2, 2], [3, 3]]) == 3
    assert s.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
    assert s.maxPoints([[0, 0]]) == 1
    print("OK")
