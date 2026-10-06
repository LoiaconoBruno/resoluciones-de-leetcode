# 144. Binary Tree Preorder Traversal (Fácil)
# https://leetcode.com/problems/binary-tree-preorder-traversal/
#
# Idea: preorden iterativo con una pila: visito el nodo y apilo primero el hijo derecho y después el
#       izquierdo, para que el izquierdo salga antes.
# Tiempo: O(n) · Espacio: O(h)

from typing import List, Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        pila = [root] if root else []
        while pila:
            nodo = pila.pop()
            res.append(nodo.val)
            if nodo.right:
                pila.append(nodo.right)
            if nodo.left:
                pila.append(nodo.left)
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
    assert s.preorderTraversal(crear([1, None, 2, 3])) == [1, 2, 3]
    assert s.preorderTraversal(crear([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])) == [1, 2, 4, 5, 6, 7, 3, 8, 9]
    assert s.preorderTraversal(crear([])) == []
    print("OK")
