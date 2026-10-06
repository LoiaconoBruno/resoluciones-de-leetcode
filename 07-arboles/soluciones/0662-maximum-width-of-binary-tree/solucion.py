# 662. Maximum Width of Binary Tree (Media)
# https://leetcode.com/problems/maximum-width-of-binary-tree/
#
# Idea: numero los nodos como en un heap (hijos de i: 2i y 2i + 1) y hago BFS; el ancho de un nivel
#       es último número - primer número + 1. Resto el primero de cada nivel para que los números no
#       crezcan sin control.
# Tiempo: O(n) · Espacio: O(n)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mejor = 0
        nivel = [(root, 0)]
        while nivel:
            primero = nivel[0][1]
            mejor = max(mejor, nivel[-1][1] - primero + 1)
            siguiente = []
            for nodo, i in nivel:
                i -= primero
                if nodo.left:
                    siguiente.append((nodo.left, 2 * i))
                if nodo.right:
                    siguiente.append((nodo.right, 2 * i + 1))
            nivel = siguiente
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
    assert s.widthOfBinaryTree(crear([1, 3, 2, 5, 3, None, 9])) == 4
    assert s.widthOfBinaryTree(crear([1, 3, 2, 5, None, None, 9, 6, None, 7])) == 7
    assert s.widthOfBinaryTree(crear([1, 3, 2, 5])) == 2
    print("OK")
