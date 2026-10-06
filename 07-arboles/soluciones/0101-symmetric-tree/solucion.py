# 101. Symmetric Tree (Fácil)
# https://leetcode.com/problems/symmetric-tree/
#
# Idea: un árbol es simétrico si su subárbol izquierdo es espejo del derecho: comparo afuera con
#       afuera (izq.left con der.right) y adentro con adentro.
# Tiempo: O(n) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def espejo(a, b):
            if not a or not b:
                return a is b
            return a.val == b.val and espejo(a.left, b.right) and espejo(a.right, b.left)

        return espejo(root.left, root.right)


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
    assert s.isSymmetric(crear([1, 2, 2, 3, 4, 4, 3])) is True
    assert s.isSymmetric(crear([1, 2, 2, None, 3, None, 3])) is False
    print("OK")
