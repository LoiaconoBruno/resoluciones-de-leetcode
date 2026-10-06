# 2017. Grid Game (Media)
# https://leetcode.com/problems/grid-game/
#
# Idea: el robot 1 baja en alguna columna i; al robot 2 le queda lo mejor entre lo de arriba a la
#       derecha de i y lo de abajo a la izquierda de i. Pruebo cada i con sumas prefijas y minimizo.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        arriba = sum(grid[0])
        abajo = 0
        res = float("inf")
        for i in range(len(grid[0])):
            arriba -= grid[0][i]
            res = min(res, max(arriba, abajo))
            abajo += grid[1][i]
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.gridGame([[2, 5, 4], [1, 5, 1]]) == 4
    assert s.gridGame([[3, 3, 1], [8, 5, 2]]) == 4
    assert s.gridGame([[1, 3, 1, 15], [1, 3, 3, 1]]) == 7
    print("OK")
