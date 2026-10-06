# 61. Rotate List (Media)
# https://leetcode.com/problems/rotate-list/
#
# Idea: cuento el largo y uno la cola con la cabeza (queda un anillo); después corto en el lugar justo: la nueva cola está a largo - k % largo - 1 pasos de la cabeza.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        largo, cola = 1, head
        while cola.next:
            cola = cola.next
            largo += 1
        k %= largo
        if k == 0:
            return head
        nueva_cola = head
        for _ in range(largo - k - 1):
            nueva_cola = nueva_cola.next
        nueva_cabeza = nueva_cola.next
        nueva_cola.next = None
        cola.next = head
        return nueva_cabeza


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
    assert a_lista(s.rotateRight(crear([1, 2, 3, 4, 5]), 2)) == [4, 5, 1, 2, 3]
    assert a_lista(s.rotateRight(crear([0, 1, 2]), 4)) == [2, 0, 1]
    assert a_lista(s.rotateRight(crear([]), 0)) == []
    print("OK")
