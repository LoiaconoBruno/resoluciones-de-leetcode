# 83. Remove Duplicates From Sorted List (Fácil)
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#
# Idea: como está ordenada, los repetidos están pegados: si el siguiente tiene el mismo valor, lo salteo.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        actual = head
        while actual and actual.next:
            if actual.next.val == actual.val:
                actual.next = actual.next.next
            else:
                actual = actual.next
        return head


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
    assert a_lista(s.deleteDuplicates(crear([1, 1, 2]))) == [1, 2]
    assert a_lista(s.deleteDuplicates(crear([1, 1, 2, 3, 3]))) == [1, 2, 3]
    assert a_lista(s.deleteDuplicates(crear([]))) == []
    print("OK")
