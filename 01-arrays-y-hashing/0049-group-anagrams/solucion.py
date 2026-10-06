# 49. Group Anagrams (Media)
# https://leetcode.com/problems/group-anagrams/
#
# Idea: dos anagramas tienen la misma cuenta de letras; uso esa cuenta (26 números) como clave de un
#       diccionario.
# Tiempo: O(n · k), con k el largo de la palabra más larga · Espacio: O(n · k)

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos = defaultdict(list)
        for palabra in strs:
            cuenta = [0] * 26
            for c in palabra:
                cuenta[ord(c) - ord("a")] += 1
            grupos[tuple(cuenta)].append(palabra)
        return list(grupos.values())


if __name__ == "__main__":
    s = Solution()

    def normalizar(grupos):
        return sorted(sorted(g) for g in grupos)

    assert normalizar(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == \
        normalizar([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"]) == [["a"]]
    print("OK")
