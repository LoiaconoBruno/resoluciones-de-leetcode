# 1882. Process Tasks Using Servers (Media)
# https://leetcode.com/problems/process-tasks-using-servers/
#
# Idea: dos heaps: libres por (peso, índice) y ocupados por (hora en que se liberan, peso, índice).
#       Para cada tarea avanzo el reloj, libero los servidores que terminaron y asigno el mejor
#       libre.
# Tiempo: O((n + m) log n) · Espacio: O(n)

import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        libres = [(peso, i) for i, peso in enumerate(servers)]
        heapq.heapify(libres)
        ocupados = []
        res = []
        tiempo = 0
        for j, duracion in enumerate(tasks):
            tiempo = max(tiempo, j)
            if not libres:
                tiempo = max(tiempo, ocupados[0][0])
            while ocupados and ocupados[0][0] <= tiempo:
                _, peso, i = heapq.heappop(ocupados)
                heapq.heappush(libres, (peso, i))
            peso, i = heapq.heappop(libres)
            res.append(i)
            heapq.heappush(ocupados, (tiempo + duracion, peso, i))
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.assignTasks([3, 3, 2], [1, 2, 3, 2, 1, 2]) == [2, 2, 0, 2, 1, 2]
    assert s.assignTasks([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1]) == [1, 4, 1, 4, 1, 3, 2]
    print("OK")
