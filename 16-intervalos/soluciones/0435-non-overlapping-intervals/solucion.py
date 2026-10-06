# 435. Non Overlapping Intervals (Media)
# https://leetcode.com/problems/non-overlapping-intervals/
#
# Idea: quiero quedarme con la mayor cantidad de intervalos sin solaparse: ordeno por final y elijo
#       siempre el que termina primero (deja más lugar). Los que no entran son los que borro.
# Tiempo: O(n log n) · Espacio: O(1) extra

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])
        borrados = 0
        ultimo_fin = float("-inf")
        for inicio, fin in intervals:
            if inicio >= ultimo_fin:
                ultimo_fin = fin
            else:
                borrados += 1
        return borrados


if __name__ == "__main__":
    s = Solution()
    assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    print("OK")
