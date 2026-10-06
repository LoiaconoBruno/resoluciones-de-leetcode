# 352. Data Stream as Disjoint Intervals (Difícil)
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/
#
# Idea: guardo los intervalos ordenados y disjuntos; con búsqueda binaria ubico dónde cae el número
#       nuevo y veo si ya está cubierto, si estira al de la izquierda, al de la derecha, si une a
#       los dos o si arranca uno nuevo.
# Tiempo: O(log n) para buscar (O(n) en el peor caso por insertar en la lista); getIntervals O(n) · Espacio: O(n)

from bisect import bisect_left
from typing import List


class SummaryRanges:
    def __init__(self):
        self.intervalos = []

    def addNum(self, value: int) -> None:
        iv = self.intervalos
        i = bisect_left(iv, [value, value])
        if (i < len(iv) and iv[i][0] == value) or (i > 0 and iv[i - 1][1] >= value):
            return
        une_izquierda = i > 0 and iv[i - 1][1] == value - 1
        une_derecha = i < len(iv) and iv[i][0] == value + 1
        if une_izquierda and une_derecha:
            iv[i - 1][1] = iv[i][1]
            iv.pop(i)
        elif une_izquierda:
            iv[i - 1][1] = value
        elif une_derecha:
            iv[i][0] = value
        else:
            iv.insert(i, [value, value])

    def getIntervals(self) -> List[List[int]]:
        return [intervalo[:] for intervalo in self.intervalos]


if __name__ == "__main__":
    import random
    r = SummaryRanges()
    esperado = [[[1, 1]], [[1, 1], [3, 3]], [[1, 1], [3, 3], [7, 7]], [[1, 3], [7, 7]], [[1, 3], [6, 7]]]
    for valor, intervalos in zip([1, 3, 7, 2, 6], esperado):
        r.addNum(valor)
        assert r.getIntervals() == intervalos
    for _ in range(100):
        r, vistos = SummaryRanges(), set()
        for _ in range(30):
            v = random.randint(0, 25)
            r.addNum(v)
            vistos.add(v)
            ordenados, bloques = sorted(vistos), []
            for x in ordenados:
                if bloques and bloques[-1][1] == x - 1:
                    bloques[-1][1] = x
                else:
                    bloques.append([x, x])
            assert r.getIntervals() == bloques
    print("OK")
