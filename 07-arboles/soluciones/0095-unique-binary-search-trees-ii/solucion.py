# 95. Unique Binary Search Trees II (Media)
# https://leetcode.com/problems/unique-binary-search-trees-ii/
#
# Idea: para el rango [izq, der] pruebo cada valor como raíz y combino cada árbol posible de la
#       izquierda con cada árbol posible de la derecha (memoizando por rango).
# Tiempo: O(n · Catalan(n)) · Espacio: O(n · Catalan(n))

from functools import lru_cache
from typing import List, Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(maxsize=None)
        def armar(izq, der):
            if izq > der:
                return [None]
            res = []
            for raiz in range(izq, der + 1):
                for a in armar(izq, raiz - 1):
                    for b in armar(raiz + 1, der):
                        res.append(TreeNode(raiz, a, b))
            return res

        return armar(1, n)


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
    obtenido = sorted(str(a_lista(t)) for t in s.generateTrees(3))
    esperado = sorted(str(x) for x in [[1, None, 2, None, 3], [1, None, 3, 2], [2, 1, 3], [3, 1, None, None, 2], [3, 2, None, 1]])
    assert obtenido == esperado
    assert [a_lista(t) for t in s.generateTrees(1)] == [[1]]
    assert len(s.generateTrees(5)) == 42
    print("OK")
