# 12. Integer to Roman (Media)
# https://leetcode.com/problems/integer-to-roman/
#
# Idea: tabla de valores de mayor a menor que incluye los casos de resta (CM, CD, XC, XL, IX, IV);
#       mientras el número alcance, uso el símbolo más grande posible.
# Tiempo: O(1) (el número está acotado) · Espacio: O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        simbolos = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                    (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        res = []
        for valor, simbolo in simbolos:
            veces, num = divmod(num, valor)
            res.append(simbolo * veces)
        return "".join(res)


if __name__ == "__main__":
    s = Solution()
    assert s.intToRoman(3749) == "MMMDCCXLIX"
    assert s.intToRoman(58) == "LVIII"
    assert s.intToRoman(1994) == "MCMXCIV"
    print("OK")
