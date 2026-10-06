# 2483. Minimum Penalty for a Shop (Media)
# https://leetcode.com/problems/minimum-penalty-for-a-shop/
#
# Idea: si cierro a la hora 0 la penalidad es la cantidad de 'Y'; al correr el cierre una hora, una 'Y' resta 1 y una 'N' suma 1. Me quedo con la primera hora de penalidad mínima.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalidad = customers.count("Y")
        minima, mejor_hora = penalidad, 0
        for i, c in enumerate(customers):
            penalidad += -1 if c == "Y" else 1
            if penalidad < minima:
                minima, mejor_hora = penalidad, i + 1
        return mejor_hora


if __name__ == "__main__":
    s = Solution()
    assert s.bestClosingTime("YYNY") == 2
    assert s.bestClosingTime("NNNNN") == 0
    assert s.bestClosingTime("YYYY") == 4
    print("OK")
