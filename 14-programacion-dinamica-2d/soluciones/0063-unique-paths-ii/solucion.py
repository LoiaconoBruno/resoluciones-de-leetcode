# 63. Unique Paths II (Media)
# https://leetcode.com/problems/unique-paths-ii/
#
# Idea: igual que Unique Paths, pero una celda con obstáculo tiene 0 caminos.
# Tiempo: O(m · n) · Espacio: O(n)

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cols = len(obstacleGrid[0])
        fila = [0] * cols
        fila[0] = 1
        for obstaculos in obstacleGrid:
            for c in range(cols):
                if obstaculos[c]:
                    fila[c] = 0
                elif c > 0:
                    fila[c] += fila[c - 1]
        return fila[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert s.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
    assert s.uniquePathsWithObstacles([[1]]) == 0
    print("OK")
