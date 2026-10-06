# 129. Sum Root to Leaf Numbers (Media)
# https://leetcode.com/problems/sum-root-to-leaf-numbers/
#
# Idea: DFS llevando el número armado hasta el padre: al bajar, numero = numero · 10 + valor; en
#       cada hoja sumo el número completo.
# Tiempo: O(n) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumar(nodo, numero):
            if not nodo:
                return 0
            numero = numero * 10 + nodo.val
            if not nodo.left and not nodo.right:
                return numero
            return sumar(nodo.left, numero) + sumar(nodo.right, numero)

        return sumar(root, 0)


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
    assert s.sumNumbers(crear([1, 2, 3])) == 25
    assert s.sumNumbers(crear([4, 9, 0, 5, 1])) == 1026
    print("OK")
