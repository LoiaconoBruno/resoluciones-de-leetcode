# 2013. Detect Squares (Media)
# https://leetcode.com/problems/detect-squares/
#
# Idea: cuento cuántas veces se agregó cada punto. Para una consulta (x, y) pruebo cada punto (px,
#       py) que pueda ser la esquina opuesta (misma distancia en x que en y) y multiplico las
#       cantidades de las otras dos esquinas.
# Tiempo: O(1) add, O(puntos distintos) count · Espacio: O(puntos distintos)

from collections import Counter
from typing import List


class DetectSquares:
    def __init__(self):
        self.puntos = Counter()

    def add(self, point: List[int]) -> None:
        self.puntos[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        total = 0
        for (px, py), veces in list(self.puntos.items()):
            if abs(px - x) != abs(py - y) or px == x:
                continue
            total += veces * self.puntos[(x, py)] * self.puntos[(px, y)]
        return total


if __name__ == "__main__":
    d = DetectSquares()
    d.add([3, 10])
    d.add([11, 2])
    d.add([3, 2])
    assert d.count([11, 10]) == 1
    assert d.count([14, 8]) == 0
    d.add([11, 2])
    assert d.count([11, 10]) == 2
    print("OK")
