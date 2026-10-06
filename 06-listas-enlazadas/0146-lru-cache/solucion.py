# 146. LRU Cache (Media)
# https://leetcode.com/problems/lru-cache/
#
# Idea: diccionario clave -> nodo para buscar en O(1) y una lista doblemente enlazada para el orden de uso: lo usado va al final y se desaloja desde el principio.
# Tiempo: O(1) por operación · Espacio: O(capacidad)

class Nodo:
    def __init__(self, clave=0, valor=0):
        self.clave, self.valor = clave, valor
        self.ant = self.sig = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacidad = capacity
        self.nodos = {}
        # Centinelas: izq.sig es el menos usado y der.ant el más reciente.
        self.izq, self.der = Nodo(), Nodo()
        self.izq.sig, self.der.ant = self.der, self.izq

    def _sacar(self, nodo):
        nodo.ant.sig, nodo.sig.ant = nodo.sig, nodo.ant

    def _agregar_al_final(self, nodo):
        anterior = self.der.ant
        anterior.sig = nodo
        nodo.ant, nodo.sig = anterior, self.der
        self.der.ant = nodo

    def get(self, key: int) -> int:
        if key not in self.nodos:
            return -1
        nodo = self.nodos[key]
        self._sacar(nodo)
        self._agregar_al_final(nodo)
        return nodo.valor

    def put(self, key: int, value: int) -> None:
        if key in self.nodos:
            self._sacar(self.nodos[key])
        nodo = Nodo(key, value)
        self.nodos[key] = nodo
        self._agregar_al_final(nodo)
        if len(self.nodos) > self.capacidad:
            viejo = self.izq.sig
            self._sacar(viejo)
            del self.nodos[viejo.clave]


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4
    c.put(3, 30)
    assert c.get(3) == 30
    print("OK")
