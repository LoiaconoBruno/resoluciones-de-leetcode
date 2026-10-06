# 160. Intersection of Two Linked Lists (Fácil)
# https://leetcode.com/problems/intersection-of-two-linked-lists/
#
# Idea: dos punteros que, al terminar su lista, saltan al principio de la otra; así los dos recorren a + b nodos y se encuentran en la intersección (o en None si no hay).
# Tiempo: O(n + m) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


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
    comun = crear([8, 4, 5])
    a = crear([4, 1])
    a.next.next = comun
    b = crear([5, 6, 1])
    b.next.next.next = comun
    assert s.getIntersectionNode(a, b) is comun
    assert s.getIntersectionNode(crear([2, 6, 4]), crear([1, 5])) is None
    print("OK")
