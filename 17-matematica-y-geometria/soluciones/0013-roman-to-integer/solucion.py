# 13. Roman to Integer (Fácil)
# https://leetcode.com/problems/roman-to-integer/
#
# Idea: sumo el valor de cada símbolo, salvo cuando un símbolo es menor que el que le sigue (IV, IX,
#       XC...): en ese caso se resta.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        valor = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i, c in enumerate(s):
            if i + 1 < len(s) and valor[c] < valor[s[i + 1]]:
                total -= valor[c]
            else:
                total += valor[c]
        return total


if __name__ == "__main__":
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    print("OK")
