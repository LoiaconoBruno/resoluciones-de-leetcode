# 1020. Number of Enclaves (Media)
# https://leetcode.com/problems/number-of-enclaves/
#
# Idea: hundo la tierra que toca el borde (desde ahí se puede salir caminando); la tierra que queda
#       son los enclaves y la cuento.
# Tiempo: O(f · c) · Espacio: O(f · c)

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        filas, cols = len(grid), len(grid[0])
        pila = [(f, c) for f in range(filas) for c in range(cols) if f in (0, filas - 1) or c in (0, cols - 1)]
        while pila:
            f, c = pila.pop()
            if 0 <= f < filas and 0 <= c < cols and grid[f][c] == 1:
                grid[f][c] = 0
                pila.extend(((f + 1, c), (f - 1, c), (f, c + 1), (f, c - 1)))
        return sum(map(sum, grid))


if __name__ == "__main__":
    s = Solution()
    assert s.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 3
    assert s.numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) == 0
    print("OK")
