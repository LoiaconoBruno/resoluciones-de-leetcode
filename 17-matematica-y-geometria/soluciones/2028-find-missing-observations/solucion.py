# 2028. Find Missing Observations (Media)
# https://leetcode.com/problems/find-missing-observations/
#
# Idea: la suma que falta es mean · (n + m) - suma de rolls; si no entra entre n y 6n, no hay
#       solución. Si entra, la reparto lo más pareja posible: todos reciben faltante // n y los
#       primeros faltante % n reciben uno más.
# Tiempo: O(n + m) · Espacio: O(n) (la respuesta)

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        faltante = mean * (n + len(rolls)) - sum(rolls)
        if not n <= faltante <= 6 * n:
            return []
        base, extra = divmod(faltante, n)
        return [base + 1] * extra + [base] * (n - extra)


if __name__ == "__main__":
    s = Solution()

    def valido(rolls, mean, n, res):
        return len(res) == n and all(1 <= r <= 6 for r in res) and sum(rolls + res) == mean * (n + len(rolls))

    assert s.missingRolls([3, 2, 4, 3], 4, 2) == [6, 6]
    assert valido([1, 5, 6], 3, 4, s.missingRolls([1, 5, 6], 3, 4))
    assert s.missingRolls([1, 2, 3, 4], 6, 4) == []
    print("OK")
