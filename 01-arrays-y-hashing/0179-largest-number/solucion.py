# 179. Largest Number (Media)
# https://leetcode.com/problems/largest-number/
#
# Idea: ordeno los números como strings con un comparador: a va antes que b si a + b > b + a. Cuidado con el caso de todos ceros.
# Tiempo: O(n log n · k), con k la cantidad de dígitos · Espacio: O(n · k)

from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        textos = [str(n) for n in nums]

        def comparar(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        textos.sort(key=cmp_to_key(comparar))
        res = "".join(textos)
        return "0" if res[0] == "0" else res


if __name__ == "__main__":
    s = Solution()
    assert s.largestNumber([10, 2]) == "210"
    assert s.largestNumber([3, 30, 34, 5, 9]) == "9534330"
    assert s.largestNumber([0, 0]) == "0"
    print("OK")
