# 783. Minimum Distance between BST Nodes (Fácil)
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
#
# Idea: el inorden de un BST sale ordenado, así que la diferencia mínima está entre dos valores
#       consecutivos del recorrido; llevo el anterior y comparo.
# Tiempo: O(n) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        anterior = None
        mejor = float("inf")

        def inorden(nodo):
            nonlocal anterior, mejor
            if not nodo:
                return
            inorden(nodo.left)
            if anterior is not None:
                mejor = min(mejor, nodo.val - anterior)
            anterior = nodo.val
            inorden(nodo.right)

        inorden(root)
        return mejor


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
    assert s.minDiffInBST(crear([4, 2, 6, 1, 3])) == 1
    assert s.minDiffInBST(crear([1, 0, 48, None, None, 12, 49])) == 1
    print("OK")
