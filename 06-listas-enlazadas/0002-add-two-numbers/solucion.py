# 2. Add Two Numbers (Media)
# https://leetcode.com/problems/add-two-numbers/
#
# Idea: sumo dígito a dígito como en la escuela (las listas ya vienen al revés), llevando el acarreo; sigo mientras quede algún dígito o acarreo.
# Tiempo: O(max(n, m)) · Espacio: O(max(n, m)) (la respuesta)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ficticio = cola = ListNode()
        acarreo = 0
        while l1 or l2 or acarreo:
            suma = acarreo
            if l1:
                suma += l1.val
                l1 = l1.next
            if l2:
                suma += l2.val
                l2 = l2.next
            acarreo, digito = divmod(suma, 10)
            cola.next = ListNode(digito)
            cola = cola.next
        return ficticio.next


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
    assert a_lista(s.addTwoNumbers(crear([2, 4, 3]), crear([5, 6, 4]))) == [7, 0, 8]
    assert a_lista(s.addTwoNumbers(crear([0]), crear([0]))) == [0]
    assert a_lista(s.addTwoNumbers(crear([9, 9, 9, 9, 9, 9, 9]), crear([9, 9, 9, 9]))) == [8, 9, 9, 9, 0, 0, 0, 1]
    print("OK")
