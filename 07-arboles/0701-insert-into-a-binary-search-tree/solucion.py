# 701. Insert into a Binary Search Tree (Media)
# https://leetcode.com/problems/insert-into-a-binary-search-tree/
#
# Idea: bajo por el BST como en una búsqueda (izquierda si es menor, derecha si es mayor) hasta
#       encontrar un hueco, y ahí cuelgo el nodo nuevo.
# Tiempo: O(h) · Espacio: O(1)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        actual = root
        while True:
            if val < actual.val:
                if not actual.left:
                    actual.left = TreeNode(val)
                    return root
                actual = actual.left
            else:
                if not actual.right:
                    actual.right = TreeNode(val)
                    return root
                actual = actual.right


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
    assert a_lista(s.insertIntoBST(crear([4, 2, 7, 1, 3]), 5)) == [4, 2, 7, 1, 3, 5]
    assert a_lista(s.insertIntoBST(crear([40, 20, 60, 10, 30, 50, 70]), 25)) == \
        [40, 20, 60, 10, 30, 50, 70, None, None, 25]
    assert a_lista(s.insertIntoBST(crear([]), 5)) == [5]
    print("OK")
