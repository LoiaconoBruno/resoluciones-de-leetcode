# 441. Arranging Coins (Fácil)
# https://leetcode.com/problems/arranging-coins/
#
# Idea: con k filas completas uso k·(k+1)/2 monedas; busco con búsqueda binaria el k más grande que entra en n.
# Tiempo: O(log n) · Espacio: O(1)

class Solution:
    def arrangeCoins(self, n: int) -> int:
        izq, der = 0, n
        while izq < der:
            k = (izq + der + 1) // 2
            if k * (k + 1) // 2 <= n:
                izq = k
            else:
                der = k - 1
        return izq


if __name__ == "__main__":
    s = Solution()
    assert s.arrangeCoins(5) == 2
    assert s.arrangeCoins(8) == 3
    assert s.arrangeCoins(1) == 1
    print("OK")
