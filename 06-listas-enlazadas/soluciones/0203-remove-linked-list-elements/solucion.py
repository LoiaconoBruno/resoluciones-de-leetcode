# 203. Remove Linked List Elements (Fácil)
# https://leetcode.com/problems/remove-linked-list-elements/
#
# Idea: con un nodo ficticio adelante, recorro mirando el siguiente: si tiene el valor, lo salteo;
#       si no, avanzo.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ficticio = ListNode(0, head)
        actual = ficticio
        while actual.next:
            if actual.next.val == val:
                actual.next = actual.next.next
            else:
                actual = actual.next
        return ficticio.next


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
    assert a_lista(s.removeElements(crear([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]
    assert a_lista(s.removeElements(crear([]), 1)) == []
    assert a_lista(s.removeElements(crear([7, 7, 7, 7]), 7)) == []
    print("OK")
