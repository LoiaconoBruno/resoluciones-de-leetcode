# 1094. Car Pooling (Media)
# https://leetcode.com/problems/car-pooling/
#
# Idea: ordeno los viajes por dónde empiezan y llevo en un min-heap los que están arriba, por dónde
#       terminan; antes de subir a los nuevos, bajo a todos los que ya llegaron.
# Tiempo: O(n log n) · Espacio: O(n)

import heapq
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        arriba = []
        pasajeros = 0
        for cantidad, desde, hasta in trips:
            while arriba and arriba[0][0] <= desde:
                pasajeros -= heapq.heappop(arriba)[1]
            pasajeros += cantidad
            if pasajeros > capacity:
                return False
            heapq.heappush(arriba, (hasta, cantidad))
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.carPooling([[2, 1, 5], [3, 3, 7]], 4) is False
    assert s.carPooling([[2, 1, 5], [3, 3, 7]], 5) is True
    assert s.carPooling([[2, 1, 5], [3, 5, 7]], 3) is True
    print("OK")
