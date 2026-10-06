# 978. Longest Turbulent Array (Media)
# https://leetcode.com/problems/longest-turbulent-subarray/
#
# Idea: recorro las comparaciones entre vecinos; mientras el signo vaya alternando, la racha crece.
#       Si se repite el signo, la racha vuelve a 2, y si son iguales, vuelve a 1.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        mejor = racha = 1
        signo_anterior = 0
        for i in range(1, len(arr)):
            signo = (arr[i] > arr[i - 1]) - (arr[i] < arr[i - 1])
            if signo == 0:
                racha = 1
            elif signo == -signo_anterior:
                racha += 1
            else:
                racha = 2
            signo_anterior = signo
            mejor = max(mejor, racha)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5
    assert s.maxTurbulenceSize([4, 8, 12, 16]) == 2
    assert s.maxTurbulenceSize([100]) == 1
    print("OK")
