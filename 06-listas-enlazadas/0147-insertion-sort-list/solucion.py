# 147. Insertion Sort List (Media)
# https://leetcode.com/problems/insertion-sort-list/
#
# Idea: voy armando una lista ordenada detrás de un nodo ficticio; si el nodo nuevo es mayor o igual que el último ordenado queda donde está, si no, lo saco y lo inserto en su lugar.
# Tiempo: O(n²) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        ficticio = ListNode(0, head)
        ultimo_ordenado, actual = head, head.next
        while actual:
            if actual.val >= ultimo_ordenado.val:
                ultimo_ordenado = actual
            else:
                anterior = ficticio
                while anterior.next.val <= actual.val:
                    anterior = anterior.next
                ultimo_ordenado.next = actual.next
                actual.next = anterior.next
                anterior.next = actual
            actual = ultimo_ordenado.next
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
    assert a_lista(s.insertionSortList(crear([4, 2, 1, 3]))) == [1, 2, 3, 4]
    assert a_lista(s.insertionSortList(crear([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]
    for _ in range(100):
        valores = [random.randint(-9, 9) for _ in range(random.randint(0, 20))]
        assert a_lista(s.insertionSortList(crear(valores))) == sorted(valores)
    print("OK")
