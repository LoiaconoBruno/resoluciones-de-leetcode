# 112. Path Sum (Fácil)
# https://leetcode.com/problems/path-sum/
#
# Idea: bajo restando el valor de cada nodo a targetSum; en una hoja, el camino sirve si lo que
#       queda es justo su valor.
# Tiempo: O(n) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        resto = targetSum - root.val
        return self.hasPathSum(root.left, resto) or self.hasPathSum(root.right, resto)


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
    assert s.hasPathSum(crear([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22) is True
    assert s.hasPathSum(crear([1, 2, 3]), 5) is False
    assert s.hasPathSum(crear([]), 0) is False
    print("OK")
