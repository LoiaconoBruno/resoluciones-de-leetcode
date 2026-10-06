# 554. Brick Wall (Media)
# https://leetcode.com/problems/brick-wall/
#
# Idea: la línea que menos ladrillos corta es la que pasa por más bordes; cuento en qué posiciones caen los bordes de cada fila (sin el borde final).
# Tiempo: O(total de ladrillos) · Espacio: O(ancho)

from collections import defaultdict
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        bordes = defaultdict(int)
        for fila in wall:
            posicion = 0
            for ladrillo in fila[:-1]:
                posicion += ladrillo
                bordes[posicion] += 1
        return len(wall) - max(bordes.values(), default=0)


if __name__ == "__main__":
    s = Solution()
    assert s.leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]) == 2
    assert s.leastBricks([[1], [1], [1]]) == 3
    print("OK")
