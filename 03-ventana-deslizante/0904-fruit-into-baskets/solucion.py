# 904. Fruits into Basket (Media)
# https://leetcode.com/problems/fruit-into-baskets/
#
# Idea: es la ventana más larga con a lo sumo 2 tipos de fruta distintos; cuento frutas en la ventana y achico cuando hay 3 tipos.
# Tiempo: O(n) · Espacio: O(1)

from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cuenta = defaultdict(int)
        izq = mejor = 0
        for der, f in enumerate(fruits):
            cuenta[f] += 1
            while len(cuenta) > 2:
                cuenta[fruits[izq]] -= 1
                if cuenta[fruits[izq]] == 0:
                    del cuenta[fruits[izq]]
                izq += 1
            mejor = max(mejor, der - izq + 1)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.totalFruit([1, 2, 1]) == 3
    assert s.totalFruit([0, 1, 2, 2]) == 3
    assert s.totalFruit([1, 2, 3, 2, 2]) == 4
    print("OK")
