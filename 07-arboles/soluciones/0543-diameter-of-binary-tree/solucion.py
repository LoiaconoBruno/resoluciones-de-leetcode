# 543. Diameter of Binary Tree (Fácil)
# https://leetcode.com/problems/diameter-of-binary-tree/
#
# Idea: el camino más largo que pasa por un nodo como "punto más alto" mide altura(izq) +
#       altura(der); calculo alturas con DFS y voy guardando la mayor de esas sumas.
# Tiempo: O(n) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mejor = 0

        def altura(nodo):
            nonlocal mejor
            if not nodo:
                return 0
            izq, der = altura(nodo.left), altura(nodo.right)
            mejor = max(mejor, izq + der)
            return 1 + max(izq, der)

        altura(root)
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
    assert s.diameterOfBinaryTree(crear([1, 2, 3, 4, 5])) == 3
    assert s.diameterOfBinaryTree(crear([1, 2])) == 1
    print("OK")
