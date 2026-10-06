# 199. Binary Tree Right Side View (Media)
# https://leetcode.com/problems/binary-tree-right-side-view/
#
# Idea: BFS por niveles; desde la derecha se ve el último nodo de cada nivel.
# Tiempo: O(n) · Espacio: O(n)

from collections import deque
from typing import List, Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        cola = deque([root])
        while cola:
            for i in range(len(cola)):
                nodo = cola.popleft()
                if i == 0:
                    res.append(nodo.val)
                if nodo.right:
                    cola.append(nodo.right)
                if nodo.left:
                    cola.append(nodo.left)
        return res


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
    assert s.rightSideView(crear([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert s.rightSideView(crear([1, None, 3])) == [1, 3]
    assert s.rightSideView(crear([])) == []
    assert s.rightSideView(crear([1, 2, 3, 4])) == [1, 3, 4]
    print("OK")
