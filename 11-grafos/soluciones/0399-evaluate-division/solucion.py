# 399. Evaluate Division (Media)
# https://leetcode.com/problems/evaluate-division/
#
# Idea: cada ecuación a / b = v es una arista a -> b con peso v (y b -> a con 1/v). Para una
#       consulta x / y busco un camino de x a y con BFS multiplicando los pesos.
# Tiempo: O(q · (V + E)) · Espacio: O(V + E)

from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        vecinos = defaultdict(list)
        for (a, b), v in zip(equations, values):
            vecinos[a].append((b, v))
            vecinos[b].append((a, 1 / v))

        def resolver(origen, destino):
            if origen not in vecinos or destino not in vecinos:
                return -1.0
            vistos = {origen}
            cola = deque([(origen, 1.0)])
            while cola:
                nodo, producto = cola.popleft()
                if nodo == destino:
                    return producto
                for v, peso in vecinos[nodo]:
                    if v not in vistos:
                        vistos.add(v)
                        cola.append((v, producto * peso))
            return -1.0

        return [resolver(x, y) for x, y in queries]


if __name__ == "__main__":
    s = Solution()

    def cerca(a, b):
        return all(abs(x - y) < 1e-9 for x, y in zip(a, b)) and len(a) == len(b)

    assert cerca(s.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                                [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]),
                 [6.0, 0.5, -1.0, 1.0, -1.0])
    assert cerca(s.calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0],
                                [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]),
                 [3.75, 0.4, 5.0, 0.2])
    print("OK")
