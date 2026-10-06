# 169. Majority Element (Fácil)
# https://leetcode.com/problems/majority-element/
#
# Idea: votación de Boyer-Moore: el candidato suma con los iguales y resta con los distintos; como el mayoritario es más de la mitad, siempre sobrevive.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidato, votos = None, 0
        for n in nums:
            if votos == 0:
                candidato = n
            votos += 1 if n == candidato else -1
        return candidato


if __name__ == "__main__":
    s = Solution()
    assert s.majorityElement([3, 2, 3]) == 3
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    print("OK")
