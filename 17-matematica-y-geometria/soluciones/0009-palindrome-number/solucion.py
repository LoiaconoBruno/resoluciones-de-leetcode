# 9. Palindrome Number (Fácil)
# https://leetcode.com/problems/palindrome-number/
#
# Idea: sin pasar a string: doy vuelta la mitad derecha del número y la comparo con la mitad
#       izquierda. Los negativos y los que terminan en 0 (salvo el 0) no son palíndromos.
# Tiempo: O(log n) · Espacio: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        mitad = 0
        while x > mitad:
            mitad = mitad * 10 + x % 10
            x //= 10
        return x == mitad or x == mitad // 10


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(121) is True
    assert s.isPalindrome(-121) is False
    assert s.isPalindrome(10) is False
    assert s.isPalindrome(0) is True
    assert all(s.isPalindrome(x) == (str(x) == str(x)[::-1]) for x in range(5000))
    print("OK")
