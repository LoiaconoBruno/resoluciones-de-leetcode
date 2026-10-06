# 135. Candy (Difícil)
# https://leetcode.com/problems/candy/
#
# Idea: dos pasadas: de izquierda a derecha, si alguien tiene más rating que el de su izquierda,
#       recibe uno más que él; de derecha a izquierda, lo mismo con el de su derecha (sin bajar lo
#       que ya tenía).
# Tiempo: O(n) · Espacio: O(n)

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        caramelos = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                caramelos[i] = caramelos[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                caramelos[i] = max(caramelos[i], caramelos[i + 1] + 1)
        return sum(caramelos)


if __name__ == "__main__":
    s = Solution()
    assert s.candy([1, 0, 2]) == 5
    assert s.candy([1, 2, 2]) == 4
    print("OK")
