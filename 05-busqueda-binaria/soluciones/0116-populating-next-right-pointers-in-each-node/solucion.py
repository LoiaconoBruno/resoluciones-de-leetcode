# 116. Populating Next Right Pointers In Each Node (Media)
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#
# Idea: como el árbol es perfecto, uso los next del nivel actual para recorrerlo como una lista y
#       conectar el nivel de abajo: el hijo izquierdo apunta al derecho, y el derecho al izquierdo
#       del vecino.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define Node; está acá para poder probar localmente.
class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        inicio_nivel = root
        while inicio_nivel and inicio_nivel.left:
            actual = inicio_nivel
            while actual:
                actual.left.next = actual.right
                if actual.next:
                    actual.right.next = actual.next.left
                actual = actual.next
            inicio_nivel = inicio_nivel.left
        return root


if __name__ == "__main__":
    s = Solution()
    nodos = [Node(i) for i in range(1, 8)]
    for i in range(3):
        nodos[i].left, nodos[i].right = nodos[2 * i + 1], nodos[2 * i + 2]
    raiz = s.connect(nodos[0])
    niveles = []
    inicio = raiz
    while inicio:
        nivel, actual = [], inicio
        while actual:
            nivel.append(actual.val)
            actual = actual.next
        niveles.append(nivel)
        inicio = inicio.left
    assert niveles == [[1], [2, 3], [4, 5, 6, 7]]
    assert s.connect(None) is None
    print("OK")
