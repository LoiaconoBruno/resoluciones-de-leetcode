# 622. Design Circular Queue (Media)
# https://leetcode.com/problems/design-circular-queue/
#
# Idea: array fijo de tamaño k, el índice del frente y la cantidad de elementos; el fondo está en
#       (frente + cantidad - 1) % k, así los índices dan la vuelta.
# Tiempo: O(1) por operación · Espacio: O(k)

class MyCircularQueue:
    def __init__(self, k: int):
        self.datos = [0] * k
        self.frente = 0
        self.cantidad = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.datos[(self.frente + self.cantidad) % len(self.datos)] = value
        self.cantidad += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.frente = (self.frente + 1) % len(self.datos)
        self.cantidad -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.datos[self.frente]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.datos[(self.frente + self.cantidad - 1) % len(self.datos)]

    def isEmpty(self) -> bool:
        return self.cantidad == 0

    def isFull(self) -> bool:
        return self.cantidad == len(self.datos)


if __name__ == "__main__":
    q = MyCircularQueue(3)
    assert q.enQueue(1) is True
    assert q.enQueue(2) is True
    assert q.enQueue(3) is True
    assert q.enQueue(4) is False
    assert q.Rear() == 3
    assert q.isFull() is True
    assert q.deQueue() is True
    assert q.enQueue(4) is True
    assert q.Rear() == 4
    assert q.Front() == 2
    print("OK")
