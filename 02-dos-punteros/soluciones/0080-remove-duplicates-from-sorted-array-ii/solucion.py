# 80. Remove Duplicates From Sorted Array II (Media)
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
#
# Idea: igual que la versión I, pero comparo contra el que está dos lugares atrás en la parte ya
#       armada: si es distinto, este número todavía no apareció dos veces.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for n in nums:
            if k < 2 or n != nums[k - 2]:
                nums[k] = n
                k += 1
        return k


if __name__ == "__main__":
    s = Solution()
    a = [1, 1, 1, 2, 2, 3]
    k = s.removeDuplicates(a)
    assert k == 5 and a[:k] == [1, 1, 2, 2, 3]
    a = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = s.removeDuplicates(a)
    assert k == 7 and a[:k] == [0, 0, 1, 1, 2, 3, 3]
    print("OK")
