# 1405. Longest Happy String (Media)
# https://leetcode.com/problems/longest-happy-string/
#
# Idea: greedy con max-heap: agrego la letra con más disponibles, salvo que ya tenga dos iguales
#       seguidas al final; en ese caso uso la segunda con más disponibles.
# Tiempo: O(a + b + c) · Espacio: O(1)

import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-n, letra) for n, letra in ((a, "a"), (b, "b"), (c, "c")) if n]
        heapq.heapify(heap)
        res = []
        while heap:
            n, letra = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == res[-2] == letra:
                if not heap:
                    break
                n2, letra2 = heapq.heappop(heap)
                res.append(letra2)
                if n2 + 1:
                    heapq.heappush(heap, (n2 + 1, letra2))
                heapq.heappush(heap, (n, letra))
            else:
                res.append(letra)
                if n + 1:
                    heapq.heappush(heap, (n + 1, letra))
        return "".join(res)


if __name__ == "__main__":
    s = Solution()

    def feliz(r, a, b, c):
        return ("aaa" not in r and "bbb" not in r and "ccc" not in r
                and r.count("a") <= a and r.count("b") <= b and r.count("c") <= c)

    for a, b, c, largo in ((1, 1, 7, 8), (7, 1, 0, 5), (2, 2, 1, 5), (0, 0, 3, 2)):
        r = s.longestDiverseString(a, b, c)
        assert feliz(r, a, b, c) and len(r) == largo, r
    print("OK")
