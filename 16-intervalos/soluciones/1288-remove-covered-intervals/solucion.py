# 1288. Remove Covered Intervals (Media)
# https://leetcode.com/problems/remove-covered-intervals/
#
# Idea: ordeno por inicio y, a igual inicio, el más largo primero; así un intervalo está cubierto si
#       su final no supera el mayor final visto hasta ahora.
# Tiempo: O(n log n) · Espacio: O(1) extra

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: (i[0], -i[1]))
        quedan = 0
        mayor_fin = 0
        for _, fin in intervals:
            if fin > mayor_fin:
                quedan += 1
                mayor_fin = fin
        return quedan


if __name__ == "__main__":
    s = Solution()
    assert s.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]) == 2
    assert s.removeCoveredIntervals([[1, 4], [2, 3]]) == 1
    assert s.removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]) == 1
    print("OK")
