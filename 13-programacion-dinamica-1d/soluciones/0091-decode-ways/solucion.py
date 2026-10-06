# 91. Decode Ways (Media)
# https://leetcode.com/problems/decode-ways/
#
# Idea: formas(i) = formas de decodificar s[i:]. Desde i tomo un dígito (si no es '0') o dos dígitos
#       (si forman un número entre 10 y 26). Lo calculo de atrás para adelante con dos variables.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def numDecodings(self, s: str) -> int:
        siguiente, despues = 1, 0
        for i in range(len(s) - 1, -1, -1):
            actual = 0
            if s[i] != "0":
                actual = siguiente
                if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                    actual += despues
            siguiente, despues = actual, siguiente
        return siguiente


if __name__ == "__main__":
    s = Solution()
    assert s.numDecodings("12") == 2
    assert s.numDecodings("226") == 3
    assert s.numDecodings("06") == 0
    assert s.numDecodings("11106") == 2
    print("OK")
