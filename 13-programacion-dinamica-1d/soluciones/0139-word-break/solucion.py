# 139. Word Break (Media)
# https://leetcode.com/problems/word-break/
#
# Idea: dp[i] dice si s[:i] se puede armar con el diccionario: es cierto si para algún j, dp[j] es
#       cierto y s[j:i] es una palabra.
# Tiempo: O(n² · m), con m el largo de la palabra (por cortar el string) · Espacio: O(n)

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        palabras = set(wordDict)
        largos = {len(p) for p in palabras}
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            dp[i] = any(dp[i - largo] and s[i - largo:i] in palabras for largo in largos if largo <= i)
        return dp[len(s)]


if __name__ == "__main__":
    s = Solution()
    assert s.wordBreak("leetcode", ["leet", "code"]) is True
    assert s.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    print("OK")
