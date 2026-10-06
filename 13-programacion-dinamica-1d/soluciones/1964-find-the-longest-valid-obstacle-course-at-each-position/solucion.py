# 1964. Find the Longest Valid Obstacle Course at Each Position (Difícil)
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
#
# Idea: es la subsecuencia no decreciente más larga que termina en cada posición. Como en LIS con
#       búsqueda binaria, pero uso bisect_right (se permiten iguales) y guardo la posición donde cae
#       cada obstáculo.
# Tiempo: O(n log n) · Espacio: O(n)

from bisect import bisect_right
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        colas = []
        res = []
        for o in obstacles:
            i = bisect_right(colas, o)
            if i == len(colas):
                colas.append(o)
            else:
                colas[i] = o
            res.append(i + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.longestObstacleCourseAtEachPosition([1, 2, 3, 2]) == [1, 2, 3, 3]
    assert s.longestObstacleCourseAtEachPosition([2, 2, 1]) == [1, 2, 1]
    assert s.longestObstacleCourseAtEachPosition([3, 1, 5, 6, 4, 2]) == [1, 1, 2, 3, 2, 2]
    print("OK")
