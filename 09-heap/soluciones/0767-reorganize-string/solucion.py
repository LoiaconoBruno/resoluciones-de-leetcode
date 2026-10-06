# 767. Reorganize String (Media)
# https://leetcode.com/problems/reorganize-string/
#
# Idea: greedy con max-heap: siempre pongo la letra con más repeticiones pendientes, salvo la que
#       acabo de usar, que guardo aparte un turno. Si en algún momento solo queda esa, no se puede.
# Tiempo: O(n log 26) · Espacio: O(26)

import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-c, letra) for letra, c in Counter(s).items()]
        heapq.heapify(heap)
        res = []
        anterior = None
        while heap or anterior:
            if not heap:
                return ""
            c, letra = heapq.heappop(heap)
            res.append(letra)
            if anterior:
                heapq.heappush(heap, anterior)
                anterior = None
            if c + 1 < 0:
                anterior = (c + 1, letra)
        return "".join(res)


if __name__ == "__main__":
    s = Solution()

    def valido(original, r):
        return sorted(r) == sorted(original) and all(a != b for a, b in zip(r, r[1:]))

    assert valido("aab", s.reorganizeString("aab"))
    assert s.reorganizeString("aaab") == ""
    assert valido("vvvlo", s.reorganizeString("vvvlo"))
    print("OK")
