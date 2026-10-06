# 134. Gas Station (Media)
# https://leetcode.com/problems/gas-station/
#
# Idea: si el total de nafta alcanza para el total de costo, hay solución. Recorro sumando gas -
#       cost; si el tanque queda negativo, ninguna estación hasta acá sirve como inicio y arranco de
#       nuevo desde la siguiente.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tanque = inicio = 0
        for i in range(len(gas)):
            tanque += gas[i] - cost[i]
            if tanque < 0:
                tanque = 0
                inicio = i + 1
        return inicio


if __name__ == "__main__":
    s = Solution()
    assert s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert s.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
    print("OK")
