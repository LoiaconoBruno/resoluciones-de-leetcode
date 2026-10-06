# 706. Design HashMap (Fácil)
# https://leetcode.com/problems/design-hashmap/
#
# Idea: igual que el HashSet pero cada cubeta guarda pares [clave, valor]; put actualiza si la clave ya estaba.
# Tiempo: O(1) promedio por operación · Espacio: O(n)

class MyHashMap:
    def __init__(self):
        self.tam = 10007
        self.cubetas = [[] for _ in range(self.tam)]

    def _cubeta(self, key: int) -> list:
        return self.cubetas[key % self.tam]

    def put(self, key: int, value: int) -> None:
        cubeta = self._cubeta(key)
        for par in cubeta:
            if par[0] == key:
                par[1] = value
                return
        cubeta.append([key, value])

    def get(self, key: int) -> int:
        for k, v in self._cubeta(key):
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        cubeta = self._cubeta(key)
        for i, (k, _) in enumerate(cubeta):
            if k == key:
                cubeta.pop(i)
                return


if __name__ == "__main__":
    m = MyHashMap()
    m.put(1, 1)
    m.put(2, 2)
    assert m.get(1) == 1
    assert m.get(3) == -1
    m.put(2, 1)
    assert m.get(2) == 1
    m.remove(2)
    assert m.get(2) == -1
    print("OK")
