# 560. Subarray Sum Equals K (Media)
# https://leetcode.com/problems/subarray-sum-equals-k/
#
# Idea: si la suma prefija hasta acá es p, cada prefijo anterior que valga p - k cierra un subarray
#       que suma k; cuento los prefijos en un diccionario.
# Tiempo: O(n) · Espacio: O(n)

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefijos = defaultdict(int)
        prefijos[0] = 1
        suma = res = 0
        for n in nums:
            suma += n
            res += prefijos[suma - k]
            prefijos[suma] += 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.subarraySum([1, 1, 1], 2) == 2
    assert s.subarraySum([1, 2, 3], 3) == 2
    assert s.subarraySum([1, -1, 0], 0) == 3
    print("OK")
