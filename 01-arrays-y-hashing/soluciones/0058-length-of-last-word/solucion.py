# 58. Length of Last Word (Fácil)
# https://leetcode.com/problems/length-of-last-word/
#
# Idea: desde el final salteo los espacios y después cuento letras hasta el próximo espacio.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == " ":
            i -= 1
        largo = 0
        while i >= 0 and s[i] != " ":
            largo += 1
            i -= 1
        return largo


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLastWord("Hello World") == 5
    assert s.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert s.lengthOfLastWord("luffy is still joyboy") == 6
    print("OK")
