# 28. Find The Index of The First Occurrence in a String (Fácil)
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
#
# Idea: pruebo cada posición de inicio y comparo la ventana del largo de needle; la primera que
#       coincide es la respuesta.
# Tiempo: O(n · m) · Espacio: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    assert s.strStr("sadbutsad", "sad") == 0
    assert s.strStr("leetcode", "leeto") == -1
    assert s.strStr("aabaaabaaac", "aabaaac") == 4
    assert s.strStr("a", "a") == 0
    print("OK")
