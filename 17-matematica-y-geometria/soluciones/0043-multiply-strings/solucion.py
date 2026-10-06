# 43. Multiply Strings (Media)
# https://leetcode.com/problems/multiply-strings/
#
# Idea: multiplicación de la escuela: el dígito i de num1 por el j de num2 cae en la posición i + j
#       + 1 del resultado; acumulo ahí y voy pasando el acarreo a la izquierda.
# Tiempo: O(n · m) · Espacio: O(n + m)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                total = res[i + j + 1] + int(num1[i]) * int(num2[j])
                res[i + j + 1] = total % 10
                res[i + j] += total // 10
        texto = "".join(map(str, res)).lstrip("0")
        return texto or "0"


if __name__ == "__main__":
    s = Solution()
    assert s.multiply("2", "3") == "6"
    assert s.multiply("123", "456") == "56088"
    assert s.multiply("0", "52") == "0"
    assert s.multiply("999", "999") == "998001"
    print("OK")
