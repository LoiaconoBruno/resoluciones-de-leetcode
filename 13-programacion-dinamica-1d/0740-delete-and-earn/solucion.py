# 740. Delete And Earn (Media)
# https://leetcode.com/problems/delete-and-earn/
#
# Idea: si tomo un valor v, me conviene tomar todas sus copias y pierdo v - 1 y v + 1. Sumo los
#       puntos por valor y resuelvo House Robber sobre los valores ordenados.
# Tiempo: O(n + M), con M el valor máximo · Espacio: O(M)

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        puntos = [0] * (max(nums) + 1)
        for n in nums:
            puntos[n] += n
        antes, ultimo = 0, 0
        for p in puntos:
            antes, ultimo = ultimo, max(ultimo, antes + p)
        return ultimo


if __name__ == "__main__":
    s = Solution()
    assert s.deleteAndEarn([3, 4, 2]) == 6
    assert s.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
    print("OK")
