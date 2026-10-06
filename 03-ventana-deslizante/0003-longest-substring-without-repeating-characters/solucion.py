# 3. Longest Substring Without Repeating Characters (Media)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Idea: ventana [izq, der] sin repetidos; guardo la última posición de cada letra y, si la letra que
#       entra ya está en la ventana, salto izq justo después de esa posición.
# Tiempo: O(n) · Espacio: O(min(n, alfabeto))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ultima = {}
        izq = mejor = 0
        for der, c in enumerate(s):
            if c in ultima and ultima[c] >= izq:
                izq = ultima[c] + 1
            ultima[c] = der
            mejor = max(mejor, der - izq + 1)
        return mejor


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring("abba") == 2
    print("OK")
