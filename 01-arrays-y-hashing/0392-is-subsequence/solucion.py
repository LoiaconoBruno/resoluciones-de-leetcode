# 392. Is Subsequence (Fácil)
# https://leetcode.com/problems/is-subsequence/
#
# Idea: un puntero en s y otro en t; avanzo siempre en t y solo avanzo en s cuando las letras coinciden.
# Tiempo: O(len(t)) · Espacio: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
        return i == len(s)


if __name__ == "__main__":
    s = Solution()
    assert s.isSubsequence("abc", "ahbgdc") is True
    assert s.isSubsequence("axc", "ahbgdc") is False
    assert s.isSubsequence("", "ahbgdc") is True
    print("OK")
