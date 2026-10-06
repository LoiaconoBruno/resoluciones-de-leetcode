# 110. Balanced Binary Tree (Fácil)
# https://leetcode.com/problems/balanced-binary-tree/
#
# Idea: DFS que devuelve la altura de cada subárbol, o -1 si ya encontró un desbalance; así resuelvo
#       todo en una sola pasada desde abajo.
# Tiempo: O(n) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def altura(nodo):
            if not nodo:
                return 0
            izq, der = altura(nodo.left), altura(nodo.right)
            if izq < 0 or der < 0 or abs(izq - der) > 1:
                return -1
            return 1 + max(izq, der)

        return altura(root) >= 0


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
    assert s.isBalanced(crear([3, 9, 20, None, None, 15, 7])) is True
    assert s.isBalanced(crear([1, 2, 2, 3, 3, None, None, 4, 4])) is False
    assert s.isBalanced(crear([])) is True
    print("OK")
