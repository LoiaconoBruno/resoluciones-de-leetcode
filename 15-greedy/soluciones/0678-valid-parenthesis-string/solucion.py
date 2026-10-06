# 678. Valid Parenthesis String (Media)
# https://leetcode.com/problems/valid-parenthesis-string/
#
# Idea: llevo el rango posible de paréntesis abiertos [mínimo, máximo] tratando cada '*' como ')'
#       para el mínimo y como '(' para el máximo. Si el máximo baja de 0 es inválido; el mínimo
#       nunca baja de 0. Al final el mínimo tiene que ser 0.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def checkValidString(self, s: str) -> bool:
        minimo = maximo = 0
        for c in s:
            if c == "(":
                minimo += 1
                maximo += 1
            elif c == ")":
                minimo -= 1
                maximo -= 1
            else:
                minimo -= 1
                maximo += 1
            if maximo < 0:
                return False
            minimo = max(minimo, 0)
        return minimo == 0


if __name__ == "__main__":
    s = Solution()
    assert s.checkValidString("()") is True
    assert s.checkValidString("(*)") is True
    assert s.checkValidString("(*))") is True
    assert s.checkValidString(")(") is False
    assert s.checkValidString("(((*)") is False
    print("OK")
