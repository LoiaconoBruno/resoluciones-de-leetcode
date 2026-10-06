# 235. Lowest Common Ancestor of a Binary Search Tree (Media)
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#
# Idea: en un BST, si p y q son los dos menores que el nodo, el ancestro está a la izquierda; si los
#       dos son mayores, a la derecha. Si se separan (o uno es el nodo), ese es el ancestro.
# Tiempo: O(h) · Espacio: O(1)

# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        actual = root
        while actual:
            if p.val < actual.val and q.val < actual.val:
                actual = actual.left
            elif p.val > actual.val and q.val > actual.val:
                actual = actual.right
            else:
                return actual


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

    def buscar(raiz, val):
        while raiz and raiz.val != val:
            raiz = raiz.left if val < raiz.val else raiz.right
        return raiz

    s = Solution()
    raiz = crear([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert s.lowestCommonAncestor(raiz, buscar(raiz, 2), buscar(raiz, 8)).val == 6
    assert s.lowestCommonAncestor(raiz, buscar(raiz, 2), buscar(raiz, 4)).val == 2
    raiz = crear([2, 1])
    assert s.lowestCommonAncestor(raiz, buscar(raiz, 2), buscar(raiz, 1)).val == 2
    print("OK")
