# 143. Reorder List (Media)
# https://leetcode.com/problems/reorder-list/
#
# Idea: tres pasos: encuentro el medio (lenta/rápida), doy vuelta la segunda mitad y después
#       intercalo las dos mitades.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lenta, rapida = head, head.next
        while rapida and rapida.next:
            lenta = lenta.next
            rapida = rapida.next.next
        segunda = lenta.next
        lenta.next = None
        anterior = None
        while segunda:
            siguiente = segunda.next
            segunda.next = anterior
            anterior, segunda = segunda, siguiente
        primera, segunda = head, anterior
        while segunda:
            sig1, sig2 = primera.next, segunda.next
            primera.next = segunda
            segunda.next = sig1
            primera, segunda = sig1, sig2


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
    for valores, esperado in (([1, 2, 3, 4], [1, 4, 2, 3]), ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]), ([1], [1])):
        cabeza = crear(valores)
        s.reorderList(cabeza)
        assert a_lista(cabeza) == esperado
    print("OK")
