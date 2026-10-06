# 951. Flip Equivalent Binary Trees (Media)
# https://leetcode.com/problems/flip-equivalent-binary-trees/
#
# Idea: dos nodos son equivalentes si tienen el mismo valor y sus hijos coinciden tal cual (izq con
#       izq, der con der) o cruzados (izq con der).
# Tiempo: O(n) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return root1 is root2
        if root1.val != root2.val:
            return False
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or
                (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))


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
    assert s.flipEquiv(crear([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]),
                       crear([1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7])) is True
    assert s.flipEquiv(crear([]), crear([])) is True
    assert s.flipEquiv(crear([]), crear([1])) is False
    print("OK")
