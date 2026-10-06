# 1929. Concatenation of Array (Fácil)
# https://leetcode.com/problems/concatenation-of-array/
#
# Idea: la respuesta es el array seguido de sí mismo: ans[i] = ans[i + n] = nums[i].
# Tiempo: O(n) · Espacio: O(n) (la respuesta)

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, x in enumerate(nums):
            ans[i] = ans[i + n] = x
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert s.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
    print("OK")
