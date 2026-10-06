# 57. Insert Interval (Media)
# https://leetcode.com/problems/insert-interval/
#
# Idea: recorro los intervalos: los que terminan antes del nuevo van tal cual, los que se pisan con
#       él los fusiono (estirando el nuevo) y, cuando aparece uno que empieza después, agrego el
#       nuevo y el resto.
# Tiempo: O(n) · Espacio: O(n) (la respuesta)

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inicio, fin = newInterval
        for i, (a, b) in enumerate(intervals):
            if b < inicio:
                res.append([a, b])
            elif fin < a:
                return res + [[inicio, fin]] + intervals[i:]
            else:
                inicio, fin = min(inicio, a), max(fin, b)
        res.append([inicio, fin])
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert s.insert([], [5, 7]) == [[5, 7]]
    assert s.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    print("OK")
