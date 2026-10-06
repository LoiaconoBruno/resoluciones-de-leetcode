# 2439. Minimize Maximum of Array (Media)
# https://leetcode.com/problems/minimize-maximum-of-array/
#
# Idea: las operaciones solo mueven valor hacia la izquierda, así que los primeros i + 1 números no
#       pueden bajar de ceil(suma_prefija / (i + 1)). La respuesta es el mayor de esos promedios
#       redondeados para arriba.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        suma = res = 0
        for i, n in enumerate(nums):
            suma += n
            res = max(res, (suma + i) // (i + 1))
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.minimizeArrayValue([3, 7, 1, 6]) == 5
    assert s.minimizeArrayValue([10, 1]) == 10
    print("OK")
