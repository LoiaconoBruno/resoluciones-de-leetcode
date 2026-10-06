# 56. Merge Intervals (Media)
# https://leetcode.com/problems/merge-intervals/
#
# Idea: ordeno por inicio; si un intervalo empieza antes de que termine el último que guardé, los
#       fusiono estirando el final; si no, empieza uno nuevo.
# Tiempo: O(n log n) · Espacio: O(n)

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0][:]]
        for inicio, fin in intervals[1:]:
            if inicio <= res[-1][1]:
                res[-1][1] = max(res[-1][1], fin)
            else:
                res.append([inicio, fin])
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert s.merge([[1, 4], [2, 3]]) == [[1, 4]]
    print("OK")
