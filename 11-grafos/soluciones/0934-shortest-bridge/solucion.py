# 934. Shortest Bridge (Media)
# https://leetcode.com/problems/shortest-bridge/
#
# Idea: con un DFS marco toda la primera isla y la uso como punto de partida de un BFS por el agua;
#       el primer nivel en el que toco la otra isla es la cantidad de celdas a rellenar.
# Tiempo: O(n²) · Espacio: O(n²)

from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        inicio = next((f, c) for f in range(n) for c in range(n) if grid[f][c] == 1)
        grid[inicio[0]][inicio[1]] = 2
        pila = [inicio]
        cola = deque()
        while pila:
            f, c = pila.pop()
            cola.append((f, c))
            for nf, nc in ((f + 1, c), (f - 1, c), (f, c + 1), (f, c - 1)):
                if 0 <= nf < n and 0 <= nc < n and grid[nf][nc] == 1:
                    grid[nf][nc] = 2
                    pila.append((nf, nc))
        pasos = 0
        while cola:
            for _ in range(len(cola)):
                f, c = cola.popleft()
                for nf, nc in ((f + 1, c), (f - 1, c), (f, c + 1), (f, c - 1)):
                    if 0 <= nf < n and 0 <= nc < n:
                        if grid[nf][nc] == 1:
                            return pasos
                        if grid[nf][nc] == 0:
                            grid[nf][nc] = 2
                            cola.append((nf, nc))
            pasos += 1
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.shortestBridge([[0, 1], [1, 0]]) == 1
    assert s.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]) == 2
    assert s.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 1
    print("OK")
