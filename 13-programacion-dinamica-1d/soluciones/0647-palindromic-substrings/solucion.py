# 647. Palindromic Substrings (Media)
# https://leetcode.com/problems/palindromic-substrings/
#
# Idea: igual que el palíndromo más largo: expando desde cada centro (impar y par), pero en vez de
#       guardar el más largo, cuento cada expansión exitosa.
# Tiempo: O(n²) · Espacio: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for centro in range(len(s)):
            for izq, der in ((centro, centro), (centro, centro + 1)):
                while izq >= 0 and der < len(s) and s[izq] == s[der]:
                    total += 1
                    izq -= 1
                    der += 1
        return total


if __name__ == "__main__":
    s = Solution()
    assert s.countSubstrings("abc") == 3
    assert s.countSubstrings("aaa") == 6
    print("OK")
