# 1071. Greatest Common Divisor of Strings (Fácil)
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
#
# Idea: si existe un divisor común, str1 + str2 == str2 + str1; y en ese caso el más grande es el
#       prefijo de largo gcd(len(str1), len(str2)).
# Tiempo: O(n + m) · Espacio: O(n + m)

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]


if __name__ == "__main__":
    s = Solution()
    assert s.gcdOfStrings("ABCABC", "ABC") == "ABC"
    assert s.gcdOfStrings("ABABAB", "ABAB") == "AB"
    assert s.gcdOfStrings("LEET", "CODE") == ""
    print("OK")
