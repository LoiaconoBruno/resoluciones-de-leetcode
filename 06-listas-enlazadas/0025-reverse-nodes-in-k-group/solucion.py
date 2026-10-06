# 25. Reverse Nodes In K Group (Difícil)
# https://leetcode.com/problems/reverse-nodes-in-k-group/
#
# Idea: por cada grupo busco el k-ésimo nodo (si no hay k nodos, dejo el resto como está), doy
#       vuelta el grupo y lo reengancho entre el grupo anterior y el siguiente.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ficticio = ListNode(0, head)
        antes_del_grupo = ficticio
        while True:
            kesimo = antes_del_grupo
            for _ in range(k):
                kesimo = kesimo.next
                if not kesimo:
                    return ficticio.next
            despues_del_grupo = kesimo.next
            anterior, actual = despues_del_grupo, antes_del_grupo.next
            while actual is not despues_del_grupo:
                siguiente = actual.next
                actual.next = anterior
                anterior, actual = actual, siguiente
            primero = antes_del_grupo.next
            antes_del_grupo.next = kesimo
            antes_del_grupo = primero


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
    assert a_lista(s.reverseKGroup(crear([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert a_lista(s.reverseKGroup(crear([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert a_lista(s.reverseKGroup(crear([1, 2, 3, 4, 5]), 1)) == [1, 2, 3, 4, 5]
    assert a_lista(s.reverseKGroup(crear([1, 2, 3, 4]), 4)) == [4, 3, 2, 1]
    print("OK")
