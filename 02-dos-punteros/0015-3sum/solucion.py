# 15. 3Sum (Media)
# https://leetcode.com/problems/3sum/
#
# Idea: ordeno, fijo el primer número y busco los otros dos con dos punteros (como Two Sum II); salteo los repetidos para no duplicar tripletas.
# Tiempo: O(n²) · Espacio: O(1) extra (sin contar el ordenamiento)

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            izq, der = i + 1, len(nums) - 1
            while izq < der:
                suma = a + nums[izq] + nums[der]
                if suma > 0:
                    der -= 1
                elif suma < 0:
                    izq += 1
                else:
                    res.append([a, nums[izq], nums[der]])
                    izq += 1
                    der -= 1
                    while izq < der and nums[izq] == nums[izq - 1]:
                        izq += 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.threeSum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
    assert s.threeSum([0, 1, 1]) == []
    assert s.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert sorted(s.threeSum([-2, 0, 0, 2, 2])) == [[-2, 0, 2]]
    print("OK")
