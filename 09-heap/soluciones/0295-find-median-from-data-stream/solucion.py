# 295. Find Median From Data Stream (Difícil)
# https://leetcode.com/problems/find-median-from-data-stream/
#
# Idea: dos heaps: un max-heap con la mitad chica y un min-heap con la mitad grande, balanceados
#       (como mucho uno más en la chica). La mediana sale de las raíces.
# Tiempo: O(log n) addNum, O(1) findMedian · Espacio: O(n)

import heapq


class MedianFinder:
    def __init__(self):
        self.chicos = []
        self.grandes = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.chicos, -num)
        heapq.heappush(self.grandes, -heapq.heappop(self.chicos))
        if len(self.grandes) > len(self.chicos):
            heapq.heappush(self.chicos, -heapq.heappop(self.grandes))

    def findMedian(self) -> float:
        if len(self.chicos) > len(self.grandes):
            return float(-self.chicos[0])
        return (-self.chicos[0] + self.grandes[0]) / 2


if __name__ == "__main__":
    import random
    m = MedianFinder()
    m.addNum(1)
    m.addNum(2)
    assert m.findMedian() == 1.5
    m.addNum(3)
    assert m.findMedian() == 2.0
    m, vistos = MedianFinder(), []
    for _ in range(300):
        v = random.randint(-50, 50)
        m.addNum(v)
        vistos.append(v)
        o, n = sorted(vistos), len(vistos)
        assert m.findMedian() == (o[n // 2] if n % 2 else (o[n // 2 - 1] + o[n // 2]) / 2)
    print("OK")
