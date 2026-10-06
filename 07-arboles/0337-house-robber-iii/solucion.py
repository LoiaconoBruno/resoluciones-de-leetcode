# 337. House Robber III (Media)
# https://leetcode.com/problems/house-robber-iii/
#
# Idea: cada nodo devuelve dos números: lo mejor robándolo (valor + lo mejor de los hijos sin
#       robarlos) y lo mejor sin robarlo (para cada hijo, el máximo de sus dos opciones).
# Tiempo: O(n) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def mejor(nodo):
            if not nodo:
                return 0, 0
            izq_con, izq_sin = mejor(nodo.left)
            der_con, der_sin = mejor(nodo.right)
            con = nodo.val + izq_sin + der_sin
            sin = max(izq_con, izq_sin) + max(der_con, der_sin)
            return con, sin

        return max(mejor(root))


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
    assert s.rob(crear([3, 2, 3, None, 3, None, 1])) == 7
    assert s.rob(crear([3, 4, 5, 1, 3, None, 1])) == 9
    print("OK")
