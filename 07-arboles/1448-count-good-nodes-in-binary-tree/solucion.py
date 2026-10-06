# 1448. Count Good Nodes In Binary Tree (Media)
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
#
# Idea: DFS llevando el máximo del camino desde la raíz; un nodo es "bueno" si su valor es mayor o
#       igual a ese máximo.
# Tiempo: O(n) · Espacio: O(h)

# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def contar(nodo, maximo):
            if not nodo:
                return 0
            bueno = 1 if nodo.val >= maximo else 0
            maximo = max(maximo, nodo.val)
            return bueno + contar(nodo.left, maximo) + contar(nodo.right, maximo)

        return contar(root, root.val)


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
    assert s.goodNodes(crear([3, 1, 4, 3, None, 1, 5])) == 4
    assert s.goodNodes(crear([3, 3, None, 4, 2])) == 3
    assert s.goodNodes(crear([1])) == 1
    print("OK")
