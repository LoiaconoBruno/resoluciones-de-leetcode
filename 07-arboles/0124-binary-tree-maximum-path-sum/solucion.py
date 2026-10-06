# 124. Binary Tree Maximum Path Sum (Difícil)
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
#
# Idea: DFS que devuelve la mejor "rama" que baja desde cada nodo (ignorando ramas negativas); en
#       cada nodo pruebo el camino que dobla ahí: valor + rama izquierda + rama derecha.
# Tiempo: O(n) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mejor = root.val

        def rama(nodo):
            nonlocal mejor
            if not nodo:
                return 0
            izq = max(rama(nodo.left), 0)
            der = max(rama(nodo.right), 0)
            mejor = max(mejor, nodo.val + izq + der)
            return nodo.val + max(izq, der)

        rama(root)
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
    assert s.maxPathSum(crear([1, 2, 3])) == 6
    assert s.maxPathSum(crear([-10, 9, 20, None, None, 15, 7])) == 42
    assert s.maxPathSum(crear([-3])) == -3
    print("OK")
