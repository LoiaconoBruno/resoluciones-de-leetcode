# 200. Number of Islands (Media)
# https://leetcode.com/problems/number-of-islands/
#
# Idea: recorro la grilla; cada '1' que no visité es una isla nueva, y con un DFS (pila) hundo toda
#       esa isla para no contarla de nuevo.
# Tiempo: O(f · c) · Espacio: O(f · c)

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        filas, cols = len(grid), len(grid[0])
        islas = 0
        for f in range(filas):
            for c in range(cols):
                if grid[f][c] != "1":
                    continue
                islas += 1
                grid[f][c] = "0"
                pila = [(f, c)]
                while pila:
                    i, j = pila.pop()
                    for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= ni < filas and 0 <= nj < cols and grid[ni][nj] == "1":
                            grid[ni][nj] = "0"
                            pila.append((ni, nj))
        return islas


if __name__ == "__main__":
    s = Solution()
    assert s.numIslands([list("11110"), list("11010"), list("11000"), list("00000")]) == 1
    assert s.numIslands([list("11000"), list("11000"), list("00100"), list("00011")]) == 3
    print("OK")
