# 2002. Maximum Product of The Length of Two Palindromic Subsequences (Media)
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/
#
# Idea: con n ≤ 12 pruebo todas las máscaras: largo[m] es el largo si m es palíndromo; mejor[m] es el palíndromo más largo dentro de m. Para cada palíndromo m, lo combino con mejor[complemento].
# Tiempo: O(2^n · n) · Espacio: O(2^n)

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        total = 1 << n
        largo = [0] * total
        for m in range(1, total):
            sub = [s[i] for i in range(n) if m >> i & 1]
            if sub == sub[::-1]:
                largo[m] = len(sub)
        mejor = largo[:]
        for m in range(1, total):
            for i in range(n):
                if m >> i & 1:
                    mejor[m] = max(mejor[m], mejor[m ^ (1 << i)])
        lleno = total - 1
        return max(largo[m] * mejor[lleno ^ m] for m in range(1, total))


if __name__ == "__main__":
    s = Solution()
    assert s.maxProduct("leetcodecom") == 9
    assert s.maxProduct("bb") == 1
    assert s.maxProduct("accbcaxxcxx") == 25
    print("OK")
