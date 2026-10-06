# 380. Insert Delete Get Random O(1) (Media)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
#
# Idea: una lista para elegir al azar en O(1) y un diccionario valor -> índice; para borrar, piso el
#       elemento con el último y hago pop.
# Tiempo: O(1) promedio por operación · Espacio: O(n)

import random


class RandomizedSet:
    def __init__(self):
        self.valores = []
        self.indice = {}

    def insert(self, val: int) -> bool:
        if val in self.indice:
            return False
        self.indice[val] = len(self.valores)
        self.valores.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indice:
            return False
        i = self.indice.pop(val)
        ultimo = self.valores.pop()
        if i < len(self.valores):
            self.valores[i] = ultimo
            self.indice[ultimo] = i
        return True

    def getRandom(self) -> int:
        return random.choice(self.valores)


if __name__ == "__main__":
    r = RandomizedSet()
    assert r.insert(1) is True
    assert r.remove(2) is False
    assert r.insert(2) is True
    assert r.getRandom() in (1, 2)
    assert r.remove(1) is True
    assert r.insert(2) is False
    assert r.getRandom() == 2
    assert r.remove(2) is True and r.insert(3) is True and r.getRandom() == 3
    print("OK")
