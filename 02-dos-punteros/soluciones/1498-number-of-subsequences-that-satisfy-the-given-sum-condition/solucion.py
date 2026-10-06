# 1498. Number of Subsequences That Satisfy The Given Sum Condition (Media)
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
#
# Idea: ordeno; si el mínimo nums[izq] más el máximo nums[der] entra en target, cualquier
#       subconjunto de lo que está entre ellos (con izq adentro) sirve: 2^(der - izq) subsecuencias.
# Tiempo: O(n log n) · Espacio: O(n)

from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)
        potencias = [1] * n
        for i in range(1, n):
            potencias[i] = potencias[i - 1] * 2 % MOD
        res = 0
        izq, der = 0, n - 1
        while izq <= der:
            if nums[izq] + nums[der] > target:
                der -= 1
            else:
                res = (res + potencias[der - izq]) % MOD
                izq += 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.numSubseq([3, 5, 6, 7], 9) == 4
    assert s.numSubseq([3, 3, 6, 8], 10) == 6
    assert s.numSubseq([2, 3, 3, 4, 6, 7], 12) == 61
    print("OK")
