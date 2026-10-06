# 621. Task Scheduler (Media)
# https://leetcode.com/problems/task-scheduler/
#
# Idea: simulo el tiempo: en cada paso hago la tarea con más repeticiones pendientes (max-heap) y la
#       mando a una cola de espera hasta que pase el enfriamiento n. Si no hay nada para hacer,
#       salto el tiempo hasta que vuelva la primera.
# Tiempo: O(t · log 26), con t la cantidad de tareas · Espacio: O(26)

import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-c for c in Counter(tasks).values()]
        heapq.heapify(heap)
        espera = deque()
        tiempo = 0
        while heap or espera:
            tiempo += 1
            if heap:
                restantes = heapq.heappop(heap) + 1
                if restantes:
                    espera.append((restantes, tiempo + n))
            else:
                tiempo = espera[0][1]
            if espera and espera[0][1] == tiempo:
                heapq.heappush(heap, espera.popleft()[0])
        return tiempo


if __name__ == "__main__":
    s = Solution()
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert s.leastInterval(["A", "C", "A", "B", "D", "B"], 1) == 6
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 3) == 10
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    print("OK")
