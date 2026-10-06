# 252. Meeting Rooms (Fácil)
# https://www.lintcode.com/problem/920/
#
# Idea: ordeno las reuniones por hora de inicio; si alguna empieza antes de que termine la anterior,
#       se pisan y no puedo ir a todas.
# Tiempo: O(n log n) · Espacio: O(1) extra

from typing import List


# LintCode usa esta clase para los intervalos (en LeetCode vienen como listas [inicio, fin]).
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for anterior, actual in zip(intervals, intervals[1:]):
            if actual.start < anterior.end:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.canAttendMeetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)]) is False
    assert s.canAttendMeetings([Interval(5, 8), Interval(9, 15)]) is True
    assert s.canAttendMeetings([Interval(0, 8), Interval(8, 10)]) is True
    print("OK")
