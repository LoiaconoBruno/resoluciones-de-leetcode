# 105. Construct Binary Tree From Preorder And Inorder Traversal (Media)
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#
# Idea: el primero del preorden es la raíz; buscándola en el inorden sé cuántos nodos van a la
#       izquierda y cuántos a la derecha. Uso un diccionario valor -> posición en el inorden para no
#       buscar cada vez.
# Tiempo: O(n) · Espacio: O(n)

from typing import List, Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        posicion = {v: i for i, v in enumerate(inorder)}
        siguiente = 0

        def armar(izq, der):
            nonlocal siguiente
            if izq > der:
                return None
            valor = preorder[siguiente]
            siguiente += 1
            nodo = TreeNode(valor)
            medio = posicion[valor]
            nodo.left = armar(izq, medio - 1)
            nodo.right = armar(medio + 1, der)
            return nodo

        return armar(0, len(inorder) - 1)


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
    assert a_lista(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])) == [3, 9, 20, None, None, 15, 7]
    assert a_lista(s.buildTree([-1], [-1])) == [-1]
    print("OK")
