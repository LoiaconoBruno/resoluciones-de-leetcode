# 52. N Queens II (Difícil)
# https://leetcode.com/problems/n-queens-ii/
#
# Idea: lo mismo que N-Queens pero solo cuento: una reina por fila y tres sets (columnas, diagonales
#       y antidiagonales) para saber qué casillas están atacadas.
# Tiempo: O(n!) · Espacio: O(n)

class Solution:
    def totalNQueens(self, n: int) -> int:
        columnas, diagonales, antidiagonales = set(), set(), set()

        def contar(f):
            if f == n:
                return 1
            total = 0
            for c in range(n):
                if c in columnas or f - c in diagonales or f + c in antidiagonales:
                    continue
                columnas.add(c)
                diagonales.add(f - c)
                antidiagonales.add(f + c)
                total += contar(f + 1)
                columnas.remove(c)
                diagonales.remove(f - c)
                antidiagonales.remove(f + c)
            return total

        return contar(0)


if __name__ == "__main__":
    s = Solution()
    assert s.totalNQueens(4) == 2
    assert s.totalNQueens(1) == 1
    assert s.totalNQueens(8) == 92
    print("OK")
