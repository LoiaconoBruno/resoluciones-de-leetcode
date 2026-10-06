# 1838. Frequency of The Most Frequent Element (Media)
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/
#
# Idea: ordeno; en una ventana llevo todos al valor del máximo nums[der], y eso cuesta nums[der] ·
#       largo - suma. Si el costo pasa k, achico desde la izquierda.
# Tiempo: O(n log n) · Espacio: O(1) extra

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        izq = suma = mejor = 0
        for der, n in enumerate(nums):
            suma += n
            while n * (der - izq + 1) - suma > k:
                suma -= nums[izq]
                izq += 1
            mejor = max(mejor, der - izq + 1)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.maxFrequency([1, 2, 4], 5) == 3
    assert s.maxFrequency([1, 4, 8, 13], 5) == 2
    assert s.maxFrequency([3, 9, 6], 2) == 1
    print("OK")
