# 22. Generate Parentheses (Media)
# https://leetcode.com/problems/generate-parentheses/
#
# Idea: backtracking: puedo abrir mientras me queden aperturas y cerrar solo si hay más abiertos que
#       cerrados; así cada string que llega a 2n es válido.
# Tiempo: O(4^n / √n) (el número de Catalan) · Espacio: O(n) de recursión

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        actual = []

        def armar(abiertos, cerrados):
            if abiertos == cerrados == n:
                res.append("".join(actual))
                return
            if abiertos < n:
                actual.append("(")
                armar(abiertos + 1, cerrados)
                actual.pop()
            if cerrados < abiertos:
                actual.append(")")
                armar(abiertos, cerrados + 1)
                actual.pop()

        armar(0, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert s.generateParenthesis(1) == ["()"]
    print("OK")
