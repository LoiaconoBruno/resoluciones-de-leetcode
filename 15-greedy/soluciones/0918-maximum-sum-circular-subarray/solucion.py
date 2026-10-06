# 918. Maximum Sum Circular Subarray (Media)
# https://leetcode.com/problems/maximum-sum-circular-subarray/
#
# Idea: el mejor subarray o no da la vuelta (Kadane normal) o da la vuelta, y en ese caso es el
#       total menos el subarray de suma mínima. Ojo: si todos son negativos, el segundo caso daría
#       el subarray vacío.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maximo = minimo = actual_max = actual_min = nums[0]
        for n in nums[1:]:
            actual_max = max(n, actual_max + n)
            actual_min = min(n, actual_min + n)
            maximo = max(maximo, actual_max)
            minimo = min(minimo, actual_min)
        if maximo < 0:
            return maximo
        return max(maximo, sum(nums) - minimo)


if __name__ == "__main__":
    s = Solution()
    assert s.maxSubarraySumCircular([1, -2, 3, -2]) == 3
    assert s.maxSubarraySumCircular([5, -3, 5]) == 10
    assert s.maxSubarraySumCircular([-3, -2, -3]) == -2
    print("OK")
