# 752. Open The Lock (Media)
# https://leetcode.com/problems/open-the-lock/
#
# Idea: BFS sobre las 10.000 combinaciones: desde cada una hay 8 vecinas (cada rueda +1 o -1). Las
#       combinaciones prohibidas las marco como visitadas desde el principio.
# Tiempo: O(10^4 · 8) · Espacio: O(10^4)

from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        vistos = set(deadends)
        if "0000" in vistos:
            return -1
        vistos.add("0000")
        cola = deque([("0000", 0)])
        while cola:
            combinacion, giros = cola.popleft()
            if combinacion == target:
                return giros
            for i in range(4):
                digito = int(combinacion[i])
                for cambio in (1, -1):
                    nueva = combinacion[:i] + str((digito + cambio) % 10) + combinacion[i + 1:]
                    if nueva not in vistos:
                        vistos.add(nueva)
                        cola.append((nueva, giros + 1))
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6
    assert s.openLock(["8888"], "0009") == 1
    assert s.openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888") == -1
    assert s.openLock(["0000"], "8888") == -1
    print("OK")
