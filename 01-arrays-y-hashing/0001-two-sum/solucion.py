# 1. Two Sum (Fácil)
# https://leetcode.com/problems/two-sum/
#
# Idea: recorro una sola vez guardando número -> índice; para cada número me pregunto si ya vi el que le falta para llegar al target.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice = {}
        for i, n in enumerate(nums):
            falta = target - n
            if falta in indice:
                return [indice[falta], i]
            indice[n] = i
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    print("OK")
