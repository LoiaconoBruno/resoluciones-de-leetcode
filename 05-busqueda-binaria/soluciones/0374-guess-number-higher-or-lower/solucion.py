# 374. Guess Number Higher Or Lower (Fácil)
# https://leetcode.com/problems/guess-number-higher-or-lower/
#
# Idea: búsqueda binaria entre 1 y n usando la respuesta de guess para saber hacia qué lado seguir.
# Tiempo: O(log n) · Espacio: O(1)

# LeetCode ya trae definida guess(num): devuelve -1 si num es mayor que el elegido,
# 1 si es menor y 0 si acertaste. Abajo hay una versión para probar localmente.


class Solution:
    def guessNumber(self, n: int) -> int:
        izq, der = 1, n
        while True:
            medio = (izq + der) // 2
            r = guess(medio)
            if r == 0:
                return medio
            if r < 0:
                der = medio - 1
            else:
                izq = medio + 1


if __name__ == "__main__":
    def guess(num: int) -> int:
        if num > ELEGIDO:
            return -1
        return 1 if num < ELEGIDO else 0

    s = Solution()
    for n, ELEGIDO in ((10, 6), (1, 1), (2, 1), (2, 2), (2 ** 31 - 1, 1702766719)):
        assert s.guessNumber(n) == ELEGIDO
    print("OK")
