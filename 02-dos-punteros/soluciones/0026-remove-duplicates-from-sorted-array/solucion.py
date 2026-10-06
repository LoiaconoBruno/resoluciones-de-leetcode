# 26. Remove Duplicates From Sorted Array (Fácil)
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#
# Idea: como está ordenado, un número es nuevo si es distinto del último que guardé; un puntero k
#       marca dónde va el siguiente único.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    s = Solution()
    a = [1, 1, 2]
    k = s.removeDuplicates(a)
    assert k == 2 and a[:k] == [1, 2]
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = s.removeDuplicates(a)
    assert k == 5 and a[:k] == [0, 1, 2, 3, 4]
    print("OK")
