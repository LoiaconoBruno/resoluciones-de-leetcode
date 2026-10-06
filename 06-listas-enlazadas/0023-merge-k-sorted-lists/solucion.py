# 23. Merge K Sorted Lists (Difícil)
# https://leetcode.com/problems/merge-k-sorted-lists/
#
# Idea: divide y vencerás: mezclo las listas de a pares (como en Merge Two Sorted Lists) y repito
#       con el resultado hasta que queda una sola.
# Tiempo: O(N log k), con N el total de nodos · Espacio: O(1) extra (sin contar la lista de listas)

from typing import List, Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            mezcladas = []
            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i + 1] if i + 1 < len(lists) else None
                mezcladas.append(self.mezclar(a, b))
            lists = mezcladas
        return lists[0]

    def mezclar(self, a, b):
        ficticio = cola = ListNode()
        while a and b:
            if a.val <= b.val:
                cola.next, a = a, a.next
            else:
                cola.next, b = b, b.next
            cola = cola.next
        cola.next = a or b
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
    assert a_lista(s.mergeKLists([crear([1, 4, 5]), crear([1, 3, 4]), crear([2, 6])])) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert a_lista(s.mergeKLists([])) == []
    assert a_lista(s.mergeKLists([crear([])])) == []
    print("OK")
