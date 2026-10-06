# 567. Permutation In String (Media)
# https://leetcode.com/problems/permutation-in-string/
#
# Idea: una permutación de s1 es una ventana de s2 del mismo largo con la misma cuenta de letras; deslizo la ventana y comparo las cuentas.
# Tiempo: O(n · 26) · Espacio: O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        objetivo = [0] * 26
        ventana = [0] * 26
        for c in s1:
            objetivo[ord(c) - 97] += 1
        for i, c in enumerate(s2):
            ventana[ord(c) - 97] += 1
            if i >= len(s1):
                ventana[ord(s2[i - len(s1)]) - 97] -= 1
            if ventana == objetivo:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.checkInclusion("ab", "eidbaooo") is True
    assert s.checkInclusion("ab", "eidboaoo") is False
    print("OK")
