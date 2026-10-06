# 981. Time Based Key Value Store (Media)
# https://leetcode.com/problems/time-based-key-value-store/
#
# Idea: por cada clave guardo la lista de (timestamp, valor); como los set llegan con timestamps
#       crecientes, la lista ya está ordenada y en get hago búsqueda binaria del último timestamp ≤
#       al pedido.
# Tiempo: O(1) set, O(log n) get · Espacio: O(n)

from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.datos = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.datos[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        valores = self.datos[key]
        izq, der = 0, len(valores) - 1
        res = ""
        while izq <= der:
            medio = (izq + der) // 2
            if valores[medio][0] <= timestamp:
                res = valores[medio][1]
                izq = medio + 1
            else:
                der = medio - 1
        return res


if __name__ == "__main__":
    t = TimeMap()
    t.set("foo", "bar", 1)
    assert t.get("foo", 1) == "bar"
    assert t.get("foo", 3) == "bar"
    t.set("foo", "bar2", 4)
    assert t.get("foo", 4) == "bar2"
    assert t.get("foo", 5) == "bar2"
    assert t.get("foo", 0) == ""
    assert t.get("otra", 9) == ""
    print("OK")
