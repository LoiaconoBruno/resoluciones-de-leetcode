# 1898. Maximum Number of Removable Characters (Media)
# https://leetcode.com/problems/maximum-number-of-removable-characters/
#
# Idea: si puedo sacar k caracteres, también puedo sacar menos; eso permite búsqueda binaria sobre
#       k, chequeando cada vez si p sigue siendo subsecuencia.
# Tiempo: O(n log n) · Espacio: O(n)

from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def sigue_siendo_subsecuencia(k):
            sacados = set(removable[:k])
            j = 0
            for i, c in enumerate(s):
                if i not in sacados and j < len(p) and c == p[j]:
                    j += 1
            return j == len(p)

        izq, der = 0, len(removable)
        while izq < der:
            k = (izq + der + 1) // 2
            if sigue_siendo_subsecuencia(k):
                izq = k
            else:
                der = k - 1
        return izq


if __name__ == "__main__":
    s = Solution()
    assert s.maximumRemovals("abcacb", "ab", [3, 1, 0]) == 2
    assert s.maximumRemovals("abcbddddd", "abcd", [3, 2, 1, 4, 5, 6]) == 1
    assert s.maximumRemovals("abcab", "abc", [0, 1, 2, 3, 4]) == 0
    print("OK")
