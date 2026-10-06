# 347. Top K Frequent Elements (Media)
# https://leetcode.com/problems/top-k-frequent-elements/
#
# Idea: cuento frecuencias y las reparto en cubetas por frecuencia (bucket sort); después recorro las cubetas de la más alta a la más baja.
# Tiempo: O(n) · Espacio: O(n)

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cuenta = Counter(nums)
        cubetas = [[] for _ in range(len(nums) + 1)]
        for n, veces in cuenta.items():
            cubetas[veces].append(n)
        res = []
        for veces in range(len(cubetas) - 1, 0, -1):
            for n in cubetas[veces]:
                res.append(n)
                if len(res) == k:
                    return res
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert s.topKFrequent([1], 1) == [1]
    assert sorted(s.topKFrequent([4, 4, 5, 5, 5, 6], 2)) == [4, 5]
    print("OK")
