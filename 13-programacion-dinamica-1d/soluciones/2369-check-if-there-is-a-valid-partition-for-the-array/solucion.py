# 2369. Check if There is a Valid Partition For The Array (Media)
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
#
# Idea: dp[i] dice si los primeros i números se pueden partir bien; el último bloque son 2 iguales,
#       3 iguales o 3 consecutivos crecientes, así que miro dp[i - 2] y dp[i - 3].
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [True] + [False] * n
        for i in range(2, n + 1):
            a, b = nums[i - 2], nums[i - 1]
            if a == b and dp[i - 2]:
                dp[i] = True
            if i >= 3 and dp[i - 3]:
                x = nums[i - 3]
                if x == a == b or (a == x + 1 and b == x + 2):
                    dp[i] = True
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    assert s.validPartition([4, 4, 4, 5, 6]) is True
    assert s.validPartition([1, 1, 1, 2]) is False
    print("OK")
