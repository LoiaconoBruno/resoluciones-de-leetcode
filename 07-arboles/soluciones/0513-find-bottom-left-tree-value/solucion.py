# 513. Find Bottom Left Tree Value (Media)
# https://leetcode.com/problems/find-bottom-left-tree-value/
#
# Idea: BFS recorriendo cada nivel de derecha a izquierda; el último nodo que sale de la cola es el
#       de más a la izquierda del último nivel.
# Tiempo: O(n) · Espacio: O(n)

from collections import deque
from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        cola = deque([root])
        while cola:
            nodo = cola.popleft()
            if nodo.right:
                cola.append(nodo.right)
            if nodo.left:
                cola.append(nodo.left)
        return nodo.val


if __name__ == "__main__":
    def crear(valores):
        # Arma el árbol desde la lista por niveles que usa LeetCode (None = hueco).
        if not valores or valores[0] is None:
            return None
        raiz = TreeNode(valores[0])
        pendientes = [raiz]
        i = 1
        for nodo in pendientes:
            for lado in ("left", "right"):
                if i < len(valores) and valores[i] is not None:
                    hijo = TreeNode(valores[i])
                    setattr(nodo, lado, hijo)
                    pendientes.append(hijo)
                i += 1
        return raiz

    def a_lista(raiz):
        # El camino inverso: árbol -> lista por niveles, sin los None del final.
        res, nodos = [], [raiz]
        for nodo in nodos:
            if nodo:
                res.append(nodo.val)
                nodos += [nodo.left, nodo.right]
            else:
                res.append(None)
        while res and res[-1] is None:
            res.pop()
        return res

    s = Solution()
    assert s.findBottomLeftValue(crear([2, 1, 3])) == 1
    assert s.findBottomLeftValue(crear([1, 2, 3, 4, None, 5, 6, None, None, 7])) == 7
    print("OK")
