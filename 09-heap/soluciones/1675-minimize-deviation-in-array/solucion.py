# 1675. Minimize Deviation in Array (Difícil)
# https://leetcode.com/problems/minimize-deviation-in-array/
#
# Idea: llevo todos los números a su máximo posible (los impares se duplican una vez) y después solo
#       puedo bajar dividiendo pares. Con un max-heap, achico siempre el máximo mientras sea par,
#       llevando el mínimo actual.
# Tiempo: O(n log n log M) · Espacio: O(n)

import heapq
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = [-(n * 2 if n % 2 else n) for n in nums]
        heapq.heapify(heap)
        minimo = -max(heap)
        mejor = float("inf")
        while True:
            maximo = -heapq.heappop(heap)
            mejor = min(mejor, maximo - minimo)
            if maximo % 2:
                return mejor
            maximo //= 2
            minimo = min(minimo, maximo)
            heapq.heappush(heap, -maximo)


if __name__ == "__main__":
    s = Solution()
    assert s.minimumDeviation([1, 2, 3, 4]) == 1
    assert s.minimumDeviation([4, 1, 5, 20, 3]) == 3
    assert s.minimumDeviation([2, 10, 8]) == 3
    print("OK")
