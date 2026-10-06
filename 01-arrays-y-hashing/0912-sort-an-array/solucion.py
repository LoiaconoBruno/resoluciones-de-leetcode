# 912. Sort an Array (Media)
# https://leetcode.com/problems/sort-an-array/
#
# Idea: merge sort: parto el array a la mitad, ordeno cada mitad y las intercalo con dos punteros.
# Tiempo: O(n log n) · Espacio: O(n)

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        medio = len(nums) // 2
        izq = self.sortArray(nums[:medio])
        der = self.sortArray(nums[medio:])
        res = []
        i = j = 0
        while i < len(izq) and j < len(der):
            if izq[i] <= der[j]:
                res.append(izq[i])
                i += 1
            else:
                res.append(der[j])
                j += 1
        res.extend(izq[i:])
        res.extend(der[j:])
        return res


if __name__ == "__main__":
    import random
    s = Solution()
    assert s.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert s.sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
    for _ in range(100):
        nums = [random.randint(-50, 50) for _ in range(random.randint(0, 30))]
        assert s.sortArray(nums) == sorted(nums)
    print("OK")
