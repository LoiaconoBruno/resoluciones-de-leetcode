# 40. Combination Sum II (Media)
# https://leetcode.com/problems/combination-sum-ii/
#
# Idea: ordeno; en cada nivel pruebo cada candidato a partir de i, pero salteo un número si es igual
#       al anterior del mismo nivel (evita combinaciones repetidas). Corto cuando el número ya se
#       pasa del resto.
# Tiempo: O(n · 2^n) · Espacio: O(n) de recursión

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        actual = []

        def buscar(inicio, resto):
            if resto == 0:
                res.append(actual[:])
                return
            for i in range(inicio, len(candidates)):
                if i > inicio and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > resto:
                    break
                actual.append(candidates[i])
                buscar(i + 1, resto - candidates[i])
                actual.pop()

        buscar(0, target)
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert sorted(s.combinationSum2([2, 5, 2, 1, 2], 5)) == [[1, 2, 2], [5]]
    print("OK")
