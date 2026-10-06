# 168. Excel Sheet Column Title (Fácil)
# https://leetcode.com/problems/excel-sheet-column-title/
#
# Idea: es pasar a base 26, pero sin cero (las letras van de 1 a 26); por eso resto 1 antes de cada
#       división.
# Tiempo: O(log n) · Espacio: O(log n)

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letras = []
        while columnNumber:
            columnNumber, resto = divmod(columnNumber - 1, 26)
            letras.append(chr(ord("A") + resto))
        return "".join(reversed(letras))


if __name__ == "__main__":
    s = Solution()
    assert s.convertToTitle(1) == "A"
    assert s.convertToTitle(28) == "AB"
    assert s.convertToTitle(701) == "ZY"
    assert s.convertToTitle(26) == "Z"
    print("OK")
