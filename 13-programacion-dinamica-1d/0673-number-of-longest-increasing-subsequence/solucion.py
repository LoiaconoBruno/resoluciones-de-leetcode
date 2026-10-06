# 673. Number of Longest Increasing Subsequence (Media)
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
#
# Idea: para cada posición guardo el largo de la LIS que termina ahí y cuántas hay de ese largo; al
#       combinar con un j anterior más chico, si mejora el largo heredo su cuenta y si empata la
#       sumo.
# Tiempo: O(n²) · Espacio: O(n)

from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        largo = [1] * n
        cuenta = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if largo[j] + 1 > largo[i]:
                        largo[i], cuenta[i] = largo[j] + 1, cuenta[j]
                    elif largo[j] + 1 == largo[i]:
                        cuenta[i] += cuenta[j]
        maximo = max(largo)
        return sum(c for l, c in zip(largo, cuenta) if l == maximo)


if __name__ == "__main__":
    s = Solution()
    assert s.findNumberOfLIS([1, 3, 5, 4, 7]) == 2
    assert s.findNumberOfLIS([2, 2, 2, 2, 2]) == 5
    print("OK")
