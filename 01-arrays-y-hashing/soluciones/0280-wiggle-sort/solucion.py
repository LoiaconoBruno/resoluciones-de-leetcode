# 280. Wiggle Sort (Media)
# https://www.lintcode.com/problem/508/
#
# Idea: en las posiciones impares tiene que haber un "pico" y en las pares un "valle"; recorro una
#       vez y, si un par de vecinos no cumple, los intercambio.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            if (i % 2 == 1) == (nums[i] < nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]


if __name__ == "__main__":
    import random
    s = Solution()

    def es_wiggle(a):
        return all(a[i] <= a[i + 1] if i % 2 == 0 else a[i] >= a[i + 1] for i in range(len(a) - 1))

    for nums in ([3, 5, 2, 1, 6, 4], [1, 2, 3, 4]):
        original = sorted(nums)
        s.wiggleSort(nums)
        assert es_wiggle(nums) and sorted(nums) == original
    for _ in range(200):
        nums = [random.randint(0, 5) for _ in range(random.randint(0, 15))]
        original = sorted(nums)
        s.wiggleSort(nums)
        assert es_wiggle(nums) and sorted(nums) == original
    print("OK")
