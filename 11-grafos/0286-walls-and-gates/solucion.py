# 286. Walls And Gates (Media)
# https://www.lintcode.com/problem/663/
#
# Idea: BFS desde todas las puertas a la vez; la primera vez que llego a una habitación vacía, esa
#       es su distancia a la puerta más cercana.
# Tiempo: O(f · c) · Espacio: O(f · c)

from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        VACIO = 2147483647
        filas, cols = len(rooms), len(rooms[0])
        cola = deque((f, c) for f in range(filas) for c in range(cols) if rooms[f][c] == 0)
        while cola:
            f, c = cola.popleft()
            for nf, nc in ((f + 1, c), (f - 1, c), (f, c + 1), (f, c - 1)):
                if 0 <= nf < filas and 0 <= nc < cols and rooms[nf][nc] == VACIO:
                    rooms[nf][nc] = rooms[f][c] + 1
                    cola.append((nf, nc))


if __name__ == "__main__":
    INF = 2147483647
    s = Solution()
    cuartos = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]
    s.wallsAndGates(cuartos)
    assert cuartos == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
    print("OK")
