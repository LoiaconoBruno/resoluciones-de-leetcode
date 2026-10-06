# 45. Jump Game II (Media)
# https://leetcode.com/problems/jump-game-ii/
#
# Idea: BFS por "niveles": el rango [izq, der] son los índices alcanzables con s saltos; el
#       siguiente rango llega hasta el salto más lejano que se puede hacer desde ese rango.
# Tiempo: O(n) · Espacio: O(1)

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        saltos = 0
        izq = der = 0
        while der < len(nums) - 1:
            mas_lejos = max(i + nums[i] for i in range(izq, der + 1))
            izq, der = der + 1, mas_lejos
            saltos += 1
        return saltos


if __name__ == "__main__":
    s = Solution()
    assert s.jump([2, 3, 1, 1, 4]) == 2
    assert s.jump([2, 3, 0, 1, 4]) == 2
    assert s.jump([0]) == 0
    print("OK")
