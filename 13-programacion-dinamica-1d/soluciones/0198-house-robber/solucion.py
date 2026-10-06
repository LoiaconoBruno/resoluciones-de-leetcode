# 198. House Robber (Media)
# https://leetcode.com/problems/house-robber/
#
# Idea: en cada casa elijo: robarla (su plata + lo mejor hasta dos casas antes) o saltearla (lo
#       mejor hasta la anterior). Solo necesito los dos últimos resultados.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        antes, ultimo = 0, 0
        for plata in nums:
            antes, ultimo = ultimo, max(ultimo, antes + plata)
        return ultimo


if __name__ == "__main__":
    s = Solution()
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
    print("OK")
