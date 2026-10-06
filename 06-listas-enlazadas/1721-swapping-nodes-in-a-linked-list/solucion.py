# 1721. Swapping Nodes in a Linked List (Media)
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
#
# Idea: llego al k-ésimo desde el principio; desde ahí arranco un segundo puntero en la cabeza y avanzo los dos hasta el final: el segundo queda en el k-ésimo desde el final. Intercambio los valores.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        primero = head
        for _ in range(k - 1):
            primero = primero.next
        segundo, rapido = head, primero
        while rapido.next:
            segundo = segundo.next
            rapido = rapido.next
        primero.val, segundo.val = segundo.val, primero.val
        return head


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
    assert a_lista(s.swapNodes(crear([1, 2, 3, 4, 5]), 2)) == [1, 4, 3, 2, 5]
    assert a_lista(s.swapNodes(crear([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), 5)) == [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]
    assert a_lista(s.swapNodes(crear([1]), 1)) == [1]
    print("OK")
