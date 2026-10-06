# 230. Kth Smallest Element In a Bst (Media)
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#
# Idea: el recorrido inorden de un BST sale ordenado; lo hago iterativo con una pila y corto al
#       visitar el k-ésimo nodo.
# Tiempo: O(h + k) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pila = []
        actual = root
        while True:
            while actual:
                pila.append(actual)
                actual = actual.left
            actual = pila.pop()
            k -= 1
            if k == 0:
                return actual.val
            actual = actual.right


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
    assert s.kthSmallest(crear([3, 1, 4, None, 2]), 1) == 1
    assert s.kthSmallest(crear([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
    print("OK")
