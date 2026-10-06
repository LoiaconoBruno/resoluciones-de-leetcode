# 24. Swap Nodes In Pairs (Media)
# https://leetcode.com/problems/swap-nodes-in-pairs/
#
# Idea: con un nodo ficticio, tomo de a dos nodos (a, b) y los reengancho como anterior -> b -> a -> resto; después avanzo dos.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ficticio = ListNode(0, head)
        anterior = ficticio
        while anterior.next and anterior.next.next:
            a = anterior.next
            b = a.next
            a.next = b.next
            b.next = a
            anterior.next = b
            anterior = a
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
    assert a_lista(s.swapPairs(crear([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert a_lista(s.swapPairs(crear([]))) == []
    assert a_lista(s.swapPairs(crear([1]))) == [1]
    assert a_lista(s.swapPairs(crear([1, 2, 3]))) == [2, 1, 3]
    print("OK")
