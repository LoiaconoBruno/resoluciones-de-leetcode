# 958. Check Completeness of a Binary Tree (Media)
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
#
# Idea: BFS metiendo también los hijos vacíos; en un árbol completo, una vez que aparece el primer
#       hueco ya no puede aparecer ningún nodo más.
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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        cola = deque([root])
        vi_hueco = False
        while cola:
            nodo = cola.popleft()
            if not nodo:
                vi_hueco = True
                continue
            if vi_hueco:
                return False
            cola.append(nodo.left)
            cola.append(nodo.right)
        return True


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
    assert s.isCompleteTree(crear([1, 2, 3, 4, 5, 6])) is True
    assert s.isCompleteTree(crear([1, 2, 3, 4, 5, None, 7])) is False
    assert s.isCompleteTree(crear([1, 2, 3, None, 4])) is False
    print("OK")
