# 1888. Minimum Number of Flips to Make The Binary String Alternating (Media)
# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
#
# Idea: la operación 1 (pasar la primera letra al final) equivale a mirar ventanas de largo n sobre
#       s + s; en cada ventana cuento las diferencias contra "0101..." y "1010...".
# Tiempo: O(n) · Espacio: O(n)

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        t = s + s
        dif1 = dif2 = 0
        res = n
        for i, c in enumerate(t):
            esperado = "0" if i % 2 == 0 else "1"
            dif1 += c != esperado
            dif2 += c == esperado
            if i >= n:
                viejo = "0" if (i - n) % 2 == 0 else "1"
                dif1 -= t[i - n] != viejo
                dif2 -= t[i - n] == viejo
            if i >= n - 1:
                res = min(res, dif1, dif2)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.minFlips("111000") == 2
    assert s.minFlips("010") == 0
    assert s.minFlips("1110") == 1
    print("OK")
