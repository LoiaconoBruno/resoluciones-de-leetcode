# 649. Dota2 Senate (Media)
# https://leetcode.com/problems/dota2-senate/
#
# Idea: dos colas con los turnos de cada partido. El senador que vota primero banea al próximo del
#       otro partido y vuelve a la fila para la ronda siguiente (su turno + n).
# Tiempo: O(n) · Espacio: O(n)

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque(i for i, c in enumerate(senate) if c == "R")
        dire = deque(i for i, c in enumerate(senate) if c == "D")
        while radiant and dire:
            r, d = radiant.popleft(), dire.popleft()
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        return "Radiant" if radiant else "Dire"


if __name__ == "__main__":
    s = Solution()
    assert s.predictPartyVictory("RD") == "Radiant"
    assert s.predictPartyVictory("RDD") == "Dire"
    assert s.predictPartyVictory("DDRRR") == "Dire"
    print("OK")
