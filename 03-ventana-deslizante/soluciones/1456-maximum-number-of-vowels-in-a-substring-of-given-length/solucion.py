# 1456. Maximum Number of Vowels in a Substring of Given Length (Media)
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
#
# Idea: ventana fija de k: sumo 1 si la letra que entra es vocal y resto 1 si la que sale lo era.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vocales = set("aeiou")
        actual = mejor = 0
        for i, c in enumerate(s):
            actual += c in vocales
            if i >= k:
                actual -= s[i - k] in vocales
            mejor = max(mejor, actual)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.maxVowels("abciiidef", 3) == 3
    assert s.maxVowels("aeiou", 2) == 2
    assert s.maxVowels("leetcode", 3) == 2
    print("OK")
