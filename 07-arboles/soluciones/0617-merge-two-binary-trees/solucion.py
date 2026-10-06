# 617. Merge Two Binary Trees (Fácil)
# https://leetcode.com/problems/merge-two-binary-trees/
#
# Idea: recorro los dos árboles a la par: si uno de los dos nodos falta uso el otro tal cual; si
#       están los dos, sumo los valores y combino los hijos.
# Tiempo: O(min(n, m)) · Espacio: O(min(h1, h2))

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 or root2
        return TreeNode(root1.val + root2.val,
                        self.mergeTrees(root1.left, root2.left),
                        self.mergeTrees(root1.right, root2.right))


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
    assert a_lista(s.mergeTrees(crear([1, 3, 2, 5]), crear([2, 1, 3, None, 4, None, 7]))) == [3, 4, 5, 5, 4, None, 7]
    assert a_lista(s.mergeTrees(crear([1]), crear([1, 2]))) == [2, 2]
    print("OK")
