# 90. Subsets II (Media)
# https://leetcode.com/problems/subsets-ii/
#
# Idea: ordeno para que los repetidos queden juntos; si decido no usar un número, salteo también
#       todas sus copias. Así cada subconjunto aparece una sola vez.
# Tiempo: O(n · 2^n) · Espacio: O(n) de recursión

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        actual = []

        def decidir(i):
            if i == len(nums):
                res.append(actual[:])
                return
            actual.append(nums[i])
            decidir(i + 1)
            actual.pop()
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            decidir(i + 1)

        decidir(0)
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.subsetsWithDup([1, 2, 2])) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert sorted(s.subsetsWithDup([0])) == [[], [0]]
    print("OK")
