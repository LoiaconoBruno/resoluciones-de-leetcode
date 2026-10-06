# 269. Alien Dictionary (Difícil)
# https://www.lintcode.com/problem/892/
#
# Idea: comparando palabras vecinas, la primera letra distinta me da una regla "a va antes que b"
#       (una arista). Después hago orden topológico (Kahn); con un min-heap, entre las opciones
#       elijo la menor, así sale el orden lexicográficamente más chico. Si una palabra es prefijo de
#       la anterior o hay ciclo, no hay orden.
# Tiempo: O(C + U log U), con C el total de letras y U las letras distintas · Espacio: O(U²)

import heapq
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        siguientes = {c: set() for palabra in words for c in palabra}
        entrantes = {c: 0 for c in siguientes}
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    if y not in siguientes[x]:
                        siguientes[x].add(y)
                        entrantes[y] += 1
                    break
            else:
                if len(a) > len(b):
                    return ""
        heap = [c for c, grado in entrantes.items() if grado == 0]
        heapq.heapify(heap)
        orden = []
        while heap:
            c = heapq.heappop(heap)
            orden.append(c)
            for d in siguientes[c]:
                entrantes[d] -= 1
                if entrantes[d] == 0:
                    heapq.heappush(heap, d)
        return "".join(orden) if len(orden) == len(entrantes) else ""


if __name__ == "__main__":
    s = Solution()
    assert s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    assert s.alienOrder(["z", "x"]) == "zx"
    assert s.alienOrder(["z", "x", "z"]) == ""
    assert s.alienOrder(["abc", "ab"]) == ""
    assert s.alienOrder(["zy", "zx"]) == "yxz"
    print("OK")
