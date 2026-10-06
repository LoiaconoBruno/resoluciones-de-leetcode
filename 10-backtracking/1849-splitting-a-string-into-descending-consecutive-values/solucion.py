# 1849. Splitting a String Into Descending Consecutive Values (Media)
# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/
#
# Idea: pruebo cada prefijo como primer número; después busco con backtracking un pedazo que valga
#       exactamente el anterior - 1, y sigo hasta consumir todo el string (con al menos dos partes).
# Tiempo: O(n²) por cada primer número, O(n³) en total · Espacio: O(n) de recursión

class Solution:
    def splitString(self, s: str) -> bool:
        def seguir(i, anterior):
            if i == len(s):
                return True
            for j in range(i + 1, len(s) + 1):
                valor = int(s[i:j])
                if valor == anterior - 1 and seguir(j, valor):
                    return True
                if valor >= anterior:
                    break
            return False

        return any(seguir(i, int(s[:i])) for i in range(1, len(s)))


if __name__ == "__main__":
    s = Solution()
    assert s.splitString("1234") is False
    assert s.splitString("050043") is True
    assert s.splitString("9080701") is False
    assert s.splitString("10009998") is True
    assert s.splitString("200100") is True
    print("OK")
