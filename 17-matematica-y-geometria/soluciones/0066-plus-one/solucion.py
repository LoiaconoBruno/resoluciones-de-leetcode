# 66. Plus One (Fácil)
# https://leetcode.com/problems/plus-one/
#
# Idea: sumo 1 desde el último dígito: los 9 se vuelven 0 y sigo con el acarreo; el primer dígito
#       que no es 9 sube uno y termino. Si todos eran 9, agrego un 1 adelante.
# Tiempo: O(n) · Espacio: O(1) (salvo el caso de todos 9)

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == "__main__":
    s = Solution()
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert s.plusOne([9]) == [1, 0]
    assert s.plusOne([9, 9]) == [1, 0, 0]
    print("OK")
