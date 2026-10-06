# 19. Remove Nth Node From End of List (Media)
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#
# Idea: adelanto un puntero n pasos y después muevo los dos juntos; cuando el adelantado llega al final, el otro quedó justo antes del nodo a borrar.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ficticio = ListNode(0, head)
        izq, der = ficticio, head
        for _ in range(n):
            der = der.next
        while der:
            izq, der = izq.next, der.next
        izq.next = izq.next.next
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
    assert a_lista(s.removeNthFromEnd(crear([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert a_lista(s.removeNthFromEnd(crear([1]), 1)) == []
    assert a_lista(s.removeNthFromEnd(crear([1, 2]), 1)) == [1]
    assert a_lista(s.removeNthFromEnd(crear([1, 2]), 2)) == [2]
    print("OK")
