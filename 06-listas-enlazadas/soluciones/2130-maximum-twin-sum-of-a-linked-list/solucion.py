# 2130. Maximum Twin Sum Of A Linked List (Media)
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
#
# Idea: doy vuelta la segunda mitad; así el nodo i y su gemelo quedan a la misma altura en las dos
#       mitades y los sumo de a pares.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lenta = rapida = head
        while rapida and rapida.next:
            lenta = lenta.next
            rapida = rapida.next.next
        anterior = None
        while lenta:
            siguiente = lenta.next
            lenta.next = anterior
            anterior, lenta = lenta, siguiente
        mejor = 0
        izq, der = head, anterior
        while der:
            mejor = max(mejor, izq.val + der.val)
            izq, der = izq.next, der.next
        return mejor


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
    assert s.pairSum(crear([5, 4, 2, 1])) == 6
    assert s.pairSum(crear([4, 2, 2, 3])) == 7
    assert s.pairSum(crear([1, 100000])) == 100001
    print("OK")
