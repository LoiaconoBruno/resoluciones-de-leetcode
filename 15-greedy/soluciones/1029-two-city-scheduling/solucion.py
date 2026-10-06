# 1029. Two City Scheduling (Media)
# https://leetcode.com/problems/two-city-scheduling/
#
# Idea: ordeno por cuánto me ahorro mandando a cada persona a A en vez de a B (costA - costB); la
#       primera mitad va a A y el resto a B.
# Tiempo: O(n log n) · Espacio: O(1) extra

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda c: c[0] - c[1])
        mitad = len(costs) // 2
        return sum(a for a, _ in costs[:mitad]) + sum(b for _, b in costs[mitad:])


if __name__ == "__main__":
    s = Solution()
    assert s.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]) == 110
    assert s.twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]) == 1859
    assert s.twoCitySchedCost([[515, 563], [451, 713], [537, 709], [343, 819],
                               [855, 779], [457, 60], [650, 359], [631, 42]]) == 3086
    print("OK")
