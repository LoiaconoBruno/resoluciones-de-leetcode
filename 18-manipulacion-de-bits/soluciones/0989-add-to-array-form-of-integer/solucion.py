# 989. Add to Array-Form of Integer (Fácil)
# https://leetcode.com/problems/add-to-array-form-of-integer/
#
# Idea: sumo k desde el último dígito como en la escuela: el dígito actual + k, me quedo con el
#       último dígito y el resto de k sigue como acarreo. Si al terminar queda k, sus dígitos van
#       adelante.
# Tiempo: O(max(n, log k)) · Espacio: O(1) extra (sin contar la respuesta)

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        i = len(num) - 1
        while i >= 0 or k:
            if i >= 0:
                k += num[i]
                i -= 1
            k, digito = divmod(k, 10)
            res.append(digito)
        return res[::-1]


if __name__ == "__main__":
    s = Solution()
    assert s.addToArrayForm([1, 2, 0, 0], 34) == [1, 2, 3, 4]
    assert s.addToArrayForm([2, 7, 4], 181) == [4, 5, 5]
    assert s.addToArrayForm([2, 1, 5], 806) == [1, 0, 2, 1]
    assert s.addToArrayForm([0], 0) == [0]
    print("OK")
