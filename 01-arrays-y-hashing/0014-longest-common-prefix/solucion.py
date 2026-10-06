# 14. Longest Common Prefix (Fácil)
# https://leetcode.com/problems/longest-common-prefix/
#
# Idea: comparo columna por columna contra la primera palabra; corto en la primera letra que no coincide o cuando una palabra se termina.
# Tiempo: O(n · m), con m el largo del prefijo · Espacio: O(1)

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        primera = strs[0]
        for i, c in enumerate(primera):
            for palabra in strs[1:]:
                if i == len(palabra) or palabra[i] != c:
                    return primera[:i]
        return primera


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert s.longestCommonPrefix(["ab", "a"]) == "a"
    print("OK")
