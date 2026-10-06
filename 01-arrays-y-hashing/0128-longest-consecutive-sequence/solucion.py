# 128. Longest Consecutive Sequence (Media)
# https://leetcode.com/problems/longest-consecutive-sequence/
#
# Idea: meto todo en un set; un número arranca una secuencia solo si n - 1 no está, y desde ahí
#       cuento hacia arriba.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numeros = set(nums)
        mejor = 0
        for n in numeros:
            if n - 1 not in numeros:
                largo = 1
                while n + largo in numeros:
                    largo += 1
                mejor = max(mejor, largo)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert s.longestConsecutive([]) == 0
    print("OK")
