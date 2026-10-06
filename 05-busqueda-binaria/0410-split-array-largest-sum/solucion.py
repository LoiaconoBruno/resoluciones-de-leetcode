# 410. Split Array Largest Sum (Difícil)
# https://leetcode.com/problems/split-array-largest-sum/
#
# Idea: búsqueda binaria sobre la suma máxima permitida; para una suma dada corto en forma greedy y cuento cuántas partes necesito.
# Tiempo: O(n log S), con S la suma total · Espacio: O(1)

from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def partes_necesarias(limite):
            partes, suma = 1, 0
            for n in nums:
                if suma + n > limite:
                    partes += 1
                    suma = 0
                suma += n
            return partes

        izq, der = max(nums), sum(nums)
        while izq < der:
            medio = (izq + der) // 2
            if partes_necesarias(medio) <= k:
                der = medio
            else:
                izq = medio + 1
        return izq


if __name__ == "__main__":
    s = Solution()
    assert s.splitArray([7, 2, 5, 10, 8], 2) == 18
    assert s.splitArray([1, 2, 3, 4, 5], 2) == 9
    assert s.splitArray([1, 4, 4], 3) == 4
    print("OK")
