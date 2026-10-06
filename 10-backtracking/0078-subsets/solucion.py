# 78. Subsets (Media)
# https://leetcode.com/problems/subsets/
#
# Idea: para cada número decido si entra o no entra en el subconjunto; el árbol de decisiones tiene
#       2^n hojas y cada hoja es un subconjunto.
# Tiempo: O(n · 2^n) · Espacio: O(n) de recursión (sin contar la respuesta)

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        actual = []

        def decidir(i):
            if i == len(nums):
                res.append(actual[:])
                return
            actual.append(nums[i])
            decidir(i + 1)
            actual.pop()
            decidir(i + 1)

        decidir(0)
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.subsets([1, 2, 3])) == sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    assert sorted(s.subsets([0])) == [[], [0]]
    print("OK")
