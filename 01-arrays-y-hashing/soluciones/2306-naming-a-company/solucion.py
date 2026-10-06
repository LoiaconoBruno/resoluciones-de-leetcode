# 2306. Naming a Company (Difícil)
# https://leetcode.com/problems/naming-a-company/
#
# Idea: agrupo los sufijos por primera letra; para dos letras a y b, solo sirven los sufijos que no
#       están en ambos grupos, y cada par válido cuenta dos veces (orden).
# Tiempo: O(26² · n) · Espacio: O(n)

from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        grupos = [set() for _ in range(26)]
        for idea in ideas:
            grupos[ord(idea[0]) - 97].add(idea[1:])
        res = 0
        for a in range(26):
            for b in range(a + 1, 26):
                comunes = len(grupos[a] & grupos[b])
                res += 2 * (len(grupos[a]) - comunes) * (len(grupos[b]) - comunes)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.distinctNames(["coffee", "donuts", "time", "toffee"]) == 6
    assert s.distinctNames(["lack", "back"]) == 0
    print("OK")
