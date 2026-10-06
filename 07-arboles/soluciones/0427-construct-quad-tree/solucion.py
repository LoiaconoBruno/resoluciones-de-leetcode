# 427. Construct Quad Tree (Media)
# https://leetcode.com/problems/construct-quad-tree/
#
# Idea: divido la grilla en 4 cuadrantes y armo cada uno recursivamente; si los 4 resultan hojas con
#       el mismo valor, los junto en una sola hoja.
# Tiempo: O(n²) · Espacio: O(log n) de recursión (más el árbol)

from typing import List


# LeetCode ya define Node; está acá para poder probar localmente.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def armar(fila, col, tam):
            if tam == 1:
                return Node(grid[fila][col] == 1, True, None, None, None, None)
            m = tam // 2
            hijos = [armar(fila, col, m), armar(fila, col + m, m),
                     armar(fila + m, col, m), armar(fila + m, col + m, m)]
            if all(h.isLeaf for h in hijos) and len({h.val for h in hijos}) == 1:
                return Node(hijos[0].val, True, None, None, None, None)
            return Node(True, False, *hijos)

        return armar(0, 0, len(grid))


if __name__ == "__main__":
    def a_lista(raiz):
        res, nodos = [], [raiz]
        for nodo in nodos:
            if nodo:
                res.append([int(nodo.isLeaf), int(nodo.val)])
                nodos += [nodo.topLeft, nodo.topRight, nodo.bottomLeft, nodo.bottomRight]
            else:
                res.append(None)
        while res and res[-1] is None:
            res.pop()
        return res

    s = Solution()
    assert a_lista(s.construct([[0, 1], [1, 0]])) == [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]
    grilla = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0],
              [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]
    assert a_lista(s.construct(grilla)) == [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None,
                                            [1, 0], [1, 0], [1, 1], [1, 1]]
    assert a_lista(s.construct([[1]])) == [[1, 1]]
    print("OK")
