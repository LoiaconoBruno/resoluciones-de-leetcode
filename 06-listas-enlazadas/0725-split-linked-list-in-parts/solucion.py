# 725. Split Linked List in Parts (Media)
# https://leetcode.com/problems/split-linked-list-in-parts/
#
# Idea: con el largo n, cada parte tiene n // k nodos y las primeras n % k tienen uno extra; recorro cortando la lista en esos tamaños.
# Tiempo: O(n + k) · Espacio: O(k) (la respuesta)

from typing import List, Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        largo, nodo = 0, head
        while nodo:
            largo += 1
            nodo = nodo.next
        base, extra = divmod(largo, k)
        partes = []
        actual = head
        for i in range(k):
            partes.append(actual)
            tam = base + (1 if i < extra else 0)
            for _ in range(tam - 1):
                actual = actual.next
            if actual and tam:
                actual.next, actual = None, actual.next
        return partes


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
    assert [a_lista(p) for p in s.splitListToParts(crear([1, 2, 3]), 5)] == [[1], [2], [3], [], []]
    assert [a_lista(p) for p in s.splitListToParts(crear(list(range(1, 11))), 3)] == \
        [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
    assert [a_lista(p) for p in s.splitListToParts(crear([]), 2)] == [[], []]
    print("OK")
