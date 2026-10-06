# 1968. Array With Elements Not Equal to Average of Neighbors (Media)
# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
#
# Idea: ordeno e intercambio cada par (1,2), (3,4), ...; así cada número queda como pico o como valle respecto de sus vecinos, y un pico o un valle nunca es el promedio.
# Tiempo: O(n log n) · Espacio: O(1) extra

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums


if __name__ == "__main__":
    import random
    s = Solution()

    def valido(a):
        return all(2 * a[i] != a[i - 1] + a[i + 1] for i in range(1, len(a) - 1))

    for nums in ([1, 2, 3, 4, 5], [6, 2, 0, 9, 7]):
        assert valido(s.rearrangeArray(nums[:]))
    for _ in range(200):
        nums = random.sample(range(100), random.randint(3, 20))
        assert valido(s.rearrangeArray(nums))
    print("OK")
