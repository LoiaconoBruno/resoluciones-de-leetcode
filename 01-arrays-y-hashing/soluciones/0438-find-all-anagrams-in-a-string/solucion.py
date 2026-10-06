# 438. Find All Anagrams in a String (Media)
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
#
# Idea: ventana de largo fijo len(p) que se desliza sobre s; mantengo la cuenta de letras de la
#       ventana y la comparo con la de p.
# Tiempo: O(n · 26) · Espacio: O(1)

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        objetivo = [0] * 26
        ventana = [0] * 26
        for c in p:
            objetivo[ord(c) - 97] += 1
        res = []
        for i, c in enumerate(s):
            ventana[ord(c) - 97] += 1
            if i >= len(p):
                ventana[ord(s[i - len(p)]) - 97] -= 1
            if ventana == objetivo:
                res.append(i - len(p) + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert s.findAnagrams("abab", "ab") == [0, 1, 2]
    assert s.findAnagrams("a", "ab") == []
    print("OK")
