# 1462. Course Schedule IV (Media)
# https://leetcode.com/problems/course-schedule-iv/
#
# Idea: recorro los cursos en orden topológico y propago "quiénes son mis prerrequisitos" como un
#       conjunto (acá, bits de un entero): los de mi prerrequisito directo más él mismo. Cada
#       consulta es mirar un bit.
# Tiempo: O(n · (n + E) / 64 + q) · Espacio: O(n²) bits

from collections import deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        siguientes = [[] for _ in range(numCourses)]
        faltan = [0] * numCourses
        for previo, curso in prerequisites:
            siguientes[previo].append(curso)
            faltan[curso] += 1
        requisitos = [0] * numCourses
        cola = deque(i for i in range(numCourses) if faltan[i] == 0)
        while cola:
            curso = cola.popleft()
            for sig in siguientes[curso]:
                requisitos[sig] |= requisitos[curso] | (1 << curso)
                faltan[sig] -= 1
                if faltan[sig] == 0:
                    cola.append(sig)
        return [bool(requisitos[v] >> u & 1) for u, v in queries]


if __name__ == "__main__":
    s = Solution()
    assert s.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]) == [False, True]
    assert s.checkIfPrerequisite(2, [], [[1, 0], [0, 1]]) == [False, False]
    assert s.checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]) == [True, True]
    print("OK")
