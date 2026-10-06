# 39. Combination Sum (Media)
# https://leetcode.com/problems/combination-sum/
#
# Idea: backtracking desde el índice i: o vuelvo a usar candidates[i] (me quedo en i) o lo salteo y
#       paso a i + 1. Así no genero la misma combinación en otro orden.
# Tiempo: O(n^(t/m)), con t el target y m el candidato más chico · Espacio: O(t/m) de recursión

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        actual = []

        def buscar(i, resto):
            if resto == 0:
                res.append(actual[:])
                return
            if i == len(candidates) or resto < 0:
                return
            actual.append(candidates[i])
            buscar(i, resto - candidates[i])
            actual.pop()
            buscar(i + 1, resto)

        buscar(0, target)
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.combinationSum([2, 3, 6, 7], 7)) == [[2, 2, 3], [7]]
    assert sorted(s.combinationSum([2, 3, 5], 8)) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert s.combinationSum([2], 1) == []
    print("OK")
