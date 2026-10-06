# 173. Binary Search Tree Iterator (Media)
# https://leetcode.com/problems/binary-search-tree-iterator/
#
# Idea: es un inorden iterativo "en pausa": la pila guarda el camino hacia la izquierda; next saca
#       el tope y, antes de devolverlo, apila el camino izquierdo de su hijo derecho.
# Tiempo: O(1) amortizado por next · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.pila = []
        self._apilar_izquierda(root)

    def _apilar_izquierda(self, nodo):
        while nodo:
            self.pila.append(nodo)
            nodo = nodo.left

    def next(self) -> int:
        nodo = self.pila.pop()
        self._apilar_izquierda(nodo.right)
        return nodo.val

    def hasNext(self) -> bool:
        return bool(self.pila)


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

    it = BSTIterator(crear([7, 3, 15, None, None, 9, 20]))
    assert it.next() == 3
    assert it.next() == 7
    assert it.hasNext() is True
    assert it.next() == 9
    assert it.hasNext() is True
    assert it.next() == 15
    assert it.hasNext() is True
    assert it.next() == 20
    assert it.hasNext() is False
    print("OK")
