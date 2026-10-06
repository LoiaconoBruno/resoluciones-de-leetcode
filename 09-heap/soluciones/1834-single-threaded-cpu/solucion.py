# 1834. Single Threaded Cpu (Media)
# https://leetcode.com/problems/single-threaded-cpu/
#
# Idea: ordeno las tareas por hora de llegada; cuando la CPU se libera, meto en un heap las que ya
#       llegaron y elijo la de menor duración (y menor índice). Si no hay ninguna, salto a la
#       próxima llegada.
# Tiempo: O(n log n) · Espacio: O(n)

import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        orden = sorted(range(len(tasks)), key=lambda i: tasks[i][0])
        heap = []
        res = []
        tiempo = i = 0
        while len(res) < len(tasks):
            if not heap and tiempo < tasks[orden[i]][0]:
                tiempo = tasks[orden[i]][0]
            while i < len(orden) and tasks[orden[i]][0] <= tiempo:
                j = orden[i]
                heapq.heappush(heap, (tasks[j][1], j))
                i += 1
            duracion, j = heapq.heappop(heap)
            tiempo += duracion
            res.append(j)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.getOrder([[1, 2], [2, 4], [3, 2], [4, 1]]) == [0, 2, 3, 1]
    assert s.getOrder([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]) == [4, 3, 2, 0, 1]
    print("OK")
