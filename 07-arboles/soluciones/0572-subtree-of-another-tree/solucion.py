# 572. Subtree of Another Tree (Fácil)
# https://leetcode.com/problems/subtree-of-another-tree/
#
# Idea: recorro cada nodo de root y me pregunto si el árbol que empieza ahí es igual a subRoot (con
#       la función de Same Tree).
# Tiempo: O(n · m) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.iguales(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def iguales(self, p, q):
        if not p or not q:
            return p is q
        return p.val == q.val and self.iguales(p.left, q.left) and self.iguales(p.right, q.right)


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
    assert s.isSubtree(crear([3, 4, 5, 1, 2]), crear([4, 1, 2])) is True
    assert s.isSubtree(crear([3, 4, 5, 1, 2, None, None, None, None, 0]), crear([4, 1, 2])) is False
    print("OK")
