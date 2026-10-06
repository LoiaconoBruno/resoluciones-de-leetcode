# 367. Valid Perfect Square (Fácil)
# https://leetcode.com/problems/valid-perfect-square/
#
# Idea: búsqueda binaria de un r con r · r == num, sin usar raíz cuadrada.
# Tiempo: O(log n) · Espacio: O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        izq, der = 1, num
        while izq <= der:
            r = (izq + der) // 2
            if r * r == num:
                return True
            if r * r < num:
                izq = r + 1
            else:
                der = r - 1
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.isPerfectSquare(16) is True
    assert s.isPerfectSquare(14) is False
    assert s.isPerfectSquare(1) is True
    print("OK")
