# 1993. Operations On Tree (Media)
# https://leetcode.com/problems/operations-on-tree/
#
# Idea: guardo quién bloqueó cada nodo y la lista de hijos. upgrade sube por los padres para ver que
#       ninguno esté bloqueado y baja por los descendientes desbloqueando los bloqueados (tiene que
#       haber al menos uno).
# Tiempo: O(1) lock/unlock, O(n) upgrade · Espacio: O(n)

from typing import List


class LockingTree:
    def __init__(self, parent: List[int]):
        self.padre = parent
        self.bloqueado_por = [0] * len(parent)
        self.hijos = [[] for _ in parent]
        for nodo, p in enumerate(parent):
            if p != -1:
                self.hijos[p].append(nodo)

    def lock(self, num: int, user: int) -> bool:
        if self.bloqueado_por[num]:
            return False
        self.bloqueado_por[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.bloqueado_por[num] != user:
            return False
        self.bloqueado_por[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        ancestro = num
        while ancestro != -1:
            if self.bloqueado_por[ancestro]:
                return False
            ancestro = self.padre[ancestro]
        desbloqueados = 0
        pila = list(self.hijos[num])
        while pila:
            nodo = pila.pop()
            if self.bloqueado_por[nodo]:
                self.bloqueado_por[nodo] = 0
                desbloqueados += 1
            pila.extend(self.hijos[nodo])
        if desbloqueados == 0:
            return False
        self.bloqueado_por[num] = user
        return True


if __name__ == "__main__":
    t = LockingTree([-1, 0, 0, 1, 1, 2, 2])
    assert t.lock(2, 2) is True
    assert t.unlock(2, 3) is False
    assert t.unlock(2, 2) is True
    assert t.lock(4, 5) is True
    assert t.upgrade(0, 1) is True
    assert t.lock(0, 1) is False
    assert t.upgrade(0, 1) is False
    print("OK")
