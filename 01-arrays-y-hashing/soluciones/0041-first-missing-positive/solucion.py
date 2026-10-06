# 41. First Missing Positive (Difícil)
# https://leetcode.com/problems/first-missing-positive/
#
# Idea: la respuesta está entre 1 y n + 1; ubico cada número v (1 ≤ v ≤ n) en la posición v - 1 con
#       intercambios y después busco la primera posición que no tiene su número.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == "__main__":
    s = Solution()
    assert s.firstMissingPositive([1, 2, 0]) == 3
    assert s.firstMissingPositive([3, 4, -1, 1]) == 2
    assert s.firstMissingPositive([7, 8, 9, 11, 12]) == 1
    assert s.firstMissingPositive([1, 1]) == 2
    print("OK")
