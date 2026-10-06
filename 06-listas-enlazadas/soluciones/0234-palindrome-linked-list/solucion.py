# 234. Palindrome Linked List (Fácil)
# https://leetcode.com/problems/palindrome-linked-list/
#
# Idea: encuentro el medio, doy vuelta la segunda mitad y la comparo nodo a nodo con la primera.
# Tiempo: O(n) · Espacio: O(1)

from typing import Optional


# LeetCode ya define ListNode; está acá para poder probar localmente.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lenta = rapida = head
        while rapida and rapida.next:
            lenta = lenta.next
            rapida = rapida.next.next
        anterior = None
        while lenta:
            siguiente = lenta.next
            lenta.next = anterior
            anterior, lenta = lenta, siguiente
        izq, der = head, anterior
        while der:
            if izq.val != der.val:
                return False
            izq, der = izq.next, der.next
        return True


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
    assert s.isPalindrome(crear([1, 2, 2, 1])) is True
    assert s.isPalindrome(crear([1, 2])) is False
    assert s.isPalindrome(crear([1])) is True
    assert s.isPalindrome(crear([1, 2, 1])) is True
    print("OK")
