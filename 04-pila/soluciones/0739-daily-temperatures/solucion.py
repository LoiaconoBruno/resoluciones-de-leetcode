# 739. Daily Temperatures (Media)
# https://leetcode.com/problems/daily-temperatures/
#
# Idea: pila de índices de días que todavía esperan un día más cálido (temperaturas decrecientes);
#       cuando llega uno más caliente, resuelve a todos los más fríos de arriba.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        pila = []
        for i, t in enumerate(temperatures):
            while pila and temperatures[pila[-1]] < t:
                j = pila.pop()
                res[j] = i - j
            pila.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert s.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert s.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
    print("OK")
