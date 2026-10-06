# 27. Remove Element (Fácil)
# https://leetcode.com/problems/remove-element/
#
# Idea: un puntero k marca dónde va el próximo número que se queda; copio ahí todo lo que no sea
#       val.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for n in nums:
            if n != val:
                nums[k] = n
                k += 1
        return k


if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 2, 3]
    k = s.removeElement(nums, 3)
    assert k == 2 and sorted(nums[:k]) == [2, 2]
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = s.removeElement(nums, 2)
    assert k == 5 and sorted(nums[:k]) == [0, 0, 1, 3, 4]
    print("OK")
