# 103. Binary Tree Zigzag Level Order Traversal (Media)
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#
# Idea: BFS por niveles como en Level Order; en los niveles impares doy vuelta la lista del nivel
#       antes de guardarla.
# Tiempo: O(n) · Espacio: O(n)

from collections import deque
from typing import List, Optional


# LeetCode ya define TreeNode; está acá para poder probar localmente.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        cola = deque([root])
        while cola:
            nivel = []
            for _ in range(len(cola)):
                nodo = cola.popleft()
                nivel.append(nodo.val)
                if nodo.left:
                    cola.append(nodo.left)
                if nodo.right:
                    cola.append(nodo.right)
            res.append(nivel[::-1] if len(res) % 2 else nivel)
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
    assert s.zigzagLevelOrder(crear([3, 9, 20, None, None, 15, 7])) == [[3], [20, 9], [15, 7]]
    assert s.zigzagLevelOrder(crear([1, 2, 3, 4, None, None, 5])) == [[1], [3, 2], [4, 5]]
    assert s.zigzagLevelOrder(crear([])) == []
    print("OK")
