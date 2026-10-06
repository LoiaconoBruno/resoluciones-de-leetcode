# 125. Valid Palindrome (Fácil)
# https://leetcode.com/problems/valid-palindrome/
#
# Idea: un puntero en cada punta; salteo lo que no sea letra o número y comparo en minúscula
#       mientras se acercan.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        izq, der = 0, len(s) - 1
        while izq < der:
            if not s[izq].isalnum():
                izq += 1
            elif not s[der].isalnum():
                der -= 1
            else:
                if s[izq].lower() != s[der].lower():
                    return False
                izq += 1
                der -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") is True
    assert s.isPalindrome("race a car") is False
    assert s.isPalindrome(" ") is True
    print("OK")
