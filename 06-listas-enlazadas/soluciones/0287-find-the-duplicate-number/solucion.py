# 287. Find The Duplicate Number (Media)
# https://leetcode.com/problems/find-the-duplicate-number/
#
# Idea: veo el array como una lista enlazada (i -> nums[i]); el número repetido es la entrada de un
#       ciclo, y lo encuentro con Floyd: primero el encuentro y después avanzo desde el inicio a la
#       par.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lenta = rapida = 0
        while True:
            lenta = nums[lenta]
            rapida = nums[nums[rapida]]
            if lenta == rapida:
                break
        otra = 0
        while otra != lenta:
            otra = nums[otra]
            lenta = nums[lenta]
        return lenta


if __name__ == "__main__":
    s = Solution()
    assert s.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert s.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert s.findDuplicate([3, 3, 3, 3, 3]) == 3
    print("OK")
