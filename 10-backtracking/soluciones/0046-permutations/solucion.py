# 46. Permutations (Media)
# https://leetcode.com/problems/permutations/
#
# Idea: voy armando la permutación lugar por lugar; en cada lugar pruebo cada número que todavía no
#       usé y deshago la elección al volver.
# Tiempo: O(n · n!) · Espacio: O(n) de recursión (sin contar la respuesta)

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        actual = []
        usado = [False] * len(nums)

        def armar():
            if len(actual) == len(nums):
                res.append(actual[:])
                return
            for i, n in enumerate(nums):
                if not usado[i]:
                    usado[i] = True
                    actual.append(n)
                    armar()
                    actual.pop()
                    usado[i] = False

        armar()
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.permute([1, 2, 3])) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sorted(s.permute([0, 1])) == [[0, 1], [1, 0]]
    assert s.permute([1]) == [[1]]
    print("OK")
