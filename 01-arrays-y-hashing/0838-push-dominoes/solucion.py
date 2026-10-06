# 838. Push Dominoes (Media)
# https://leetcode.com/problems/push-dominoes/
#
# Idea: calculo una "fuerza" por posición: de izquierda a derecha la de cada 'R' (que se gasta con la distancia) y de derecha a izquierda la de cada 'L'; gana la más fuerte.
# Tiempo: O(n) · Espacio: O(n)

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        fuerza = [0] * n
        f = 0
        for i, c in enumerate(dominoes):
            if c == "R":
                f = n
            elif c == "L":
                f = 0
            else:
                f = max(f - 1, 0)
            fuerza[i] += f
        f = 0
        for i in range(n - 1, -1, -1):
            c = dominoes[i]
            if c == "L":
                f = n
            elif c == "R":
                f = 0
            else:
                f = max(f - 1, 0)
            fuerza[i] -= f
        return "".join("R" if x > 0 else "L" if x < 0 else "." for x in fuerza)


if __name__ == "__main__":
    s = Solution()
    assert s.pushDominoes("RR.L") == "RR.L"
    assert s.pushDominoes(".L.R...LR..L..") == "LL.RR.LLRRLL.."
    print("OK")
