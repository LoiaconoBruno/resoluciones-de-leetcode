# 909. Snakes And Ladders (Media)
# https://leetcode.com/problems/snakes-and-ladders/
#
# Idea: BFS sobre los casilleros: desde cada uno pruebo las 6 tiradas del dado y, si caigo en una
#       escalera o serpiente, salto a su destino. Lo único difícil es pasar de número de casillero a
#       (fila, columna) por el zigzag.
# Tiempo: O(n²) · Espacio: O(n²)

from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def valor(casillero):
            fila, col = divmod(casillero - 1, n)
            if fila % 2:
                col = n - 1 - col
            return board[n - 1 - fila][col]

        meta = n * n
        tiradas = {1: 0}
        cola = deque([1])
        while cola:
            actual = cola.popleft()
            if actual == meta:
                return tiradas[actual]
            for dado in range(1, 7):
                siguiente = actual + dado
                if siguiente > meta:
                    break
                destino = valor(siguiente)
                if destino != -1:
                    siguiente = destino
                if siguiente not in tiradas:
                    tiradas[siguiente] = tiradas[actual] + 1
                    cola.append(siguiente)
        return -1


if __name__ == "__main__":
    s = Solution()
    tablero = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1],
               [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]
    assert s.snakesAndLadders(tablero) == 4
    assert s.snakesAndLadders([[-1, -1], [-1, 3]]) == 1
    print("OK")
