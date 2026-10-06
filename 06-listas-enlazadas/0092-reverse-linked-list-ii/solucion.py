# 92. Reverse Linked List II (Media)
# https://leetcode.com/problems/reverse-linked-list-ii/
#
# Idea: me paro en el nodo anterior a left y, right - left veces, tomo el nodo que sigue al tramo y lo muevo al principio del tramo; así lo doy vuelta en una pasada.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ficticio = ListNode(0, head)
        antes = ficticio
        for _ in range(left - 1):
            antes = antes.next
        actual = antes.next
        for _ in range(right - left):
            mover = actual.next
            actual.next = mover.next
            mover.next = antes.next
            antes.next = mover
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
    assert a_lista(s.reverseBetween(crear([1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
    assert a_lista(s.reverseBetween(crear([5]), 1, 1)) == [5]
    assert a_lista(s.reverseBetween(crear([3, 5]), 1, 2)) == [5, 3]
    print("OK")
