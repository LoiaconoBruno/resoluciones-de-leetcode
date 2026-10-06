# 646. Maximum Length of Pair Chain (Media)
# https://leetcode.com/problems/maximum-length-of-pair-chain/
#
# Idea: igual que elegir la mayor cantidad de intervalos sin solaparse: ordeno por el final y tomo
#       cada par que empieza después del último final elegido.
# Tiempo: O(n log n) · Espacio: O(1) extra

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: p[1])
        cadena = 0
        ultimo_fin = float("-inf")
        for inicio, fin in pairs:
            if inicio > ultimo_fin:
                cadena += 1
                ultimo_fin = fin
        return cadena


if __name__ == "__main__":
    s = Solution()
    assert s.findLongestChain([[1, 2], [2, 3], [3, 4]]) == 2
    assert s.findLongestChain([[1, 2], [7, 8], [4, 5]]) == 3
    print("OK")
