# 6. Zigzag Conversion (Media)
# https://leetcode.com/problems/zigzag-conversion/
#
# Idea: reparto las letras en numRows filas, bajando y subiendo como un zigzag (cambio de sentido en
#       la primera y en la última fila), y al final pego las filas.
# Tiempo: O(n) · Espacio: O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        filas = [[] for _ in range(numRows)]
        fila, paso = 0, 1
        for c in s:
            filas[fila].append(c)
            if fila == 0:
                paso = 1
            elif fila == numRows - 1:
                paso = -1
            fila += paso
        return "".join("".join(f) for f in filas)


if __name__ == "__main__":
    s = Solution()
    assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert s.convert("A", 1) == "A"
    assert s.convert("AB", 1) == "AB"
    print("OK")
