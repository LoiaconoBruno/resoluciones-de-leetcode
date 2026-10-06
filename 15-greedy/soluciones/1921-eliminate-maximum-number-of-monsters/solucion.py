# 1921. Eliminate Maximum Number of Monsters (Media)
# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
#
# Idea: calculo en qué minuto llega cada monstruo (dist / speed redondeado para arriba) y los mato
#       en orden de llegada: en el minuto i mato al i-ésimo, que tiene que llegar después de i.
# Tiempo: O(n log n) · Espacio: O(n)

from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        llegadas = sorted((d + v - 1) // v for d, v in zip(dist, speed))
        for minuto, llegada in enumerate(llegadas):
            if llegada <= minuto:
                return minuto
        return len(llegadas)


if __name__ == "__main__":
    s = Solution()
    assert s.eliminateMaximum([1, 3, 4], [1, 1, 1]) == 3
    assert s.eliminateMaximum([1, 1, 2, 3], [1, 1, 1, 1]) == 1
    assert s.eliminateMaximum([3, 2, 4], [5, 3, 2]) == 1
    print("OK")
