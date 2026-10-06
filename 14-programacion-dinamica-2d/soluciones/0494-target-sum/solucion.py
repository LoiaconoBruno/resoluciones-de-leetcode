# 494. Target Sum (Media)
# https://leetcode.com/problems/target-sum/
#
# Idea: llevo un diccionario suma -> cantidad de formas de llegar a ella; con cada número, cada suma
#       se divide en dos: + número y - número.
# Tiempo: O(n · S), con S el rango de sumas posibles · Espacio: O(S)

from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        formas = {0: 1}
        for n in nums:
            nuevas = defaultdict(int)
            for suma, cantidad in formas.items():
                nuevas[suma + n] += cantidad
                nuevas[suma - n] += cantidad
            formas = nuevas
        return formas.get(target, 0)


if __name__ == "__main__":
    s = Solution()
    assert s.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
    assert s.findTargetSumWays([1], 1) == 1
    assert s.findTargetSumWays([0, 0], 0) == 4
    print("OK")
