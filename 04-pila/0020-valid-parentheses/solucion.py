# 20. Valid Parentheses (Fácil)
# https://leetcode.com/problems/valid-parentheses/
#
# Idea: apilo los que abren; cada uno que cierra tiene que coincidir con el que está arriba de la pila. Al final la pila tiene que quedar vacía.
# Tiempo: O(n) · Espacio: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        pareja = {")": "(", "]": "[", "}": "{"}
        pila = []
        for c in s:
            if c in pareja:
                if not pila or pila.pop() != pareja[c]:
                    return False
            else:
                pila.append(c)
        return not pila


if __name__ == "__main__":
    s = Solution()
    assert s.isValid("()") is True
    assert s.isValid("()[]{}") is True
    assert s.isValid("(]") is False
    assert s.isValid("([])") is True
    assert s.isValid("([)]") is False
    assert s.isValid("]") is False
    print("OK")
