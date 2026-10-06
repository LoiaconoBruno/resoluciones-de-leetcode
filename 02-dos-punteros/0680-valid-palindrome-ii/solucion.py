# 680. Valid Palindrome II (Fácil)
# https://leetcode.com/problems/valid-palindrome-ii/
#
# Idea: dos punteros como en un palíndromo normal; en la primera diferencia pruebo borrar la letra
#       de la izquierda o la de la derecha y chequeo si lo que queda es palíndromo.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def es_palindromo(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        izq, der = 0, len(s) - 1
        while izq < der:
            if s[izq] != s[der]:
                return es_palindromo(izq + 1, der) or es_palindromo(izq, der - 1)
            izq += 1
            der -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.validPalindrome("aba") is True
    assert s.validPalindrome("abca") is True
    assert s.validPalindrome("abc") is False
    print("OK")
