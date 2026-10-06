# 377. Combination Sum IV (Media)
# https://leetcode.com/problems/combination-sum-iv/
#
# Idea: dp[t] = cantidad de secuencias (importa el orden) que suman t; para cada t pruebo cuál fue
#       el último número: dp[t] = suma de dp[t - n].
# Tiempo: O(target · n) · Espacio: O(target)

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for t in range(1, target + 1):
            for n in nums:
                if n <= t:
                    dp[t] += dp[t - n]
        return dp[target]


if __name__ == "__main__":
    s = Solution()
    assert s.combinationSum4([1, 2, 3], 4) == 7
    assert s.combinationSum4([9], 3) == 0
    print("OK")
