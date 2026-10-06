# 1343. Number of Sub Arrays of Size K and Avg Greater than or Equal to Threshold (Media)
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
#
# Idea: ventana fija de k: sumo el que entra, resto el que sale y comparo la suma contra k ·
#       threshold (así evito dividir).
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        minimo = k * threshold
        suma = res = 0
        for i, n in enumerate(arr):
            suma += n
            if i >= k:
                suma -= arr[i - k]
            if i >= k - 1 and suma >= minimo:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4) == 3
    assert s.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5) == 6
    print("OK")
