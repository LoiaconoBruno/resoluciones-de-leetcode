# 207. Course Schedule (Media)
# https://leetcode.com/problems/course-schedule/
#
# Idea: orden topológico de Kahn: arranco por los cursos sin prerrequisitos y, al "tomar" uno, le
#       resto un prerrequisito a los que dependen de él. Si al final no tomé todos, hay un ciclo.
# Tiempo: O(V + E) · Espacio: O(V + E)

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependientes = [[] for _ in range(numCourses)]
        faltan = [0] * numCourses
        for curso, previo in prerequisites:
            dependientes[previo].append(curso)
            faltan[curso] += 1
        cola = deque(i for i in range(numCourses) if faltan[i] == 0)
        tomados = 0
        while cola:
            curso = cola.popleft()
            tomados += 1
            for siguiente in dependientes[curso]:
                faltan[siguiente] -= 1
                if faltan[siguiente] == 0:
                    cola.append(siguiente)
        return tomados == numCourses


if __name__ == "__main__":
    s = Solution()
    assert s.canFinish(2, [[1, 0]]) is True
    assert s.canFinish(2, [[1, 0], [0, 1]]) is False
    print("OK")
