# 1239. Maximum Length of a Concatenated String With Unique Characters (Media)
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
#
# Idea: me quedo solo con las palabras sin letras repetidas (como set de letras) y hago
#       backtracking: para cada palabra decido si la agrego, si no choca con las letras que ya
#       tengo.
# Tiempo: O(2^n · 26) · Espacio: O(n)

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        palabras = [set(p) for p in arr if len(set(p)) == len(p)]

        def mejor(i, letras):
            if i == len(palabras):
                return len(letras)
            res = mejor(i + 1, letras)
            if not letras & palabras[i]:
                res = max(res, mejor(i + 1, letras | palabras[i]))
            return res

        return mejor(0, set())


if __name__ == "__main__":
    s = Solution()
    assert s.maxLength(["un", "iq", "ue"]) == 4
    assert s.maxLength(["cha", "r", "act", "ers"]) == 6
    assert s.maxLength(["abcdefghijklmnopqrstuvwxyz"]) == 26
    assert s.maxLength(["aa", "bb"]) == 0
    print("OK")
