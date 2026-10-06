# 225. Implement Stack Using Queues (Fácil)
# https://leetcode.com/problems/implement-stack-using-queues/
#
# Idea: con una sola cola: después de cada push roto la cola para que el recién llegado quede adelante; así el frente de la cola es el tope de la pila.
# Tiempo: O(n) push, O(1) el resto · Espacio: O(n)

from collections import deque


class MyStack:
    def __init__(self):
        self.cola = deque()

    def push(self, x: int) -> None:
        self.cola.append(x)
        for _ in range(len(self.cola) - 1):
            self.cola.append(self.cola.popleft())

    def pop(self) -> int:
        return self.cola.popleft()

    def top(self) -> int:
        return self.cola[0]

    def empty(self) -> bool:
        return not self.cola


if __name__ == "__main__":
    p = MyStack()
    p.push(1)
    p.push(2)
    assert p.top() == 2
    assert p.pop() == 2
    assert p.empty() is False
    assert p.pop() == 1
    assert p.empty() is True
    print("OK")
