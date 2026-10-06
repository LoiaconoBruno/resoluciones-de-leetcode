# 2300. Successful Pairs of Spells and Potions (Media)
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
#
# Idea: ordeno las pociones; para un hechizo s necesito pociones ≥ ceil(success / s), y con búsqueda binaria encuentro la primera que cumple: todas las de la derecha también sirven.
# Tiempo: O((n + m) log m) · Espacio: O(1) extra

from bisect import bisect_left
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []
        for s in spells:
            minima = (success + s - 1) // s
            res.append(m - bisect_left(potions, minima))
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7) == [4, 0, 3]
    assert s.successfulPairs([3, 1, 2], [8, 5, 8], 16) == [2, 0, 2]
    print("OK")
