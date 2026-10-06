# 210. Course Schedule II (Media)
# https://leetcode.com/problems/course-schedule-ii/
#
# Idea: el mismo orden topológico de Kahn que en Course Schedule, pero guardando el orden en que
#       tomo los cursos; si no llego a tomarlos todos, hay un ciclo y devuelvo [].
# Tiempo: O(V + E) · Espacio: O(V + E)

from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependientes = [[] for _ in range(numCourses)]
        faltan = [0] * numCourses
        for curso, previo in prerequisites:
            dependientes[previo].append(curso)
            faltan[curso] += 1
        cola = deque(i for i in range(numCourses) if faltan[i] == 0)
        orden = []
        while cola:
            curso = cola.popleft()
            orden.append(curso)
            for siguiente in dependientes[curso]:
                faltan[siguiente] -= 1
                if faltan[siguiente] == 0:
                    cola.append(siguiente)
        return orden if len(orden) == numCourses else []


if __name__ == "__main__":
    s = Solution()

    def valido(n, prerrequisitos, orden):
        posicion = {c: i for i, c in enumerate(orden)}
        return sorted(orden) == list(range(n)) and all(posicion[p] < posicion[c] for c, p in prerrequisitos)

    assert s.findOrder(2, [[1, 0]]) == [0, 1]
    assert valido(4, [[1, 0], [2, 0], [3, 1], [3, 2]], s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    assert s.findOrder(1, []) == [0]
    assert s.findOrder(2, [[1, 0], [0, 1]]) == []
    print("OK")
