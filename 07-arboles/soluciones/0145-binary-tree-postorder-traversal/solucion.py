# 145. Binary Tree Postorder Traversal (Fácil)
# https://leetcode.com/problems/binary-tree-postorder-traversal/
#
# Idea: el postorden (izq, der, raíz) es el revés de recorrer raíz, der, izq; hago ese recorrido con
#       una pila (como el preorden pero al revés) y doy vuelta el resultado.
# Tiempo: O(n) · Espacio: O(h)

from typing import List, Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        pila = [root] if root else []
        while pila:
            nodo = pila.pop()
            res.append(nodo.val)
            if nodo.left:
                pila.append(nodo.left)
            if nodo.right:
                pila.append(nodo.right)
        return res[::-1]


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
    assert s.postorderTraversal(crear([1, None, 2, 3])) == [3, 2, 1]
    assert s.postorderTraversal(crear([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])) == [4, 6, 7, 5, 2, 9, 8, 3, 1]
    assert s.postorderTraversal(crear([])) == []
    print("OK")
