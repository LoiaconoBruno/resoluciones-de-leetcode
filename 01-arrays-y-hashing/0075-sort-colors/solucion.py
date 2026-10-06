# 75. Sort Colors (Media)
# https://leetcode.com/problems/sort-colors/
#
# Idea: bandera holandesa: tres punteros; los 0 van al principio, los 2 al final y los 1 quedan en el medio, en una sola pasada.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        izq, i, der = 0, 0, len(nums) - 1
        while i <= der:
            if nums[i] == 0:
                nums[izq], nums[i] = nums[i], nums[izq]
                izq += 1
                i += 1
            elif nums[i] == 2:
                nums[der], nums[i] = nums[i], nums[der]
                der -= 1
            else:
                i += 1


if __name__ == "__main__":
    s = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    s.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]
    nums = [2, 0, 1]
    s.sortColors(nums)
    assert nums == [0, 1, 2]
    print("OK")
