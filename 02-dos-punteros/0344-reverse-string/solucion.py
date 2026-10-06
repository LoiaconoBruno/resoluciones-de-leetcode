# 344. Reverse String (Fácil)
# https://leetcode.com/problems/reverse-string/
#
# Idea: intercambio las puntas y voy cerrando hacia el medio.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        izq, der = 0, len(s) - 1
        while izq < der:
            s[izq], s[der] = s[der], s[izq]
            izq += 1
            der -= 1


if __name__ == "__main__":
    s = Solution()
    texto = list("hello")
    s.reverseString(texto)
    assert texto == list("olleh")
    texto = list("Hannah")
    s.reverseString(texto)
    assert texto == list("hannaH")
    print("OK")
