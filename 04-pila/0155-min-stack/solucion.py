# 155. Min Stack (Media)
# https://leetcode.com/problems/min-stack/
#
# Idea: junto a cada valor apilo el mínimo de la pila en ese momento; así el mínimo actual siempre está arriba, incluso después de un pop.
# Tiempo: O(1) por operación · Espacio: O(n)

class MinStack:
    def __init__(self):
        self.pila = []

    def push(self, val: int) -> None:
        minimo = min(val, self.pila[-1][1]) if self.pila else val
        self.pila.append((val, minimo))

    def pop(self) -> None:
        self.pila.pop()

    def top(self) -> int:
        return self.pila[-1][0]

    def getMin(self) -> int:
        return self.pila[-1][1]


if __name__ == "__main__":
    m = MinStack()
    m.push(-2)
    m.push(0)
    m.push(-3)
    assert m.getMin() == -3
    m.pop()
    assert m.top() == 0
    assert m.getMin() == -2
    print("OK")
