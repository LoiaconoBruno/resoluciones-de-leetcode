# 217. Contains Duplicate (Fácil)
# https://leetcode.com/problems/contains-duplicate/
#
# Idea: guardo en un set lo que ya vi; si un número aparece de nuevo, hay duplicado.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for n in nums:
            if n in vistos:
                return True
            vistos.add(n)
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) is True
    assert s.containsDuplicate([1, 2, 3, 4]) is False
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    print("OK")
