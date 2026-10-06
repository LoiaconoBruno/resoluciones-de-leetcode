# 62. Unique Paths (Media)
# https://leetcode.com/problems/unique-paths/
#
# Idea: a cada celda se llega desde arriba o desde la izquierda, así que caminos[f][c] = caminos de
#       arriba + caminos de la izquierda. Alcanza con una fila que voy actualizando.
# Tiempo: O(m · n) · Espacio: O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        fila = [1] * n
        for _ in range(m - 1):
            for c in range(1, n):
                fila[c] += fila[c - 1]
        return fila[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(3, 2) == 3
    assert s.uniquePaths(1, 1) == 1
    print("OK")
