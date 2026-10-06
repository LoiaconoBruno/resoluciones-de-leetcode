# 876. Middle of the Linked List (Fácil)
# https://leetcode.com/problems/middle-of-the-linked-list/
#
# Idea: lenta de a 1 y rápida de a 2: cuando la rápida llega al final, la lenta está en el medio (el
#       segundo medio si son pares).
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lenta = rapida = head
        while rapida and rapida.next:
            lenta = lenta.next
            rapida = rapida.next.next
        return lenta


if __name__ == "__main__":
    def crear(valores):
        cabeza = actual = ListNode()
        for v in valores:
            actual.next = ListNode(v)
            actual = actual.next
        return cabeza.next

    def a_lista(nodo):
        res = []
        while nodo:
            res.append(nodo.val)
            nodo = nodo.next
        return res

    s = Solution()
    assert a_lista(s.middleNode(crear([1, 2, 3, 4, 5]))) == [3, 4, 5]
    assert a_lista(s.middleNode(crear([1, 2, 3, 4, 5, 6]))) == [4, 5, 6]
    print("OK")
