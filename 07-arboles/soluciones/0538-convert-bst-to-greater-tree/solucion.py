# 538. Convert Bst to Greater Tree (Media)
# https://leetcode.com/problems/convert-bst-to-greater-tree/
#
# Idea: recorro el BST en inorden al revés (derecha, nodo, izquierda), o sea de mayor a menor,
#       acumulando la suma; cada nodo pasa a valer la suma acumulada.
# Tiempo: O(n) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        suma = 0

        def recorrer(nodo):
            nonlocal suma
            if not nodo:
                return
            recorrer(nodo.right)
            suma += nodo.val
            nodo.val = suma
            recorrer(nodo.left)

        recorrer(root)
        return root


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
    assert a_lista(s.convertBST(crear([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]))) == \
        [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]
    assert a_lista(s.convertBST(crear([0, None, 1]))) == [1, None, 1]
    print("OK")
