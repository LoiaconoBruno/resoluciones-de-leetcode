# 148. Sort List (Media)
# https://leetcode.com/problems/sort-list/
#
# Idea: merge sort sobre la lista: corto en el medio (lenta/rápida), ordeno cada mitad
#       recursivamente y las mezclo.
# Tiempo: O(n log n) · Espacio: O(log n) de recursión

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        lenta, rapida = head, head.next
        while rapida and rapida.next:
            lenta = lenta.next
            rapida = rapida.next.next
        segunda = lenta.next
        lenta.next = None
        return self.mezclar(self.sortList(head), self.sortList(segunda))

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
    import random
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
    assert a_lista(s.sortList(crear([4, 2, 1, 3]))) == [1, 2, 3, 4]
    assert a_lista(s.sortList(crear([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]
    assert a_lista(s.sortList(crear([]))) == []
    for _ in range(100):
        valores = [random.randint(-9, 9) for _ in range(random.randint(0, 20))]
        assert a_lista(s.sortList(crear(valores))) == sorted(valores)
    print("OK")
