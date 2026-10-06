# 881. Boats to Save People (Media)
# https://leetcode.com/problems/boats-to-save-people/
#
# Idea: ordeno; la persona más pesada sube siempre, y si entra con la más liviana, suben juntas (greedy con dos punteros).
# Tiempo: O(n log n) · Espacio: O(1) extra

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        izq, der = 0, len(people) - 1
        botes = 0
        while izq <= der:
            if people[izq] + people[der] <= limit:
                izq += 1
            der -= 1
            botes += 1
        return botes


if __name__ == "__main__":
    s = Solution()
    assert s.numRescueBoats([1, 2], 3) == 1
    assert s.numRescueBoats([3, 2, 2, 1], 3) == 3
    assert s.numRescueBoats([3, 5, 3, 4], 5) == 4
    print("OK")
