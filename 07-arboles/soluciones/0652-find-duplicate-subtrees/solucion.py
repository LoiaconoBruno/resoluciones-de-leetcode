# 652. Find Duplicate Subtrees (Media)
# https://leetcode.com/problems/find-duplicate-subtrees/
#
# Idea: serializo cada subárbol (de abajo hacia arriba) como texto; si una misma serialización
#       aparece por segunda vez, ese subárbol está duplicado.
# Tiempo: O(n²) en el peor caso, por armar los textos · Espacio: O(n²)

from collections import defaultdict
from typing import List, Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        vistos = defaultdict(int)
        res = []

        def serializar(nodo):
            if not nodo:
                return "N"
            clave = f"{nodo.val},{serializar(nodo.left)},{serializar(nodo.right)}"
            vistos[clave] += 1
            if vistos[clave] == 2:
                res.append(nodo)
            return clave

        serializar(root)
        return res


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

    def resultado(valores):
        return sorted(str(a_lista(n)) for n in s.findDuplicateSubtrees(crear(valores)))

    assert resultado([1, 2, 3, 4, None, 2, 4, None, None, 4]) == sorted(["[2, 4]", "[4]"])
    assert resultado([2, 1, 1]) == ["[1]"]
    assert resultado([2, 2, 2, 3, None, 3, None]) == sorted(["[2, 3]", "[3]"])
    print("OK")
