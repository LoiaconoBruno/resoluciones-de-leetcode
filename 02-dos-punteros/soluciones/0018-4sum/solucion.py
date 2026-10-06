# 18. 4Sum (Media)
# https://leetcode.com/problems/4sum/
#
# Idea: como 3Sum pero con un nivel más: ordeno, fijo los dos primeros con dos bucles y busco el par
#       restante con dos punteros, salteando repetidos en cada nivel.
# Tiempo: O(n³) · Espacio: O(1) extra

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                izq, der = j + 1, n - 1
                while izq < der:
                    suma = nums[i] + nums[j] + nums[izq] + nums[der]
                    if suma < target:
                        izq += 1
                    elif suma > target:
                        der -= 1
                    else:
                        res.append([nums[i], nums[j], nums[izq], nums[der]])
                        izq += 1
                        der -= 1
                        while izq < der and nums[izq] == nums[izq - 1]:
                            izq += 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.fourSum([1, 0, -1, 0, -2, 2], 0)) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert s.fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    print("OK")
