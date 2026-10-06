# 86. Partition List (Media)
# https://leetcode.com/problems/partition-list/
#
# Idea: armo dos listas aparte, una con los menores a x y otra con el resto (respetando el orden), y
#       al final engancho la segunda detrás de la primera.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        menores = cola_menores = ListNode()
        mayores = cola_mayores = ListNode()
        while head:
            if head.val < x:
                cola_menores.next = head
                cola_menores = head
            else:
                cola_mayores.next = head
                cola_mayores = head
            head = head.next
        cola_mayores.next = None
        cola_menores.next = mayores.next
        return menores.next


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
    assert a_lista(s.partition(crear([1, 4, 3, 2, 5, 2]), 3)) == [1, 2, 2, 4, 3, 5]
    assert a_lista(s.partition(crear([2, 1]), 2)) == [1, 2]
    print("OK")
