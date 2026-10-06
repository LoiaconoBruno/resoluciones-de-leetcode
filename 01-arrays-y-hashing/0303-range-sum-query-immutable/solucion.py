# 303. Range Sum Query - Immutable (Fácil)
# https://leetcode.com/problems/range-sum-query-immutable/
#
# Idea: precalculo sumas prefijas (prefijo[i] = suma de los primeros i números); la suma de un rango es una resta.
# Tiempo: O(n) para construir, O(1) por consulta · Espacio: O(n)

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefijo = [0]
        for n in nums:
            self.prefijo.append(self.prefijo[-1] + n)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefijo[right + 1] - self.prefijo[left]


if __name__ == "__main__":
    a = NumArray([-2, 0, 3, -5, 2, -1])
    assert a.sumRange(0, 2) == 1
    assert a.sumRange(2, 5) == -1
    assert a.sumRange(0, 5) == -3
    print("OK")
