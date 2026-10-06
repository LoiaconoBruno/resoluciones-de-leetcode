# 682. Baseball Game (Fácil)
# https://leetcode.com/problems/baseball-game/
#
# Idea: simulo con una pila de puntajes: un número se apila, "C" saca el último, "D" apila el doble y "+" la suma de los dos de arriba.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        pila = []
        for op in operations:
            if op == "C":
                pila.pop()
            elif op == "D":
                pila.append(2 * pila[-1])
            elif op == "+":
                pila.append(pila[-1] + pila[-2])
            else:
                pila.append(int(op))
        return sum(pila)


if __name__ == "__main__":
    s = Solution()
    assert s.calPoints(["5", "2", "C", "D", "+"]) == 30
    assert s.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
    assert s.calPoints(["1", "C"]) == 0
    print("OK")
