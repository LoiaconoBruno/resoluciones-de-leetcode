# 150. Evaluate Reverse Polish Notation (Media)
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
#
# Idea: los números van a la pila; cada operador saca los dos de arriba, opera (ojo con el orden:
#       primero sale el segundo operando) y apila el resultado.
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pila = []
        for t in tokens:
            if t in "+-*/":
                b, a = pila.pop(), pila.pop()
                if t == "+":
                    pila.append(a + b)
                elif t == "-":
                    pila.append(a - b)
                elif t == "*":
                    pila.append(a * b)
                else:
                    pila.append(int(a / b))
            else:
                pila.append(int(t))
        return pila[0]


if __name__ == "__main__":
    s = Solution()
    assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    print("OK")
