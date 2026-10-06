# 209. Minimum Size Subarray Sum (Media)
# https://leetcode.com/problems/minimum-size-subarray-sum/
#
# Idea: agrando la ventana sumando; mientras la suma llegue a target, guardo el largo y achico desde la izquierda.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        izq = suma = 0
        mejor = float("inf")
        for der, n in enumerate(nums):
            suma += n
            while suma >= target:
                mejor = min(mejor, der - izq + 1)
                suma -= nums[izq]
                izq += 1
        return 0 if mejor == float("inf") else mejor


if __name__ == "__main__":
    s = Solution()
    assert s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert s.minSubArrayLen(4, [1, 4, 4]) == 1
    assert s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    print("OK")
