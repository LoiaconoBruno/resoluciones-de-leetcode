# 1260. Shift 2D Grid (Fácil)
# https://leetcode.com/problems/shift-2d-grid/
#
# Idea: si aplano la grilla en una lista, mover k veces es rotar la lista k lugares; la celda en
#       posición i (aplanada) va a la (i + k) % total.
# Tiempo: O(f · c) · Espacio: O(f · c)

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        filas, cols = len(grid), len(grid[0])
        total = filas * cols
        res = [[0] * cols for _ in range(filas)]
        for i in range(total):
            destino = (i + k) % total
            res[destino // cols][destino % cols] = grid[i // cols][i % cols]
        return res


if __name__ == "__main__":
    s = Solution()
    g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert s.shiftGrid(g, 1) == [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
    assert s.shiftGrid(g, 9) == g
    assert s.shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4) == \
        [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]
    print("OK")
