# 98. Validate Binary Search Tree (Media)
# https://leetcode.com/problems/validate-binary-search-tree/
#
# Idea: cada nodo tiene que caer dentro de un rango (mínimo, máximo) que heredan de sus ancestros:
#       al ir a la izquierda baja el máximo y al ir a la derecha sube el mínimo.
# Tiempo: O(n) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valido(nodo, minimo, maximo):
            if not nodo:
                return True
            if not minimo < nodo.val < maximo:
                return False
            return valido(nodo.left, minimo, nodo.val) and valido(nodo.right, nodo.val, maximo)

        return valido(root, float("-inf"), float("inf"))


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
    assert s.isValidBST(crear([2, 1, 3])) is True
    assert s.isValidBST(crear([5, 1, 4, None, None, 3, 6])) is False
    assert s.isValidBST(crear([5, 4, 6, None, None, 3, 7])) is False
    assert s.isValidBST(crear([2, 2, 2])) is False
    print("OK")
