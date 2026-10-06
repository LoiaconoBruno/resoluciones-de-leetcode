# 242. Valid Anagram (Fácil)
# https://leetcode.com/problems/valid-anagram/
#
# Idea: cuento las letras de s y las voy descontando con las de t; si alguna queda en negativo, no es anagrama.
# Tiempo: O(n) · Espacio: O(1) (a lo sumo 26 letras)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cuenta = {}
        for c in s:
            cuenta[c] = cuenta.get(c, 0) + 1
        for c in t:
            if cuenta.get(c, 0) == 0:
                return False
            cuenta[c] -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") is True
    assert s.isAnagram("rat", "car") is False
    assert s.isAnagram("a", "ab") is False
    print("OK")
