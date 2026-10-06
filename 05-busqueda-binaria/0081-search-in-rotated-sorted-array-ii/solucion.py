# 81. Search In Rotated Sorted Array II (Media)
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
#
# Idea: igual que la versión sin repetidos, pero si nums[izq] == nums[medio] no sé qué mitad está ordenada; en ese caso descarto izq y sigo.
# Tiempo: O(log n) promedio, O(n) en el peor caso (muchos repetidos) · Espacio: O(1)

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        izq, der = 0, len(nums) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if nums[medio] == target:
                return True
            if nums[izq] == nums[medio]:
                izq += 1
            elif nums[izq] < nums[medio]:
                if nums[izq] <= target < nums[medio]:
                    der = medio - 1
                else:
                    izq = medio + 1
            else:
                if nums[medio] < target <= nums[der]:
                    izq = medio + 1
                else:
                    der = medio - 1
        return False


if __name__ == "__main__":
    import random
    s = Solution()
    assert s.search([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert s.search([2, 5, 6, 0, 0, 1, 2], 3) is False
    for _ in range(500):
        a = sorted(random.randint(0, 5) for _ in range(random.randint(1, 10)))
        k = random.randint(0, len(a) - 1)
        a = a[k:] + a[:k]
        t = random.randint(-1, 6)
        assert s.search(a, t) == (t in a)
    print("OK")
