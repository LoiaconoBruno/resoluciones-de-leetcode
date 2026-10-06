# 926. Flip String to Monotone Increasing (Media)
# https://leetcode.com/problems/flip-string-to-monotone-increasing/
#
# Idea: recorro de izquierda a derecha contando los '1' vistos; ante un '0' tengo dos opciones:
#       darlo vuelta (cambios + 1) o dar vuelta todos los '1' anteriores. Me quedo con la menor.
# Tiempo: O(n) · Espacio: O(1)

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        unos = cambios = 0
        for c in s:
            if c == "1":
                unos += 1
            else:
                cambios = min(cambios + 1, unos)
        return cambios


if __name__ == "__main__":
    s = Solution()
    assert s.minFlipsMonoIncr("00110") == 1
    assert s.minFlipsMonoIncr("010110") == 2
    assert s.minFlipsMonoIncr("00011000") == 2
    print("OK")
