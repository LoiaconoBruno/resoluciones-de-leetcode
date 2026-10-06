# 253. Meeting Rooms II (Media)
# https://www.lintcode.com/problem/919/
#
# Idea: separo inicios y finales y los ordeno; recorro los inicios y, por cada uno, libero las salas
#       de las reuniones que ya terminaron. El máximo de salas ocupadas a la vez es la respuesta.
# Tiempo: O(n log n) · Espacio: O(n)

from typing import List


# LintCode usa esta clase para los intervalos (en LeetCode vienen como listas [inicio, fin]).
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        inicios = sorted(i.start for i in intervals)
        finales = sorted(i.end for i in intervals)
        ocupadas = mejor = 0
        j = 0
        for inicio in inicios:
            while finales[j] <= inicio:
                ocupadas -= 1
                j += 1
            ocupadas += 1
            mejor = max(mejor, ocupadas)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]) == 2
    assert s.minMeetingRooms([Interval(2, 7)]) == 1
    assert s.minMeetingRooms([Interval(0, 8), Interval(8, 10)]) == 1
    assert s.minMeetingRooms([]) == 0
    print("OK")
