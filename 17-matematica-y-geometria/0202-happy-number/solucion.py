# 202. Happy Number (Fácil)
# https://leetcode.com/problems/happy-number/
#
# Idea: aplico la operación una y otra vez; o llego a 1 o entro en un ciclo. Detecto el ciclo con
#       tortuga y liebre (Floyd), sin guardar los números vistos.
# Tiempo: O(log n) por paso; la cantidad de pasos es chica · Espacio: O(1)

class Solution:
    def isHappy(self, n: int) -> bool:
        def siguiente(x):
            return sum(int(d) ** 2 for d in str(x))

        lenta, rapida = n, siguiente(n)
        while rapida != 1 and lenta != rapida:
            lenta = siguiente(lenta)
            rapida = siguiente(siguiente(rapida))
        return rapida == 1


if __name__ == "__main__":
    s = Solution()
    assert s.isHappy(19) is True
    assert s.isHappy(2) is False
    assert s.isHappy(1) is True
    print("OK")
