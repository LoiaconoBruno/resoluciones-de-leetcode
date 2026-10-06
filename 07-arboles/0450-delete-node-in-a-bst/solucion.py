# 450. Delete Node in a BST (Media)
# https://leetcode.com/problems/delete-node-in-a-bst/
#
# Idea: busco la clave como en un BST. Si el nodo tiene un solo hijo, lo reemplazo por ese hijo; si
#       tiene dos, copio el menor valor de su subárbol derecho y borro ese valor de la derecha.
# Tiempo: O(h) · Espacio: O(h)

from typing import Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            sucesor = root.right
            while sucesor.left:
                sucesor = sucesor.left
            root.val = sucesor.val
            root.right = self.deleteNode(root.right, sucesor.val)
        return root


if __name__ == "__main__":
    import random
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

    def inorden(n):
        return inorden(n.left) + [n.val] + inorden(n.right) if n else []

    s = Solution()
    assert a_lista(s.deleteNode(crear([5, 3, 6, 2, 4, None, 7]), 3)) == [5, 4, 6, 2, None, None, 7]
    assert a_lista(s.deleteNode(crear([5, 3, 6, 2, 4, None, 7]), 0)) == [5, 3, 6, 2, 4, None, 7]
    assert a_lista(s.deleteNode(crear([]), 0)) == []
    for _ in range(200):
        valores = random.sample(range(30), random.randint(1, 12))
        raiz = None
        for v in valores:
            nuevo, padre, actual = TreeNode(v), None, raiz
            while actual:
                padre, actual = actual, actual.left if v < actual.val else actual.right
            if not padre:
                raiz = nuevo
            elif v < padre.val:
                padre.left = nuevo
            else:
                padre.right = nuevo
        clave = random.choice(valores + [99])
        assert inorden(s.deleteNode(raiz, clave)) == sorted(v for v in valores if v != clave)
    print("OK")
