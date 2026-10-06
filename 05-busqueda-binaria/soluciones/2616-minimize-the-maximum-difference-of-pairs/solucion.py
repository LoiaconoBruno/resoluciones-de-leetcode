# 2616. Minimize the Maximum Difference of Pairs (Media)
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
#
# Idea: búsqueda binaria sobre la diferencia máxima permitida; para chequear una, ordeno y armo
#       pares de vecinos en forma greedy (si dos vecinos entran, los emparejo).
# Tiempo: O(n log n + n log M) · Espacio: O(1) extra

from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def alcanza(limite):
            pares = i = 0
            while i < len(nums) - 1 and pares < p:
                if nums[i + 1] - nums[i] <= limite:
                    pares += 1
                    i += 2
                else:
                    i += 1
            return pares >= p

        izq, der = 0, nums[-1] - nums[0]
        while izq < der:
            medio = (izq + der) // 2
            if alcanza(medio):
                der = medio
            else:
                izq = medio + 1
        return izq


if __name__ == "__main__":
    s = Solution()
    assert s.minimizeMax([10, 1, 2, 7, 1, 3], 2) == 1
    assert s.minimizeMax([4, 2, 1, 2], 1) == 0
    assert s.minimizeMax([3, 9], 0) == 0
    print("OK")
