# 895. Maximum Frequency Stack (Difícil)
# https://leetcode.com/problems/maximum-frequency-stack/
#
# Idea: guardo la frecuencia de cada valor y una pila por frecuencia; un valor con frecuencia f se apila en la pila f. El pop sale de la pila de frecuencia máxima.
# Tiempo: O(1) por operación · Espacio: O(n)

from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.frecuencia = defaultdict(int)
        self.pilas = defaultdict(list)
        self.max_frec = 0

    def push(self, val: int) -> None:
        self.frecuencia[val] += 1
        f = self.frecuencia[val]
        self.max_frec = max(self.max_frec, f)
        self.pilas[f].append(val)

    def pop(self) -> int:
        val = self.pilas[self.max_frec].pop()
        self.frecuencia[val] -= 1
        if not self.pilas[self.max_frec]:
            self.max_frec -= 1
        return val


if __name__ == "__main__":
    f = FreqStack()
    for v in [5, 7, 5, 7, 4, 5]:
        f.push(v)
    assert [f.pop() for _ in range(4)] == [5, 7, 5, 4]
    print("OK")
