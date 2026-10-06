# 77. Combinations (Media)
# https://leetcode.com/problems/combinations/
#
# Idea: elijo los números en orden creciente: después de elegir i, el siguiente solo puede ser
#       mayor. Corto cuando ya no quedan suficientes números para llegar a k.
# Tiempo: O(k · C(n, k)) · Espacio: O(k) de recursión

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        actual = []

        def elegir(inicio):
            if len(actual) == k:
                res.append(actual[:])
                return
            faltan = k - len(actual)
            for i in range(inicio, n - faltan + 2):
                actual.append(i)
                elegir(i + 1)
                actual.pop()

        elegir(1)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert s.combine(1, 1) == [[1]]
    assert len(s.combine(10, 4)) == 210
    print("OK")
