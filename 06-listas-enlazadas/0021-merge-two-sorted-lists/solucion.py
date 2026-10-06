# 21. Merge Two Sorted Lists (Fácil)
# https://leetcode.com/problems/merge-two-sorted-lists/
#
# Idea: un nodo ficticio al principio y un puntero "cola"; engancho siempre el menor de los dos
#       frentes y al final pego lo que sobre.
# Tiempo: O(n + m) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ficticio = cola = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                cola.next, list1 = list1, list1.next
            else:
                cola.next, list2 = list2, list2.next
            cola = cola.next
        cola.next = list1 or list2
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
    assert a_lista(s.mergeTwoLists(crear([1, 2, 4]), crear([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert a_lista(s.mergeTwoLists(crear([]), crear([]))) == []
    assert a_lista(s.mergeTwoLists(crear([]), crear([0]))) == [0]
    print("OK")
