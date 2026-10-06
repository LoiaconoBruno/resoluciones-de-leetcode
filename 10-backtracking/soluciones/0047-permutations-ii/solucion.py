# 47. Permutations II (Media)
# https://leetcode.com/problems/permutations-ii/
#
# Idea: en vez de elegir posiciones, elijo valores distintos desde un contador: en cada lugar pruebo
#       cada valor que todavía tenga copias disponibles. Así nunca repito una permutación.
# Tiempo: O(n · n!) · Espacio: O(n)

from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        actual = []
        cuenta = Counter(nums)

        def armar():
            if len(actual) == len(nums):
                res.append(actual[:])
                return
            for n in cuenta:
                if cuenta[n]:
                    cuenta[n] -= 1
                    actual.append(n)
                    armar()
                    actual.pop()
                    cuenta[n] += 1

        armar()
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.permuteUnique([1, 1, 2])) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert len(s.permuteUnique([1, 2, 3])) == 6
    print("OK")
