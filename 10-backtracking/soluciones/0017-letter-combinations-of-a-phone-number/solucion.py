# 17. Letter Combinations of a Phone Number (Media)
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#
# Idea: cada dígito es una decisión entre sus 3 o 4 letras; backtracking que elige una letra por
#       dígito y arma todas las combinaciones.
# Tiempo: O(n · 4^n) · Espacio: O(n) de recursión

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        teclas = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                  "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        def armar(i, actual):
            if i == len(digits):
                res.append(actual)
                return
            for letra in teclas[digits[i]]:
                armar(i + 1, actual + letra)

        armar(0, "")
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert s.letterCombinations("") == []
    assert s.letterCombinations("2") == ["a", "b", "c"]
    print("OK")
