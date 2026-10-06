# 691. Stickers to Spell Word (Difícil)
# https://leetcode.com/problems/stickers-to-spell-word/
#
# Idea: memoizo por "letras que todavía me faltan" (ordenadas, para que sea una clave). Siempre
#       cubro la primera letra que falta: solo pruebo stickers que la tengan, lo que poda muchísimo.
# Tiempo: O(2^t · s · t) en el peor caso, con t el largo del target · Espacio: O(2^t)

from collections import Counter
from functools import lru_cache
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        cuentas = [Counter(s) for s in stickers]

        @lru_cache(maxsize=None)
        def minimo(faltan):
            if not faltan:
                return 0
            resto = Counter(faltan)
            mejor = float("inf")
            for cuenta in cuentas:
                if faltan[0] not in cuenta:
                    continue
                nuevo = "".join(sorted((resto - cuenta).elements()))
                mejor = min(mejor, 1 + minimo(nuevo))
            return mejor

        res = minimo("".join(sorted(target)))
        return -1 if res == float("inf") else res


if __name__ == "__main__":
    s = Solution()
    assert s.minStickers(["with", "example", "science"], "thehat") == 3
    assert s.minStickers(["notice", "possible"], "basicbasic") == -1
    print("OK")
