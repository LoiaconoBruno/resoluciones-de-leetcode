# 705. Design HashSet (Fácil)
# https://leetcode.com/problems/design-hashset/
#
# Idea: un array de cubetas; la clave va a la cubeta key % tamaño y cada cubeta es una lista (encadenamiento para las colisiones).
# Tiempo: O(1) promedio por operación · Espacio: O(n)

class MyHashSet:
    def __init__(self):
        self.tam = 10007
        self.cubetas = [[] for _ in range(self.tam)]

    def _cubeta(self, key: int) -> list:
        return self.cubetas[key % self.tam]

    def add(self, key: int) -> None:
        cubeta = self._cubeta(key)
        if key not in cubeta:
            cubeta.append(key)

    def remove(self, key: int) -> None:
        cubeta = self._cubeta(key)
        if key in cubeta:
            cubeta.remove(key)

    def contains(self, key: int) -> bool:
        return key in self._cubeta(key)


if __name__ == "__main__":
    h = MyHashSet()
    h.add(1)
    h.add(2)
    assert h.contains(1) is True
    assert h.contains(3) is False
    h.add(2)
    assert h.contains(2) is True
    h.remove(2)
    assert h.contains(2) is False
    h.add(10008)
    assert h.contains(1) is True and h.contains(10008) is True
    print("OK")
