# 1984. Minimum Difference Between Highest And Lowest of K Scores (Fácil)
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
#
# Idea: ordeno; los k elegidos conviene que sean consecutivos, así que deslizo una ventana de k y miro último - primero.
# Tiempo: O(n log n) · Espacio: O(1) extra

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))


if __name__ == "__main__":
    s = Solution()
    assert s.minimumDifference([90], 1) == 0
    assert s.minimumDifference([9, 4, 1, 7], 2) == 2
    print("OK")
