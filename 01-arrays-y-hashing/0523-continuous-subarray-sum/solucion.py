# 523. Continuous Subarray Sum (Media)
# https://leetcode.com/problems/continuous-subarray-sum/
#
# Idea: si dos sumas prefijas dan el mismo resto módulo k, lo que hay entre ellas es múltiplo de k; guardo el primer índice de cada resto y pido que estén a distancia ≥ 2.
# Tiempo: O(n) · Espacio: O(min(n, k))

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        primer_indice = {0: -1}
        suma = 0
        for i, n in enumerate(nums):
            suma = (suma + n) % k
            if suma not in primer_indice:
                primer_indice[suma] = i
            elif i - primer_indice[suma] >= 2:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.checkSubarraySum([23, 2, 4, 6, 7], 6) is True
    assert s.checkSubarraySum([23, 2, 6, 4, 7], 6) is True
    assert s.checkSubarraySum([23, 2, 6, 4, 7], 13) is False
    assert s.checkSubarraySum([0], 1) is False
    assert s.checkSubarraySum([5, 0, 0, 0], 3) is True
    print("OK")
