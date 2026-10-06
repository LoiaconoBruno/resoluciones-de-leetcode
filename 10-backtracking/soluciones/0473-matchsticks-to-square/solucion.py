# 473. Matchsticks to Square (Media)
# https://leetcode.com/problems/matchsticks-to-square/
#
# Idea: cada lado tiene que medir total / 4; ubico los fósforos de mayor a menor en alguno de los 4
#       lados y retrocedo si no entra. Si dos lados miden lo mismo, probar el segundo es repetir
#       trabajo.
# Tiempo: O(4^n) en el peor caso, mucho menos con las podas · Espacio: O(n) de recursión

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False
        lado = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > lado:
            return False
        lados = [0] * 4

        def ubicar(i):
            if i == len(matchsticks):
                return True
            probados = set()
            for j in range(4):
                if lados[j] + matchsticks[i] <= lado and lados[j] not in probados:
                    probados.add(lados[j])
                    lados[j] += matchsticks[i]
                    if ubicar(i + 1):
                        return True
                    lados[j] -= matchsticks[i]
            return False

        return ubicar(0)


if __name__ == "__main__":
    s = Solution()
    assert s.makesquare([1, 1, 2, 2, 2]) is True
    assert s.makesquare([3, 3, 3, 3, 4]) is False
    assert s.makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]) is True
    print("OK")
