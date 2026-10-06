# 141. Linked List Cycle (Fácil)
# https://leetcode.com/problems/linked-list-cycle/
#
# Idea: tortuga y liebre (Floyd): una avanza de a 1 y otra de a 2; si hay ciclo, la rápida termina
#       alcanzando a la lenta.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lenta = rapida = head
        while rapida and rapida.next:
            lenta = lenta.next
            rapida = rapida.next.next
            if lenta is rapida:
                return True
        return False


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

    def con_ciclo(valores, pos):
        cabeza = crear(valores)
        if pos >= 0:
            nodos = []
            n = cabeza
            while n:
                nodos.append(n)
                n = n.next
            nodos[-1].next = nodos[pos]
        return cabeza

    s = Solution()
    assert s.hasCycle(con_ciclo([3, 2, 0, -4], 1)) is True
    assert s.hasCycle(con_ciclo([1, 2], 0)) is True
    assert s.hasCycle(con_ciclo([1], -1)) is False
    print("OK")
