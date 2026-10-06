# 416. Partition Equal Subset Sum (Media)
# https://leetcode.com/problems/partition-equal-subset-sum/
#
# Idea: si la suma total es par, la pregunta es si algún subconjunto suma la mitad. Llevo el set de
#       todas las sumas alcanzables y lo actualizo con cada número.
# Tiempo: O(n · suma) · Espacio: O(suma)

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        objetivo = total // 2
        alcanzables = {0}
        for n in nums:
            alcanzables |= {a + n for a in alcanzables if a + n <= objetivo}
            if objetivo in alcanzables:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.canPartition([1, 5, 11, 5]) is True
    assert s.canPartition([1, 2, 3, 5]) is False
    print("OK")
