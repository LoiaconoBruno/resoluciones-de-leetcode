# 698. Partition to K Equal Sum Subsets (Media)
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
#
# Idea: cada grupo tiene que sumar total / k; ubico los números de mayor a menor en alguno de los k
#       grupos y retrocedo si no entran. Si dos grupos suman lo mismo, probar el segundo es repetir
#       trabajo.
# Tiempo: O(k^n) en el peor caso, mucho menos con las podas · Espacio: O(n) de recursión

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        objetivo = total // k
        nums.sort(reverse=True)
        if nums[0] > objetivo:
            return False
        grupos = [0] * k

        def ubicar(i):
            if i == len(nums):
                return True
            probados = set()
            for j in range(k):
                if grupos[j] + nums[i] <= objetivo and grupos[j] not in probados:
                    probados.add(grupos[j])
                    grupos[j] += nums[i]
                    if ubicar(i + 1):
                        return True
                    grupos[j] -= nums[i]
            return False

        return ubicar(0)


if __name__ == "__main__":
    s = Solution()
    assert s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) is True
    assert s.canPartitionKSubsets([1, 2, 3, 4], 3) is False
    assert s.canPartitionKSubsets([2, 2, 2, 2, 3, 4, 5], 4) is False
    print("OK")
