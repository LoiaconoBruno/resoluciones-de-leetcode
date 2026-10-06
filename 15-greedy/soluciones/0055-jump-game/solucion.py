# 55. Jump Game (Media)
# https://leetcode.com/problems/jump-game/
#
# Idea: recorro de atrás para adelante con una "meta": si desde i puedo saltar hasta la meta, ahora
#       la meta es i. Al final, la meta tiene que haber llegado al índice 0.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        meta = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= meta:
                meta = i
        return meta == 0


if __name__ == "__main__":
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4]) is True
    assert s.canJump([3, 2, 1, 0, 4]) is False
    print("OK")
