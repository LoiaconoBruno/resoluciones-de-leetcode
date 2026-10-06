# 472. Concatenated Words (Difícil)
# https://leetcode.com/problems/concatenated-words/
#
# Idea: para cada palabra hago Word Break contra el set de palabras, sin permitir que la palabra
#       entera se use a sí misma (así hacen falta al menos dos pedazos).
# Tiempo: O(n · L³), con L el largo de las palabras (por los cortes) · Espacio: O(n · L)

from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        palabras = set(w for w in words if w)
        res = []
        for w in words:
            largo = len(w)
            if not largo:
                continue
            dp = [True] + [False] * largo
            for i in range(1, largo + 1):
                for j in range(i):
                    if dp[j] and w[j:i] in palabras and not (j == 0 and i == largo):
                        dp[i] = True
                        break
            if dp[largo]:
                res.append(w)
        return res


if __name__ == "__main__":
    s = Solution()
    palabras = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    assert sorted(s.findAllConcatenatedWordsInADict(palabras)) == ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
    assert s.findAllConcatenatedWordsInADict(["cat", "dog", "catdog"]) == ["catdog"]
    print("OK")
