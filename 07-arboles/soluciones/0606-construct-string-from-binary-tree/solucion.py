# 606. Construct String From Binary Tree (Fácil)
# https://leetcode.com/problems/construct-string-from-binary-tree/
#
# Idea: preorden armando el texto: valor, después "(izquierdo)" y "(derecho)". Solo hay que poner
#       "()" para el izquierdo vacío cuando existe un hijo derecho.
# Tiempo: O(n) · Espacio: O(n)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        partes = []

        def recorrer(nodo):
            if not nodo:
                return
            partes.append(str(nodo.val))
            if nodo.left or nodo.right:
                partes.append("(")
                recorrer(nodo.left)
                partes.append(")")
            if nodo.right:
                partes.append("(")
                recorrer(nodo.right)
                partes.append(")")

        recorrer(root)
        return "".join(partes)


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
    assert s.tree2str(crear([1, 2, 3, 4])) == "1(2(4))(3)"
    assert s.tree2str(crear([1, 2, 3, None, 4])) == "1(2()(4))(3)"
    print("OK")
