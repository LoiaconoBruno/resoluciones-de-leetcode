# 460. LFU Cache (Difícil)
# https://leetcode.com/problems/lfu-cache/
#
# Idea: por cada clave guardo valor y frecuencia, y por cada frecuencia una lista ordenada por uso
#       (OrderedDict, que por dentro es una lista doblemente enlazada). Se desaloja el más viejo de
#       la frecuencia mínima.
# Tiempo: O(1) por operación · Espacio: O(capacidad)

from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacidad = capacity
        self.valor = {}
        self.frecuencia = {}
        self.por_frecuencia = defaultdict(OrderedDict)
        self.min_frec = 0

    def _usar(self, key):
        f = self.frecuencia[key]
        del self.por_frecuencia[f][key]
        if not self.por_frecuencia[f]:
            del self.por_frecuencia[f]
            if self.min_frec == f:
                self.min_frec += 1
        self.frecuencia[key] = f + 1
        self.por_frecuencia[f + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.valor:
            return -1
        self._usar(key)
        return self.valor[key]

    def put(self, key: int, value: int) -> None:
        if self.capacidad == 0:
            return
        if key in self.valor:
            self.valor[key] = value
            self._usar(key)
            return
        if len(self.valor) == self.capacidad:
            viejo, _ = self.por_frecuencia[self.min_frec].popitem(last=False)
            if not self.por_frecuencia[self.min_frec]:
                del self.por_frecuencia[self.min_frec]
            del self.valor[viejo]
            del self.frecuencia[viejo]
        self.valor[key] = value
        self.frecuencia[key] = 1
        self.por_frecuencia[1][key] = None
        self.min_frec = 1


if __name__ == "__main__":
    c = LFUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    assert c.get(3) == 3
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4
    c = LFUCache(0)
    c.put(0, 0)
    assert c.get(0) == -1
    print("OK")
