# 1423. Maximum Points You Can Obtain From Cards (Media)
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
#
# Idea: tomar k cartas de las puntas es dejar en el medio una ventana de n - k cartas; la mejor
#       jugada deja la ventana de suma mínima.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        largo = n - k
        ventana = sum(cardPoints[:largo])
        minima = ventana
        for i in range(largo, n):
            ventana += cardPoints[i] - cardPoints[i - largo]
            minima = min(minima, ventana)
        return sum(cardPoints) - minima


if __name__ == "__main__":
    s = Solution()
    assert s.maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12
    assert s.maxScore([2, 2, 2], 2) == 4
    assert s.maxScore([9, 7, 7, 9, 7, 7, 9], 7) == 55
    print("OK")
