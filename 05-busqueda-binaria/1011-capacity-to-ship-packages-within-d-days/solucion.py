# 1011. Capacity to Ship Packages (Media)
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
#
# Idea: búsqueda binaria sobre la capacidad (entre el paquete más pesado y la suma total); para cada capacidad simulo cuántos días necesito cargando en orden.
# Tiempo: O(n log S), con S la suma de pesos · Espacio: O(1)

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def dias_necesarios(capacidad):
            dias, carga = 1, 0
            for w in weights:
                if carga + w > capacidad:
                    dias += 1
                    carga = 0
                carga += w
            return dias

        izq, der = max(weights), sum(weights)
        while izq < der:
            medio = (izq + der) // 2
            if dias_necesarios(medio) <= days:
                der = medio
            else:
                izq = medio + 1
        return izq


if __name__ == "__main__":
    s = Solution()
    assert s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert s.shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6
    assert s.shipWithinDays([1, 2, 3, 1, 1], 4) == 3
    print("OK")
