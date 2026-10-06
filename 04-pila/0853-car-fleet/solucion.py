# 853. Car Fleet (Media)
# https://leetcode.com/problems/car-fleet/
#
# Idea: ordeno los autos del más cercano a la meta al más lejano y calculo cuánto tarda cada uno; si uno tarda menos o igual que la flota de adelante, la alcanza y se une. Si tarda más, arma una flota nueva.
# Tiempo: O(n log n) · Espacio: O(n)

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        autos = sorted(zip(position, speed), reverse=True)
        flotas = []
        for pos, vel in autos:
            tiempo = (target - pos) / vel
            if not flotas or tiempo > flotas[-1]:
                flotas.append(tiempo)
        return len(flotas)


if __name__ == "__main__":
    s = Solution()
    assert s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert s.carFleet(10, [3], [3]) == 1
    assert s.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
    print("OK")
