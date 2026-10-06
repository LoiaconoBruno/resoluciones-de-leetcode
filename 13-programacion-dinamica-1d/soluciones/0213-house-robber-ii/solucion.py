# 213. House Robber II (Media)
# https://leetcode.com/problems/house-robber-ii/
#
# Idea: como es un círculo, la primera y la última casa no pueden ir juntas: resuelvo House Robber
#       sin la última y sin la primera, y me quedo con el mejor.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robar_fila(nums[:-1]), self.robar_fila(nums[1:]))

    def robar_fila(self, casas):
        antes, ultimo = 0, 0
        for plata in casas:
            antes, ultimo = ultimo, max(ultimo, antes + plata)
        return ultimo


if __name__ == "__main__":
    s = Solution()
    assert s.rob([2, 3, 2]) == 3
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([1, 2, 3]) == 3
    assert s.rob([1]) == 1
    print("OK")
