# 994. Rotting Oranges (Media)
# https://leetcode.com/problems/rotting-oranges/
#
# Idea: BFS que arranca desde todas las naranjas podridas a la vez; cada nivel del BFS es un minuto.
#       Al final, si queda alguna fresca, es imposible.
# Tiempo: O(f · c) · Espacio: O(f · c)

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        filas, cols = len(grid), len(grid[0])
        cola = deque()
        frescas = 0
        for f in range(filas):
            for c in range(cols):
                if grid[f][c] == 2:
                    cola.append((f, c))
                elif grid[f][c] == 1:
                    frescas += 1
        minutos = 0
        while cola and frescas:
            minutos += 1
            for _ in range(len(cola)):
                f, c = cola.popleft()
                for nf, nc in ((f + 1, c), (f - 1, c), (f, c + 1), (f, c - 1)):
                    if 0 <= nf < filas and 0 <= nc < cols and grid[nf][nc] == 1:
                        grid[nf][nc] = 2
                        frescas -= 1
                        cola.append((nf, nc))
        return -1 if frescas else minutos


if __name__ == "__main__":
    s = Solution()
    assert s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert s.orangesRotting([[0, 2]]) == 0
    print("OK")
