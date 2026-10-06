# 206. Reverse Linked List (Fácil)
# https://leetcode.com/problems/reverse-linked-list/
#
# Idea: recorro la lista dando vuelta cada flecha: guardo el siguiente, apunto el actual al anterior
#       y avanzo.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        anterior, actual = None, head
        while actual:
            siguiente = actual.next
            actual.next = anterior
            anterior, actual = actual, siguiente
        return anterior


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
    assert a_lista(s.reverseList(crear([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert a_lista(s.reverseList(crear([1, 2]))) == [2, 1]
    assert a_lista(s.reverseList(crear([]))) == []
    print("OK")
