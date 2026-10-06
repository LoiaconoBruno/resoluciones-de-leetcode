# 894. All Possible Full Binary Trees (Media)
# https://leetcode.com/problems/all-possible-full-binary-trees/
#
# Idea: un árbol binario lleno tiene cantidad impar de nodos; para n, pruebo poner i nodos a la
#       izquierda y n - 1 - i a la derecha y combino todas las opciones de cada lado (memoizando por
#       n).
# Tiempo: O(2^(n/2)) aprox., proporcional a la cantidad de árboles · Espacio: O(2^(n/2))

from functools import lru_cache
from typing import List, Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(maxsize=None)
        def armar(nodos):
            if nodos % 2 == 0:
                return []
            if nodos == 1:
                return [TreeNode(0)]
            res = []
            for izq in range(1, nodos, 2):
                for a in armar(izq):
                    for b in armar(nodos - 1 - izq):
                        res.append(TreeNode(0, a, b))
            return res

        return armar(n)


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
    obtenido = sorted(str(a_lista(t)) for t in s.allPossibleFBT(7))
    esperado = sorted(str(x) for x in [[0, 0, 0, None, None, 0, 0, None, None, 0, 0], [0, 0, 0, None, None, 0, 0, 0, 0],
                                       [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, None, None, None, None, 0, 0],
                                       [0, 0, 0, 0, 0, None, None, 0, 0]])
    assert obtenido == esperado
    assert [a_lista(t) for t in s.allPossibleFBT(3)] == [[0, 0, 0]]
    assert s.allPossibleFBT(4) == []
    print("OK")
