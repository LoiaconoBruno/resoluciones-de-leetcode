# 665. Non Decreasing Array (Media)
# https://leetcode.com/problems/non-decreasing-array/
#
# Idea: al encontrar una bajada nums[i] < nums[i-1] la arreglo de la forma que menos molesta: bajo
#       nums[i-1] si puedo y, si no, subo nums[i]. Si hay dos bajadas, no se puede.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cambios = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                cambios += 1
                if cambios > 1:
                    return False
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.checkPossibility([4, 2, 3]) is True
    assert s.checkPossibility([4, 2, 1]) is False
    assert s.checkPossibility([3, 4, 2, 3]) is False
    assert s.checkPossibility([5, 7, 1, 8]) is True
    print("OK")
