# 1658. Minimum Operations to Reduce X to Zero (Media)
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
#
# Idea: sacar de las puntas hasta sumar x es lo mismo que dejar en el medio el subarray más largo que sume total - x; ese lo busco con ventana deslizante.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        objetivo = sum(nums) - x
        if objetivo < 0:
            return -1
        izq = suma = 0
        mas_largo = -1
        for der, n in enumerate(nums):
            suma += n
            while suma > objetivo:
                suma -= nums[izq]
                izq += 1
            if suma == objetivo:
                mas_largo = max(mas_largo, der - izq + 1)
        return -1 if mas_largo == -1 else len(nums) - mas_largo


if __name__ == "__main__":
    s = Solution()
    assert s.minOperations([1, 1, 4, 2, 3], 5) == 2
    assert s.minOperations([5, 6, 7, 8, 9], 4) == -1
    assert s.minOperations([3, 2, 20, 1, 1, 3], 10) == 5
    assert s.minOperations([1, 1], 3) == -1
    assert s.minOperations([5, 2, 3], 10) == 3
    print("OK")
