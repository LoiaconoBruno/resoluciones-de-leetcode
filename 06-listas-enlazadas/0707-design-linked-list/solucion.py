# 707. Design Linked List (Media)
# https://leetcode.com/problems/design-linked-list/
#
# Idea: lista simple con un nodo ficticio al principio y un contador de tamaño; toda operación
#       camina hasta el nodo anterior a la posición pedida.
# Tiempo: O(n) por operación (O(1) addAtHead) · Espacio: O(n)

class Nodo:
    def __init__(self, val=0, sig=None):
        self.val = val
        self.sig = sig


class MyLinkedList:
    def __init__(self):
        self.ficticio = Nodo()
        self.tam = 0

    def _anterior(self, index):
        nodo = self.ficticio
        for _ in range(index):
            nodo = nodo.sig
        return nodo

    def get(self, index: int) -> int:
        if not 0 <= index < self.tam:
            return -1
        return self._anterior(index).sig.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.tam, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if not 0 <= index <= self.tam:
            return
        anterior = self._anterior(index)
        anterior.sig = Nodo(val, anterior.sig)
        self.tam += 1

    def deleteAtIndex(self, index: int) -> None:
        if not 0 <= index < self.tam:
            return
        anterior = self._anterior(index)
        anterior.sig = anterior.sig.sig
        self.tam -= 1


if __name__ == "__main__":
    lista = MyLinkedList()
    lista.addAtHead(1)
    lista.addAtTail(3)
    lista.addAtIndex(1, 2)
    assert lista.get(1) == 2
    lista.deleteAtIndex(1)
    assert lista.get(1) == 3
    assert lista.get(5) == -1
    lista.addAtIndex(5, 9)
    assert lista.tam == 2
    print("OK")
